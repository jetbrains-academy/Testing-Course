<h2>Switching between browser tabs</h2>

<p>When working with web applications, we sometimes need to use links that open in a new browser tab. WebDriver can only work with one tab. When a new tab is opened, WebDriver continues working with the old tab. To switch to a new tab, we need to indicate which tab we want to use. You can do that with the switch_to.window command:</p>

<pre><code class="language-python">browser.switch_to.window(window_name)</code></pre>

<p>To find out the name of the new tab, use the window_handles method, which returns an array of all tab names. As we know that the browser now has two open tabs, we can choose the second one:</p>

<pre><code class="language-python">new_window = browser.window_handles[1]</code></pre>

<p>We can also take notice of the first tab's name so that we can return to it later:</p>

<pre><code class="language-python">first_window = browser.window_handles[0]</code></pre>

<p>After we have switched to a new tab, the search and the interaction with elements will proceed on a new page.</p>
