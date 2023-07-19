<h2>Task: clicking checkboxes and radio buttons (captcha test)</h2>

<p>Let's continue using the power of robots 🤖 for everyday tasks. In this <a href="https://suninjuly.github.io/math.html" rel="nofollow noopener noreferrer">page</a>, we've added a captcha test, i.e., a test that is easy for a computer but complicated for a human.</p>

<p>Your program has to perform the following steps:</p>

<ol>
	<li>Open the page <a href="https://suninjuly.github.io/math.html" rel="nofollow noopener noreferrer" title="Link: http://suninjuly.github.io/math.html">https://suninjuly.github.io/math.html</a>.</li>
	<li>Read the value of the variable x.</li>
	<li>Calculate the mathematical function of x (the code is provided below).</li>
	<li>Output the answer in the text field.</li>
	<li>Mark the checkbox "I'm a robot".</li>
	<li>Select the radiobutton "Robots rule!"</li>
	<li>Press the Submit button.</li>
</ol>

<p>In this task, you will need to use the .text attribute of the found element. Notice that you don't need brackets here:</p>

<pre><code class="language-python">x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
y = calc(x)</code></pre>

<p>The "text" attribute returns the text located between the opening and closing tags of the element. For example, "text" for the following element <code>&lt;div class="message"&gt;You have a new message.&lt;/div&gt;</code> will return the string: "You have a new message".</p>

<p>Use the calc() function, which will calculate and return the function value, which you need to enter in the text field. Don't forget to insert the following code at the top of your script:</p>

<pre><code>import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))</code></pre>
