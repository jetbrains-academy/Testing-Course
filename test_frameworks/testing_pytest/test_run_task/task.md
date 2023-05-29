<h2>Task: running tests</h2>

<p>An applicant sent a testing project as a test task for a vacancy in your company: </p>

<p><img alt="" src="https://ucarecdn.com/c115593c-155f-4cb4-a8f3-f58cdb9bcda7/"></p>

<p>The content of the files looks like this: </p>

<p><strong>tests_for_pytest/test_main_page: </strong></p>

<pre><code># number 1
def main_page_buttons(browser):

# number 2
def test_main_page_navbar(browser):</code></pre>

<p><strong>smoke_tests/login.py:</strong></p>

<pre><code># number 3
def test_guest_can_login(browser, language):

# number 4
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
</code></pre>

<p><strong>(the root directory of the project) test_regression.py:</strong></p>

<pre><code>class TestLessonCreate():
    # number 5
    def test_create_lesson(self, browser):

    # number 6
    def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):


class CourseCreate():
    # number 7
    def test_create_course(self, browser):

# number 8
def test_guest_can_open_new_course(browser):</code></pre>

<p>You are trying to run the tests from the directory with the test_project using a PyTest command: </p>

<pre><code class="language-bash">pytest test_project
</code></pre>

<p>Mark only those test methods that PyTest will find and execute: </p>
