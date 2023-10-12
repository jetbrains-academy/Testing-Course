<h2>Элементы страниц в паттерне Page Object</h2>

<p>Помните, мы говорили о том, что тесты почти соответствуют подходу&nbsp;Page Object?&nbsp;</p>

<p>Сейчас разберемся, почему <strong>почти&nbsp;</strong>на примере короткой и поучительной истории.</p>

<p>У нас уже есть два тест-кейса, которые так или иначе взаимодействуют со ссылкой на логин. Представим себе&nbsp;ситуацию, что у нас модный быстрый&nbsp;agile: разработчики постоянно вносят изменения в продукт. В&nbsp;какой-то прекрасный момент изменения коснулись и шапки сайта. Вот приходит к вам разработчик с новой ссылкой и говорит протестировать.</p>

<p>Замените линк, на котором запускаются тесты на <a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer</a>&nbsp;</p>

<p>Запустите тесты командой:</p>

<pre>
<code class="language-bash">pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>Тесты упали, и теперь нам нужно их поддерживать, то есть <em>чинить.&nbsp;</em>Подберите новый селектор к ссылке на логин.&nbsp;</p>

<p>Нам придется&nbsp;поправить в файле <em>main_page.py</em>&nbsp;несколько мест, где используется измененный селектор. Посчитайте, сколько строк вам нужно будет отредактировать, чтобы починить ваши тесты, и внесите полученное число&nbsp;в первое поле ответа ниже.&nbsp;</p>

<p>Чтобы этого избежать, при проектировании тестов (да и вообще кода) хорошей практикой является выносить селектор&nbsp;во внешнюю переменную.&nbsp;</p>

<p>Давайте этим и займемся:&nbsp;</p>

<p>1. В папке pages откройте файл <em>locators.py&nbsp;</em></p>

<p>2. Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject:&nbsp;</p>

<pre>
<code>from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")</code></pre>

<p>теперь каждый селектор&nbsp;&mdash; это пара: как искать и что искать.&nbsp;</p>

<p>3. В файле main_page.py импортируйте новый класс с локаторами&nbsp;</p>

<pre>
<code>from .locators import MainPageLocators</code></pre>

<p>4. Теперь в классе MainPage замените все&nbsp;строки, где содержится &quot;<strong>#login_link</strong>&quot; таким образом:</p>

<pre>
<code class="language-python">def should_be_login_link(self):
    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"</code></pre>

<p>Обратите внимание здесь на символ<strong> *</strong>, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.&nbsp;</p>

<p>5. Запустите тесты с помощью той же самой команды:&nbsp;</p>

<pre>
<code class="language-bash">pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>Они,&nbsp;конечно, снова упадут. Но теперь обратите внимание, сколько строк вам нужно будет отредактировать, когда тесты написаны в такой конфигурации? </p>

<p>&nbsp;</p>

<p><strong>Итак, PageObject&nbsp;&mdash; это не только <em>методы</em>, но и <em>элементы</em>.&nbsp;&nbsp;</strong></p>

<p>Исправлять руками сломанные селекторы во всем проекте&nbsp;&mdash; долго и трудозатратно, и есть большой риск забыть и оставить старый селектор. Когда мы выносим селекторы в отдельную сущность, мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе.&nbsp;</p>

<p>А ещё&nbsp;спринт спустя промоакция закончилась, и фичу с изменением шапки откатили назад.&nbsp;Теперь ссылка&nbsp;работает так же, как раньше. Удалите ссылку с промоакцией, и верните обычную ссылку для запуска тестов:&nbsp;</p>

<pre>
<code>link = "http://selenium1py.pythonanywhere.com/"</code></pre>

<p>Не забудьте вернуть старый&nbsp;селектор <strong>#login_link</strong>, так чтобы тесты снова проходили. Они&nbsp;нам еще пригодятся!&nbsp;</p>
