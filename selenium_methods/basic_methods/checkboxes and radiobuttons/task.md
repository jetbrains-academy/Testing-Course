<h2>Working with checkboxes and radiobuttons</h2>

<p>Checkbox and radiobutton are commonly used form elements.
The main difference between them is that checkboxes allow you to select/deselect any amount of the presented options,
while radio buttons allow you to select only one of the options.</p>

<p>checkboxes:</p>

<p><img alt="" src="https://ucarecdn.com/417d5b2f-e732-4128-a8f7-e0342f205565/" /></p>

<p>radiobuttons:<br />
<img alt="" src="https://ucarecdn.com/e3804c8d-769e-4794-9964-b5b3d8360e3d/" /><br />

Both of these elements are created using the HTML `<input>` tag with the type attribute set to "checkbox" or "radio," respectively. 
In the HTML code of the page, you will see:</p>

<pre>
<code class="language-html">&lt;input type="checkbox"&gt;
&lt;input type="radio"&gt;</code></pre>

<p>
If a checkbox or radiobutton is selected, the element will have a new attribute called "checked" without a value.
Often, the "checked" attribute is already set for one of the elements by default.</p>

<pre>
<code class="language-html">&lt;input type="checkbox" checked&gt;
&lt;input type="radio" checked&gt;
</code></pre>

<p>Radiobuttons are grouped together, where all elements have the same value for the "name" attribute but different values for the "value" attribute.</p>

<pre>
<code class="language-html">&lt;input type="radio" name="language" value="python" checked&gt;
&lt;input type="radio" name="language" value="selenium"&gt;
</code></pre>

<p>Checkboxes can have both the same and different values for the "name" attribute. Therefore, both types are best identified using the "id" value or the "value" attribute value. If you see a checkbox on the page with a unique "name" value, you can also search by the "name" attribute.</p>

<p>To uncheck/check a checkbox element or select an option from a group of radiobuttons, you need to specify a WebDriver method to locate the element and then execute the click() method on the found element:</p>

<pre>
<code class="language-python">option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
option1.click()</code></pre>

You may also see a `<label>` tag next to an `<input>` element. 
This tag is used to make the text displayed next to the checkbox clickable.
The text is enclosed within the `<label>` tag. The `<label>` element is associated with the `<input>` element using the "for" attribute, where the value of the "for" 
attribute corresponds to the "id" attribute value of the `<input>` element:

<pre>
<code class="language-html">&lt;div&gt;
  &lt;input type="radio" id="python" name="language" checked&gt;
  &lt;label for="python"&gt;Python&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
  &lt;input type="radio" id="java" name="language"&gt;
  &lt;label for="java"&gt;Java&lt;/label&gt;
&lt;/div&gt;</code></pre>

In this case, you can also select the desired item using WebDriver by executing the `click()`
method on the `<label>` element:


This action will have the same effect as clicking on the associated `<input>` element with the specified "id" value.</p>

<pre>
<code>option1 = browser.find_element(By.CSS_SELECTOR, "[for='java']")
option1.click()</code></pre>
