import pytest

from common.constants import LoginConstants
from models.auth_data import AuthData


class TestAuth:
    def test_auth_valid_data(self, app, fix_auth):
        """
        Steps
        1. Open main page - fixture app
        2. Auth with valid data - fixture fix_auth
        3. Check auth result
        """
        # assert in fixture fix_auth
        pass

    @pytest.mark.parametrize("field", ["login", "password", None])
    def test_auth_empty_and_invalid_data(self, app, field):
        """
        Steps
        1. Open main page - fixture app
        2. Auth with empty, invalid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        if field:
            setattr(data, field, None)
        app.login_page.auth(data)
        assert (
            app.login_page.auth_error_text() == LoginConstants.AUTH_ERROR_TEXT
        ), "We are auth!"
