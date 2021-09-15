class TestCourseData:
    def test_input_valid_general_course_data(self, app, fix_auth):
        """
        Steps
        1. Open auth page  = fixture app
        2. Auth with valid data = fixture fix_auth
        3. Check auth result
        4. Go to page with editing course data
        5. Edit basic course data with valid data
        6. Check successfully editing
        """
        assert app.nav_bar.open_course_page() == "Добавить курс"
        course_full_name = app.course_page.edit_general_course_data()
        assert app.course_page.is_add_course(course_full_name), "Course not add!"
