<h2>Task: compound error messages and substring search</h2>

<p>Sometimes when working with texts, we do not need strict checks for exact matching – instead, we just need to check that a certain text is a substring of another text. We can do that either with the <strong>in</strong> key word or with the <strong>find</strong> function:</p>

<pre><code>s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
</code></pre>

<p>Try running that code in the interpreter to see the difference in the two approaches.</p>

<p>The <code><samp><strong>'Name' in s</strong></samp></code> construct returns just <strong>True</strong> or <strong>False</strong>, while <strong>find()</strong> returns the index of the first occurrence of the substring in the string; otherwise, if the substring has not been found, it returns -1. In most cases, it's sufficient to use <strong>in</strong> in automated tests because of better readability.</p>

<p>For example, we can check that the current URL contains the string login: </p>

<pre><code>assert "login" in browser.current_url, # error message</code></pre>

<p>Implement such a check yourself. </p>

<p>You are given a template for the <samp><code><strong>test_substring</strong></code></samp> function, which receives two values: <strong>full_string</strong> and <strong>substring</strong>. </p>

<p>The function needs to check for the occurrence of the <strong>substring</strong> in the <strong>full_string </strong>with the help of the <strong>assert</strong> operator and, in the case of a mismatch, provide a comprehensive error message. </p>

<p><strong>Important!</strong> The format of the error should exactly match that in the example so that the checking system accepts it! </p>

<p>You don't need to handle the situation with empty or invalid input. </p>