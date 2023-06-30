<h2>Task: finalizing fixtures, fixtures returning value</h2>

<p>
In this task you need to implement two fixture functions - browser fixture, and 'answer_file' fixture. 
</p>

Fixture function `answer_file()` should open file by `'filename'` and return file object. 
Fixture must close the file after test passes.

<p>Then implement pytest test case test_math() with the following steps:</p>

<ol>
	<li>Open the page <a href="https://suninjuly.github.io/math.html" rel="nofollow noopener noreferrer" title="Link: http://suninjuly.github.io/math.html">https://suninjuly.github.io/math.html</a>.</li>
	<li>Read the value of the variable x.</li>
	<li>Calculate the mathematical function of x (the code is provided below).</li>
	<li>Output the answer in the text field.</li>
	<li>Mark the checkbox "I'm a robot".</li>
	<li>Select the radiobutton "Robots rule!"</li>
	<li>Press the Submit button.</li>
    <li>Switch to alert</li>
    <li>Read text from alert</li>
    <li>Write number from alert text to file, using file object from fixture</li>
</ol>

<p>Use the calc() function, which will calculate and return the function value, which you need to enter in the text field. Don't forget to insert the following code at the top of your script:</p>

<pre><code>import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))</code></pre>
