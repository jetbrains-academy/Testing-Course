<h2>A few words about Code Style</h2>

<p>Among those who frequently write code,
there is a certain agreement about the &quot;code style&quot;.
Code style is what does not refer to code functionality:
it is about formatting, the names of variables, functions, constants, etc.
A good thing about Python is that it is easy to read. However,
even such an easily understandable language may be turned
into a mess. As a result, you won't be able to figure out
your own code within a couple of weeks, and others will never be able to read it.
Well written code saves time when you need to fix tests,
introduce a new team member, and also when you write new code.
All in all, style is a vital issue, and you always need to mind code readability.</p>

<p>We've briefly touched upon this issue in our previous modules. Now, as we're gradually heading for a bigger abstraction, it's about time we discussed it in more detail.</p>
 
<h3>&nbsp;Indentation</h3>

<p>Indents are part of the Python syntax. They indicate code block nesting – whether it's the body of a function, a conditional statement, a cycle, etc. What's important for our further steps is that all functions within a class must also be indented:</p>

<pre>
<code>@pytest.mark.regression
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

</code></pre>
