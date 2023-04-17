<h2>Better solutions: Selenium Waits (Implicit Waits)</h2>

<p>Hopefully, you've figured out that the solution involving <strong> time.sleep() </strong>isn't a good one: 
it is not scalable and is hard to support.</p>

<p>An ideal solution might be as follows: we need to avoid
false test crashes due to the asynchronous work of scripts or server delays,
so we will wait for the element's appearance on the page for a set time period
(e.g., 5 seconds).
We will check for the presence of the element every 500 ms.
As soon as the element has been located, we immediately proceed to the following test step.
Thus, in the ideal-case scenario, we will get the required element immediately, and in the worst-case scenario within 5 seconds.</p>

<p>Selenium WebDriver offers a way to set up such waits.
It allows setting up a wait for driver initialization
and applying it to all tests. It is called an
<strong>Implicit wait</strong>, as we don't need to explicitly indicate it each time we search for an element – it will be applied automatically at the call of each subsequent command.</p>

<p>Let's improve our test with the help of implicit waits.
To do that, we need to remove time.sleep() 
and add a line with the <strong>implicitly_wait</strong> method:</p>

<pre><code class="language-python">
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
finally:
    browser.quit()

</code></pre>

<p>Now, we can be sure that small
delays in the site's work won't affect the stability of our tests.
With each call of the <strong>find_element</strong> command,
WebDriver will wait for the element's appearance for 5 seconds before throwing
<strong>NoSuchElementException</strong>.</p>
