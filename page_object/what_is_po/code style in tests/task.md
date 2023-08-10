<h2>Code Style in autotests</h2>

<p>Here we tried to summarize the important principles of autotest writing: </p>

<ul>
	<li>Aim at maximum linearity of test code: avoid branches and cycles in test cases. If you feel like adding an "if" statement, better divide the test into two or arrange the test environment so that you won't need branching.</li>
	<li>Avoid dependent tests, which need to be run in a specific order. 
As the number of autotests grows, you will want to run them in parallel,
which is impossible if you have dependent tests.
Besides, dependent tests are quite unreliable.</li>
	<li>Try to write tests that do not rely on a content but rather prepare data on their own (and delete it after execution). Use clear browsers and new users for better reproducibility.</li>
	<li>Mind absolute linearity in tests. When you write an assert statement in a function, do not use branches or cycles. Test logic must be linear; otherwise, bug analysis and autotest fixing will be quite expensive.</li>
	<li>Use a consistent style in naming your checks so that it would be immediately clear that a check is a check. For example, you can use the should_be_smth pattern in function naming:
	<pre><code>def should_be_reply_comment()</code></pre>
	</li>
	<li>Tests should be named in a similar style. Test names need to clearly reflect differences in similar scenarios. You can use the same approach you do when adding names to test cases in test documentation. For example, <code>test_guest_can_see_teach_button()</code> — notice the explicitly indicated user role.</li>
	<li>Similar tests differing only in some content (for example, the interface language) should be parametrized rather than copied.</li>
	<li>Write maximally indivisible and atomic tests. Don't try to write a single mega-test, which checks absolutely everything. Better write a dozen of small ones – it will be easier to localize the problem when it occurs.</li>
</ul>

<p>In case you do not have sufficient experience in code writing, you can use the links below to find articles with additional code style recommendations.</p>

<p>In English:</p>

<p><a href="https://docs.python-guide.org/writing/style/" rel="noopener noreferrer nofollow">https://docs.python-guide.org/writing/style/</a></p>

<p><a href="https://www.python.org/dev/peps/pep-0008/" rel="noopener noreferrer nofollow">https://www.python.org/dev/peps/pep-0008/</a></p>
