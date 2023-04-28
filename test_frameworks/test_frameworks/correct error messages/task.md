<h2>Compound error messages </h2>

<p>Another thing we need to focus on is the quality of the error messages appearing when tests fail. Why is that important? A well-written text helps quickly locate the bug and figure out what has happened and why the test failed. A good assert will save you hours of work, especially when the number of tests is over a hundred.</p>

<p>Generally speaking, it's like with any feedback: it should be precise and timely. If you're checking for the presence of an element, make sure to write what kind of element it is: </p>

<pre><code class="language-python">assert self.is_element_present('create_class_button', timeout=30), "No create class button"</code></pre>

<p><em>Note: The is_element_present() function is auxiliary. Later we'll talk about how to realize and implement it.</em></p>

<p>If the element appears on several pages of the application, indicate where exactly the error occurred: </p>

<pre><code class="language-python">assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"</code></pre>

<p>If you're working with some text (e.g., checking an information message, current URL, link, placeholder in an input element, or any other text), mention both values in the error message: the one you expected and the one you actually received. Like in a good bug report: the expected and actual result.</p>

<h3>Formatting strings with concatenation</h3>

<p>In Python, you can do that with concatenation, for example:</p>

<pre><code class="language-python">actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")</code></pre>

<p>However, due to the abundance of quotes, pluses, et., that way is not really convenient and looks messy.</p>

<h3>Formatting strings with str.format</h3>

<p>A better option is shaping the text with Python's formatting features. You can read about it in more detail here: <a href="https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat" rel="noopener noreferrer nofollow">https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat</a>.</p>

<p>In short, Python can insert the user's values in strings with the help of the <strong>.format()</strong> function. The syntax looks as follows:</p>

<pre><code class="language-python">"Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")</code></pre>

<p>Try running it in the interpreter:</p>

<pre><code class="language-python">print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))</code></pre>

<p>With code execution, such a string will turn into: </p>

<pre><code class="language-no-highlight">Let's count together: one, then goes two, and then three</code></pre>

<p>Thus, we can conveniently combine the expected and the actual values in one string.</p>

<h3>Formatting strings with f-strings</h3>

<p>Finally, the most up-to-date method of string formatting, which appeared in Python3.6, is called f-strings. It allows executing Python expressions right within the string and is even more concise and convenient. To use the features of  f-strings, prefix the string with the f symbol in the following way: f"your string {my_var}". In curly brackets, put the name of the variable, the value that must be used in the string, or the expression the result of which should also appear in the string.</p>

<p>You can read in more detail about f-strings here: <a href="https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36" rel="noopener noreferrer nofollow">https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36</a>. As we assume that you're using the latest Python version, we recommend applying that approach in our course.</p>

<p>Example 1:</p>

<pre><code class="language-python">str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")</code></pre>

<p>The result of execution in the interpreter:</p>

<pre><code class="language-no-highlight">Let's count together: one, then goes two, and then three</code></pre>

<p>Example 2:</p>

<pre><code class="language-python">actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"
</code></pre>

<p>The result of execution in the interpreter:</p>

<pre><code class="language-no-highlight">Wrong text, got abrakadabra, something wrong</code></pre>

<p>Example 3:</p>

<pre><code class="language-no-highlight">&gt;&gt;&gt; f"{2+3}"
'5'</code></pre>

<p> </p>

<p>Another important thing: when you're working with the text of an element on a page or with any other content that may change, always write it into a separate variable for the sake of comparison. </p>

<p><span style="color: #ff4363;"><strong>Incorrect: </strong></span></p>

<pre><code class="language-python">assert self.catalog_link.text  == "Catalog", \
    f"Wrong language, got {self.catalog_link.text} instead of 'Catalog'" </code></pre>

<p>It's a bad practice to read an attribute twice because the text on the page may change by the second reading and you will receive an irrelevant error text. It's hard to analyze the result of such a test: </p>

<pre><code class="language-python">"Wrong language, got 'Catalog' instead of 'Catalog'"</code></pre>

<p><span style="color: #66cc66;"><strong>Correct: </strong></span></p>

<pre><code class="language-python">catalog_text = self.catalog_link.text # reading the text and writing it into a variable
assert catalog_text == "Catalog", \
    f"Wrong language, got {catalog_text} instead of 'Catalog'"  </code></pre>