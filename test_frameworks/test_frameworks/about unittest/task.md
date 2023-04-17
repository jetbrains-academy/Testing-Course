<h2>unittest</h2>

<p>Test runners can find test methods in the files defined at the test start; however, to ensure that, we need to follow common rules. Here is a common rule for all frameworks: the name of a test method must start with the word "test_".  What follows is any text – the unique name of the test:</p>

<pre><code class="language-python">def test_name_for_your_test():</code></pre>

<p>unittest also has its own additional rules:</p>

<ul>
	<li>Tests need to be located in a special test class.</li>
	<li>Instead of assert, we need to use special assertion methods.</li>
</ul>

<p>Now, let's modify our previous tests so that we can run them with unittest. We'll need to execute the following steps:</p>

<ol>
	<li>Import unittest into a file: <strong>import unittest</strong>.</li>
	<li>Create a class that inherits from the TestCase class: <strong>class TestAbs(unittest.TestCase):</strong>.</li>
	<li>Turn test functions into methods by adding a reference to a class copy self as the first argument of the function: <strong>def test_abs1(self):</strong>.</li>
	<li>Change assert to <strong>self.assertEqual()</strong>.</li>
	<li>Change the command of running the program to <strong>unittest.main()</strong>.</li>
</ol>

<pre><code class="language-python">import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
</code></pre>

<p>After all the changes, let's run the file with the tests using Python:</p>

<pre><code class="language-bash">python test_abs_project.py

.F

======================================================================

FAIL: test_abs2 (__main__.TestAbs)

----------------------------------------------------------------------

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in test_abs2

    self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

AssertionError: Should be absolute value of a number

----------------------------------------------------------------------

Ran 2 tests in 0.000s

FAILED (failures=1)</code></pre>

<p>Now we see more detailed information about the results of the run: two tests were run, one test threw an error. The location of the error and comments on it are shown in the log.</p>

<p>In the following lesson, we'll consider the advantages and features of using the <strong>PyTest</strong> test framework. If you want to use <strong>unittest</strong> in your tests, you can study the <a href="https://docs.python.org/3/library/unittest.html" rel="nofollow noopener noreferrer">documentation</a> on your own.</p>