---
layout: post
tags: [advanced, logo]
title:  "Steam logo Comipo"
preview: 
  file: steam.png
  width: 125
  height: 125
date:   2014-12-31 12:56:41
curlang: en
linkadd: ../
picdir: ../pic/tutorials/steam/OneMangaDay-
markdown: True
---

Steam logo creation is almost the same to [Android logo creation](android-logo.html). With few differences. First: it is not enought only spheres and cyllinders. Second: you need accurate geometry, to correctly display the conjugation. You need to import existance Steam logo image to Comipo to reach geometry accuracy. You can drag&drop image directly from file manager, or add it via "User Image" tab:

<img src="{{ page.picdir }}steam-start.png" alt="Imported Steam picture in Comipo" class="imgshad">

Lay out 3D primitives (2 spheres and 2 cones), as shown on picture:

![Comipo: adding sphere]({{ page.picdir }}start-objects.png)

Make objects white (Brightness 100%), hide it via "Visible" button. Than place 2 spheres for holes, make it black or dark blue:

<img src="{{ page.picdir }}hole-shperes.png" alt="Comipo: Hole spheres" class="imgshad">

Repeat previous step for inner spheres:

![Comipo: inner spheres]({{ page.picdir }}inner-spheres.png)

Make all visible, add column:

![Comipo: Steam column]({{ page.picdir }}column.png)

Make column white, than add shadow. You need to duplicate bottom primitives, to make a shadow (this is shown in [Android logo creation](android-logo.html) tutorial). The you need to add some blur to shadow, use "Filter"(F) button:

<img src="{{ page.picdir }}filter-blur.png" alt="Comipo: Blur" class="imgshad">

Now logo looks like this:

![Comipo: Steam logo with shadow]({{ page.picdir }}logo-shadow.png)

Now we add a sphere on bottom layer, as we want to get a round Steam icon. You also need to scroll sphere so the shaded part of it was on top, and light - on bottom of picture. Thus we will achieve a blue gradient later:

![Comipo: Background sphere]({{ page.picdir }}bg-sphere.png)

You can begin to play with color. The color should maximally repeat the color of the original image. I got the following settings:

![Comipo: Background sphere color]({{ page.picdir }}sphere-colorize.png)

You can now delete the original background image, and export the resulting icon:

![Comipo: Ready tutorial result]({{ page.picdir }}ready.png)

Good luck for creating logos!
