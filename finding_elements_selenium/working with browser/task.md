<h2>Работа с браузером в Selenium</h2>

<p>Если вы уже пробовали запускать примеры скриптов, то могли заметить, что браузер не всегда закрывается после выполнения кода. Поэтому обратите внимание на то, что необходимо явно закрывать окно браузера в нашем коде при помощи команды <strong>browser.quit().</strong> Каждый раз при открытии браузера <code>browser = webdriver.Chrome() </code>в системе создается процесс, который останется висеть, если вы вручную закроете окно браузера. Чтобы не остаться без оперативной памяти после запуска нескольких скриптов, всегда добавляйте к своим скриптам команду закрытия:</p>

<pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()</code></pre>

<p>Важно еще пояснить разницу между двумя командами:<strong> browser.close()</strong> и<strong> browser.quit()</strong>. Какая между ними разница, ведь на первый взгляд обе они осуществляют одно и то же? </p>

<p>На самом деле, <strong>browser.close() </strong>закрывает <em>текущее </em>окно браузера. Это значит, что если ваш скрипт вызвал всплывающее окно, или открыл что-то в новом окне или вкладке браузера, то закроется только текущее окно, а все остальные останутся висеть. В свою очередь <strong>browser.quit() </strong>закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии. Подробнее можно посмотреть здесь: <a href="https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit" rel="noopener noreferrer nofollow">Difference between webdriver.Dispose(), .Close() and .Quit()</a>. Будьте внимательны с этими методами и, в общем случае, всегда используйте <strong>browser.quit(). </strong></p>

<p>Но что будет, если скрипт не дойдет до выполнения этого финального шага, а упадет с ошибкой где-то раньше? </p>

<p>Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, проще всего использовать конструкцию <strong>try/finally</strong>: </p>

<pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()</code></pre>

<p>Можете попробовать запустить оба примера и обратить внимание на разницу.</p>

<p>Подробно говорить об обработке исключений мы сейчас не будем, здесь важно понимать только то, что даже если в коде внутри блока <strong>try</strong> произойдет какая-то ошибка, то код внутри блока <strong>finally</strong> выполнится в любом случае. Советуем добавлять такую обработку ко всем своим скриптам при выполнении задач этого и следующего модулей, а в третьем модуле мы обсудим более лаконичные конструкции.</p>

<p>Если хотите узнать больше про исключения, как их кидать, ловить и как с ними жить, то советуем к прохождению вот этот урок: <a href="https://stepik.org/lesson/24463/step/1?unit=6771" rel="noopener noreferrer nofollow"> Ошибки и исключения</a>.</p>

<p>(За замечание и дополнение спасибо за него нашему студенту <a href="https://stepik.org/users/41632287" rel="noopener noreferrer nofollow">Михаилу λ</a>)</p>
