<h2>Task: Content independence, finding a bug</h2>
This task is for true testing ninjas. Not because it's difficult, but because now we'll be catching a real bug with our automated tests. Several new promotions were launched for our online store, one of which led to the appearance of a bug. The promotion is activated by adding the parameter ?promo=offerN to the product link.</p>

<p>Fortunately, we don't have to change our test to check the code changes. We'll simply run the same test on the page&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/</a>&nbsp;with parameterization. You need to determine at which value of the promo parameter the automated test will fail. To do this, check the PyTest result and find the URL where the error occurred. The parameter value can range from offer0 to offer9.</p>

<p>Example link:&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0</a>. If the bug is found on this page, enter <a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0</a> as your answer.</p>

<p>You can run multiple tests at once using <strong>@pytest.mark.parametrize</strong>. We've already provided a test template for you:</p>

<pre>
<code>@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # your test implementation</code></pre>

<p>Hint: The bug should be found using the check method.</p>

<p> After you've discovered the bug, paste the link to the problematic URL into the bugreport.txt file </problems> </p>

<p>Once you've found the bug,
considering that it won't be fixed,
it's best to mark the failing test as <strong>xfail</strong>&nbsp;or <strong>skip.&nbsp;</strong>Remember how we did it in Module 3?&nbsp;Refresh your memory: <a href="/lesson/236918/step/5?unit=209305" rel="noopener noreferrer nofollow">XFail: mark the test as expected to fail</a>.</p>

<p>With parameterization, it's done like this:&nbsp;&nbsp;</p>

<pre>
<code class="language-python">@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])</code></pre>

<p>Подробнее:&nbsp;<a href="https://pytest.org/en/stable/skipping.html#skip-xfail-with-parametrize" rel="noopener noreferrer nofollow">Skip/xfail with parametrize</a></p>
