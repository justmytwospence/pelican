The world of scientific computing is rapidly developing fantastic publication tools for the modern age - tools that make it easy to communicate your methodology with literate programming documents and produce beautiful interactive plots for public consupmtion. These tools span many programming languages:
- [D3.js](d3js.org)
- [IPython (notebooks)](http://ipython.org/notebook)
- [Knitr](http://yihui.name/knitr/)

... just to name a few. The web is integral to publishing from all these tools, but there's not currently a simple publishing platform that plays nice with all of them at once, out of the box. This is my attempt to create a blogging framework specifically for the data scientists who already know and love these tools, and need a place where they can all come together to publish their work.

It is built with [Pelican](http://docs.getpelican.com), a static blogging framework that eats page templates written with liquid tags, together with posts written in reStructured text/markdown/HTML, and "bakes" your website into a collection of all the necessary HTML files. The static nature of these files means that it can be hosted on GitHub Pages and publishing is as simple as `git push`. I'm choosing to use the pelican-bootstrap3 template as a starting point, because the Bootstrap framework is highly customizable/flexible and relatively easy to pick up for us data-types who aren't designers. 

None of this is particularly novel, I'm simply attempting build an out-of-the-box solution that anyone can fork and start publishing with R, Python, D3, etc, without days of configuration.

TO DO
=====

- Switch from Knitr's syntax highlighting to Pygments. This might require custom hooks in Knitr.
- Improve typography.
- Look into simpler ways to add scripts to individual posts.
- Add the sidebar modifications to templates other than index, article, and page.
- Figure out where a few ugly CSS styles are coming from (mainly the dashed underlines for links).
- Remove border from code snippets that aren't part of an IPython notebook.
