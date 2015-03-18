---
layout: post
tags: [advanced,ext3d,background]
title:  "Конвертирование PMX, или новые сцены, 3D фоны для Comipo"
preview: 
  file: pmx.png
  width: 220
  height: 132
date:   2015-03-18 17:02:01
curlang: ru
linkadd: ../../
picdir: ../../pic/tutorials/pmx/OneMangaDay-
markdown: True
---


Импорт из PMD уже был рассмотрен в [уроке про дополнительные причёски](pmd-custom-hair.html). Цель этого урока - подчеркнуть, что импортировать можно не только причёски, сумочки, крылышки. Импортировать можно что угодно. Особенно полезным является импорт полноценной 3D-сцены, 3D-окружения. Например, это может быть парк, интерьер конкретного здания, или часть города с домами. Вот пример импортированной сцены в Comipo:

<img src="{{ page.picdir }}BlueStage-Comipo.png" alt="Импортированная сцена в Comipo" class="imgshad" />

Основным отличием 3D-сцен от мелких предметов является то, что они могут распространятся в большом количестве форматов. Например: PMD, PMX, X, MQO. Импорт PMD уже был рассмотрен в [уроке про дополнительные причёски](pmd-custom-hair.html). Хочу обрадовать, с помощью dxPmdxConverter можно конвертировать и PMX!

<a href="https://github.com/DeXP/dxPmdxConverter/releases/latest" target="_blank"><img src="{{ page.picdir }}dxPmdxConverter.png" alt="dxPmdxConverter" class="imgshad"></a>

В dxPmdxConverter в качестве выходного формата лучше использовать MQO - его Comipo импортирует более корректно. Конвертировать текстуры из BMP в PNG  тоже не обязательно - Comipo поддерживает BMP-текстуры с прозрачностями.

Для примера рассмотрим ещё одну работу MMDFakewings18: <a href="http://mmdfakewings18.deviantart.com/art/MMD-Blue-Stage-DL-216834158" target="_blank">Blue Stage</a>. Она хороша тем, что в архиве есть сцена сразу в нескольких форматах. Можно сравнить, как они будут отображаться на экране.

Для просмотра файлов типа "X" советую использовать программу <a href="http://www.open3mod.com/" target="_blank">Open 3 Mod</a>. Она бесплатна, позволяет просматривать многие 3D-форматы и конвертировать всё в том числе в OBJ. Вот как сцена выглядит в Open3mod:

<img src="{{ page.picdir }}open3mod.png" alt="Импортированная сцена в Open3mod" class="imgshad" />

Чтобы сохранить открытый файл как OBJ из меню программы "Tools" надо выбрать пункт "Export":

<img src="{{ page.picdir }}open3mod-export.png" alt="Экспорт файла из Open3mod" class="imgshad" />

Далее можно удостовериться, что разные конвертеры делают своё дело по-разному: размер файла может отличаться более, чем в 2 раза. Но с этой моделью нам повезло - вне зависимости, MQO или OBJ импортировать в Comipo, всё отобразится корректно и одинаково!

![Экспортированная из Comipo Blue Stage]({{ page.picdir }}BlueStage-ready.png)

Импорт в Comipo может занять несколько минут. После импорта может всплыть вот такое предупреждение:

<img src="{{ page.picdir }}Comipo-LargeData.png" alt="Comipo импорт большого файла" class="imgshad" />

Это значит, что у импортированного файла сложная геометрия, и что Comipo может на таких файлах подтормаживать. Но чаще всего это так же означает, что файл был импортирован корректно и можно пользоваться! Гораздо хуже, если при импорте выпала следующая ошибка:

<img src="{{ page.picdir }}Comipo-TooMany.png" alt="Comipo импорт слишком большого файла" class="imgshad" />

Это означает, что количество треугольников в модели больше, чем может поместиться в Comipo. Без серьёзных модификаций такую модель импортировать не удастся. На практике это означает, что можно сразу же начинать искать другую 3D-модель.

Напоследок хочу показать несколько импортированных в Comipo окружений. <a href="http://mmd3dcgparts.deviantart.com/art/MMD-Stage-39-486084016" target="_blank">MMD Stage 39</a> от MMD3DCGParts:

![Comipo Anime House Outside]({{ page.picdir }}AnimeHouseOutside.png) 


<a href="http://amiamy111.deviantart.com/art/MMD-HIGH-QAULITY-room-with-stairs-285462351" target="_blank">MMD HIGH QAULITY room with stairs</a> от amiamy111:

![Comipo качественна жилая комната]({{ page.picdir }}HQ-LivingRoom.png) 

<a href="http://danthrox.deviantart.com/art/Change-me-stage-MMD-295399315" target="_blank">Change me stage MMD</a> от Danthrox:

![Comipo Meiko Stage]({{ page.picdir }}MeikoStage.png) 


Скачать сцены можно с DeviantArt по запросу <a href="http://www.deviantart.com/browse/all/?q=MMD+Stage" target="_blank">MMD Stage</a>.

Удачи при создании новых 3D фонов!
