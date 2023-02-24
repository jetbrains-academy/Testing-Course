<h2>PyTest — отчёты</h2>

<p>Вы могли заметить, что PyTest позволяет генерировать подробный отчёт с поддержкой цветовых схем и форматированием прямо из коробки.</p>

<p>Давайте еще раз запустим наши тесты с помощью unittest и PyTest, чтобы сравнить выводимый результат.</p>

<p>Мы видим, что в PyTest-отчёте упавший тест выделен красным шрифтом, что делает разбор логов более приятным занятием.</p>

<p><strong>unittest:</strong></p>

<p><img alt="" src="https://ucarecdn.com/7cb1723f-3a3b-4fb6-a6bd-6a2e1904d02f/"></p>

<p><strong>PyTest: </strong></p>

<p><img alt="" src="https://ucarecdn.com/81ceab3c-0d25-4beb-ab87-09d110294d63/"></p>

<p>Если запустить PyTest с параметром <strong>-v</strong> (<strong>verbose</strong>, то есть подробный), то в отчёт добавится дополнительная информация со списком тестов и статусом их прохождения: </p>

<p><img alt="" src="https://ucarecdn.com/6a53144b-e083-410f-92ef-404511fc6c07/"></p>

<p>Другие полезные команды для манипуляции выводом тестов PyTest можно найти по ссылке: <a href="https://gist.github.com/amatellanes/12136508b816469678c2" rel="noopener noreferrer nofollow">Useful py.test commands.</a></p>