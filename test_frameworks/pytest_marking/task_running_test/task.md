<h2>Task: running tests</h2>

<p>In this task, you need to figure out the intricacies of test marking. We have a file with tests that have been marked for different launching situations.</p>

<p><strong>test_task_run_1.py:</strong></p>

<pre><code class="language-python">import pytest


class TestMainPage():
    # number 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # number 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # number 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # number 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # number 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # number 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# number 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
</code></pre>

<p>Below, identify the test methods that will be found and executed by PyTest if we run the following command: </p>

<pre><code class="language-python">pytest -v -m "smoke and not beta_users" test_task_run_1.py</code></pre>
