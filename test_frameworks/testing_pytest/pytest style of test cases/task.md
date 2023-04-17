<h2>PyTest — how to write tests</h2>

<p>Unlike unittest, PyTest does not require writing additional specific constructs in tests.</p>

<p>We've already seen that PyTest can run tests written in the unittest style. Let's rewrite our tests from <strong>test_abs_project.py</strong> in a simpler format, which is also understood by PyTest. Let's name the new file test_abs.py:</p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

</code></pre>

<p>Let's run the tests in the file:</p>

<pre><code class="language-python">pytest test_abs.py</code></pre>

<p>Test code has become more concise and readable.</p>