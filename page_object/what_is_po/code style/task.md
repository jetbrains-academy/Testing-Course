<h2>Code Style: basic principles</h2>

<h3>Names of variables and functions</h3>

<p>One of the crucial aspects of code readability is naming – in variable declarations, function description, class names, etc. When naming entities, it's very important to use meaningful names, the ones that reflect the essence of the object. Avoid single-letter and senseless names, like var1, x, y, my_function, class2, etc. Ideal code is self-documenting, i.e., it does not require additional explanations. If you feel that you want to write a comment, it is an excuse to write new code, which won't need the comment.</p>

<p>Usually, each company has additional inside agreements on naming variables; however, the general rules in the industry are more or less the same.</p>

<p>Functions are named with an underscore:</p>

<p><code>def test_guest_can_see_lesson_name_in_lesson_without_course(self, driver):</code></p>

<p>Class names use the CamelCase:</p>

<p><code>class TestLessonNameWithoutCourseForGuest():</code></p>

<p>Constants are named in the UPPERCASE style:</p>

<p><code>MAIN_PAGE = "/catalog"</code></p>

<h3>Maximum simplicity of code</h3>

<p>Here, the well-known code writing principles come to the resque: <a href="https://en.wikipedia.org/wiki/Don't_repeat_yourself" rel="noopener noreferrer nofollow">DRY</a> (Don't repeat yourself) and <a href="https://en.wikipedia.org/wiki/KISS_principle" rel="noopener noreferrer nofollow">KISS</a> (Keep it simple, stupid). </p>

<ul>
	<li>Write most simple code whenever possible.</li>
	<li>Don't use over-complicated constructs unless absolutely necessary (as few lambda expressions, maps, and other magic things as possible). If a piece of code may be replaced with a simpler construct, replace it.</li>
	<li>Write maximally linear code whenever possible – it's more readable.</li>
	<li>Avoid excessive nesting of code blocks – such constructs are hard to read.</li>
	<li>If you can extract repeated logic somewhere, extract it and do not repeat yourself.</li>
	<li>Whenever possible, write explicit code rather than implicit. The less magic under the hood, the better.</li>
</ul>
