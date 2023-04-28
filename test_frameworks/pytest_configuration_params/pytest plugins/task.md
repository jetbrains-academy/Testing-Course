<h2>Plugins and test reruns</h2>

<p>There are lots of <a href="https://docs.pytest.org/en/latest/explanation/flaky.html?highlight=plugins#plugins" rel="nofollow noopener noreferrer" title="Link: https://docs.pytest.org/en/latest/plugins.html">plugins</a> written for PyTest – additional modules expanding the capacities of the framework. You can find the complete list of available plugins <a href="https://docs.pytest.org/en/latest/reference/plugin_list.html" rel="nofollow noopener noreferrer">here</a>.</p>

<p>Let's consider one more problem that you are sure to encounter when writing Selenium end-to-end tests. It's about flaky tests, i.e., tests that may sometimes fail because of circumstances beyond our control or low-reproducibility bugs, even though at other times they pass successfully. That may happen during the test because of simultaneously proceeding site updates, network problems, or unfortunate coincidences. Of course, one needs to try to avoid such problems and look for the reasons behind bugs, but in real life it may require excessive efforts. That's why we will restart a failed test to make sure that it really found a bug and did not fail accidentally.</p>

<p>That's quite easy to do. We will use the <strong>pytest-rerunfailures</strong> plugin.</p>

<p>First, we'll install the plugin in our virtual environment. After installation, PyTest will automatically find the plugin and we will be able to use its functionality without additional code modifications.:</p>

<pre><code class="language-bash">pip install pytest-rerunfailures</code></pre>

<p>In order to indicate the number of reruns for each failed test, we need to add the following parameter in the command line:</p>

<p><strong>"--reruns n"</strong>, where n  is the number of reruns. If the rerun test passes successfully, the whole test run will be considered successful. The number of reruns is shown in the report, which allows a subsequent analysis of problematic tests.<br>
We've additionally indicated the <strong>"--tb=line"</strong> parameter to make the test results log shorter. You can read more about the output setup in the <a href="https://docs.pytest.org/en/stable/usage.html#modifying-python-traceback-printing" rel="noopener noreferrer nofollow">PyTest documentation</a>:</p>

<pre><code class="language-bash">pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py</code></pre>

<p>Let's write two tests: one that will pass and the other that will fail. It will show how reruns look.</p>

<p><strong>test_rerun.py:</strong></p>

<pre><code class="language-python">link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")</code></pre>

<p>We'll see a message: "1 failed, 1 passed, 1 rerun in 9.20s﻿", which means that the failed test was rerun but failed again in the second run. If the flaky test had passed successfully at the second attempt, we would have seen the following message: ﻿﻿"2 passed, 1 rerun in 9.20s"﻿, and the ultimate result of all the tests would have been successful.</p>