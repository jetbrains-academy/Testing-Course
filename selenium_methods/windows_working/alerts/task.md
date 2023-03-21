<h2>Alerts и как с ними жить</h2>

<p>Мы уже встречали alert в нашем курсе, когда получали число-ответ в задачах. Также мы узнали, что можно самостоятельно вызвать alert с помощью JavaScript:</p>

<pre><code class="language-javascript">alert('Hello!');</code></pre>

![](img.png)

<p>Теперь рассмотрим ситуацию, когда в сценарии теста возникает необходимость не только получить содержимое alert, но и нажать кнопку OK, чтобы закрыть alert. <strong>Alert</strong> является модальным окном: это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды <strong>accept()</strong>:</p>

<pre><code class="language-python">alert = browser.switch_to.alert
alert.accept()</code></pre>

<p>Чтобы получить текст из alert, используйте свойство text объекта alert:</p>

<pre><code class="language-python">alert = browser.switch_to.alert
alert_text = alert.text</code></pre>

<p>Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется <strong>confirm</strong>. Для переключения на окно confirm<strong> </strong>используется та же команда, что и в случае с alert:</p>

<pre><code class="language-python">confirm = browser.switch_to.alert
confirm.accept()</code></pre>

![img_1.png](img_1.png)

<p>Для confirm<strong>-</strong>окон можно использовать следующий метод для отказа:</p>

<pre><code>confirm.dismiss()</code></pre>

<p>То же самое, что и при нажатии пользователем кнопки "Отмена". </p>

<p>Третий вариант модального окна — <strong>prompt </strong>— имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод <strong>send_keys()</strong>:</p>

<pre><code class="language-python">prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()</code></pre>

![img_2.png](img_2.png)
