<h2>Task: find an element by the link text</h2>

<p>In this task, we'll try to find elements by link text, and to do that, we'll use the find_element_by_link_text method:</p>

<pre><code>link = browser.find_element(By.LINK_TEXT, text)</code></pre>

<p>As an argument, the method receives the text that we want to find in a link, that is, the very text between the opening and closing tags, like &lt;a&gt; this one &lt;/a&gt;.</p>

<p>Let's say we have a page <a href="https://www.degreesymbol.net/" rel="noopener noreferrer nofollow">https://www.degreesymbol.net/</a> and we want to find a link with the text "Degree symbol in Math" and follow the link. If we want to find an exact match, we can use the following code: </p>

<pre><code>link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link.click()</code></pre>

<ol>
</ol>

<p>If we want to find a link element using a substring, we'll use the following code: </p>

<pre><code>link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()</code></pre>

<p>Usually the substring search is more convenient and flexible, but you need to be twice as careful with it and make sure that you find the right element. </p>

<h3>Task</h3>

<p>In the page indicated below, you need to find an encoded link and click it:</p>

<ol>
	<li>At the top of your code, add "import math".</li>
	<li>Add a command that opens the page: <a href="http://suninjuly.github.io/find_link_text" rel="noopener noreferrer nofollow">http://suninjuly.github.io/find_link_text</a>.</li>
	<li>Add a command that finds the link with a text. The text in the link you need to find has been encoded with the following formula: 
	<pre><code>str(math.ceil(math.pow(math.pi, math.e)*10000))</code></pre>
	<p>(you can either insert it into your code or execute it in the interpreter, copy the result, and use it in your code). </p>
	</li>
	<li>
	<p>Add the command for clicking the found link: it will take you to the registration form.</p>
	</li>
	<li>
	<p>Fill in the form with the script like you did in the previous step of the lesson.</p>
	</li>
</ol>

<p><strong>Important! </strong>The search by link text may be very convenient, as these texts are modified less often than element attributes. However, this method should rather be avoided. For example, if an application has several interface languages, your tests will pass only with one of those. Use the method with caution and remember about the possible limitations. </p>

<p>Further information: </p>

<p><a href="https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text" rel="noopener noreferrer nofollow">https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text</a></p>
