<h2>Задание: независимость контента, ищем баг</h2>

<p>Эта задача для настоящих ниндзя автотестинга. Не потому что она сложная, а потому что сейчас мы будем ловить с вами настоящий баг с помощью наших автотестов.&nbsp;Для нашего интернет-магазина было запущено несколько новых промо-акций, одна из которых привела к появлению&nbsp;бага. Промо-акция включается путем добавления параметра ?promo=offerN к ссылке на товар.</p>

<p>К счастью, нам не придется менять наш тест, чтобы проверить изменения в коде. Мы просто&nbsp;запустим&nbsp;всё тот же тест на странице&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/</a>&nbsp;с параметризацией. Вам нужно определить,&nbsp;при каком значении параметра promo автотест&nbsp;упадет. Для этого проверьте результат работы PyTest и найдите url, на котором произошла ошибка. Значение параметра может изменяться от offer0 до offer9.</p>

<p>Пример ссылки:&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0</a>. Если баг будет найден на этой странице, то введите в качестве ответа <a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0</a>.</p>

<p>Запустить сразу несколько тестов вы можете, используя <strong>@pytest.mark.parametrize</strong>. Мы уже сделали для вас шаблон теста:</p>

<pre>
<code>@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # ваша реализация теста</code></pre>

<p>Подсказка: баг должен быть найден методом проверки.</p>

<p> После того как вы обнаружили баг вставьте ссылку на проблемный URL в файл bugreport.txt</проблемы> </p>

<p>После того как вы обнаружили баг,
учитывая что чинить его не собираются,
лучше всего пометить падающий тест как <strong>xfail</strong>&nbsp;или <strong>skip.&nbsp;</strong>Помните, как мы такое проворачивали в третьем модуле?&nbsp;Освежить память: <a href="/lesson/236918/step/5?unit=209305" rel="noopener noreferrer nofollow">XFail: помечать тест как ожидаемо падающий</a>.</p>

<p>С параметризацией делается это примерно так:&nbsp;&nbsp;</p>

<pre>
<code class="language-python">@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])</code></pre>

<p>Подробнее:&nbsp;<a href="https://pytest.org/en/stable/skipping.html#skip-xfail-with-parametrize" rel="noopener noreferrer nofollow">Skip/xfail with parametrize</a></p>
