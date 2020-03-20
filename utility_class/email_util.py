import os
import email
import imaplib


class EmailHook():
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
                        msg = email.message_from_bytes(msg_response_part[1])

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
        email_datetime = email.utils.parsedate_to_datetime(msg['date'])

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

                        


    
    

