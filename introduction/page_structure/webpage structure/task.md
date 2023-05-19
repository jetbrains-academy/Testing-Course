## What's a web page?

Any interaction of the user with a web application proceeds via the web interface. 
In order to imitate the user's actions, automated tests need to be able to find page 
elements with which the scenario interacts.
In this lesson, we'll discuss the main ways of finding elements. 

Any page on the internet is an HTML file, 
with the page structure defined in the HTML language.

Besides, practically all sites use the JavaScript language,
which allows making the web page interactive – able to 
respond to the user's actions, request data from the user, and return data.

Finally, we also need to mention CSS (Cascading Style Sheets),
which is used for designing the visual appearance of a page. You've probably already
seen cases when messed up page design results in serious 
bugs in the site's work. Thanks to
WebDriver, we can catch some unexpected design problems – for example, when a
button the user needs is overlapped by some insignificant element.

Now we are mostly concerned with the page structure, i.e.,
its description in the HTML language. Being able to describe the path to a page element, we can find such an element 
and perform necessary operations on it –
for example, send a text into the text field or click the proper button.

### Next, we'll discuss several ways of finding elements on a web page:
<ul>
<li> Search with CSS selectors </li>
<li> Search with tag values or element attributes: ID, class, etc. </li>
<li> Search with the XPath query language </li>
</ul>
We believe that searching with CSS selectors is most
convenient, as this method
covers virtually all possible situations,
and CSS selectors are most readable.
