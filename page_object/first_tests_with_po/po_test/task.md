<h2>First test based on&nbsp;Page Object</h2>

<p>Hooray, we've implemented the first prototype of the page! Now let's rewrite the test using the Page Object:&nbsp;</p>

<p>1. Open the file with your test,&nbsp;<em>test_main_page.py</em>.</p>

<p>2. At the very top of the file, you need to import the class describing the main page.&nbsp;</p>

<p>3. Now let's transform the test itself in <em>test_main_page.py</em>:&nbsp;</p>

<pre>
<code class="language-python">from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # initializing the page object 
    page.open()                      # opening the page
    page.go_to_login_page()          # using the page method to open the login page 
</code></pre>

<p>4. Make sure the test passes by running it with the same command:&nbsp;</p>

<pre>
<code>pytest -v --tb=line --language=en test_main_page.py
</code></pre>

<p>Now, our test is <strong>almost </strong>completely written in the trendy Page Object style! Why <strong>almost&nbsp;</strong>&mdash; you'll find out in the following steps.</p>
