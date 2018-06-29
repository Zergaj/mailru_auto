import pytest


@pytest.mark.parametrize("user,email", [
    (
            ("vidan.ugil", "^Tomato_65^"),
            ("zergaj@mail.ru", "test_email", "adsf asdf asdf asdf asdf")
    )
])
def test_login_and_send_email(base, user, email):
    base.open_login_page()
    assert base.is_login_page()

    base.login(user)
    assert base.is_logged_in()

    base.open_send_email_form()
    assert base.is_send_email_form_opened()

    base.send_email(email)
    assert base.is_email_sent()
