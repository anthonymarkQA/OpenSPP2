import re

import pytest
from playwright.sync_api import expect

from pages.common.login_page import LoginPage


@pytest.mark.spmis
def test_login_with_valid_credentials(page, base_url, credentials):
    LoginPage(page).goto().login(credentials.login, credentials.password)

    # Odoo only redirects to /odoo once a session has actually been
    # authenticated; a failed login stays on /web/login instead.
    expect(page).to_have_url(re.compile(r"/odoo(/|$|\?)"))
    expect(page.locator("form.oe_login_form")).to_have_count(0)
