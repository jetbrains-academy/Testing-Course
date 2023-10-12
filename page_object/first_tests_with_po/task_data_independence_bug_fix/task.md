<h2>Задание: независимость контента, ищем баг</h2>

<p>После того как вы обнаружили баг,
учитывая что чинить его не собираются,
лучше всего пометить падающий тест как <strong>xfail</strong>&nbsp;или <strong>skip.&nbsp;</strong>Помните, как мы такое проворачивали в третьем модуле?&nbsp;Освежить память: <a href="/lesson/236918/step/5?unit=209305" rel="noopener noreferrer nofollow">XFail: помечать тест как ожидаемо падающий</a>.</p>

<p>С параметризацией делается это примерно так:&nbsp;&nbsp;</p>

<pre>
<code class="language-python">@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])</code></pre>

<p>Подробнее:&nbsp;<a href="https://pytest.org/en/stable/skipping.html#skip-xfail-with-parametrize" rel="noopener noreferrer nofollow">Skip/xfail with parametrize</a></p>
