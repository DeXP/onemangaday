label badend:
    $ goodEnd = False
    scene black with fade
    play music "Music/Metal1.OGG" fadeout 1 fadein 2
    centered "И захватили машины этот мир." with dissolve
    centered "И было всё плохо. " with dissolve
    centered "Ибо для победы человечества не хватило всего одних рабочих рук... " with dissolve
    centered "Твоих рук! " with dissolve
    centered "{size=36}{b}ПЛОХАЯ КОНЦОВКА{/b}{/size}" with wipeleft
    if not persistent.bad1end:
        $ achId = "b1e"
        $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
        $ achText = __("\"Не устроиться на работу\"")
        call showAchiv
    $ persistent.bad1end = True
    centered "( P.S.  Не забудьте найти другие концовки! )" with irisout
    jump titles
    return
    
    
label goodend:
    $ goodEnd = True
    scene black with fade
    #centered "Ведь мы - одна команда!"
    centered "Вместе мы сделали ещё много-много релизов."
    centered "И были все счастливы!"
    centered "{size=36}{b}ХОРОШАЯ КОНЦОВКА{/b}{/size}" with wipeleft
    jump titles
    return
    
    
    
label titles:
    scene bg Doska with fade
    centered "Над игрой работали:" with dissolve
    show Cracker at topright with dissolve
    show dexp joybig with moveinleft:
        xalign -0.27 yalign 1.0
    centered "Сюжет, графика, музыка,\n
идея и реализация:\n
{b}DeXPeriX{/b} a.k.a. Храбров Дмитрий\n
{a=http://dexperix.net}http://dexperix.net{/a}"  #with dissolve #"\n"
    hide Cracker with dissolve
    
    
    image CrEn = "items/flags/en.jpg"
    show dexp thinkbig:
        xalign -0.34 yalign 1.0
    show CrEn:
        xalign 0.52 yalign 0.85
    show prana clouds:
        xalign 1.45 yalign -2.5
    with dissolve
    centered "Перевод на английский:\n
{b}Mari Prianaja{/b},\n
{b}DeXPeriX{/b} a.k.a. Храбров Дмитрий\n\n

Улучшения английского текста:\n
{b}Mangles{/b} a.k.a. Richard Hogan,\n
Warren '{b}Wazza{/b}' Brent"
    
    show dexp thinkbigflip with dissolve:
        xalign -0.4 yalign 1.9
    centered "Вычитка английского текста:\n
bluecasuality@gmail.com (День 1)\n
{b}EeuorT{/b} a.k.a. Robert Nesbitt (День 2, 7)\n
{b}PintSizedPurple{/b} a.k.a. Will Williams (3, 4)\n
{b}Mangles{/b} a.k.a. Richard Hogan (День 5)\n
Warren '{b}Wazza{/b}' Brent (День 6)" with dissolve
    hide CrEn
    
    

    image CrRu = "items/flags/ru.jpg"
    show CrRu with dissolve:
        xalign 0.52 yalign 0.85
    show prana clouds with moveinbottom:
        xalign 1.45 yalign 3.0
    show lin laughbig with moveinright:
        xalign 1.4 yalign -1.4
    show dexp fearbigflip with dissolve:
        xalign -0.44 yalign 1.0
    centered "Вычитка русского текста:\n
{b}Selene=){/b} a.k.a. Березовская Любава,\n
{b}DeXPeriX{/b} a.k.a. Храбров Дмитрий,\n
{b}Mari Prianaja{/b}"
    
    hide dexp with moveoutleft
    hide prana with dissolve
    hide lin with moveoutbottom
    hide CrRu
    
    
    show BinocularMask at left with dissolve
    centered "Перевод на другие языки:\n\n
{image=items/flags/pl.jpg} Польский: damianklu a.k.a. Damian K."
    hide BinocularMask with dissolve
    
    
    
    show lap bigquestion with moveinright:
        xalign 1.39 yalign 1.0
    #show lap titles with moveinleft:
    #    xalign -0.25 yalign 1.0
    show mala angrybig with moveinleft:
        xalign -0.4 yalign 1.0
    show lyba eating with moveinbottom:
        xalign 0.49 yalign 7.5
    #    xalign 0.49 yalign 12.0
    centered "Вспомогательные элементы сюжета:\n
{b}Lybares{/b} a.k.a. Губарь Любовь,\n
{b}Malvina{/b} a.k.a. Скрябина Татьяна,\n
{b}lapschedui{/b} a.k.a. Погорельченко Людмила  "
    hide lap with moveoutleft
    hide mala with moveoutright
    hide lyba with moveoutbottom
    

    show lexa lookdown with moveinbottom:
        xalign 1.41 yalign -1.5
    show ulilla miltablesad with moveinleft:
        xalign -0.25 yalign 1.5   
    centered "Изображения для сканирования и клина:\n
{b}eng. Zubr{/b} a.k.a. Бурим Алексей\n
\n
Бэта-тестеры:\n
{b}Ulilla{/b} a.k.a. Байкова Юлия,\n
{b}Bismut{/b} a.k.a. Жаворовнков Дмитрий"
    hide lexa with moveoutbottom
    hide ulilla with moveoutleft

    
    show Server with dissolve:
        xalign -0.1 yalign 4.0
    centered "Использованные средства:\n
- Движок: {a=http://renpy.org}RenPy{/a} от PyTom ({a=http://www.renpy.org/dl/lgpl/}LGPL{/a})\n
- Звуки с сайта {a=http://freesound.org}FreeSound.org{/a}\n
- Графика: {a=http://www.comipo.com/en/}Manga Maker ComiPo!{/a}\n
- Дополнительная графика: {a=http://gimp.org}GIMP{/a}\n
- Музыка: {a=http://magix.com/}Magix Music Maker 2014{/a}" # with dissolve#"\nЕщё есть \"Справка\" в главном меню!"
    hide Server
    
    show Add3D with dissolve
    centered "Сторонние 3D-модели:\n
- Frilly Dress от {a=http://chibi-baka-san.deviantart.com/}Chibi-Baka-San{/a}\n
- Long Nightie из набора\n
\"B Cup Clothes\" от {a=http://ina-haru.deviantart.com/}Ina-Haru{/a}\n
- Maid Outfit от {a=http://www.comee.jp/userinfo.php?userid=457}Hekemoko{/a}\n
- Branch of tree от {a=http://www.mangasozaibox.comee.jp/users/user_info/id:13}Sion 42{/a}"
    hide Add3D with dissolve
    
    image CrKaska = "items/Kaska.png"
    show CrKaska at left:
        #xalign 0.9 yalign 0.25
        xalign 0.52 yalign 0.7
    centered "Больше информации можно найти на сайте:\n{a=http://OneMangaDay.dexp.in}http://OneMangaDay.dexp.in{/a}\n
\n
Или на сайте автора:\n
{a=http://dexperix.net}http://dexperix.net{/a}"  with dissolve
    #hide CrKaska
    
    image SteamGreenlight = "items/SteamGreenlight.png"
    image SteamIcon = "items/SteamIcon.png"
    show SteamGreenlight at left:
        xalign 0.9 yalign 0.1
    show SteamIcon at left:
        xalign 0.0 yalign 1.0
    with dissolve
    centered "Отдельное спасибо проголосовавшим за игру в {a=http://steamcommunity.com/sharedfiles/filedetails/?id=372656709}Steam Greenlight{/a}.\n
И площадке {a=http://store.steampowered.com/app/365070}Steam{/a} в общем за возможность опубликовать игру.\n
\n
Так же огромное спасибо всем бэта-тестрам финальной версии. Без вас игра не получилась бы настолько хорошей!"
    hide SteamGreenlight
    hide SteamIcon
    with dissolve
    
    show Flags at topleft
    centered "Спасибо, что были с нами!" with dissolve
    #hide Flags
    
    if goodEnd:
        show lin laughbig at right with moveinleft
        lin "Увидимся в следующей части!"
        hide lin with fade
    
        show drakoha norm with easeinright:
            xalign 0.5 yalign 2.5
        drakoha "Эй! А я только с солью вернулась..."
    return
