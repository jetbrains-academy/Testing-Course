<h2>Задание: оформляем тесты в стиле unittest </h2>

<p>Попробуйте оформить тесты из первого модуля в стиле unittest.</p>

<ul>
	<li>Возьмите тесты из шага — <a href="https://stepik.org/lesson/138920/step/11?unit=196194" rel="noopener noreferrer nofollow">https://stepik.org/lesson/138920/step/11?unit=196194</a></li>
	<li>Создайте новый файл</li>
	<li>Создайте в нем класс с тестами, который должен наследоваться от <strong>unittest.TestCase</strong> по аналогии с предыдущим шагом</li>
	<li>Перепишите в стиле unittest тест для страницы <a href="http://suninjuly.github.io/registration1.html" rel="noopener noreferrer nofollow" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration1.html</a></li>
	<li>Перепишите в стиле unittest второй тест для страницы <a href="http://suninjuly.github.io/registration2.html" rel="noopener noreferrer nofollow" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration2.html</a></li>
	<li>Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод <a href="https://docs.python.org/3/library/unittest.html#assert-methods" rel="noopener noreferrer nofollow">assertEqual</a></li>
	<li>Запустите получившиеся тесты из файла </li>
	<li>Просмотрите отчёт о запуске и найдите последнюю строчку </li>
	<li>Отправьте эту строчку в качестве ответа на это задание </li>
</ul>

<p>Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!</p>

<p>Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. </p>

<p>Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке. </p>

- You may need to refer your learners to a particular lesson,
task, or file. To achieve this, you can use the in-course links.
Specify the path using the `[link_text](course://lesson1/task1/file1)` format.

- You can insert shortcuts in the task description.
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