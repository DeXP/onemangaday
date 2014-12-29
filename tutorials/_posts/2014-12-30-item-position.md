---
layout: post
title:  "Item Positioning in Comipo"
preview: 
  file: hand.png
  width: 220
  height: 186
date:   2014-12-29 17:39:35
curlang: en
linkadd: ../
picdir: ../pic/tutorials/hand/OneMangaDay-
markdown: True
---

Today we will give a cottage into the character hands. Cottage made in the previous [tutorial](new-3d-objects-blender.html). It is understood that the object is already correctly imported and displayable in the Assest list. First you need to add a character to the panel. Than choose it's position (in this example a posture №100):

<img src="{{ page.picdir }}hand-start.png" alt="Character in Comipo" class="imgshad">

Rotation buttons (Alt+Up, Alt+Down, Alt+Left ...) are shown by a red border, green frame isolated "Change Pose" and "Change Item" buttons. The blue-marked square controls the size (scale) of the character.

Next, scale and rotate the character so that the left hand is only visible, as in the picture:

![Character's hand in Comipo]({{ page.picdir }}hand-hand.png)

Add the house to the hand. To do this, press the "Change Item"(F12), in the first screenshot is highlighted in green. Next, choose the category "Right Hand Item", specifics "Right_Hand(Palm)":

<img src="{{ page.picdir }}change-item.png" alt="Change Item in Comipo" class="imgshad">

The specifics in this case refers to how the character will keep the subject: a fist or palm. In fact, these two options differ only in the anchor point.

The previous step can end up with something like this with high probability:

![Icorrect object size in Comipo]({{ page.picdir }}incorrect-size.png)

So, the reason is wrong settings of angle, position and size. Back in the window "Change Item"(F12), and play with the sliders. Changes are immediately displayed in Comipo in the main window. I get the following:

<img src="{{ page.picdir }}correct-size-values.png" alt="Playing with size/angle/position sliders in Comipo" class="imgshad">

Now the house looks as it should be!

![Object, attached to the character in Comipo]({{ page.picdir }}hand-dom.png)

Всё, объект привязан к персонажу. Персонажу можно менять позу, размер, положение, но домик всё-равно останется с ним:
The object is attached to the character now. You can change the character's position, size, position, but the house will stay with it:

![Object in Comipo]({{ page.picdir }}hand-pose.png)

If you add a little effects from the "Image Item" tab, you can get the following picture:

![Tutorial result]({{ page.picdir }}ready.png)

Good luck in positioning!

