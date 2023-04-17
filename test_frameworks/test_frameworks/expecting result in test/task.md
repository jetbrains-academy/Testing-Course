<h2>Checking for expected result</h2>

<p>How can we check for the expected result? We can use Python's built-in <strong>assert</strong> instruction, which checks the validity of statements. <strong>assert True</strong> does not result in the output of additional messages, while <strong>assert False</strong> will throw an exception: <strong>AssertionError</strong>.</p>

<p>Let's discuss the functioning of assert using an example with the built-in function <strong>abs</strong>(), which returns the absolute value of a number. First, activate the previously created virtual environment and run the Python interpreter. </p>


<p>Now, we'll be entering the below commands and looking at the results of execution.</p>

<p>If the expression value is true, there won't be any additional messages in the console. Let's try:</p>

<pre><code>&gt;&gt;&gt; assert abs(-42) == 42

</code></pre>

<p>If the condition has not been met, you'll see the error log in the console – with the name of the file, the number of the line where the error occurred, and the error type <strong>AssertionError</strong>:</p>

<pre><code>
&gt;&gt;&gt; assert abs(-42) == -42

Traceback (most recent call last):

  File "&lt;stdin&gt;", line 1, in &lt;module&gt;

AssertionError
</code></pre>

<p>The plain message <strong>AssertionError</strong> is not very informative. When there are lots of tests, it may be difficult to remember what exactly we are checking in a given test. To add an additional message, you can call assert with the necessary message text after a comma; the message will be displayed if there's an error in the result checking:</p>

<pre><code>
&gt;&gt;&gt; assert abs(-42) == -42, "Should be absolute value of a number"

Traceback (most recent call last):

  File "&lt;stdin&gt;", line 1, in &lt;module&gt;

AssertionError: Should be absolute value of a number
</code></pre>

<h2 style="text-align: center;"> </h2>