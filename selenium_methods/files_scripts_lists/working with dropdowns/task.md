<h2>Working with lists</h2>

<p>Web pages may also have dropdown lists. Such lists have a number of important features:</p>

<ol>
	<li>Each list item usually has a unique value attribute.</li>
	<li>Depending on the list type, we can select either one or several items.</li>
	<li>Lists may look differently: in some cases, all options in the dropdown menu may be hidden (<a href="http://suninjuly.github.io/selects1.html" rel="nofollow noopener noreferrer" target="_blank">http://suninjuly.github.io/selects1.html</a>), while in other cases, the options or some of them may be visible&nbsp;(<a href="http://suninjuly.github.io/selects2.html" rel="nofollow noopener noreferrer" target="_blank">http://suninjuly.github.io/selects2.html</a>).</li>
</ol>

<p>However, we will use the same Selenium methods to interact with any list types.</p>

<p>&nbsp;</p>

<p>Let's see what the html code for lists looks like:</p>

<pre>
<code class="language-html">
&lt;label for="dropdown"&gt;Choose a programming language:&lt;/label&gt;
&lt;select id="dropdown" class="custom-select"&gt;
 &lt;option selected&gt;--&lt;/option&gt;
 &lt;option value="1"&gt;Python&lt;/option&gt;
 &lt;option value="2"&gt;Java&lt;/option&gt;
 &lt;option value="3"&gt;JavaScript&lt;/option&gt;
&lt;/select&gt;</code></pre>

<p>Answer choices are marked with the option tag, and the value may be absent.&nbsp;They may be chosen with the regular click() method. To do that, you first need to apply the click() method to the element with the select tag to open the list and then click the necessary answer choice:</p>

<pre>
<code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(link)


browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
</code></pre>

<p>The last line may also look as follows:</p>

<pre>
<code class="language-python">browser.find_element(By.CSS_SELECTOR, "[value='1']").click()</code></pre>

<p>That is not the most convenient way, as we need to make an additional click to open the list.</p>

<p>There is a better way, which involves using a special&nbsp;<strong>Select</strong> class from the WebDriver library. First, we need to initialize a new object by passing the WebElement with the select tag to it. Then, you can find any list item with the help of the <strong>select_by_value(value)</strong> method:</p>

<pre>
<code>from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # searching for the element with the text "Python"
</code></pre>

<p>You can also use two other methods: <strong>select.select_by_visible_text(&quot;text&quot;)</strong> and <strong>select.select_by_index(index)</strong>. The former searches for the element by the visible text: e.g., <strong> select.select_by_visible_text(&quot;Python&quot;)</strong>&nbsp;will find &quot;Python&quot; in our example.</p>

<p>The latter method searches for the element by its index. Indices start with zero. In order to find an element with the text &quot;Python&quot;, you need to write <strong>select.select_by_index(1)</strong> because the item with the 0 index in our case has the default value of &quot;--&quot;.</p>
