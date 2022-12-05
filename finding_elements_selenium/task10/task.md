<h2>Задание: уникальность селекторов</h2>

<p>У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте. Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной. Обновленная страница доступна по другой&nbsp;<a href="http://suninjuly.github.io/registration2.html" rel="nofollow noopener noreferrer" target="_blank" title="Link: http://suninjuly.github.io/registration2.html">ссылке</a>. К сожалению, в процессе изменений они случайно внесли баг в форму регистрации.</p>

<p>Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую&nbsp;<a href="http://suninjuly.github.io/registration2.html" rel="nofollow noopener noreferrer" target="_blank" title="Link: http://suninjuly.github.io/registration2.html">ссылку</a>. Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит,&nbsp;ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте.&nbsp;</p>

<p>Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг. В этом случае&nbsp;попробуйте поменять селекторы, сделав их уникальными. После изменения убедитесь, что ваш тест исправно проходит в старой версии&nbsp;<a href="http://suninjuly.github.io/registration1.html" rel="nofollow noopener noreferrer" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">страницы</a>.</p>

<ol>
	<li>
	<p>Тест успешно проходит&nbsp;на странице&nbsp;<a href="http://suninjuly.github.io/registration1.html" rel="noopener noreferrer nofollow" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration1.html</a>﻿</p>
	</li>
	<li>
	<p>Тест падает&nbsp;с ошибкой NoSuchElementException&nbsp;<a href="http://suninjuly.github.io/registration2.html" rel="nofollow noopener noreferrer" title="Link: http://suninjuly.github.io/registration2.html">http://suninjuly.github.io/registration2.html</a></p>
	</li>
	<li>
	<p>Используемые селекторы должны&nbsp;быть уникальны</p>
	</li>
</ol>
