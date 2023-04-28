<h2>A few words about the modern web</h2>

<p>Developers worked hard to ensure
that in 2022, web pages would look neat and open quickly 
with the transitions between pages being almost unnoticeable.
Site pages are interactive and instantly respond to the user's actions.
In most cases, in order to implement such comfortable user experience, the
<a href="https://developer.mozilla.org/en-US/docs/Glossary/SPA" rel="noopener noreferrer nofollow">Single-Page Application</a>
, which generally implies the existence of a single page on the site.
Meanwhile, the content of the page is dynamically renewed by JavaScript,
which quietly exchanges information with the server – for example, by means of REST API.</p>

<p>Everyone seems to be happy, only the authors of automated interface tests have a problem.
Suddenly appearing and disappearing page elements,
unpredictable time of page rendering,
changing text in buttons and site messages &mdash; all these features of
SPA applications need to be taken into consideration in automated tests, which, we have to admit,
is one of the most difficult and challenging aspects of developing&nbsp;
automated tests in Selenium (as well as in other frameworks for writing end-to-end tests).</p>

<p>In this lesson, we will look in more detail at the most frequent problems and discuss ways of
handling those.</p>
