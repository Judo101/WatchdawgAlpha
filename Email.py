import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class Email(object):
    def __init__(self, receiver, path):
        self.receiver = receiver
        self.path = path

        self.sender = 'testing159732486@gmail.com'
        self.password = '159732486'

    @property
    def receiver(self):
        return self._receiver
    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = 'Security Alert !!!'

        msg.attach(MIMEText('A motion was detected in your place.','plain'))

        files = []

        for filename in files:
            attachment = open(filename, 'rb')

            part = MIMEBase('application', 'octet-strean')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + filename)

            msg.attach(part)

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, self.password)

        server.sendmail(self.sender, self.receiver, text)
        server.quit()
