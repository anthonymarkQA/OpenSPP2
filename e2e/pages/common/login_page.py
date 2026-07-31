class LoginPage:
    """The Odoo /web/login page — shared across every OpenSPP product, since
    product identity comes from which modules/users exist, not page structure.
    """

    PATH = "/web/login"

    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(self.PATH)
        return self

    def login(self, login: str, password: str):
        self.page.fill('input[name="login"]', login)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')
        return self
