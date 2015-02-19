Assignment: CSS Hell
====================

You will skin 3 project gutenberg stories with custom CSS.

You will skin 2 versions of a possible professional homepage for your
self with 2 versions of CSS.

Read requirements.org

Read this comic http://theoatmeal.com/comics/design_hell

git clone https://github.com/abramhindle/CMPUT404-assignment-css-hell.git

Part 1
======
76-h.html is the only one with images.

The default CSS was left in place that was downloaded alongside the HTML. However, for the assignment, 
certain styles were overwritten to meet the criteria.

The only thing added to the HTML document was:
<link type="text/css" rel="stylesheet" href="css/styles.css" />

AND, the figcaption for 76-h.html:
<figcaption>Something Something Caption</figcaption>

After the default style tag.

"Aesthetically Pleasing"... uhhh, it looks good against the background already.
With the background as #D1BA98 from the paper, #726F92 is considered on the opposite side of the spectrum from:
http://paletton.com/#uid=30M0u0k8Jqe2eHr5buXcEm8f+hJ
Using a triad colour scheme so that the text colour stands out from the background more.

"Image caption". There really was no image captions in my story. However, if there was, we could use figcaption 
from HTML 5. I've accounted for this and added styling for it. Look for it in 76-h.html:
<figcaption>Something Something Caption</figcaption>

Vintage paper background was acquired from here:
http://freeseamlesstextures.com/gallery/38-vintage-paper-background.html

Part 2
======
Restrictions, use Python 2.7? Alright, it's programmed in Flask.

```
    python Part2.py
```

Then you will either want:

```
    http://localhost:5000/good
    http://localhost:5000/bad
```

Also, I used HTML5 Boilerplate just to get started:
https://html5boilerplate.com/

And, finally, I needed something responsive to deal with different screen sizes, so Foundation CSS was used:
http://foundation.zurb.com/

bad.css and good.css clearly outline the portions I have done and the HTML body is written by me.

To create the box shadow, I used:
http://www.cssmatic.com/box-shadow

To create the gradient that is similar to The Oatmeal, I used:
http://www.colorzilla.com/gradient-editor/

Image credits:

Wood floor:
http://gnrbishop.deviantart.com/art/Wood-floor-86913934

Python Image:
http://ubotstudio.com/blog/wp-content/uploads/2014/12/python1.png

Notepad image under CC:
http://commons.wikimedia.org/wiki/File:Notepad_icon.svg

RSS Feed under CC:
http://commons.wikimedia.org/wiki/File:Rss112.png


License/Copyright
=================

Textual content is copyright Abram Hindle (C) 2013 under the CC-BY-SA
4.0 unported license. Attribution should be a hyperlink to the
repository and (C) 2013 Abram Hindle visibile in the text.

Code is licensed under the Apache 2.0 license.


