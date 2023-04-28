<h2>PyTest — checking the expected result (assert)</h2>

<p>If you're working with unittest to check the expected test results, you need to know and use a large number of assert methods: for example, assertEqual, assertNotEqual, assertTrue, assertFalse, and <a href="https://docs.python.org/3/library/unittest.html#assert-methods﻿" rel="nofollow noopener noreferrer">others</a>.</p>

<p>PyTest uses the standard Python's assert method, which makes code more explicit.</p>

<p>Let's compare two approaches and check that two variables are equal.</p>

<p><strong>unittest:</strong></p>

<pre><code>self.assertEqual(a, b, msg="Values differ")</code></pre>

<p><strong>PyTest:</strong></p>

<pre><code>assert a == b, "Values differ"</code></pre>

<p>With the help of assert, we can check any construct that returns True/False. It may be equality or inequality checks, occurrence of a substring in a string, or any other auxiliary function that you describe yourselves. All that makes the test code clear and readable: </p>

<pre><code>assert user_is_authorised(), "User is guest"</code></pre>

<p>If we need to check that our test triggers the expected exception (which is a rare situation in UI testing, and most probably you won't ever need it), we can use a special construct <strong>with pytest.raises()</strong>. For example, we can check that a site page doesn't display a certain element:</p>

<pre><code class="language-python">import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Should be no 'Submit' button")
    finally: 
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Should be no 'Submit' button")
    finally: 
        browser.quit()</code></pre>

<p>In the first test, the element will be found, so the <strong>NoSuchElementException</strong> error expected by the pytest.raises context manager won't be thrown and the test will fail.</p>

<pre><code>test_3_3_9_pytest_raises.py:8 (test_exception1)
E   Failed: Should be no 'Submit' button</code></pre>

<p>In the second case, as we expected, the button won't be found and the test will pass. </p>