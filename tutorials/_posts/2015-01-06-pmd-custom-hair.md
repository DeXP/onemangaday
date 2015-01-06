---
layout: post
title:  "Converting PMD, or new hairstyles for Comipo"
preview: 
  file: pmd.png
  width: 239
  height: 163
date:   2015-01-06 20:51:01
curlang: en
linkadd: ../
picdir: ../pic/tutorials/pmd/OneMangaDay-
markdown: True
---

Manga Maker Comipo can import 3D models in the following formats: csu, mqo and obj. Obj format is the only widespread from this list. Obj format rather popular among game developers than in hairstyle and clothes fashion. But you can find a lot of hairstyles, clothes and other fun stuff for Miku Miku Dance, abbreviated MMD. This tutorial considered on import of custom 3D models in PMD format - the format of 3D objects in Miku Miku Dance.

<img src="{{ page.picdir }}Custom-Hair.png" alt="Imported Hairstyle in Comipo" class="imgshad">

The figure above show <a href="http://mmdfakewings18.deviantart.com/art/MMD-Sporty-Hair-DL-213356416" target="_blank">Sporty Hair</a> and <a href="http://mmdfakewings18.deviantart.com/art/MMD-Windy-Hair-DL-199392092" target="_blank">Windy Hair</a> hairstyle by MMDFakewings18. It is already imported into Comipo. The easiest way to convert PMD into MQO is a "Pmd2mqo GUI" utility: <a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank">https://github.com/DeXP/pmd2mqoGUI/releases/latest</a>

<a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank"><img src="{{ page.picdir }}pmd2mqoGUI.png" alt="Pmd2mqo GUI" class="imgshad"></a>

<a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank">Pmd2mqo GUI</a> written specifically for tutorials on "<a href='{{ page.url }}' target='_blank'>One Manga Day</a>", and uses codes from <a href="https://onedrive.live.com/?cid=9DA0FA00AC5A8258&id=9DA0FA00AC5A8258!337" target="_blank">pmd2mqo.exe</a>. Typically, the utility produces the best results in the conversion of PMD into MQO. However, the result is not always perfect. You can also try <a href="https://pypi.python.org/pypi/pymeshio/" target="_blank">PMD import for Blender</a> or PMX&nbsp;Editor (<a href="http://eoscustom3d.deviantart.com/art/English-Pmx-Editor-470421452" target="_blank">link 1</a>, <a href="http://ibozo.deviantart.com/art/PMDEditor-0139-and-0219-english-translation-375517501" target="_blank">link 2</a>), but these methods are much more complicated.

You must import result file into Comipo after converting the model into obj or mqo. This is described in the tutorial "[Making own 3D objects for Comipo](new-3d-objects-blender.html)". It is convenient to bind hairstyle or clothing to the character after importing. This is described in the tutorial "[Item Positioning in Comipo](item-position.html)".

Here is the girls with third-party hairstyles:

![Comipo: girls with third-party hairstyles]({{ page.picdir }}ready.png)

You can find a lot of MMD-stuff on deviantart.com: <a href="http://www.deviantart.com/browse/all/?q=MMD+Hair" target="_blank">hairstyles</a>, <a href="http://www.deviantart.com/browse/all/?q=MMD+Dress" target="_blank">dresses</a> and <a href="http://www.deviantart.com/browse/all/?q=MMD" target="_blank">all other stuff</a>.

Good luck in creating a fundamentally new characters!
