---
layout: post
title:  "Конвертирование PMD, или новые причёски для Comipo"
preview: 
  file: pmd.png
  width: 239
  height: 163
date:   2015-01-06 20:51:01
curlang: ru
linkadd: ../../
picdir: ../../pic/tutorials/pmd/OneMangaDay-
markdown: True
---

Manga Maker Comipo умеет импортировать 3D модели в следующих форматах: csu, mqo и obj. Из этих форматов распространённым является только obj, и тот скорее среди разработчиков 3D игр, чем среди модельеров причёсок и одежды. Зато в сети очень много причёсок, одежды и прочего удовольствия для программы Miku Miku Dance, сокращённо MMD. В данном уроке рассмотрен импорт пользовательских 3D моделей из формата PMD - формата 3D объектов Miku Miku Dance.

<img src="{{ page.picdir }}Custom-Hair.png" alt="Импортированные волосы в Comipo" class="imgshad" />

На рисунке выше показаны причёски <a href="http://mmdfakewings18.deviantart.com/art/MMD-Sporty-Hair-DL-213356416" target="_blank">Sporty Hair</a> и <a href="http://mmdfakewings18.deviantart.com/art/MMD-Windy-Hair-DL-199392092" target="_blank">Windy Hair</a> под авторством MMDFakewings18, уже импортированные в Comipo. Для конвертирования PMD в MQO проще всего воспользоваться программой "Pmd2mqo GUI": <a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank">https://github.com/DeXP/pmd2mqoGUI/releases/latest</a>

<a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank"><img src="{{ page.picdir }}pmd2mqoGUI.png" alt="Pmd2mqo GUI" class="imgshad"></a>

Сначала нужно распаковать куда-нибудь скачанный архив с причёской. Например, Windy Hair я распаковал в папку "E:\OneMangaDay\Windy Hair". Содержимое папки после распаковки архива:

<img src="{{ page.picdir }}windy-explorer-01.png" alt="Содержимое архива Windy Hair" class="imgshad" />

Хочу обратить внимание на файлы t010, t011, t013 - это текстуры, изображения "одеваемые" на модель. Без них импорт в Comipo будет работать некорректно, модель будет просто белой с чёрной обводкой.

Далее нужно сконвертировать имеемый PMD-файл в формат MQO. Для этого нужно открыть <a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank">Pmd2mqo GUI</a> и выбрать в ней нужный файл (или просто перетащить его мышкой, drag & drop). Если всё успешно выполнилось, то в папке появится ещё один файл - MQO:

<img src="{{ page.picdir }}windy-explorer-02-ru.png" alt="Конвертирование PMD-модели в формат MQO с помощью pmd2mqoGUI" class="imgshad" />


После конвертирования модели в формат mqo или obj, файл нужно импортировать в Comipo. Наиболее удобно просто перетащить мышью полученный MQO-файл в окно Comipo. Подробнее про импорт моделей можно прочитать в уроке "[Создание своих 3D объектов для Comipo](new-3d-objects-blender.html)". Причёски или одежду после импорта удобно привязывать к персонажу. Это описано в уроке "[Позиционирование объектов в Comipo](item-position.html)".

Вот так выглядят девушки со сторонними причёсками:

![Comipo: Девушки со сторонними причёсками]({{ page.picdir }}ready.png)

На сайте deviantart.com имеется много материалов для MMD: <a href="http://www.deviantart.com/browse/all/?q=MMD+Hair" target="_blank">причёски</a>, <a href="http://www.deviantart.com/browse/all/?q=MMD+Dress" target="_blank">платья</a> и <a href="http://www.deviantart.com/browse/all/?q=MMD" target="_blank">всё-всё-всё</a>.

<a href="https://github.com/DeXP/pmd2mqoGUI/releases/latest" target="_blank">Pmd2mqo GUI</a> написана специально для уроков на сайте "<a href='{{ page.url }}' target='_blank'>One Manga Day</a>", использует код конвертирования утилиты <a href="https://onedrive.live.com/?cid=9DA0FA00AC5A8258&id=9DA0FA00AC5A8258!337" target="_blank">pmd2mqo.exe</a>. Обычно утилита выдаёт наилучший результат конвертирования PMD в MQO. Однако результат далеко не всегда идеален. Можно также попробовать <a href="https://pypi.python.org/pypi/pymeshio/" target="_blank">импорт PMD для Blender</a> или PMX&nbsp;Editor (<a href="http://eoscustom3d.deviantart.com/art/English-Pmx-Editor-470421452" target="_blank">сслыка 1</a>, <a href="http://ibozo.deviantart.com/art/PMDEditor-0139-and-0219-english-translation-375517501" target="_blank">ссылка 2</a>), но эти методы гораздо сложнее.


Удачи при создании принципиально новых персонажей!
