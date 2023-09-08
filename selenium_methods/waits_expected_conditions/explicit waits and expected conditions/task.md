<h2>Explicit Waits (WebDriverWait and expected_conditions)</h2>

<p>In the previous step, we've figured out the problem of element waits on a page. However, the <strong>find_element</strong> methods check only the fact that the page element has been displayed. Meanwhile, the element might have additional properties that may be relevant to our tests. Let's consider the example with the button that sends data:</p>

<ul>
	<li>The button may be inactive, i.e., unclickable.</li>
	<li>The button may contain text that changes according to the user's actions. For example, the text "Send" may turn into "Sent" after the button has been clicked.</li>
	<li>The button may be overlapped by some other element or just be invisible.</li>
</ul>

<p>If we want to click a button in our test and the button is inactive at the moment, WebDriver will still emulate the click but no data will be sent.</p>

<p>Let's try running the following test:</p>

<pre><code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()</code></pre>

<p>We can see that WebDriver did find the button with <strong> id="verify" </strong>and did click it, but the test crashed while searching for the element "<strong>verify_message</strong>" with the resulting message:</p>

<pre><code>no such element: Unable to locate element: {"method":"id","selector":"verify_message"}</code></pre>

<p>That happened because WebDriver quickly found the button and clicked it even though the button was inactive yet. In our web page, we intentionally set up a 1-second pause between the site loading and the button activation, but an inactive button at the moment of loading is a common thing in real websites.</p>

<p>To get a reliable test, we need to make it not only find the button on the page but also wait till it becomes clickable. To implement such waits, Selenium WebDriver uses the concept of <strong>Explicit Waits</strong>, which allows assigning a specific wait for a specific element. Explicit waits are set with the help of WebDriverWait tools and <strong>expected_conditions</strong>. Let's improve our test:</p>

<pre><code class="language-python">
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")
    button = browser.find_element(By.ID, "verify")  
    # waiting for 5 seconds until button will be enabled
    button = WebDriverWait(browser, 5).until(
        element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()
</code></pre>

<p><strong>element_to_be_clickable </strong>will return the element when the latter becomes clickable; otherwise, it will return <strong>False </strong>.</p>

<p>Notice that the WebDriverWait implements the <strong>until</strong> function, which receives the wait rule, the element, and the value we will use in our element search. The <strong>expected_conditions</strong> module has many other rules, which allow implementing necessary waits:</p>

<ul>
	<li>title_is</li>
	<li>title_contains</li>
	<li>presence_of_element_located</li>
	<li>visibility_of_element_located</li>
	<li>visibility_of</li>
	<li>presence_of_all_elements_located</li>
	<li>text_to_be_present_in_element</li>
	<li>text_to_be_present_in_element_value</li>
	<li>frame_to_be_available_and_switch_to_it</li>
	<li>invisibility_of_element_located</li>
	<li>element_to_be_clickable</li>
	<li>staleness_of</li>
	<li>element_to_be_selected</li>
	<li>element_located_to_be_selected</li>
	<li>element_selection_state_to_be</li>
	<li>element_located_selection_state_to_be</li>
	<li>alert_is_present</li>
</ul>

<p>You can find rule descriptions <a href="https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions" rel="noopener noreferrer nofollow">here</a>.</p>

<p>If we want to check that the button becomes inactive after sending data, we can use a negative rule with the help of the <strong>until_not</strong> method:</p>

<pre><code class="language-python"># asking Selenium to proceed with checks for 5 seconds until the button becomes inactive
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )</code></pre>
