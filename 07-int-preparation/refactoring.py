import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_data = {'smtp': 'smtp.gmail.com', 'imap': 'imap.gmail.com',
             'login': 'login@gmail.com', 'password': 'qwerty'}  # Имитация взятия из json


class Mail:
    def __init__(self, login, password, smtp='smtp.gmail.com', imap='imap.gmail.com'):
        self.login = login
        self.password = password
        self.smtp = smtp
        self.imap = imap

    def send_email(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())

    def recieve_email(self, header=None):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    mail = Mail(login=mail_data['login'], password=mail_data['password'],
                smtp=mail_data['smtp'], imap=mail_data['imap'])
