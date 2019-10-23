import unittest
from unittest import mock

from src.mail_bomb import MailBomb
from src.mail_client import MailClient

FAKE_USER = "fake_user"


class MailClientTest(unittest.TestCase):

    @mock.patch('builtins.input', return_value=FAKE_USER)
    @mock.patch('src.mail_client.getpass')
    @mock.patch("src.mail_client.smtplib")
    def test_login_calls_login_with_email_password(self, mock_smtplib: mock.Mock,
                                                   mock_get_pass: mock.Mock,
                                                   mock_input: mock.Mock):
        mock_get_pass.getpass.return_value = "fake_pass"

        MailClient(mock_smtplib).login()

        mock_smtplib.login.assert_called_with(FAKE_USER, "fake_pass")

    @mock.patch('builtins.input', return_value="yes")
    @mock.patch('src.mail_client.getpass')
    @mock.patch("src.mail_client.smtplib")
    def test_enable_email_encryption_calls_starttls(self, mock_smtplib: mock.Mock,
                                                    mock_get_pass: mock.Mock,
                                                    mock_input: mock.Mock):
        mock_get_pass.getpass.return_value = "fake_pass"

        MailClient(mock_smtplib).enable_email_encryption("smtp.gmail.com")

        mock_smtplib.starttls.assert_called()

    @mock.patch('builtins.input', return_value=FAKE_USER)
    @mock.patch('src.mail_client.getpass')
    @mock.patch("src.mail_client.smtplib")
    def test_enable_email_encryption_when_not_gmail_does_not_call_starttls(self, mock_smtplib: mock.Mock,
                                                                           mock_get_pass: mock.Mock,
                                                                           mock_input: mock.Mock):
        mock_get_pass.getpass.return_value = "fake_pass"

        MailClient(mock_smtplib).enable_email_encryption("smtp.yahoo.com")

        mock_smtplib.starttls.assert_not_called()

    @mock.patch('builtins.input', return_value=FAKE_USER)
    @mock.patch('src.mail_client.getpass')
    @mock.patch("src.mail_client.smtplib")
    @mock.patch("src.mail_client.time")
    def test_send_email_bomb_sends_emails(self,
                                          mock_time: mock.Mock,  # for time convenience
                                          mock_smtplib: mock.Mock,
                                          mock_get_pass: mock.Mock,
                                          mock_input: mock.Mock):
        mock_get_pass.getpass.return_value = "fake_pass"
        request = MailBomb("my_mom", 10, "sorry mom sorry")

        MailClient(mock_smtplib).send_email_bomb(request)

        assert mock_smtplib.sendmail.call_count == request.times
        mock_smtplib.sendmail.assert_called_with(FAKE_USER, request.recipient, request.message)
