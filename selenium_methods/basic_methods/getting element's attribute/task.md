<h2>The get_attribute method</h2>

<p>We already know how to find the necessary element on a page and how to get a text visible to the reader. For more detailed tests, we may need to learn the value of the element attribute. Attributes may be standard properties understood and used by the browser to display and format elements and keep the technical data, for example, name, width, height, color, and <a href="https://www.w3schools.com/tags/ref_attributes.asp" rel="nofollow noopener noreferrer">other</a>. Besides, attributes may be created by project developers to set their own styles and rules.</p>

<p>The attribute value is a string. If the value is absent, that is equal to the attribute value &quot;false&quot;.&nbsp;Let's look at the page <a href="http://suninjuly.github.io/math.html" rel="nofollow noopener noreferrer">http://suninjuly.github.io/math.html</a> again. It has radio buttons with default values. In the automated test, we may need to check that one of the&nbsp;radio buttons&nbsp;has a checked default value. To do that, we can check the value of the "checked" attribute of this element. Here's the element's HTML code:</p>

<pre>
<code class="language-python">&lt;input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked&gt;</code></pre>

<p>Let's find this element with WebDriver:</p>

<pre>
<code class="language-python">people_radio = browser.find_element(By.ID, "peopleRule")</code></pre>

<p>Let's find the &quot;checked&quot; attribute with the built-in method get_attribute and check its value:</p>

<pre>
<code class="language-python">people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"</code></pre>

<p>As this attribute does not have an explicit value, the get_attribute method will return &quot;true&quot;. You've probably noticed that &quot;true&quot; is written with a lowercase "t": all WebDriver&nbsp;methods interact with the browser through JavaScript, and boolean values in JavaScript, unlike Python, are written in lowercase.</p>

<p>We can write the test in a different way and compare the strings:</p>

<pre>
<code class="language-python">assert people_checked == "true", "People radio is not selected by default"
</code></pre>

<p>If there is no attribute, the get_attribute method will return <strong>None</strong>. Let's apply the get_attribute&nbsp;method to the second radio button and make sure that the attribute is absent.</p>

<pre>
<code class="language-python">robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None</code></pre>

<p>Similarly, we can check the presence of the "disabled" attribute, which defines whether the user can interact with the element. For example, in the previous task with a captcha test, JavaScript&nbsp;sets the attribute "disabled" for the <strong>Submit</strong> button when the time allocated for solving the task expires.</p>

<pre>
<code class="language-html">&lt;button type="submit" class="btn btn-default" disabled&gt;Submit&lt;/button&gt;</code></pre>
