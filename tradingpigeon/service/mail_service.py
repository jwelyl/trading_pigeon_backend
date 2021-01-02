import smtplib
from email.mime.text import MIMEText
from tradingpigeon import app


class MailService:
    """
    메일 송신 등 메일에 관련된 서비스입니다.
    """

    def set_mail_message(
        self, from_mail: str, to_mail_list: list, subject: str, text: str
    ) -> MIMEText:
        """
        전송할 메일의 메시지 object를 정의합니다.
        set a message object of mail to send.
        """
        mail_object = MIMEText(text)

        mail_object["Subject"] = subject
        mail_object["From"] = from_mail
        mail_object["To"] = ", ".join(to_mail_list)

        return mail_object

    def send_mail(
        self,
        from_mail: str,
        from_mail_password: str,
        to_mail_list: list,
        subject: str,
        text: str,
    ):
        """
        메일을 전송합니다.
        send a mail.
        """

        mail_object = self.set_mail_message(
            from_mail, to_mail_list, subject, text
        )

        response = {}

        with smtplib.SMTP(
            app.config["NAVER_EMAIL_SMTP_URL"],
            app.config["NAVER_EMAIL_SMTP_PORT"],
        ) as server:
            server.starttls()  # TLS 보안 처리
            server.login(from_mail, from_mail_password)
            response = server.sendmail(
                from_mail, to_mail_list, mail_object.as_string()
            )
            server.close()  # SMTP 서버 연결 종료

        return response

    def send_mail_by_default(self, to_mail_list: list, subject: str, text: str):
        """
        환경 변수의 기본 email로 메일을 송신합니다.
        send a mail by default email of env.
        """

        response = self.send_mail(
            app.config["EMAIL_ID"],
            app.config["EMAIL_PASSWORD"],
            to_mail_list,
            subject,
            text,
        )

        return response