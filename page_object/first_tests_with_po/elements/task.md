<h2>Page elements in the Page Object pattern</h2>

<p>Remember, we talked about how the tests almost adhere to the Page Object approach?&nbsp;</p>

<p>Now, with the help of a short and instructive story, let's see why it's <strong>almost&nbsp;</strong>the case.</p>

<p>We already have two test cases that, in one way or another, interact with the login link. Let's imagine a situation where we have a trendy agile process: developers are constantly making changes to the product. At some moment, the changes also affect the website header. A developer comes to you with a new link and asks you to test it.</p>

<p>Change the link where tests are executed for <a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer</a>.&nbsp;</p>

<p>Run the tests with the command:</p>

<pre>
<code class="language-bash">pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>The tests failed, and now we need to maintain them, meaning <em>fix&nbsp;</em> them. Find a new selector for the login link.&nbsp;</p>

<p>We'll have to make adjustments in the <em>main_page.py</em>&nbsp;file in several places where the modified selector is used. Calculate how many lines you'll need to edit to fix your tests and enter that number in the first response field below.&nbsp;</p>

<p>To avoid this, when designing tests (and code in general), a good practice is to extract the selector into an external variable.&nbsp;</p>

<p>Let's do that:&nbsp;</p>

<p>1. In the pages folder, open the <em>locators.py&nbsp;</em>file.</p>

<p>2. Inside, create a new class. Each class will correspond to each PageObject class:&nbsp;</p>

<pre>
<code>from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")</code></pre>

<p>Now, each selector is a pair: how to find and what to find.&nbsp;</p>

<p>3. In the main_page.py file, import the new class with the locators.&nbsp;</p>

<pre>
<code>from .locators import MainPageLocators</code></pre>

<p>4. Now in the MainPage class, replace all the lines containing &quot;<strong>#login_link</strong>&quot; as follows:</p>

<pre>
<code class="language-python">def should_be_login_link(self):
    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"</code></pre>

<p>Pay attention here to the asterisk symbol<strong> *</strong>; it indicates that we passed a tuple, and this tuple needs to be unpacked.&nbsp;</p>

<p>5. Run the tests using the same command:&nbsp;</p>

<pre>
<code class="language-bash">pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>They will, of course, fail again. But now, take note of how many lines you will need to edit when the tests are written in this configuration? </p>

<p>&nbsp;</p>

<p><strong>So, a PageObject includes not only <em>methods</em> but also <em>elements</em>.&nbsp;&nbsp;</strong></p>

<p>Manually fixing broken selectors throughout the entire project is time-consuming, and there's a significant risk of forgetting and leaving the old selector. When we extract selectors into a separate entity, we reduce the time spent on maintaining tests and greatly simplify our lives in the long run.&nbsp;</p>

<p>Moreover, a sprint later, the promotion ended, and the feature with the header change was rolled back. Now the link works the same as before. Remove the promotion link and restore the regular link for running tests:&nbsp;</p>

<pre>
<code>link = "http://selenium1py.pythonanywhere.com/"</code></pre>

<p>Don't forget to revert to the old selector <strong>#login_link</strong> so that the tests pass again. We'll need them later!&nbsp;</p>
