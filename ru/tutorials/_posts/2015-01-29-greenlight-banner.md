---
layout: post
title:  "Баннер Steam Greenlight в Comipo"
preview: 
  file: greenlight.png
  width: 329
  height: 86
date:   2015-01-29 19:35:27
curlang: ru
linkadd: ../../
picdir: ../../pic/tutorials/greenlight/OneMangaDay-
markdown: markdown
---

Баннер Steam Greenlight можно разделить на 4 области: фон, освещённая планета, текст, информация о проекте. В Manga Maker Comipo можно создать каждую из них. Для начала подробнее остановимся на фоне. Он не однородно серый, имеет цветные блики в правом верхнем и левом нижнем углах.

![Создание фона для баннера Steam Greenlight в Manga Maker Comipo]({{ page.picdir }}BG-start.png)

Для начала заливаем фон панели цветом #181C1F (24 красного, 28 зелёного, 31 синего). И располагаем сферы так, как показано на рисунке выше. Убираем им 3D-обводку, ставим размытие: Blur = 50. Красной сфере выставляем следующий цвет:

<img src="{{ page.picdir }}BG-red-sphere.png" alt="Красная фоновая сфера" class="imgshad">

Зелёной сфере:

<img src="{{ page.picdir }}BG-green-sphere.png" alt="Зелёная фоновая сфера" class="imgshad">

В результате получаем:

![Фон со сферами]({{ page.picdir }}BG-spheres.png)

Теперь можно добавить планету. Для этого нужно добавить на панель сферу, разукрасить её в жёлто-зелёный:

![Свечение планеты]({{ page.picdir }}sun.png)

Дублируем сферу, нижнюю чуть смещаем и добавляем Blur = 5, верхнюю красим в цвет фоновой панели:

<img src="{{ page.picdir }}sun-color.png" alt="Цвет солнца" class="imgshad">

Результат:

![Свечение планеты]({{ page.picdir }}sun2.png)

Теперь добавляем светящейся планете блик. Для этого добавим сферу и деформируем её, как показано на рисунке:

![Свечение планеты]({{ page.picdir }}sun3.png)

Добавляем новой сфере Blur = 33 и получаем готовую планету:

![Свечение планеты]({{ page.picdir }}sun4.png)

Далее добавляется текст:

![Текст баннера]({{ page.picdir }}text.png)

Здесь как и в случае с [логотипом Amazon](amazon-logo.html) также очень важен шрифт. К счастью, полужирное начертание шрифта Arial похоже на оригинальное. Чтобы получить отступы между буквами в слове "STEAM" после каждой буквы добавлен пробел.

Добавляем картинку проекта и получаем конечный вариант баннера:

<a href="http://steamcommunity.com/sharedfiles/filedetails/?id=372656709" target="_blank"><div class="greenLight-{% if page.curlang == "ru" %}ru{% else %}en{% endif %}" style="float: none; margin-left: auto; margin-right: auto"></div></a><div class="clear"></div>

Удачи Вам на зелёный свет!
