---
layout: post
tags: [advanced,ext3d,background]
title:  "Converting PMX, or new stages and 3D backgrounds for Comipo"
preview: 
  file: pmx.png
  width: 220
  height: 132
date:   2015-03-18 17:02:01
curlang: en
linkadd: ../
picdir: ../pic/tutorials/pmx/OneMangaDay-
markdown: True
---

Imports from PMD has already been considered in [the lesson about additional hairs](pmd-custom-hair.html). The purpose of this lesson is to emphasize that you can import not only hairstyles, handbags, wings. You can import anything. The import of full 3D-scenes, 3D-environment is especially useful. For example, it could be a park, the interior of a particular building, or part of the city with houses. Here is an example of the imported stage Comipo:

<img src="{{ page.picdir }}BlueStage-Comipo.png" alt="Comipo: Imported stage" class="imgshad" />

The main difference between 3D-stages and small 3D-items is that stages can spread to a large number of formats. For example: PMD, PMX, X, MQO. Import from PMD has already been considered in [lesson about additional hair style](pmd-custom-hair.html). dxPmdxConverter can convert PMX too!

<a href="https://github.com/DeXP/dxPmdxConverter/releases/latest" target="_blank"><img src="{{ page.picdir }}dxPmdxConverter.png" alt="dxPmdxConverter" class="imgshad"></a>

It is better to set MQO as dxPmdxConverter's output format. Comipo imports MQO more correctly, than OBJ. You also do not need to convert textures from BMP to PNG - Comipo supports BMP-texture with transparency.

Let's an example. There is one more work from MMDFakewings18: <a href="http://mmdfakewings18.deviantart.com/art/MMD-Blue-Stage-DL-216834158" target="_blank">Blue Stage</a>. It is good that there is a scene in several formats. You can compare how they are displayed on the screen.

To view the "X"-files you can use <a href="http://www.open3mod.com/" target="_blank">Open 3 Mod</a> program. It is free and allows you to view many 3D-formats and convert it to everything including OBJ. Here's how the scene looks like a Open3mod:

<img src="{{ page.picdir }}open3mod.png" alt="Imported stage in Open3mod" class="imgshad" />

To save the opened file as an OBJ you must use "Tools" menu, select "Export":

<img src="{{ page.picdir }}open3mod-export.png" alt="Export from Open3mod" class="imgshad" />

Next, you can be sure that different converters do their work in different ways: file size may differ by more than 2 times. But with this model, we were lucky - regardless, MQO or OBJ import into Comipo, everything is displayed correctly and the same!

![Exported Comipo Blue Stage]({{ page.picdir }}BlueStage-ready.png)

Imports in Comipo may take several minutes. After importing a warning may emerge:

<img src="{{ page.picdir }}Comipo-LargeData.png" alt="Comipo Large file importing" class="imgshad" />

This means that the imported file have a very complex geometry, and Comipo may slow down to such files. But more often it just means that the file was imported correctly, and you can enjoy! Much worse, if imports had the following error:

<img src="{{ page.picdir }}Comipo-TooMany.png" alt="Comipo Import Too large file error" class="imgshad" />

This means that the number of triangles in the model more than can fit in Comipo. Such a model can not be imported to Comipo without serious modifications. In practice, this means that you can immediately start looking for another 3D-model.

Finally I want to show some imported into Comipo environments. <a href="http://mmd3dcgparts.deviantart.com/art/MMD-Stage-39-486084016" target="_blank">MMD Stage 39</a> by MMD3DCGParts:

![Comipo Anime House Outside]({{ page.picdir }}AnimeHouseOutside.png) 


<a href="http://amiamy111.deviantart.com/art/MMD-HIGH-QAULITY-room-with-stairs-285462351" target="_blank">MMD HIGH QAULITY room with stairs</a> by amiamy111:

![Comipo High Quality living room]({{ page.picdir }}HQ-LivingRoom.png) 

<a href="http://danthrox.deviantart.com/art/Change-me-stage-MMD-295399315" target="_blank">Change me stage MMD</a> by Danthrox:

![Comipo Meiko Stage]({{ page.picdir }}MeikoStage.png) 


You can download environments from DeviantArt by search query: <a href="http://www.deviantart.com/browse/all/?q=MMD+Stage" target="_blank">MMD Stage</a>.

Good luck in creating new 3D backgrounds!
