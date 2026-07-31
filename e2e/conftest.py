import os
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


@dataclass(frozen=True)
class Credentials:
    login: str
    password: str


@pytest.fixture(scope="session")
def base_url():
    return os.environ.get("ODOO_URL", "http://localhost:8069")


@pytest.fixture(scope="session")
def credentials():
    target = os.environ.get("TEST_TARGET", "ephemeral")

    if target == "staging":
        login = os.environ["SPMIS_STAGING_LOGIN"]
        password = os.environ["SPMIS_STAGING_PASSWORD"]
    else:
        login = os.environ.get("ODOO_ADMIN_LOGIN", "admin")
        password = os.environ.get("ODOO_ADMIN_PASSWD", "admin")

    return Credentials(login=login, password=password)
