<h2>Choosing a test runner</h2>

<p>In the previous steps, we've learned to write simple tests and run them with Python. Let's remember the test code and the results of test running from the previous step.</p>

<p><strong>test_abs_project.py:</strong></p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")

</code></pre>

<p>Console:</p>

<pre><code>
$ python test_abs_project.py

Traceback (most recent call last):

  File "test_project.py", line 9, in &lt;module&gt;

    test_abs2()

  File "test_project.py", line 5, in test_abs2

    assert abs(-42) == -42, "Should be absolute value of a number"

AssertionError: Should be absolute value of a number
</code></pre>

<p>Let's look at the drawbacks of such an approach to test running:</p>

<ul>
	<li>When the number of tests gets large, it becomes difficult to run the tests only from the necessary test suites.</li>
	<li>For each test, we need to create separate test data and an environment. For example, if we want to start the browser for each test and then close it after completing the test, we'll need to duplicate that logic in the code of each test.</li>
	<li>If one of the tests finishes with an error (for example, a test will fail with AssertionError), the subsequent tests won't run. We can't know if there were problems in those tests until we fix the failed test or run the remaining tests separately.</li>
</ul>

<p>To solve these problems and to facilitate test writing and running, there are special frameworks called test runners. We can mention three major test frameworks for Python: <strong>unittest</strong>, <strong>PyTest</strong>, and <strong>nose</strong>. The <strong>unittest</strong> module is a built-in Python tool — and that is its great advantage. <strong>PyTest</strong> and <strong>nose</strong> are installed separately, and compared with <strong>unittest</strong>, they allow more opportunities. We'll take a brief look at the use of <strong>unittest</strong> and then study the features of <strong>PyTest</strong>, which allows writing simpler test code compared with <strong>unittest</strong> and flexibly setting up test running. Another advantage of <strong>PyTest</strong> is that there are more plugins written for it – they allow solving practically any problem connected with running automated tests.</p>