<h2>How get and find_element methods work</h2>

<p>Let's consider one more WebDriver test – the one that checks the functioning of a button.</p>

<p>The test scenario is as follows:</p>

<ol>
	<li>Open the page <a href="http://suninjuly.github.io/wait1.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/wait1.html</a>.</li>
	<li>Click the "Verify" button.</li>
	<li>Check that the text "Verification was successful!" appears.</li>
</ol>

<p>To open a page, we use the get method; then we find the required button using one of the find_element_by_ methods and press it using the click method. Then, we find the new text element and check that the text corresponds to what we expected.</p>

<p>Here's the automated test code:</p>

<pre><code class="language-python">
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/wait1.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message") 
    assert "successful" in message.text
finally: 
    browser.quit()
    
</code></pre>

<p>Try launching the automated test.
The test will crash with the message NoSuchElementException for the element 
with <strong>id="verify"</strong>. Why does it happen?</p>
<p>Python commands are executed synchronously, i.e., in strict succession. The button search won't start until the get command completes. The button click won't happen until the button is found, etc.</p>

<p>However, tests will work smoothly
only if the given web page does not use JavaScript
(which is highly unlikely with modern web pages). 
<br>
The get method waits till it receives the information from the browser that the page has been downloaded,
and only then does our test start searching for the button.
If the page is interactive, the browser will consider it downloaded,
while the scripts downloaded by the browser will continue running. 
A script might control the appearance of the button on the page and, for example, display it
with a time lag so that the button would emerge slowly and beautifully. 
In such a case, the test will crash with the already familiar error NoSuchElementException, 
as at the time of executing the command
<code>button = browser.find_element(By.ID, "verify")</code>, the element with <strong>id="verify"</strong> won't be displayed yet.
On that page, the pause before showing the button is set to 1 second, 
the <strong>find_element()</strong> method will make only one attempt to find the element and,
in the case of a failure, will crash our test.</p>
