<h2>Test scenarios</h2>

<p>You need to save the created tests in a file, which is easy to run and keep
in a version control system.
Let's create a file <strong>test_abs_project.py</strong> and write the following code in it:</p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")</code></pre>

<p>We put the test scenario into a function to separate test cases and run them independently.</p>

<p>Without going into details, we'll just say that the <strong>if __name__ == "__main__"</strong> construct is designed to confirm that the script was run directly rather than called within another file as a module. All the code in the body of this condition will be executed only if the user has run the file themselves. You can find more details about it in <a href="https://www.youtube.com/watch?v=cW_-zGG4ef4" rel="noopener noreferrer nofollow" target="_blank">Oleg Molchanov's</a> video. </p>

<p>In that construct, we called the <strong> test_abs1()</strong> function, which executes the test scenario.</p>

<p>With the help of <strong>print("All tests passed!")</strong>, we output a message if all tests pass successively.</p>

<p>To run the test, execute the following command in the console:</p>

<pre><code class="language-bash">python test_abs_project.py</code></pre>

<p>In the console, you will see the message <strong> "All tests passed!"</strong></p>

<p> </p>

<p>If we need to add one more test, we can write it as a function in the same file. In the above example, we won't see the message "Everything passed" anymore, as any test's failure leads to exiting the program:</p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
</code></pre>

<p>Run the file again. You will see a message about the second test's failure:</p>

<pre><code>
$ python test_abs_project.py

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in &lt;module&gt;

    test_abs2()

  File "test_abs_project.py", line 5, in test_abs2

    assert abs(-42) == -42, "Should be absolute value of a number"

AssertionError: Should be absolute value of a number
</code></pre>