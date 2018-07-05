# -*- encoding: utf-8 -*-
'''
首先注意到两点，就感觉被骗了。一是耗时与同步阻塞相当，二是代码更复杂。要非阻塞何用？且慢。

上图第9行代码sock.setblocking(False)告诉OS，让socket上阻塞调用都改为非阻塞的方式。之前我们说到，非阻塞就是在做一件事的时候，不阻碍调用它的程序做别的事情。上述代码在执行完 sock.connect() 和 sock.recv() 后的确不再阻塞，可以继续往下执行请求准备的代码或者是执行下一次读取。

代码变得更复杂也是上述原因所致。第11行要放在try语句内，是因为socket在发送非阻塞连接请求过程中，系统底层也会抛出异常。connect()被调用之后，立即可以往下执行第15和16行的代码。

需要while循环不断尝试 send()，是因为connect()已经非阻塞，在send()之时并不知道 socket 的连接是否就绪，只有不断尝试，尝试成功为止，即发送数据成功了。recv()调用也是同理。

虽然 connect() 和 recv() 不再阻塞主程序，空出来的时间段CPU没有空闲着，但并没有利用好这空闲去做其他有意义的事情，而是在循环尝试读写 socket （不停判断非阻塞调用的状态是否就绪）。还得处理来自底层的可忽略的异常。也不能同时处理多个 socket 。

然后10次下载任务仍然按序进行。所以总体执行时间和同步阻塞相当。如果非得这样子，那还不如同步阻塞算了。
'''
import socket


def nonblocking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(("example.com", 80))
    except BlockingIOError:
        # 非阻塞连接过程中也会抛出异常
        pass

    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    data = request.encode('ascii')
    # 不知道scoket何时就绪，就不断尝试发送
    while True:
        try:
            sock.send(data)
            # 直到send不抛异常，则发送完成
            break
        except OSError:
            pass

    response = 'b'
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response


def sync_way():
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)


sync_way()




