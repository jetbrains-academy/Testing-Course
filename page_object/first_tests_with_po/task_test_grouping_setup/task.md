
This is a task description file.
Its content will be displayed to a learner
in the **Task Description** window.

It supports both Markdown and HTML.
To toggle the format, you can rename **task.md**
to **task.html**, or vice versa.
The default task description format can be changed
in **Preferences | Tools | Education**,
but this will not affect any existing task description files.

The following features are available in
**task.md/task.html** which are specific to the JetBrains Academy plugin:

- Hints can be added anywhere in the task text.
  Type "hint" and press Tab.
  Hints should be added to an empty line in the task text.
  In hints you can use both HTML and Markdown.
<div class="hint">

Text of your hint

</div>

- You may need to refer your learners to a particular lesson,
task, or file. To achieve this, you can use the in-course links.
Specify the path using the `[link_text](course://lesson1/task1/file1)` format.

- You can insert shortc<h2>Задание: группировка тестов и setup</h2>

<p><span style="color: #ff4363;"><strong>ВАЖНО! </strong></span>Вообще говоря манипулировать браузером в сетапе и уж тем более что-то там проверять — это плохая практика, лучше так не делать без особой необходимости. Здесь этот пример исключительно в учебных целях, чтобы вы попробовали писать сетапы для тестов. В реальной жизни мы реализовали бы все эти манипуляции с помощью API или напрямую через базу данных.</p>

<p>В этом задании мы хотим добавить тестовые сценарии не только для гостей сайта, но и для зарегистрированных пользователей. Для этого:</p>

<ol>
	<li>В файле <em>test_product_page.py</em> добавьте новый класс для тестов <strong>TestUserAddToBasketFromProductPage.</strong></li>
	<li>Добавьте туда уже написанные тесты <strong>test_guest_cant_see_success_message</strong> и <strong>test_guest_can_add_product_to_basket</strong> и переименуйте, заменив <strong>guest</strong> на <strong>user</strong>. Шаги тестов не изменятся, добавится лишь регистрация перед тестами. Параметризация здесь уже не нужна, не добавляйте её. </li>
	<li>Добавьте в <strong>LoginPage</strong> метод <strong>register_new_user(email, password),</strong> который принимает две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.</li>
	<li>Добавьте в <strong>BasePage</strong> проверку того, что пользователь залогинен:
	<pre><code>def should_be_authorized_user(self):
    assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"</code></pre>
	</li>
	<li>Селектор соответственно в <strong>BasePageLocators</strong>:
	<pre><code class="language-python">USER_ICON = (By.CSS_SELECTOR, ".icon-user")</code></pre>
	</li>
	<li>Добавьте в класс фикстуру setup. В этой функции нужно:
	<ul>
		<li>открыть страницу регистрации;</li>
		<li>зарегистрировать нового пользователя;</li>
		<li>проверить, что пользователь залогинен.</li>
	</ul>
	</li>
	<li>Запустите оба теста и убедитесь, что они проходят и действительно регистрируют новых пользователей</li>
	<li>Зафиксируйте изменения в репозитории коммитом с осмысленным сообщением </li>
</ol>

<p><strong>Примечание: </strong></p>

<p><strong>yield</strong> писать не нужно — пользователей удалять мы не умеем. Генерировать email адреса для пользователей можно по-разному, один из вариантов, чтобы избежать повторения, использовать текущее время с помощью модуля <strong>time</strong>:</p>

<pre><code class="language-python">import time # в начале файла

email = str(time.time()) + "@fakemail.org"</code></pre>

<p> </p>

<ol>
</ol>uts in the task description.
While **task.html/task.md** is open, right-click anywhere
on the **Editor** tab and choose the **Insert shortcut** option
from the context menu.
For example: &shortcut:FileStructurePopup;.

- Insert the &percnt;`IDE_NAME`&percnt; macro,
which will be replaced by the actual IDE name.
For example, **%IDE_NAME%**.

- Insert PSI elements, by using links like
`[element_description](psi_element://link.to.element)`.
To get such a link, right-click the class or method
and select **Copy Reference**.
Then press &shortcut:EditorPaste; to insert the link where appropriate.
For example, a [link to the "contains" method](psi_element://java.lang.String#contains).

- You can add link to file using **full path** like this:
  `[file_link](file://lesson1/task1/file.txt)`.