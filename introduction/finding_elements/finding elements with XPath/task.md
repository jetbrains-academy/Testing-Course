<h2>Finding elements with XPath</h2>

<p>When working with web pages, we can't always find a selector unambiguously describing the path to the required element. In such cases, the best solution would be talking to the front-end developer of the project and agreeing on a special attribute that will be used in automated tests. This way, you can increase the testability of the application. However, projects vary, and it's not always possible to do that. When there is no other solution for automating your tests, you can use the&nbsp;<strong>XPath</strong> query language.</p>

<p>There are different opinions as regards XPath. However, it is a powerful and versatile tool, which allows writing complex queries to find elements.</p>

<p>First of all, XPath (XML Path Language) is a query language that uses the tree structure of a document. You can check XPath queries the same way as CSS selectors&nbsp;&mdash; in the developer console. Let's open the console at the cats page <a href="http://suninjuly.github.io/cats.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/cats.html</a> and use it to figure out the syntax basics. Try typing each of the example queries in the search box and see what exactly will be found.</p>

<h3>&nbsp;1. XPath query always starts with the / or // symbol</h3>

<p>The / symbol is similar to the &gt; symbol in CSS selectors, and the // symbol is similar to a space. Here's how they work:</p>

<ul>
	<li>el1/el2&nbsp;&mdash; chooses the elements el2 that are direct descendants of el1;</li>
	<li>el1//el2&nbsp;&mdash; chooses the elements el2 that are descendants of el1 at any nesting level.</li>
</ul>

<p>The difference is that when we start an XPath query with the / symbol, we need to indicate the element which is the root of our element. The root will always be an element with the <code>&lt;html&gt;</code> tag. For example: <code>/html/body/header</code></p>

<p>We can also start a query from the // symbol. That would mean that we want to find all descendants of the root element without indicating the root element. In such a case, to find the header, we can execute the query&nbsp;<code>//header</code>, as there are no other headers.</p>

<p><span style="color:#ff4363">Important!</span> Such a query may be ambiguous. For example, the <code>//div</code> query will return all elements with the <code>&lt;div&gt;</code> tag. Avoid ambiguous situations – they negatively affect the quality of our automated tests.</p>

<ul>
</ul>

<h3>2. The [ ]&nbsp;symbol&mdash;filtering command</h3>

<p>If a query found several elements, they will be filtered according to the rule indicated in square brackets.</p>

<p>There are lots of filtering rules:</p>

<ul>
	<li>By any <strong>attribute</strong> – id, class, title, or any other. For example, if we want to find the picture with a flying cat, we can write the following query: <code>//img[@id=&#39;bullet&#39;]</code>.</li>
	<li>By <strong>ordinal number</strong>. For example, we want to find the second picture with a cat. To do that, we will find the element with the &quot;row&quot; class and take its second descendant: <code>//div[@class=&quot;row&quot;]/div[2]</code>.</li>
	<li>By <strong>exact text match</strong>. Yes, XPath is the only way to find an element by its inner text. If we want to find the text block with Lenin cat, we can use the XPath selector <code>//p[text()=&quot;Lenin cat&quot;]</code>. Such a selector will return the element only if the text matches exactly. It's important to notice that searching by text is not always a good practice, especially in the case of multilingual sites.</li>
	<li>By <strong>partial text match</strong> in text or attribute. It requires the <code>contains</code> function. The query <code>//p[contains(text(), &quot;cat&quot;)]</code> will return all text paragraphs that contain the word "cat". In a similar manner, we can search by partial match in other attributes; that may be helpful if an element has several classes. Take a look at the navbar code from the site with cats. You can find it with the following selector: <code>//div[contains(@class, &quot;navbar&quot;)]</code>.</li>
	<li>In filtering, we can also use boolean operations (and, or, not) and some simple arithmetic expressions (although it's not recommended). Imagine we want to find a picture with the data-type &quot;animal&quot; and the name &quot;bullet-cat&quot;. The query will be:&nbsp;<code>//img[@name=&#39;bullet-cat&#39; and @data-type=&#39;animal&#39;]</code>.</li>
</ul>

<h3>&nbsp;3.&nbsp; The *&nbsp;symbol&mdash;selecting all elements</h3>


<p>For example, we can find a text in the header with the following query: <code>//div/*[@class=&quot;jumbotron-heading&quot;]</code>. That may be convenient if we do not know for sure the tag of the element we are looking for.</p>


<h3>4. Search by class in XPath is case-sensitive</h3>

<p>Like in the case of CSS selectors, mind the letter case when you search by class:&nbsp;</p>

<p><strong>//div/*[@class=&quot;Jumbotron-heading&quot;]</strong>&nbsp;won't find the element on our page.</p>

<p>&nbsp;</p>

<p>What you need to know about XPath to safely use it:</p>

<ul>
	<li>Do not use selectors like <code>//div[1]/div[2]/div[3]</code> unless it's absolutely necessary: with such a selector, it's not easy to understand what element you are looking for. Besides, when the page changes, even if slightly, your selector will most probably stop working.</li>
	<li>If there's an opportunity to use CSS selectors: class, id, or name&nbsp;&mdash; it's better to use those instead of XPath search.</li>
	<li>You can search by exact or partial match of text or any attribute.</li>
	<li>You can use boolean operations and simple arithmetic.</li>
	<li>You can move through the document structure (to descendants or parents).</li>
	<li>It will work when the site is low on attributes and there's no way to contact the developer.</li>
	<li>There's a possibility that an XPath search is generally slower than search by CSS. However, there's no evidence.</li>
	<li>You shouldn't use different browser extensions in XPath search: they choose illegible and over-complicated selectors. It's better to spend some time and figure out the syntax by yourself – it is not that difficult.</li>
</ul>

<p>In this course, we will work with XPath selectors, but mostly, we will use CSS. If necessary, you can learn more about XPath using the following links:</p>

<p><a href="https://www.w3schools.com/xml/xpath_syntax.asp" rel="nofollow noopener noreferrer" style="font-size: inherit; font-weight: inherit;" title="Link: https://www.w3schools.com/xml/xpath_syntax.asp">https://www.w3schools.com/xml/xpath_syntax.asp</a></p>

<p><a href="https://msdn.microsoft.com/ru-ru/library/ms256086(v=vs.120).aspx" rel="nofollow noopener noreferrer" title="Link: https://msdn.microsoft.com/ru-ru/library/ms256086(v=vs.120).aspx">https://msdn.microsoft.com/ru-ru/library/ms256086(v=vs.120).aspx</a></p>

<p><a href="https://msiter.ru/tutorials/xpath/syntax" rel="nofollow noopener noreferrer" title="Link: https://msiter.ru/tutorials/xpath/syntax">https://msiter.ru/tutorials/xpath/syntax</a></p>

<p><a href="https://habr.com/post/114772/" rel="nofollow noopener noreferrer" title="Link: https://habr.com/post/114772/">https://habr.com/post/114772/</a></p>

<p><a href="https://testerslittlehelper.wordpress.com/2016/07/10/real-xpath/" rel="noopener noreferrer nofollow">https://testerslittlehelper.wordpress.com/2016/07/10/real-xpath/</a></p>
