<h2>Implementation of LoginPage</h2>

<p>If you're well-versed in test design, you may have noticed that there are no checks in the test for navigating to the login page. Let's verify that we have indeed navigated to the login page. For this, we'll need a new Page Object. At the same time, we'll understand how to switch between those during the test.&nbsp;</p>

<p> Open the LoginPage file in the pages folder. Inside, there are verification methods:&nbsp;</p>

<pre>
<code>should_be_login_url
should_be_login_form
should_be_register_form</code></pre>

<p>Implement them yourself:&nbsp;</p>

<p>1. In the locators.py file, create the LoginPageLocators class.</p>

<p>2. Choose selectors for the registration and login forms and add them to the LoginPageLocators class.</p>

<p>3. Write checks using these selectors. Don't forget to provide a meaningful error message separated by a comma. Write a failing test first to ensure the clarity of the output.&nbsp;</p>

<p>4. In the should_be_login_url method, implement a check that the substring &quot;login&quot; is present in the current browser URL. Use the appropriate&nbsp;<a href="https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url" rel="noopener noreferrer nofollow">WebDriver property</a> for that.</p>

<p>Now let's see how we can navigate between pages.&nbsp;</p>
