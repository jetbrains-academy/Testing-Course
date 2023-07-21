<h2>Немного о Code Style</h2>

<p>Среди тех, кто регулярно пишет код,
существует определенное соглашение о &quot;стиле кода&quot;.
Стиль кода &mdash;&nbsp;это всё то, что не относится к его функциональности:
форматирование, имена переменных, функций, констант и так далее.
Python прекрасен тем, что&nbsp;его очень легко читать,
но даже такой простой для понимания язык в своём коде можно превратить
в нечитаемую кашу. Нечитаемая каша опасна тем, что вы не разберетесь 
в своем коде уже через пару недель, а другой человек не разберется никогда.
Хорошо написанный код экономит время при починке тестов,
при внедрении нового человека в команду, да и при написании нового кода тоже.
В общем, это очень важная тема, и следует всегда помнить о читабельности кода.</p>

<p>Мы совсем немного затронули эту тему в предыдущих модулях, а теперь, раз уж мы потихоньку идём в сторону большей абстракции, настало время поговорить об этом чуть более подробно.</p>

<h3>&nbsp;Отступы</h3>

<p>Отступы являются частью синтаксиса в Python и означают вложенность блока, будь то тело&nbsp;функции условного выражения, цикла, и так далее. Самое важное для нас в будущих шагах, что все функции внутри класса так же должны быть отделены отступом:</p>

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
