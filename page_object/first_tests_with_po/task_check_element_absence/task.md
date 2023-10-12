<h2>Задание: отрицательные проверки</h2>

<p>Добавьте к себе в проект функции из предыдущего шага и реализуйте несколько простых тестов: </p>

<pre><strong>test_guest_cant_see_success_message_after_adding_product_to_basket: </strong></pre>

<ol>
	<li>Открываем страницу товара </li>
	<li>Добавляем товар в корзину </li>
	<li>Проверяем, что нет сообщения об успехе с помощью<strong> is_not_element_present</strong></li>
</ol>

<p> </p>

<pre><strong>test_guest_cant_see_success_message</strong><strong>: </strong></pre>

<ol>
	<li>Открываем страницу товара </li>
	<li>Проверяем, что нет сообщения об успехе с помощью <strong>is_not_element_present</strong></li>
</ol>

<p> </p>

<pre><strong>test_message_disappeared_after_adding_product_to_basket: </strong></pre>

<ol>
	<li>Открываем страницу товара</li>
	<li>Добавляем товар в корзину</li>
	<li>Проверяем, что нет сообщения об успехе с помощью <strong>is_disappeared</strong></li>
</ol>

<p> </p>

<p><strong>Запустите все три теста, и отметьте ниже верные утверждения для каждого теста.</strong></p>

<p><strong>Важно! </strong>После того как пройдете это задание, те тесты, которые упали пометьте как XFail или skip, как это сделать мы разбирали в модуле 3: <a href="/lesson/236918/step/5?unit=209305" rel="noopener noreferrer nofollow">XFail: помечать тест как ожидаемо падающий</a>. </p>