from model.user import User
from model.email import Email


def test_login_and_send_email(base):
    base.open_login_page()
    assert base.is_login_page()

    base.login(User.test_user())
    assert base.is_logged_in()

    base.open_send_email_form()
    assert base.is_send_email_form_opened()

    base.send_email(Email.test_email())
    assert base.is_email_sent()
