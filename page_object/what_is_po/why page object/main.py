def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # initializing page object
    page.open()                           # opening page in the browser
    page.should_be_add_to_cart_button()   # asserting button is on the page
    page.add_product_to_basket()            # pressing button
    page.should_be_success_message()      # asserting message with text is on the page