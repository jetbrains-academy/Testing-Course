<h2>Uploading files</h2>

<p>﻿In case we need to upload a file on a web page, we can use the already familiar send_keys method. However, instead of plain text, we now need to pass the file path as an argument.</p>

<p>To indicate the file path, we can use the standard Python module for working with an operating system — <strong>os</strong>. In such a case, your code won't depend on the operating system you are using. It will work with Windows, Linux, and even with MaсOS.</p>

<p>Here is a sample code that allows defining the path to the <strong> 'file.txt</strong>' file located in the same folder as the script you are launching:</p>

<pre><code class="language-python">import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # getting the path to the directory of the current executable file 
file_path = os.path.join(current_dir, 'file.txt')           # adding the file name to the path 
element.send_keys(file_path)</code></pre>

<p>Now try adding the separate commands <code><samp><strong>print(os.path.abspath(__file__))</strong> </samp></code> and <code><samp><strong>print(os.path.abspath(os.path.dirname(__file__)))</strong></samp></code> to the file and see the difference. You can read about the <strong>os</strong> module methods on your own in the documentation: <a href="https://docs.python.org/3/library/os.path.html" rel="noopener noreferrer nofollow">https://docs.python.org/3/library/os.path.html</a>. Notice that that will only work when you launch the code from a file; it won't work in an interpreter.</p>

<p>In case you totally fail to understand what's going on, here's an example: </p>

<p>Let's say we've written a script and saved it in <em>lesson2_step7.py</em> in our local folder <em>D:\stepik_homework. </em>Let's activate the virtual environment and launch  <strong>python lesson2_step7.py. </strong>Now, the  <strong>os.path.abspath(os.path.dirname(__file__)) </strong>command will return the path to the directory of the file with the code, i.e.,  <em>D:\stepik_homework</em><strong>. </strong>Let's put the file we want to attach (<em>file.txt</em>) to the same folder.</p>

<p><code>file_path = os.path.join(current_dir, 'file.txt')</code></p>

<p>If we run the above command, the <em>file_path</em>  variable will contain the full path to the file '<strong>D:\stepik_homework\file.txt'</strong>. An interesting thing is that if we move the files of  <em>lesson2_step7.py </em>together with <em> file.txt </em>to a different folder or even to a computer with a different OS, the code will still work without any alterations.</p>

<p> </p>

<p>The form element that looks like a file upload button has an attribute <strong> type="file"</strong>. We must first find that element with the help of a selector and then apply the method <strong>send_keys(file_path)</strong> to it.</p>
