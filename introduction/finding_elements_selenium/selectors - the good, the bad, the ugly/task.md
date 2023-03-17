<h2>Unique selectors: part 1</h2>

<p>We've already mentioned that an ideal selector is the one that allows us to find the single required element on a page. Thanks to unique selectors, our tests become more stable and less dependent on the modifications in the page coding. Developers frequently introduce minor changes, and we do not want to constantly fix our tests.</p>

<p>Another important comment: a good test checks only a small, atomic part of functionality. Simple tests working with one small scenario are better than a large test checking a huge number of scenarios. Thanks to simple tests we can faster localize part of the product where a bug occurred; besides, we can find several other bugs at the same time. A failed large automated test points at the first encountered problem only, as it quits after the first identified error. That's what makes it different from manual tests, in which we check the product functionality by a test case and can flexibly avoid problems, thus completing the test case and finding all the bugs.</p>

<p>Let's consider the following example: we have a registration form, which has both mandatory and optional fields. We need to check if one can successfully get registered at the site.</p>

<p><strong>A bad automated test scenario:</strong></p>

<p>1</p>

<ul>
	<li>Open the page with the form</li>
	<li>Fill in all the fields</li>
	<li>Press the &quot;Registration&quot; button</li>
	<li>Check that there's a message about successful registration</li>
</ul>

<p><strong>It's better to split the above test into a set of simpler automated tests:</strong></p>

<p>1</p>

<ul>
	<li>Open the page with the form</li>
	<li>Fill in the mandatory fields only</li>
	<li>Press the &quot;Registration&quot; button</li>
	<li>Check that there's a message about successful registration</li>
</ul>

<p>2</p>

<ul>
	<li>Open the page with the form</li>
	<li>Fill in all the mandatory fields</li>
	<li>Fill in all the optional fields</li>
	<li>Press the &quot;Registration&quot; button</li>
	<li>Check that there's a message about successful registration</li>
</ul>

<p>3</p>

<ul>
	<li>Open the page with the form</li>
	<li>Fill in the optional fields only</li>
	<li>Check that the &quot;Registration&quot; button is not active</li>
</ul>
