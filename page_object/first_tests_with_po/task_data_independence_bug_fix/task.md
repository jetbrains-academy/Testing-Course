<h2>Task: content independence, finding a bug</h2>

<p>Once you've found the bug,
considering that it won't be fixed,
it's best to mark the failing test as <strong>xfail</strong>&nbsp;or <strong>skip.&nbsp;</strong>Remember how we did it in Module 3?&nbsp;Refresh your memory: <a href="/lesson/236918/step/5?unit=209305" rel="noopener noreferrer nofollow">XFail: mark the test as expected to fail</a>.</p>

<p>With parameterization, it's done like this:&nbsp;&nbsp;</p>

<pre>
<code class="language-python">@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])</code></pre>

<p>More details here:&nbsp;<a href="https://pytest.org/en/stable/skipping.html#skip-xfail-with-parametrize" rel="noopener noreferrer nofollow">Skip/xfail with parametrize</a></p>
