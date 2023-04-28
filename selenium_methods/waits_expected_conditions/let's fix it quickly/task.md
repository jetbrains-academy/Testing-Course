<h2>Let's fix it quickly: time.sleep()</h2>

<p>Now that we know that the button is displayed with a delay,
we can add a wait before the element search starts.
We have already used the <strong>time</strong> library before. 
Let's apply it again:</p>

<pre><code class="language-python">import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/wait1.html")
    time.sleep(3)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
finally:
    browser.quit()</code></pre>

<p>Now the test passes.
However, what if the message element also has a delay?
Shall we add another <strong>time.sleep()</strong> before the message search? 
And what if the delay time of the button display changes? 
Shall we increase the wait?
Besides, different computers with different internet speed may display
the button with different time lag.
Of course, we can add a wait before each step, 
but then a considerable part of the testing time will be consumed by fruitless waiting,
and with the increasing number of tests this problem will just get worse. </p>
