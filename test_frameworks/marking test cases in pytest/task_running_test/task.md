<h2>Задание: запуск тестов</h2>

<p>В этом задании нам нужно разобраться в хитросплетениях маркировок. Мы имеем файл с тестами, которые уже размечены маркерами для разных ситуаций запуска.</p>

<p><strong>test_task_run_1.py:</strong></p>

<pre><code class="language-python">import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
</code></pre>

<p>Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды: </p>

<pre><code class="language-python">pytest -v -m "smoke and not beta_users" test_task_run_1.py</code></pre>