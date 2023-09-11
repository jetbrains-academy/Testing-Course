
from steps import *

link = "https://suninjuly.github.io/explicit_wait2.html"


def wait_test(browser):
    browser.get(link)
    wait_for_price(browser, "100$")
    book(browser)
    solve_quiz(browser)
    browser.switch_to.alert.accept


