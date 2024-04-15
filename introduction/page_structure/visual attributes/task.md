### Attributes affecting element rendering

Let's talk a bit more about element attributes. 
Some attributes affect the element's rendering on the page, 
and some don't affect it directly but may be used in JavaScript or 
may be necessary for element locating in tests.

Here are examples of attributes that affect rendering and the element's behavior: 

```
<h1 style="color: blue;"> The heading will be blue because the color is set in the style attribute </h1>

<p hidden> The attribute hidden hides the element on a page; the element won't be displayed </p>

<button disabled> The button with the attribute disabled will be blocked </button>
```

Try opening `index.html` in your browser. Now add the visual attributes and try opening this file again. 