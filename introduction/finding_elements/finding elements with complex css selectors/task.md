<h2>Finding elements with complex CSS selectors</h2>

<p>Now, let's imagine that we cannot find an element on a page using a simple selector, as such a selector finds several elements at once. Below, you can see a part of the code of a simple HTML page describing a blog. You can find the page <a href="http://suninjuly.github.io/blog_example.html" rel="noopener noreferrer nofollow">here</a>.</p>

<p>Question: how can we find a selector for the title of the second image? Here, the hierarchic page structure and the possibility of combining CSS selectors come to the resque. CSS selectors allow simultaneously using any previously considered selectors; besides, they have some additional options for fine search.</p>

<pre>
<code class="language-html">&lt;div id="posts" class="post-list"&gt;
  &lt;div id="post1" class="item"&gt;
    &lt;div class="title"&gt;My summer vacations&lt;/div&gt;
    &lt;img src="./images/summer.png"&gt;
  &lt;/div&gt;
  &lt;div id="post2" class="item"&gt;
    &lt;div class="title second"&gt;After bathing
&lt;/div&gt;
    &lt;img src="./images/bad_dog.jpg"&gt;
  &lt;/div&gt;
  &lt;div id="post3" class="item"&gt;
    &lt;div class="title"&gt;With friends&lt;/div&gt;
    &lt;img src="./images/friends.jpg"&gt;
  &lt;/div&gt;
&lt;/div&gt;
</code></pre>

<p><strong>Using descendants</strong></p>

<p>Let's try to find the element with the text &quot;After bathing&quot;. To solve that task, we can take the element located above the needed element in the hierarchy. We can write the following selector:</p>

<p><code>#post2 .title</code></p>

<p>Here, the <code><strong>#</strong></code> symbol means that we are looking for the element with the <code>post2</code> id; the space means that we also need to find the descendant element; and <code><strong>.</strong></code> signifies that the descendant element must be of the <code>title</code> class.</p>

<p>The <code>.title</code> element is called a <strong>descendant</strong> of the <code>#post2</code> element. A descendant may be located on any nesting level; all elements with the <code>.title</code> selector are also descendants of the element <code>#posts</code>, even though they are two levels below it. <code>#posts .title</code> will find all 3 elements with the class <code>title</code>.</p>

<p><span style="color:#ff4363">!Important.</span> The space symbol (&quot; &quot;) is meaningful in CSS selectors. It is an important symbol that separates the descriptions of the ancestor and the descendant. If we wrote the selector <code>#post2.title</code> without a space, we wouldn't find any elements in the given example. It would mean that we want to find an element that contains both the &quot;post2&quot; id and the &quot;title&quot; class. Thus, <code>#post2 .title</code> and <code>#post2.title</code> are different selectors<strong>.</strong></p>

<p><strong>Using child elements</strong></p>

<p>Here's another way to find that element:</p>

<p><code>#post2 &gt; div.title</code></p>

<p>Here we mention the element's tag <code>div</code><strong> </strong>and specify that we need an element with a tag and a class <code>div.title</code> that is located exactly one hierarchy level lower than the element <code>#post2</code>. For that purpose, the <code>&gt;</code> symbol is used.</p>

<p>In this case, the element <code>#post2</code> is called the <strong>parent</strong> of the element <strong> </strong><code>div.title</code>, and the <code>div.title</code> element is called the <strong>child</strong> of the <code>#post2</code> element. If the <code>&gt;</code> symbol is absent, the search will look for all <code>div.title</code> elements at any level below the first element.</p>

<p><span style="color:#ff4363">!Important. </span>In this case, unlike the previous one, the spaces around the &quot;&gt;&quot; symbol do not have any particular significance and may be omitted. Thus, <code>#post2&gt;div.title</code><strong> </strong>does the same as <code>#post2 &gt; div.title</code>.</p>

<p><strong>Using the number of the n-th child element</strong></p>

<p>Here's yet another method to find that element:</p>

<p><code>#posts &gt; .item:nth-child(2) &gt; .title</code></p>

<p>The pseudo-class <code>:nth-child(2)</code> allows finding the second child element for <code>#posts</code>. Then, with the help of the <code>&gt; .title</code> construction, we identify that we need the element <code>.title</code>, which has the previously found element <code>.item</code> as its parent.</p>

<p><strong>Using several classes</strong></p>

<p>To find an element, we can also use several of its classes simultaneously. To do that, separate the classes with a dot: <code>.title.second</code>.</p>

<p>We have discussed the basic selectors, which will be enough to write simple UI tests. If you want to learn more about CSS selectors, we recommend checking out the following sources:</p>

<p><a href="https://www.w3schools.com/cssref/css_selectors.asp" rel="nofollow noopener noreferrer">https://www.w3schools.com/cssref/css_selectors.asp</a></p>

<p><a href="https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors" rel="nofollow noopener noreferrer">https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors</a></p>
