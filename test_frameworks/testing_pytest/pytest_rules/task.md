<h2><strong>PyTest: rules of test running</strong></h2>

<p>In this step, we will briefly discuss several important aspects of running tests with PyTest. When we execute the <strong>pytest</strong> command, the test runner collects all the tests to be run according to specific rules:</p>

<ul>
	<li>
	<p>If we don't pass any arguments in the command and simply type pytest, the test runner will start looking for tests in the current directory.</p>
	</li>
	<li>
	<p>We can pass a file, directory path, or any combination of directories and files as an argument, for example: </p>
	</li>
</ul>

<pre><code class="language-python">pytest scripts/selenium_scripts
# find all tests in the directory scripts/selenium_scripts

pytest test_user_interface.py
# find and run all tests in a file

pytest scripts/drafts.py::test_register_new_user_parametrized
# find the test named test_register_new_user_parametrized in the specified file in the specified directory and run it
</code></pre>

<ul>
	<li>
	<p>Then PyTest proceeds to recursive search: it will go through all nested directories.</p>
	</li>
	<li>
	<p>In all the directories, PyTest looks for files that satisfy the rule <strong>test_*.py</strong> or <strong>*_test.py</strong> (i.e., start with test_ or end with _test and have the .py extension).</p>
	</li>
	<li>
	<p>In all these files, PyTest finds test functions according to the following rule:</p>

	<ul>
		<li>
		<p>all the tests with names starting with <strong>test</strong> that are located outside classes</p>
		</li>
		<li>
		<p>all the tests with names starting with <strong>test</strong> inside classes with names starting with <strong>Test</strong> (and without the __init__ method within the class)</p>
		</li>
	</ul>
	</li>
</ul>

<p>Details: <a href="https://docs.pytest.org/en/stable/goodpractices.html#conventions-for-python-test-discovery" rel="noopener noreferrer nofollow">Conventions for Python test discovery</a></p>
