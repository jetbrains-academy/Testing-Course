<h2>Sample execute_script task</h2>

<p>Let's consider a real-life situation where the user needs to click a page element that suddenly appears to be overlapped by another element.</p>

<p>In WebDriver, we use the click() method for a click. If the element is overlapped by another element, the program throws the following error:</p>

<pre><code>selenium.common.exceptions.WebDriverException: Message: unknown error: Element &lt;button type="submit" class="btn btn-default" style="margin-bottom: 1000px;"&gt;...&lt;/button&gt; is not clickable at point (87, 420). Other element would receive the click: &lt;p&gt;...&lt;/p&gt;
</code></pre>

<p>The error description tells us that the element cannot be clicked at the given point, as the click would be performed on a different element with the &lt;p&gt; tag.</p>

<p>To see an example of such an error, run the following script:</p>

<pre><code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()</code></pre>

<p>Now you can open the following <a href="https://SunInJuly.github.io/execute_script.html" rel="nofollow noopener noreferrer">page</a> and see that the button we need is really overlapped by a huge footer. A footer is the bottom section of a page, which is usually the same for all site pages. In order to figure out how to solve this issue, we need to understand how the <strong>click()</strong> method works.</p>

<p>First, WebDriver checks that the element's width and height are larger than 0, so that it might be clicked.</p>

<p>Next, if the element lies beyond the limits of the browser window, WebDriver automatically scrolls the page to bring the element into the visibility range, i.e., within the limits of the screen. However, that does not guarantee that the element won't be overlapped by another element, which is also located within the visibility range.</p>

<p>Now, what point of the element will be clicked? Selenium calculates the coordinates of the element's center and clicks that very point. That will also result in an error if a part of the element is visible but more than half of the element's height or width is overlapped.</p>

<p>If we face such a situation, we can make the browser additionally scroll the required element to make it clearly visible.<br>
You can do it with the following script:</p>

<pre><code>"return arguments[0].scrollIntoView(true);"</code></pre>

<p>We passed an additional argument <code>true</code> to the scrollIntoView method so that after scrolling, the element would be within the visibility range. You can find additional parameters of the method here: <a href="https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView" rel="noopener noreferrer nofollow">https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView</a></p>

<p>Thus, in order to click an overlapped button, we need to execute the following commands in our code:</p>

<pre><code class="language-python">button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()</code></pre>

<p>We passed a JavaScript text to the execute_script method together with the found button element, which we need to scroll the page to. After code execution, the button element must be at the top of the page. You can find more details about the method here: <a href="https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView" rel="noopener noreferrer nofollow">https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView</a> .</p>

<p>We also need to scroll the whole page by a given number of pixels. The following command will scroll the page down by 100 pixels:</p>

<pre><code class="language-python">browser.execute_script("window.scrollBy(0, 100);")</code></pre>

<p><span style="color: #ff4363;">!Important.</span> In this course, we will not analyze the work of JavaScript and will confine ourselves to the above example of the page scrolling script. For the sake of comparison, let's consider another JavaScript code, which does the same as the above code for WebDriver:</p>

<pre><code class="language-javascript">// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);</code></pre>

<p>You can execute it in the browser console at <a href="http://suninjuly.github.io/execute_script.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/execute_script.html</a>. To do that, open developer tools in your browser, go to the <strong>console</strong> tab, paste the code and press Enter. This way you can test parts of JS code before implementing them in your Python tests.</p>

<p>Notice that in WebDriver you need to use the key word <strong>return</strong> in your code. You also need to use it when you want to get the data after script execution. Meanwhile, when testing the script in the browser console, you don't need to use the <strong>return</strong> word.</p>
