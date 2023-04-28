<h2>Conftest.py&nbsp;&mdash; test configuration</h2>

<p>We've previously added the browser fixture, which creates a copy of the browser for tests in a given file. When we have more than one test file, we need to describe the fixture in each file. That's very inconvenient. Frequently used fixtures as well as global settings should be stored in the <strong> conftest.py</strong> file, which must be located in the upper-level directory of your project with the tests. We can also create additional conftest.py files in other directories, but then the settings in those files will be applied only to the tests in subdirectories.</p>

<p>Let's create a <strong>conftest.py</strong> file in the root directory of our test project and move the <strong>browser</strong> fixture there. See how much more concise the file with tests looks now.</p>

<p><strong>conftest.py:</strong></p>

<pre>
<code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()</code></pre>

<p>Now, no matter how many files with tests we create, the tests will have access to the browser fixture. The fixture is passed to the test method as an argument. Thus, you can conveniently reuse the same auxiliary functions in different project parts.</p>

<p><br />
<strong>test_conftest.py:</strong></p>

<pre>
<code class="language-python">from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")</code></pre>

<h3><span style="color:#ff4363"><strong>VERY&nbsp;IMPORTANT!&nbsp;</strong></span></h3>

<p>You need to be aware of one important feature of configuration files' behavior. PyTest automatically finds and loads conftest.py files that are located in the directory with the tests. If you keep all your course scripts in one directory, be cautious and make sure to avoid the situation where you run the tests from the tests folder:</p>

<pre>
<code class="language-no-highlight">tests/
├── conftest.py
├── subfolder
│   └── conftest.py
│   └── test_abs.py

Avoid that!</code></pre>

<p>In such a case, BOTH&nbsp;conftest.py files are applied, which might result in unpredictable errors and conflicts.&nbsp;&nbsp;</p>

<p>This way we can redefine different fixtures, but within our course, we recommend sticking to one file per project/task and storing them horizontally, like this::&nbsp;</p>

<pre>
<code class="language-no-highlight">selenium_course_solutions/
├── section3
│   └── conftest.py
│   └── test_languages.py
├── section4 
│   └── conftest.py
│   └── test_main_page.py

Correct!</code></pre>

<p>Be cautious and make sure not to have different conftest in nested directories, especially when you download and check your group mates' tasks.</p>

<p><a href="https://docs.pytest.org/en/7.1.x/how-to/fixtures.html?highlight=fixture%20folder#override-a-fixture-on-a-folder-conftest-level" rel="noopener noreferrer nofollow">Override a fixture on a folder (conftest) level</a></p>
