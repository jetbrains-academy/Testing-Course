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

<p><strong>Запустите все три теста, 
и обратите внимание на то, сколько времени занимает ожидание в каждом тесте.</strong></p>