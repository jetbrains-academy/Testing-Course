<h2>Negative checks: how to verify the absence of an element</h2>

<p>Sometimes, during the process of writing automated tests, a situation arises where we need to check not only the presence of an element on a page but also that an element is absent. Here, it's essential to distinguish between two fundamentally different cases, depending on how the web application behaves: </p>

<p> <strong>1. The element might potentially appear on the page (but ideally shouldn't). For example, when we open a product page and expect there to be no message about a successful addition to the cart. We check that the element is not present. However, in a positive scenario, when we add a product to the cart, the message also doesn't appear immediately. If, during negative checking, we don't include a wait and immediately provide the result as "True, the element is indeed not there, everything is good," we risk encountering a falsely green test. In other words, we might overlook a bug. </p>

<p><strong>2. The element is present on the page and should disappear over time or as a result of user actions. This could be, for instance, the removal of a product from the cart or the disappearance of a loader during loading. </p>

<h3>Why should we write such checks cautiously? </h3>

<p><em>Firstly</em>, we absolutely always have to wait. In the first example, we always need to wait for a few seconds to ensure that the element has not appeared. If we use our is_element_present function, the test with such a check will wait the full and honest 10 seconds:</p>

<pre><code>def should_not_be_success_message(self):
    assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented"</code></pre>

<p>Which is quite a lot for a green test. That is, implicit_wait is no longer suitable in such a situation; explicit waiting will have to be used, and conditions will need to be carefully selected. The wait time will also need to be empirically determined through trial and error, false positives, and false negatives. </p>

<p><em>Secondly</em>, another challenge with negative checks is that they can yield false positives if the selector is outdated. We check that there is no element with this selector—the check passes because the element already has a different selector. The element is on the screen—this is a bug, while the test is green. This is not good! </p>

<p>Therefore, each negative test must be accompanied by a positive test. In one test, we check that the element is absent; in the adjacent test, we check that the element is present. This way, we can track the relevance of the selector and avoid missing such a bug. </p>

<h3>How then should we implement such checks? </h3>

<p>It is necessary to rely on the specific situation, but a general piece of advice is to use explicit waits and Expected Conditions, which we discussed in previous modules. </p>

<p>You can add an abstract method to the BasePage that verifies that the element does not appear on the page for a specified period: </p>

<pre><code>def is_not_element_present(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return True

    return False</code></pre>

<p>Then its use in the Page Object for the product page will look like this: </p>

<pre><code>def should_not_be_success_message(self):
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"</code></pre>

<p>If we want to check that a certain element disappears, we should use explicit waiting along with the until_not function, depending on the result we expect:</p>

<pre><code>def is_disappeared(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return False

    return True</code></pre>

<p>The validation method in the product page class will look similar to <strong>should_not_be_success_message</strong>; write it yourself.</p>

<p> </p>

<p>Pay attention to the difference between the methods <strong>is_not_element_present</strong> and <strong>is_disappeared</strong>. </p>

<p><strong>is_not_element_present</strong>: it will fail as soon as it sees the sought element. If it does not appear, it's a success, and the test is green. </p>

<p><strong>is_disappeared</strong>: it will wait until the element disappears. </p>

<p> </p>

<p>Add both methods to the Base Page for future use, as well as the method 
<code>should_not_be_success_message</code> to the ProductPage class.</p>

<p>In summary, it can be said that developing such checks should be done very carefully, using explicit waits to reduce test runtime and always adding a positive check for the element in another test. Without explicit need, it's better to avoid such checks. </p>
