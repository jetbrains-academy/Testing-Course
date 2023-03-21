<h2>Задание: запуск тестов</h2>

<p>Соискатель прислал тестовый проект в качестве тестового задания на вакансию в вашу компанию: </p>

<p><img alt="" src="https://ucarecdn.com/c115593c-155f-4cb4-a8f3-f58cdb9bcda7/"></p>

<p>Содержимое самих файлов выглядит примерно так: </p>

<p><strong>tests_for_pytest/test_main_page: </strong></p>

<pre><code># номер 1
def main_page_buttons(browser):

# номер 2
def test_main_page_navbar(browser):</code></pre>

<p><strong>smoke_tests/login.py:</strong></p>

<pre><code># номер 3
def test_guest_can_login(browser, language):

# номер 4
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
</code></pre>

<p><strong>(корневая директория проекта) test_regression.py:</strong></p>

<pre><code>class TestLessonCreate():
    # номер 5
    def test_create_lesson(self, browser):

    # номер 6
    def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):


class CourseCreate():
    # номер 7
    def test_create_course(self, browser):

# номер 8
def test_guest_can_open_new_course(browser):</code></pre>

<p>Вы пытаетесь запустить тесты из директории, в которой содержится проект test_project, с помощью PyTest командой: </p>

<pre><code class="language-bash">pytest test_project
</code></pre>

<p>Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest: </p>