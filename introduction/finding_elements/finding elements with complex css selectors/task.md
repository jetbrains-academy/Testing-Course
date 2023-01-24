<h2>Поиск элементов с помощью составных CSS-селекторов</h2>

<p>Теперь предположим, что не можем найти элемент на странице, используя простой селектор, так как такой селектор находит сразу несколько элементов. Ниже мы привели часть кода простой HTML-страницы, описывающей блог. Саму страницу вы можете посмотреть по <a href="http://suninjuly.github.io/blog_example.html" rel="noopener noreferrer nofollow">ссылке</a>.</p>

<p>Вопрос: как нам найти селектор для подписи у второй картинки? Вот здесь нам поможет иерархическая структура страницы и возможность комбинировать CSS-селекторы. CSS-селекторы позволяют использовать одновременно любые селекторы, рассмотренные ранее, а также имеют некоторые дополнительные возможности для уточнения поиска.</p>

<pre>
<code class="language-html">&lt;div id="posts" class="post-list"&gt;
  &lt;div id="post1" class="item"&gt;
    &lt;div class="title"&gt;Как я провел лето&lt;/div&gt;
    &lt;img src="./images/summer.png"&gt;
  &lt;/div&gt;
  &lt;div id="post2" class="item"&gt;
    &lt;div class="title second"&gt;Ходили купаться&lt;/div&gt;
    &lt;img src="./images/bad_dog.jpg"&gt;
  &lt;/div&gt;
  &lt;div id="post3" class="item"&gt;
    &lt;div class="title"&gt;С друзьями&lt;/div&gt;
    &lt;img src="./images/friends.jpg"&gt;
  &lt;/div&gt;
&lt;/div&gt;
</code></pre>

<p><strong>Использование потомков</strong></p>

<p>Попробуем найти элемент с текстом &quot;Ходили купаться&quot;. Для решения этой задачи мы можем взять элемент, стоящий выше в иерархии нужного нам элемента, и написать следующий селектор:</p>

<p><code>#post2 .title</code></p>

<p>Здесь символ <code><strong>#</strong></code> означает, что надо искать элемент с id <code>post2</code>, пробел - что также нужно найти элемент-потомок, а <code><strong>.</strong></code>, что элемент-потомок должен иметь класс со значением <code>title</code>.</p>

<p>Элемент <code>.title</code> называется <strong>потомком</strong> (англ. <strong>descendant</strong>) элемента <code>#post2</code>. Потомок может находиться на любом уровне вложенности, все элементы с селектором <code>.title</code> также являются и потомками элемента <code>#posts</code>, хотя и расположены от него на два уровня ниже. <code>#posts .title</code> найдет все 3 элемента с классом <code>title</code>.</p>

<p><span style="color:#ff4363">!Внимание.</span> Символ пробела &quot; &quot; является значащим в CSS-селекторах. Это важный символ, который разделяет описание предка и потомка. Если бы мы записали селектор <code>#post2.title</code> без пробела, то в данном примере не было найдено ни одного элемента. Такая запись означала бы, что мы хотим найти элемент, который одновременно содержит id &quot;post2&quot; и класс &quot;title&quot;. Таким образом <code>#post2 .title</code> и <code>#post2.title</code> &mdash; это разные селекторы<strong>.</strong></p>

<p><strong>Использование дочерних элементов</strong></p>

<p>Другой способ найти этот элемент:</p>

<p><code>#post2 &gt; div.title</code></p>

<p>Здесь мы указали еще тег элемента <code>div</code><strong> </strong>и уточнили, что нужно взять элемент с тегом и классом: <code>div.title</code>, который находится строго на один уровень иерархии ниже чем элемент <code>#post2</code>. Для этого используется символ <code>&gt;</code>.</p>

<p>Элемент <code>#post2</code> в этом случае называется <strong>родителем</strong> (англ. <strong>parent</strong>) для элемента<strong> </strong><code>div.title</code>, а элемент <code>div.title</code> называется <strong>дочерним элементом</strong> (англ. <strong>child</strong>) для элемента <code>#post2</code>. Если символа <code>&gt;</code> нет, то будет выполнен поиск всех элементов <code>div.title</code> на любом уровне ниже первого элемента.</p>

<p><span style="color:#ff4363">!Внимание. </span>В данном случае символы пробела вокруг символа &quot;&gt;&quot; не несут важного значения в отличие от предыдущего примера, и могут быть опущены. Запись <code>#post2&gt;div.title</code><strong> </strong>аналогична записи <code>#post2 &gt; div.title</code>.</p>

<p><strong>Использование порядкового номера дочернего элемента</strong></p>

<p>Еще один способ найти этот элемент:</p>

<p><code>#posts &gt; .item:nth-child(2) &gt; .title</code></p>

<p>Псевдо-класс <code>:nth-child(2)</code> &mdash; позволяет найти второй по порядку элемент среди дочерних элементов для <code>#posts</code>. Затем с помощью конструкции <code>&gt; .title</code> мы указываем, что нам нужен элемент <code>.title</code>, родителем которого является найденный ранее элемент <code>.item</code>.</p>

<p><strong>Использование нескольких классов</strong></p>

<p>Также мы можем использовать сразу несколько классов элемента, чтобы его найти. Для этого классы записываются подряд через точку: <code>.title.second</code></p>

<p>Мы рассмотрели базовые селекторы, которых будет достаточно для написания простых UI-тестов. Если вы захотите разобраться подробнее в css-селекторах, то мы рекомендуем вам посмотреть следующие статьи:</p>

<p><a href="https://learn.javascript.ru/css-selectors" rel="nofollow noopener noreferrer">https://learn.javascript.ru/css-selectors</a></p>

<p><a href="https://www.w3schools.com/cssref/css_selectors.asp" rel="nofollow noopener noreferrer">https://www.w3schools.com/cssref/css_selectors.asp</a></p>

<p><a href="https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors" rel="nofollow noopener noreferrer">https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors</a></p>
