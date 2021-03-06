import os
import imaplib
import smtplib
from email import message_from_bytes, encoders
from email.utils import parsedate_to_datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


"""
1. 假设我们自己的电子邮件地址是from@163.com，对方的电子邮件地址是to@sina.com（这里的地址虚拟的），现在我们用Outlook或者Foxmail之类的软件写好邮件，填上对方的Email地址，点“发送”，电子邮件就发出去了。这些电子邮件软件被称为MUA：Mail User Agent——邮件用户代理。
2. Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等。由于我们自己的电子邮件是163.com，所以，Email首先被投递到网易提供的MTA，再由网易的MTA发到对方服务商，也就是新浪的MTA。这个过程中间可能还会经过别的MTA。
3. Email到达新浪的MTA后，由于对方使用的是@sina.com的邮箱，因此，新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理。Email到达MDA后，就会保存在新浪的某个服务器上，存放在某个文件或特殊的数据库里，我们将这个长期保存邮件的地方称之为电子邮箱。对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上。

发送一封电子邮件的过程：发件人 -> MUA -> MTA -> MTA -> 若干个MTA - 【MDA】 <- MUA <- 收件人

有了上述基本概念，要编写程序来发送和接收邮件，本质上就是:
1. 编写MUA把邮件发到MTA；
2. 编写MUA从MDA上收邮件。
"""
# Reference: https://docs.python.org/3/library/imaplib.html
#            https://support.office.com/zh-cn/article/%E7%94%B1%E4%B8%96%E7%BA%AA%E4%BA%92%E8%81%94%E8%BF%90%E8%90%A5%E7%9A%84-office-365-%E7%9A%84-pop-%E5%92%8C-imap-%E8%AE%BF%E9%97%AE%E8%AE%BE%E7%BD%AE-ca51235d-afc5-4d7d-843c-3616a37d5771
#            https://tools.ietf.org/html/rfc2060.html
class FetchEmail:
    def __init__(self, email, password, mail_server="partner.outlook.cn", mailbox="INBOX"):
        """
        与IMAP服务器连接，并且建立与对应mailbox的钩子
        :param email: 邮箱
        :param password: 邮箱密码
        :mail_server: IMAP4服务器, 默认为office365的IMAP4服务器
        :mailbox: 信箱, 默认为INBOX
        """
        self.conn = imaplib.IMAP4_SSL(mail_server)
        self.conn.login(email, password)
        self.conn.select(mailbox, readonly=False)

        
    def _close_connection(self):
        """
        断开与IMAP服务器的连接
        """
        self.conn.close()


    def fetch_unread_messages(self):
        """
        获得邮箱中的新(unread)邮件
        """
        emails = []
        fetch_status, messages = self.conn.search(None, '(UNSEEN)')

        if fetch_status == "OK":
            for msg_index in messages[0].split():
                try:
                    msg_status, msg_data = self.conn.fetch(msg_index, '(RFC822)')
                except:
                    print("There is no new email...")
                    self._close_connection()
                    return None

                for msg_response_part in msg_data:
                    if isinstance(msg_response_part, tuple):
                        msg = message_from_bytes(msg_response_part[1])

                        if not isinstance(msg, str):
                            emails.append(msg)
                            
                        response, flags = self.conn.store(msg_index, '+FLAGS', '\\Seen')

        return emails


    def download_attachment(self, msg, target_folder_root='/tmp/download_from_email'):
        """
        将邮件中的附近下载到指定目录下
        :param msg: 具体的邮件(包含内容)
        :target_folder_root: 下载路径的根目录
        :return: 下载成功后返回True
        """
        email_datetime = parsedate_to_datetime(msg['date'])

        year = email_datetime.isocalendar()[0]
        week = email_datetime.isocalendar()[1]
        week_code = '%d_WK%02d' % (year, week)
        target_folder = "/".join([target_folder_root, week_code])

        for msg_part in msg.walk():
            if msg_part.get_content_maintype() == 'multipart':
                continue

            if msg_part.get('Content-Disposition') is None:
                continue

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            filename = msg_part.get_filename()

            if bool(filename):
                filepath = os.path.join(target_folder, filename)
                if not os.path.isfile(filepath):
                    try:
                        fp = open(filepath, 'wb')
                        fp.write(msg_part.get_payload(decode=True))
                        fp.close()
                        print(f"Attachment is download to {filepath}")
                    except:
                        print("Fail to download attachment...")

        return True

                        


class SendEmail:
    def __init__(self, email, password, mail_server="smtp.partner.outlook.cn", port=587):
        """
        初始化SMTP的实例，其包含与SMTP的连接
        :param email: 发送者邮箱
        :param password: 发送者邮箱密码
        :param mail_server: SMTP服务器，公司默认用的是smtp.partner.outlook.cn
        :param port: SMTP服务端口号
        """
        self.conn = smtplib.SMTP(mail_server, port)
        self.conn.set_debuglevel(False)
        self.conn.starttls()
        self.email = email
        self.conn.login(self.email, password)


    def _close_connection(self):
        """
        断开与SMTP服务的连接
        """
        self.conn.quit()


    
    def make_email(self, to_list, subject=None, body_content=None, attachment_path_list=[]):
        """
        根据参数，自己构建要发送的邮件内容
        :param tolist: 邮件的接收列表
        :param subject: 邮件主题
        :param body_content: 邮件内容
        :param attachment_path_list: 要发送的附件的路径列表
        :return: 自定义构建的邮件
        """
        msg = MIMEMultipart()
        msg.add_header('From', self.email)
        msg.add_header('To', ", ".join(to_list))
        msg.add_header('Subject', subject)

        if body_content is not None:
            body = MIMEText(body_content, 'html')
            msg.attach(body)

        for file_path in attachment_path_list:
            try:
                filename = file_path.split("/")[-1]
                part = MIMEBase("application", "octet-stream")
                part.set_payload(open(file_path, "rb").read())

                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment", filename=filename)
                msg.attach(part)
            except:
                print(f"Fail to attach file {filename}")


        return msg


    def send_email(self, msg, to_list):
        """
        发送邮件到指定的接受者
        :param msg: 邮件
        :param to_list: 邮件接受者列表
        """
        self.conn.sendmail(msg['From'], to_list, msg.as_string())
        self._close_connection()
        
            
