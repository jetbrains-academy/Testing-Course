<h2>Уникальность селекторов: часть 2</h2>

<p>Попробуем реализовать один из автотестов из предыдущего шага. Вам дана <a href="http://suninjuly.github.io/registration1.html" rel="nofollow noopener noreferrer">страница</a> с формой регистрации. Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *: First name, last name, email. Текст для полей может быть любым. Успешность регистрации проверяется сравнением ожидаемого&nbsp;текста &quot;Congratulations! You have successfully registered!&quot; с текстом на странице, которая открывается после регистрации. Для сравнения воспользуемся стандартной&nbsp;конструкцией&nbsp;assert из языка Python.</p>

<p>Ниже дан шаблон кода, который вам нужно использовать для своего теста. Не забывайте, что селекторы должны быть уникальными.</p>

<p>Углубимся немного в использовании конструкции&nbsp;assert из данного примера, Если результат проверки&nbsp;&quot;Поздравляем! Вы успешно зарегистрировались!&quot; == welcome_text вернет значение False, то далее выполнится код <strong>assert False</strong>.<strong> </strong>Он&nbsp;бросит&nbsp;исключение&nbsp;AssertionError и номер строки, в которой произошла ошибка. Если код написан правильно и работал ранее, то такой результат равносилен тому, что наш автотест обнаружил баг в тестируемом веб-приложении. Если результат проверки вернет True, то выполнится выражение <strong>assert True</strong>. В этом случае код завершится без ошибок &mdash; тест прошел успешно. Подробнее про использование assert в коде мы поговорим в третьем модуле этого курса.</p>

<p>В этом задании нет автоматических проверок вашего кода. Просто убедитесь, что ваш тест проходит успешно, и вы не видите AssertionError в результатах работы вашего кода.</p>

<p><strong>Замечание</strong></p>

<p>В этом примере мы использовали метод <strong>time.sleep(1)</strong>, чтобы дождаться загрузки следующей страницы, прежде чем выполнять проверки. Если вы будете запускать код без этого метода, ваш код может внезапно&nbsp;упасть, хотя проходил ранее. Без использования такой паузы&nbsp;WebDriver&nbsp;может перейти к поиску&nbsp;тега h1 слишком рано, когда новая страница еще не загрузилась. В таком случаем&nbsp;будем видеть в терминале&nbsp;ошибку:</p>

<pre>
<code class="language-python">NoSuchElementException... Unable to locate element: {"method":"tag name","selector":"h1"}</code></pre>

<p>Метод time.sleep(1)&nbsp;говорит Python подождать 1 секунду, прежде&nbsp;чем выполнять следующую строчку кода. Если вы всё равно видите эту ошибку, просто увеличьте количество секунд ожидания.</p>

<p>Проблема со своевременным поиском элемента&nbsp;&mdash; одна из самых больших проблем, которую приходится решать при разработке автотестов для UI. В условиях постоянно изменяющейся скорости сетевого соединения и неравномерности&nbsp;нагрузки на серверы&nbsp;скорость загрузки страницы может сильно варьироваться. Еще одним фактором, влияющим на стабильность работы тестов, является принцип асинхронности выполнения кода&nbsp;JavaScript. На простых страницах вы можете этого и не заметить, но на функционально богатых страницах время появления элементов страницы может быть непредсказуемо. Хорошо было бы организовать тесты так, чтобы не сложилось ситуации, когда они не проходят по причине нестабильной&nbsp;скорости интернета или других причин, которые от нас не зависят.</p>

<p>Решать эту проблему с помощью time.sleep()&nbsp;считается плохой практикой, так как&nbsp;заранее трудно указать нужное время ожидания. Если выставить слишком большое время ожидания, то&nbsp;тесты будут идти неоправданно&nbsp;долго. В дальнейших уроках мы рассмотрим более красивые и эффективные способы решения этой проблемы, а пока будем использовать time.sleep() из-за его простоты и наглядности.</p>
