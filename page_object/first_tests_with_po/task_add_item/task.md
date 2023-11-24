
<p>Let's practice before moving on.&nbsp;</p>

<p>Imagine you are an automated tester in the IT department of an online store. The QA Lead assigned you the task of automating the following test scenario:&nbsp;</p>

<ol>
	<li>Open the product page (<a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear</a>). Note that the link contains the parameter &quot;?promo=newYear&quot;. Don't lose it in the automated test to get the verification code.</li>
	<li>Click the &quot;Add to Basket&quot; button.</li>
	<li>*Calculate the result of the mathematical expression and enter the answer. Use the method <strong>solve_quiz_and_get_code()</strong>, which is provided below. For example, you can add it to the <strong>BasePage</strong> class to use it on any page. This method is only needed to check that you have written a Selenium test. After that, you will get a code that needs to be entered as the answer to this task. The code will be displayed in the interpreter console where you run the test. Don't forget to add checks for the expected result at the end of the test.</li>
</ol>

<p>Expected result:&nbsp;</p>

<ol>
	<li>A message stating that the item has been added to the basket. The name of the item in the message should match the item you actually added.</li>
	<li>A message with the basket's total cost. The basket's cost should match the price of the item.&nbsp;</li>
</ol>

<p>Write the test using the Page Object pattern. To do this, you need to:&nbsp;</p>

<ol>
	<li>Open a new test file named <em>test_product_page.py.</em></li>
	<li>Create a Page Object class for the product page. Describe it in the <em>product_page.py</em> file, in the <em>pages</em> folder.</li>
	<li>Describe a method for adding to the basket.</li>
	<li>Complete the verification methods.</li>
	<li>Describe the necessary locators for page elements.</li>
	<li>Write the actual test case in the <em>test_product_page.py</em> file, using all the steps described above. Name the test <strong>test_guest_can_add_product_to_basket.</strong></li>
</ol>

<p>You can start working on any point, but it is considered good practice to first outline the steps and structure of the test and then describe the specific implementation.&nbsp;</p>

<p>*Use this method in the test to get the verification code:&nbsp;</p>

<pre>
<code class="language-python">from selenium.common.exceptions import NoAlertPresentException # в начале файла

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")</code></pre>

<p>To see the verification code in the console, run PyTest with the <strong>-s</strong> parameter:</p>

<pre>
<code>pytest -s test_product_page.py</code></pre>
