---
layout: post
title:  "Steam Greenlight banner in Comipo"
preview: 
  file: greenlight.png
  width: 329
  height: 86
date:   2015-01-29 19:35:27
curlang: en
linkadd: ../
picdir: ../pic/tutorials/greenlight/OneMangaDay-
markdown: markdown
---

Steam Greenlight banner can be divided into 4 areas: background, illuminated planet, text, information about the project. You can create each of them in Manga Maker Comipo. Take a closer look at the background. It is not uniformly gray, has colored patches in the upper right and lower left corners.

![Creating Steam Greenlight banner in Manga Maker Comipo]({{ page.picdir }}BG-start.png)

You need to fill the background with #181C1F color (24 red, 28 green, 31 blue). Place a spheres as shown in the figure above. Remove  3D-stroke, put a blur: Blur = 50. Red sphere colors:

<img src="{{ page.picdir }}BG-red-sphere.png" alt="Red background sphere" class="imgshad">

Green sphere:

<img src="{{ page.picdir }}BG-green-sphere.png" alt="Green background sphere" class="imgshad">

Result:

![Background with spheres]({{ page.picdir }}BG-spheres.png)

Now you can add the planet. This is a sphere, decorate it in the yellow-green:

![Planet glow]({{ page.picdir }}sun.png)

Duplicate the sphere, move lower one to some pixels left-top and add Blur = 5. Than paint top one into the color of the panel:

<img src="{{ page.picdir }}sun-color.png" alt="Sun color" class="imgshad">

Result:

![Planet glow]({{ page.picdir }}sun2.png)

Now add a glowing flare to planet. To do this, add a sphere and deform it, as shown below:

![Planet glow]({{ page.picdir }}sun3.png)

Add a Blur = 33 to new sphere, and the planet is getting ready:

![Planet glow]({{ page.picdir }}sun4.png)

Banner text:

![Banner text]({{ page.picdir }}text.png)

In this case font is also very important, as in the case of the [Amazon logo](amazon-logo.html). Fortunately, bold Arial font similar to the original. To get the spacing between letters in the "STEAM" word you can simply add spaces after each letter.

Add a picture of the project and obtain the final version of the banner:

<a href="http://steamcommunity.com/sharedfiles/filedetails/?id=372656709" target="_blank"><div class="greenLight-{% if page.curlang == "ru" %}ru{% else %}en{% endif %}" style="float: none; margin-left: auto; margin-right: auto">&nbsp;</div></a><div class="clear"></div>

Good luck on the green light!
