import pytest

from models.person_data import PersonData


class TestPersonalData:
    def test_input_valid_general_personal_data(self, app, fix_auth):
        """
        Steps
        1. Open auth page  = fixture app
        2. Auth with valid data = fixture fix_auth
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successfully editing profile
        """
        app.nav_bar.open_profile_page()
        app.profile_page.edit_general_personal_data(PersonData.random())
        assert app.profile_page.is_changed(), "Personal data not changed!"

    def test_load_user_picture(self, app, fix_auth):
        """
        Steps
        1. Open auth page - fixture app
        2. Auth with valid data - fixture fix_auth
        3. Check auth result
        4. Go to page with editing personal data
        5. Load picture data
        6. Check successfully editing profile
        """
        app.nav_bar.open_profile_page()
        app.profile_page.load_user_picture()
        assert app.profile_page.is_changed(), "Personal data not changed!"

    @pytest.mark.parametrize("field", ["firstname", "lastname", "email"])
    def test_personal_empty_data(self, field, app, fix_auth):
        """
        Steps
        1. Open main page - fixture app
        2. Auth with valid data - fixture fix_auth
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with empty data
        6. Check - profile not edited
        """
        app.nav_bar.open_profile_page()
        data = PersonData()
        setattr(data, field, None)
        app.profile_page.edit_general_personal_data(data)
        assert not app.profile_page.is_changed(), "Personal data is changed!"
