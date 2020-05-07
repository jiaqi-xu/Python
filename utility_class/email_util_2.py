import os
import imaplib
import smtplib
import datetime
from email import message_from_bytes, encoders
from email.utils import parsedate_to_datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from src.utils.log_util import get_logger

logger = get_logger("Email_Module")


class FetchEmail:
    def __init__(self, email, password, mail_server="partner.outlook.cn", mailbox="INBOX"):
        """
        与IMAP服务器连接，并且建立与对应mailbox的钩子
        :param email: 邮箱
        :param password: 邮箱密码
        :param mail_server: IMAP4服务器, 默认为office365的IMAP4服务器
        :param mailbox: 信箱, 默认为INBOX
        """
        self.conn = imaplib.IMAP4_SSL(mail_server)
        self.conn.login(email, password)
        self.conn.select(mailbox, readonly=False)

    def _close_connection(self):
        """
        断开与IMAP服务器的连接
        """
        self.conn.close()

    def fetch_unread_messages(self, email_specific_query):
        """
        获得邮箱中的新(unread)邮件
        :param email_specific_query: e.g (SUBJECT "Query 3") or (FROM "SOMEONE") or (FROM "someone" SUBJECT "test")
        """
        emails = []
        fetch_status, messages = self.conn.search(None, '(UNSEEN)', email_specific_query)

        if fetch_status == "OK":
            for msg_index in messages[0].split():
                try:
                    msg_status, msg_data = self.conn.fetch(msg_index, '(RFC822)')
                except:
                    logger.warning("There is no new email...")
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
        将邮件中的附件下载到指定目录下，该函数已经由通用变成只针对IC daily shipment了；
        不过仍然有相关generic code的影子.
        :param msg: 具体的邮件(包含内容)
        :param target_folder_root: 下载路径的根目录
        :return: 下载成功后返回文件保存的路径
        """
        filepath = None

        # 获取邮件时间，并转化为本地时间，从而推出该真实销量文件所对应的日期
        email_datetime_utc = parsedate_to_datetime(msg['date'])
        email_datetime_local = email_datetime_utc.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
        shipment_datetime = email_datetime_local + datetime.timedelta(days=-1)

        month = shipment_datetime.month
        day = shipment_datetime.day
        year = shipment_datetime.isocalendar()[0]
        week = shipment_datetime.isocalendar()[1]
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
                filepath = os.path.join(target_folder, f"raw_daily_shipment_{year}_{month}_{day}.XLSM")
                if not os.path.isfile(filepath):
                    try:
                        fp = open(filepath, 'wb')
                        fp.write(msg_part.get_payload(decode=True))
                        fp.close()
                        logger.info(f"Attachment is download to {filepath}")
                    except:
                        logger.error("Fail to download attachment...")
                else:
                    logger.warning("File already existed...")

        return filepath


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
        :param to_list: 邮件的接收列表
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
                logger.info(f"attachment: {filename} is added into email...")
            except:
                logger.warning(f"Fail to attach file {filename}...")

        return msg

    def send_email(self, msg, to_list):
        """
        发送邮件到指定的接受者
        :param msg: 邮件
        :param to_list: 邮件接受者列表
        """
        self.conn.sendmail(msg['From'], to_list, msg.as_string())
        logger.info("Email sent successfully...")
        self._close_connection()
