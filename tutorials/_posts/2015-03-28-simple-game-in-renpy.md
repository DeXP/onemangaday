---
layout: post
tags: [beginner]
title:  "Creating a simple game in RenPy"
preview: 
  file: renpy.png
  width: 220
  height: 150
date:   2015-03-28 14:14:01
curlang: en
linkadd: ../
picdir: ../pic/tutorials/renpy/OneMangaDay-
markdown: True
needHighLight: True
---

Visual novels creating is not such a difficult thing, as it might seem. And RenPy engine will help us: [http://renpy.org](http://renpy.org){:target="_blank"}. On the one hand, the engine is simple and understandable even for beginners. On the other hand, the engine is quite powerful and allows you to create really cool games. You need to download engine and install it. Nothing complicated in this process is not present, the default settings are good. Here is the RenPy main window:

![RenPy main window]({{ page.picdir }}RenPy-main-en.png){:.imgshad}

There is a list of projects on left. And active project options on the right (the active project is highlighted with blue in projects list ). To create your game you need to click "Add New Project" under the list of projects. Further, the engine will ask a few simple questions. Remember the name of the game should be in English (do not use international/unicode symbols).

So, you can proceed to writing game after creating the project. In the list, select edit script.rpy. This opens file editor (default editor offered by RenPy - Editra, is good enough). I like the dark color schemes for writing texts, so Dessert-theme just saves me. Here is my Editra after some tweaking:

![Editra Main Window]({{ page.picdir }}Editra-start-en.png){:.imgshad}

The code is quite simple too. In line 7 we define a character named "Eileen", whose name will be written with color #c8ffc8 (color can be taken in any graphics program, for example, GIMP or Photoshop). For brevity of writing a character assigned to the short name of "e". In 13 and 15 line literally written the character "e" (Eileen) says on the screen that is specified in quotes. Lines starting with a hash mark (#) are developer comments and not affected the game process.

Let's make some graphics for the game. The default resolution is 800x600 pixels. This setting can be changed in the options.rpy file, but for the first game such permission is optimal. Therefore it is necessary to create a Comipo panel with size 800x600. When you change the size by dragging the mouse near the panel is written, what size it is:

![Comipo Panel resize]({{ page.picdir }}Comipo-panel-resize.png){:.imgshad}

Let  we want to re-create such a scene in the game:

![Image in Comipo]({{ page.picdir }}Comipo-image.png){:.imgshad}


Exporting the layers one by one. We start with a background image, select the height was about 600, width 800. Details for beginners described in the tutorial [about export](comipo-basics-exporting.html). Other layers export must be done with the same settings. That's how exported knight layer looks like:

![Dex knight]({{ page.picdir }}Dex-knight.png){:.flag}


First consider a plot of the novel. I see a novel like this (left click works):

<p class="centered"><iframe src="{{ page.picdir }}ScratchMalvinaEn/index.html" class="noborder hidover" width="800" height="600" id="novell"></iframe></p>

This is how the RenPy code looks:

{% capture _code %}{% highlight python %}
define m = Character('Malya', color="#76e2e4")
image m oho = "Mala-o.png"
image m keks = "Mala-yee.png"

define dex = Character('Dex', color="#999999")
image dex norm = "Dex-knight.png"

image bg Green = "bg.jpg"


label start:
    scene black
    "It is not known when this story was there..." with dissolve
    "But once ... It still happened!" with dissolve
    scene bg Green with fade
    show dex norm at left with dissolve
    dex "Oh yeah! It looks even better when polished!"
    
    show m oho at right with dissolve
    m "Wow! How did you get so big?"
    m "Are you sure know how to use it?"
    dex "For sure! You're getting ahead now!"
    show dex norm at right with moveinright
    show m oho at left with moveinleft
    m "Wow! Indeed, you know how!"
    show m keks with dissolve
    m "This is awesome! Scratch the back once more, eh?"
    
    scene black
    "THE END!"
    return
{% endhighlight %}{% endcapture %}{% include customhighlight.html %}{{ _code }}

Code of creating characters has already been examined. Here we are in lines 1 and 5, creating new characters: *m* and *dex*. Innovation is the character states and image for each state. For example, for the character *m* state is set to *oho*, corresponds to the image *Mala-o.png* (line 2).

The game begins with the execution of the label *label start:* (line 11). Next we show that we will start on the black screen (*scene black*). Lines 13 and 14 - just the text that will be shown on the screen. Modifier *with* indicates modifier (animation), which will display the object. There is much animations, and each can be applied to almost anything.

Line 16: *show dex norm at left with dissolve*. Reads as follows: show character *dex* with state *norm*, on left, with animation fade. Line 17 - also a display of text, but as before the text we have the name of the character, the name will also be displayed.

Lines 23 and 24 - the animation of Malya and Dex position exchange. In these lines we use the *show* command, but since the character is already on the screen, then only animation will be applied.

In fact - everything our first game ready. It has a small source, is not very difficult to understand. Here lies another trick in the RenPy study - study it is necessary to gradually adding one new feature, and depending on how they affect. Good help is [Quickstart Guide](http://www.renpy.org/doc/html/quickstart.html){:target="_blank"}. Much more useful links can be found in the [Ren'Py Wiki](http://www.renpy.org/wiki/renpy/Wiki_Home_Page){:target="_blank"}.

Good luck in creating games!
