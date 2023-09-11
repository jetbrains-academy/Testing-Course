<h2>Task: finalizing fixtures, fixtures returning value</h2>

<p>
In this task, you need to implement two fixture functions – the browser fixture, and the 'answer_file' fixture. 
</p>

The fixture function `answer_file()` should open a file by `'filename'` and return a file object. 
The fixture must close the file after the test passes.

<p>Then implement the pytest test case test_math() with the following steps:</p>

<ol>
	<li>Open the page <a href="https://suninjuly.github.io/math.html" rel="nofollow noopener noreferrer" title="Link: http://suninjuly.github.io/math.html">https://suninjuly.github.io/math.html</a>.</li>
	<li>Read the value of the variable x.</li>
	<li>Calculate the mathematical function of x (the code is provided below).</li>
	<li>Output the answer in the text field.</li>
	<li>Mark the checkbox "I'm a robot".</li>
	<li>Select the radiobutton "Robots rule!"</li>
	<li>Press the Submit button.</li>
    <li>Switch to the alert.</li>
    <li>Read the text from the alert.</li>
    <li>Write the number from the alert text to a file, using the file object from the fixture.</li>
</ol>

<p>Use the calc() function, which will calculate and return the function value, which you need to enter in the text field. Don't forget to insert the following code at the top of your script:</p>

<pre><code>import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))</code></pre>
