
<p>Давайте,&nbsp;прежде чем двигаться дальше, закрепим знания на практике.&nbsp;</p>

<p>Представьте, что вы работаете тестировщиком-автоматизатором в IT-отделе интернет-магазина. QA Lead&nbsp;поручил вам&nbsp;задание автоматизировать следующий тестовый сценарий:&nbsp;</p>

<ol>
	<li>Открываем страницу товара (<a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear</a>). Обратите внимание, что в ссылке есть параметр &quot;?promo=newYear&quot;. Не теряйте его в авто-тесте, чтобы получить проверочный код.</li>
	<li>Нажимаем на кнопку &quot;Добавить в корзину&quot;.</li>
	<li>*Посчитать результат математического выражения и ввести ответ. Используйте для этого метод <strong>solve_quiz_and_get_code()</strong>, который приведен ниже. Например, можете добавить его в класс <strong>BasePage</strong>, чтобы использовать его на любой странице. Этот метод&nbsp;нужен только для проверки того, что вы написали тест на Selenium.&nbsp;После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.</li>
</ol>

<p>Ожидаемый результат:&nbsp;</p>

<ol>
	<li>Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.</li>
	<li>Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.&nbsp;</li>
</ol>

<p>Тест нужно написать, используя паттерн&nbsp;Page Object. Для этого вам нужно:&nbsp;</p>

<ol>
	<li>Откройте новый файл с тестами<em> test_product_page.py.</em></li>
	<li>Создать класс Page Object для страницы товара. Опишите его в файле <em>product_page.py</em> в папке <em>pages.</em></li>
	<li>Описать в нем метод для добавления в корзину.</li>
	<li>Дописать&nbsp;методы-проверки.</li>
	<li>Описать необходимые локаторы к элементам страницы.</li>
	<li>Написать сам тест-кейс в файле  <em>test_product_page.py</em>, используя все вышеописанное. Назовите тест <strong>test_guest_can_add_product_to_basket.</strong></li>
</ol>

<p>Можете начинать работу с любого пункта, но хорошей практикой считается написать сначала шаги и структуру теста, а потом описывать конкретную реализацию.&nbsp;</p>

<p>*Используйте этот метод в тесте для получения проверочного кода:&nbsp;</p>

<pre>
<code class="language-python">from selenium.common.exceptions import NoAlertPresentException # в начале файла

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")</code></pre>

<p>Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром <strong>-s</strong>:</p>

<pre>
<code>pytest -s test_product_page.py</code></pre>
