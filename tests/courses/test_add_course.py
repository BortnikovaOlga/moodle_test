import datetime
import logging

import pytest

from log_settings import LOGGING_CONFIG
from models.course_data import CourseData
from common.constants import CourseConstants

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("moodle")


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
        7. Delete added course
        6. Check successfully deleting
        """
        assert app.nav_bar.open_add_course_page() == CourseConstants.ADD_COURSE_HEADER
        course = CourseData.random()
        app.course_page.edit_general_course_data(course)
        assert app.course_page.is_added_course(course.full_name), "Course not add!"
        logger.info(
            f"Add curse, fullname = {course.full_name} shortname = {course.short_name}"
        )
        app.nav_bar.open_menage_course_page()
        app.course_page.delete_course(course.full_name)
        assert app.course_page.is_deleted_course(
            course.short_name
        ), "Course not delete!"
        logger.info(
            f"Delete curse, fullname = {course.full_name} \
            shortname = {course.short_name}"
        )

    @pytest.mark.parametrize("field", ["full_name", "short_name"])
    def test_input_invalid_general_course_data(self, app, fix_auth, field):
        """
        Steps
        1. Open auth page  = fixture app
        2. Auth with valid data = fixture fix_auth
        3. Check auth result
        4. Go to page with editing course data
        5. Edit basic course data with empty fullname or shortname
        6. Check that course not add
        """
        assert app.nav_bar.open_add_course_page() == CourseConstants.ADD_COURSE_HEADER
        course = CourseData.random()
        setattr(course, field, None)
        app.course_page.edit_general_course_data(course)
        assert not app.course_page.is_added_course(
            course.full_name
        ), "Course has been added!"
        logger.info(
            f"Not add curse, fullname = {course.full_name} \
            shortname = {course.short_name}"
        )

    def test_input_invalid_date_end_course(self, app, fix_auth):
        """
        Steps
        1. Open auth page  = fixture app
        2. Auth with valid data = fixture fix_auth
        3. Check auth result
        4. Go to page with editing course data
        5. Edit basic course data with invalid end data course
        6. Check that course not add
        """
        assert app.nav_bar.open_add_course_page() == CourseConstants.ADD_COURSE_HEADER
        course = CourseData.random()
        setattr(course, "date_end", datetime.date(1980, 12, 12))
        app.course_page.edit_general_course_data(course)
        assert not app.course_page.is_added_course(
            course.full_name
        ), "Course has been added!"
        logger.info(
            f"Not add curse, fullname = {course.full_name} \
                        date_start = {course.date_start.isoformat()} \
                        date_end = {course.date_end.isoformat()}"
        )
