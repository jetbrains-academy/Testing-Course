@pytest.mark.regression
# test out of scope of a class
def test_student_can_see_lesson_name_in_lesson_in_course_after_joining(self, driver):
    # lines inside the scope of the test method with indent
    page = CoursePromoPage(url=self.course.url, driver=driver)
    page.open()


class TestLessonNameInCourseForTeacher():
    @pytest.mark.regression
    # test inside the class
    def test_teacher_can_see_lesson_name_in_lesson_in_course(self, driver):
        page = LessonPlayerPage(url=self.lesson_url, driver=driver)
        page.open()
        try:
            # indent for any new scope
            dangerous_function()
        except:
            close_something()