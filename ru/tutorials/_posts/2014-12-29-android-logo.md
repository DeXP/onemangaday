---
layout: post
tags: [middle, logo]
title:  "Логотип Android в Comipo"
preview: 
  file: android.png
  width: 112
  height: 115
date:   2014-12-29 17:39:35
curlang: ru
linkadd: ../../
picdir: ../../pic/tutorials/android/OneMangaDay-
markdown: True
---

Для создания робота-логотипа Android воспользуемся трёхмерными примитивами со вкладки "3D Item", раздел "91. Primitive". А именно нам понадобятся: колонна, сфера, куб. Всё, больше ничего не нужно. 

Начнём построение с головы Андроида. Для этого возьмём сферу, растянем её на всю 3D область, как на картинке:

<img src="{{ page.picdir }}start-sphere.png" alt="Стартовая сфера в Comipo" class="imgshad">

Далее сдвигаем 3D-объект сферы частично за отображаемые рамки. Для этого надо взяться мышью примерно там, где зелёный крестик, и потянуть:

![Comipo: движение сферы]({{ page.picdir }}move-sphere.png)

Ставим цвет сферы с помощью кнопки "Change Color"(C) в соотвествии с рисунком:

<img src="{{ page.picdir }}change-color.png" alt="Изменение цвета 3D объекта в Comipo" class="imgshad">

Далее располагаем на голове ещё 2 сферы и 2 цилиндра. Это наши глаза и антенны соответственно. Вращать можно за помеченные зелёным кружки:

![Comipo: глаза и антенны]({{ page.picdir }}2-sphere-2-cyl.png)

Антеннам выставляем те же параметры цвета, что и голове. У глаз ползунок яркости ("Brightness") выкручиваем на 100%. Получаем:

![Comipo: голова андроида без тени]({{ page.picdir }}head-no-shadow.png)

Голова готова, осталось добавить тень. Для этого выделяем голову и антенны, копируем (Ctrl+C), опять вставляем (Ctrl+V).

![Comipo: голова андроида]({{ page.picdir }}select-shadow.png)

Вставленные слои отправляем на задний план (B, Shift+F4), немного сдвигаем, ставим в качестве цвета чуть более тёмный зелёный. При необходимости можно выключить 3D обводку (F9):

<img src="{{ page.picdir }}3d-outline.png" alt="Настройки 3D обводки Comipo" class="imgshad">

И получаем конечный результат:

![Comipo: готовая голова андроида]({{ page.picdir }}head-ready.png)

Дальнейшее рисование Андроида не представляет проблем, т.к. и дальше используются только эти техники. 

![Comipo: готовый Андроид]({{ page.picdir }}Android-Ready.png)

Удачи, и да пребудет с Вами сила Android!