import pytest
from playwright.sync_api import expect

from pages.common.login_page import LoginPage


@pytest.mark.spmis
def test_login_with_valid_credentials(page, base_url, credentials):
    LoginPage(page).goto().login(credentials.login, credentials.password)

    expect(page).not_to_have_url(f"{base_url}/web/login")
    expect(page.locator(".o_main_navbar")).to_be_visible()
