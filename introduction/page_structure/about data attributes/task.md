## More about attributes (data attributes)

As we've already said, some attributes directly affect the representation of the element on a page.
We've already discussed some of these important attributes.

Actually, the list of attributes can be expanded: it means that developers can create their own
attributes and assign any values to them.
What does it mean to testers?
It means that we can agree with developers on a special attribute
that won't change when the page coding is modified
and that we'll use it in our tests to find necessary elements.
It will make your tests more stable. 
However, there are several limitations. 

Websites needs to follow the HTML5 standard (most sites today do),
and the attribute name can contain only Latin characters and the following symbols: hyphen (-), colon (:), and underscore (_).
The names of such attributes should start with the word "data": for example, "data-button".

What else do you need to know about element attributes? 

Some attributes are universal: they can 
apply to any tag and any element type.
For example, we can make any element "hidden".
Meanwhile, some attributes are associated with a specific tag: for example, for an image, 
which is defined by the "img" tag, we need to specify the "src" attribute.

If you are planning to work with automated testing of web products in the future,
you will need to study HTML in more detail.
It will help you quickly choose the right selectors, and looking at the HTML code, you
will immediately see that `<a>` is a link,
`<p>` is text, and `<ul>` is an unordered (bulleted) list. 
However, it's a big topic that deserves a separate course (you can take such a course on your own,
for example, at https://www.w3schools.com/html/).
