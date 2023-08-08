<h2>Почему именно Page Object?</h2>

<p>Можно, конечно, хранить всю логику наших тестов в одном файле под каким-нибудь условным названием steps.py, и для начала это уже неплохо. Но если мы тестируем большой веб-продукт с множеством разных состояний и переходов, этот файл может разрастись до огромных размеров, и найти в нем нужный метод будет непросто. Еще бывают ситуации, когда на разных страницах логически один и тот же метод имеет разную реализацию. Например, у нашего интернет-магазина может быть метод "добавить в корзину". Но пользователь может добавлять товар в корзину как со страницы каталога, так и со страницы самого товара. </p>

<p>Было бы удобно выделить все методы, которые логически относятся к одной веб-странице в нашем продукте, в отдельный класс в нашем коде. Отсюда и название Page Object — это абстрактный объект, который содержит в себе методы для работы с конкретной веб-страницей. </p>

<p><strong>Важно! </strong>Обычно методы у Page Object бывают двух типов: <em>сделать что-то</em> и <em>проверить что-то.</em></p>

<p>Рассмотрим страницу товара в интернет магазине <a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/</a>.</p>

<p>Какие могут быть методы у Page Object, ассоциированного с такой страницей? Запишем основные сценарии: </p>

<ul>
	<li>добавить в корзину;</li>
	<li>проверить, что есть сообщение об успешном добавлении в корзину;</li>
	<li>перейти к написанию отзыва;</li>
	<li>проверить, что есть название, цена, описание товара;</li>
	<li>вернуться на главную.</li>
</ul>

<p>Обратите внимание, что все проверки у нас тоже становятся отдельными методами. В самом тест-кейсе не остается никаких вспомогательных слов типа assert, только описание шагов. Прямо как в нашей тестовой документации.  </p>

<p>Тесты будут выглядеть примерно так:</p>

<pre><code class="language-python">def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # initializing page object
    page.open()                           # opening page in the browser
    page.should_be_add_to_cart_button()   # asserting button is on the page
    page.add_product_to_cart()            # pressing button
    page.should_be_success_message()      # asserting message with text is on the page
</code></pre>

Таким образом, тесты становятся более абстрактными и понятными. А все детали реализации абстрактных методов скрыты внутри методов Page Object, и при необходимости могут быть переиспользованы в разных тестах.