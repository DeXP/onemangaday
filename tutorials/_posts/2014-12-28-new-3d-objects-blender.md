---
layout: post
title:  "Making own 3D objects for Comipo"
preview: 
  file: blender.png
  width: 220
  height: 143
date:   2014-12-28 12:37:01
curlang: en
linkadd: ../
picdir: ../pic/tutorials/blender/OneMangaDay-
markdown: True
---

If you want to add a new 3D object to Manga Maker Comipo, than you need to create it in any 3D graphics program: Blender, 3DMax, Maya etc. I chose the house of the protagonist as the object. I painted it in <a href="http://www.blender.org/" target="_blank">Blender</a>. This is how the house looks initially in Blender:

<img src="{{ page.picdir }}Blender-init-object.png" alt="Initital object in Blender" class="imgshad">

First you need to make export from Blender to .Obj-file. Than import it in Comipo. Go to "User 3D Data" tab and press "Import User 3D Data" (F4). After that, the imported object will appear in Comipo:

![Comipo: Import of new User 3D model]({{ page.picdir }}Comipo-new-3D.png)

The very important option is "3D Edge Outline". It is responsible for the way Comipo will trace the egdes of a 3D object. Usual value is "Outline Only", it is only to make a stroke on a path. But it is better to choose the option "All Edge Outline" for house, then corners of the roof, windows and a balcony will be better. Incidentally, you can set up a preview image for the Asset List in the "Object Properties" or "Import" dialog:

<img src="{{ page.picdir }}Comipo-thumbnail.png" alt="Comipo Object settings" class="imgshad">

Ultimately, the house in Comipo looks like this:

<img src="{{ page.picdir }}Comipo-3D-result.png" alt="Correctly imported object in Comipo" class="imgshad">

Incorrect import example:

![Incorrect imported object in Comipo]({{ page.picdir }}House-Bad.png)

Firstly, import option "Outline Only" has been selected. Because of this windows and a balcony are poorly visible. You need to select "All Edge Outline" import option to correct this.

Secondly, the geometry is imported not correctly - this is especially evident from the trimmed triangle door. This is due to the fact that Blender used "rectangle" primitive for exporting, but Comipo not always correctly perceive them. Comipo likes "triangle" primitive. To fix this, you must correctly export model from Blender: enable the option "Triangulate Faces":

<img src="{{ page.picdir }}Blender-export.png" alt="Correct export in Blender for Comipo" class="imgshad">

Now the entire object correctly imported into Comipo:

![Correctly imported object in Comipo]({{ page.picdir }}House-Good.png)

You can not only create 3D models from scratch, but download from the Internet. Import is actually the same (pre-convert into a Obj format). Comipo is not always correctly imports 3D models, and often you must edit the models for correct import. However, you can increase likehood of correct import by using low-poly models, a models with a small number of polygons.

Good luck to you in a 3D format!

