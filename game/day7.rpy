label day7:
    play music "Music/Chillout6v7.OGG" fadeout 1 fadein 2
    scene black with fade
    centered "День 7" with dissolve
    centered "Ведь всё ещё только начинается?"
    
    
    $ renpy.sound.play("sound/flathill_rain-and-thunder-4.ogg", fadein=2, loop=True)
    #$ renpy.music.play("Music/Chillout6v7.OGG", fadein=2, synchro_start=True)
    scene bg SchoolRain with fade
    show lexa norm at center with dissolve
    lexa "Кажется, дождик начинается..."
    
    show lyba zont behind lexa with moveinright:
        xalign 0.85 yalign 1.2
    lyba "Лёша! Не стой под дождём, простынешь!"
    lyba "Ну и что, что работы от тебя не дождешься? Ты ж всё-равно часть команды..."
    lyba "В общем, не смей заболевать!"
    lyba "... Блин, и почему за всеми должна следить я? Я вам что, мама что ли?"
    lyba "О чём задумался?"
    menu:
        ""
        "О дожде":
            show lexa attention with dissolve
            lexa "Сильный дождь не длится долго. Он скоро закончится."
        "О серверах":
            show lexa attention with dissolve
            lexa "Думаю о том, как поставить HTML на мой сервер XW!"
        "О людях":
            show lexa attention with dissolve
            lexa "Видишь, люди идут? Так вот, они все когда-нибудь умрут!"
        "Может отдадим проект перехватчикам?":
            $ penalty += 1
            show lexa attention with dissolve
            lexa "Зачем мы взвалили на себя лишнюю работу?"
            lexa "Может, пускай перехватчики забирают свой проект?"
            lexa "Жизнь так сложна..."
    show lyba zontcrazy with dissolve
    lyba "А ну иди под крышу!"
    show lexa norm at center with dissolve
    lyba "Философ, блин..."
    
    
    scene black with fade
    centered "В то же время, пока Лайби спасает Лёшу от насморка" with dissolve
    
    
    play music "Music/ePop.OGG" fadeout 1 fadein 2
    scene bg EmptyClass42 with fade 
    stop sound
    
    show lap norm at right with dissolve
    show dexp think at left behind lap with dissolve
    dexp "Лап!"
    dexp "Я активно работаю над мангой. Вот недавно отдал свой перевод на редактуру Янушке."
    dexp "Но даже работа не помогает мне отвлечься..."
    dexp "Ты мне всё-таки нравишься!"
    $ lap_sex = False
    show dexp norm with dissolve
    menu:
        ""
        "Шпилли-вилли":
            $ lap_sex = True
            dexp "Пойдём сегодня вечером шпилли-вилли!"
        "Заняться любовью":
            $ lap_sex = True
            dexp "Я хочу заняться с тобой половой любовью!"
        "Нравишься только как клинер!":
            dexp "Но нравишься ты мне только как клинер."
            dexp "У тебя получаются прелестные изображения!"
            show lap joy with dissolve
            lap "Спасибо, Дэкс! Знаешь, я..."
            dexp "Но как девушка ты меня совершенно не интересуешь!"
            dexp "Я даже не считаю тебя красивой!"
            
    show lap angry with dissolve
    lap "Чего-чего, прости?"
    if lap_sex:
        dexp "Ну, это, того..."
    else:
        dexp "Я сказал то, что считаю нужным..."
    
    play music "Music/Metal1.OGG" fadein 1
    hide lap with dissolve
    show lap fight with dissolve:
        xalign 1.2 yalign 1.5
    play sound "sound/mattskydoodle_censor-beep.ogg"
    #show dexp 
    show lap fight with moveinright:
        xalign 0.5 yalign 0.15
    play sound "sound/ekokubza123_punch.ogg"
    show Punch with dissolve:
        xalign 0.23 yalign 0.42
    show dexp fly with dissolve
    show dexp fly with hpunch
    lap "Умри!"
    
    show dexp fly with moveinright:
        xalign -4.0 yalign 1.5
    hide Punch with dissolve
    show lap angry at center with dissolve
    lap "А ну-ка повтори ещё раз, что сказал!"
    hide lap with moveoutleft
    play sound "sound/ekokubza123_punch.ogg"
    show dexp fearbig at offscreenleft with hpunch 
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Лап! Ты всё не так поняла!" with vpunch
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Я всё объясню!" with hpunch
    play sound "sound/ekokubza123_punch.ogg"
    hide dexp with vpunch
    
    
    
    scene black with fade
    play music "Music/Chillout6v7.OGG" fadeout 1 fadein 2
    centered "А тем временем" with dissolve
    
    scene bg Office with fade
    show TopCrack at topleft with dissolve
    show yana down at left with dissolve
    yana "Господи! За что мне эти мучения?"
    show yana down2 at left with dissolve
    yana "Неужели Дэкс не может переводить по-человечески!?"
    
    show mirei norm at center with moveinright
    mirei "Ну, ну. Янушка, не плачь!"
    show yana down at left with dissolve
    mirei "Он когда-нибудь научится."
    mirei "Будет и на твоей улице праздник!"
    
    show dexp norm at right with moveinright
    show yana down2 at left with dissolve
    dexp "Расступитесь, пропустите! Спешу!"
    hide dexp with moveoutleft
    
    play music "Music/Metal1.OGG" fadein 1
    show lap angry at right with moveinright
    lap "Здесь Дэкс мимо не пробегал?"
    
    menu:
        ""
        "Нет, не пробегал":
            lap "Обмануть решили? Вот же его следы!"
            pass
        "Да, только что тут был":
            lap "Ага! Вижу его следы!"
            pass
    show lap fight with dissolve
    hide lap with moveoutleft
    show dexp fearbig at offscreenleft
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Лап! Я не хотел!" with vpunch
    
    play music "Music/eDance1.OGG" fadein 1
    mirei "Ну вот видишь?"
    hide TopCrack with dissolve
    show yana downhappy with dissolve
    yana "Спасибо! Продолжим работать?"
    mirei "Ага!"
    
    
    
    scene bg Staircase with fade
    show carry spy at left with dissolve
    carry "Да. Я наконец получила коды доступа к главному компьютеру!"
    carry "Записывайте: \"икc, игрек, и краткое"
    play music "Music/Movie7.OGG" fadein 1
    show lyblabla normal at center with moveinright
    lyblabla "Кэрри, что это ты делаешь..."
    hide lyblabla
    show lyba angryflip with dissolve
    lyba "Совсем обалдела уже?!"
    hide carry with moveoutleft
    show carry norm at left with easeinleft
    carry "Лайби! Я больше не буду!"
    show lyba pistol1 with dissolve
    lyba "Не будешь. Не сможешь."
    show carry question with dissolve
    carry "Ч... что это?"
    carry "Неужели, пистолет!?"
    show lyba pistol2 with dissolve
    lyba "Да! И я тебя замочу!"
    show carry fear with dissolve
    carry "Нет! Не надо!"
    carry "Я жить хочу!"
    carry "Я честно-честно больше не будууу!!!"
    hide lyba
    show lyblabla normal at center with dissolve
    #play music "Music/EuroDance2.OGG" fadein 1
    play music "Music/Dubstep1.OGG" fadeout 1 fadein 2
    lyblabla "Ну... Ладно!"
    show carry question with dissolve
    lyblabla "Смотри мне! Чтоб больше не повторялось..."
    show lyblabla silent
    #centered ""
    show Question with dissolve:
        xalign 0.33 yalign 0.0
    $ renpy.pause(0.5)
    hide Question with dissolve
    carry "Лайби... А ты правда нажала бы на курок?"
    show lyblabla sulk with dissolve
    lyblabla "Конечно. Я уже не раз так делала!"
    show carry fear with dissolve
    carry "И я бы умерла?"
    show lyblabla normal with dissolve
    lyblabla "Нет конечно!"
    show carry question with dissolve
    lyblabla "Пистолет же водяной!"
    show lyblabla silent
    show carry surprised with dissolve
    carry "Ну и дела..."
    
    
    
    play music "Music/EuroDance2.OGG" fadein 1
    scene black with fade
    centered "Несколько позже, на крыше" with dissolve
    
    scene bg Roof with fade
    show lyblabla silent at right with dissolve
    show ulilla norm at center
    show dexp norm at left with moveinleft
    dexp "Так!"
    show dexp laugh with dissolve
    dexp "А давайте мириться!"
    #vetka
    $ together = False
    $ allowGoodEnd = True
    menu:
        ""
        "Работать над проектом вместе":
            $ together = True
        "Отдать проект":
            $ penalty += 3
    if penalty >= 7:
        $ allowGoodEnd = False
        
    if allowGoodEnd:
        dexp "У нас были разногласия, но теперь давайте работать вместе!"
        if together == False:
            dexp "Тем более, большая часть команды против того, что бы отдать этот проект."
        show ulilla joy with dissolve
        ulilla "А давайте!"
        show lyblabla normal with dissolve
        lyblabla "Я не против."
        lyblabla "Мы ведь решили все разногласия."
        lyblabla "Теперь всё будет хорошо!"
        show lyblabla sulk with dissolve
        lyblabla "О! У меня идея..."
    
        jump photoend
    else:
        # Shrine end
        show lyblabla normal
        lyblabla "Изначально я была против."
        if together:
            lyblabla "И некоторые меня в этом поддерживают."
        lyblabla "Но раз большая часть команды хочет именно так..."
        show lyblabla sulk with dissolve
        lyblabla "Хорошо. Мы отдаём проект!"
        lyblabla "Переводите на здоровье."
        show lyblabla silent with dissolve
        
        play music "Music/Fast.OGG" fadein 1
        show dexp angry with dissolve
        dexp "Да что же это происходит такое, а?"
        dexp "Это был мой любимый проект!!!"
        dexp "Раз так, то я ухожу!"
        hide dexp with moveoutleft
        
        show ulilla joy with dissolve
        ulilla "Хорошо, что мы смогли договориться!"
        show ulilla norm with dissolve
        ulilla "Жаль только, что Дэкс ушёл..."
        
        show lap joy at left with moveinleft
        lap "Всем привет!"
        lap "А где Дэкс?"
        show lyblabla normal
        lyblabla "Он ушёл."
        lap "Куда?"
        lyblabla "Совсем..."
        show lyblabla silent 
        show lap surprized with dissolve
        lap "Ч... что?"
        
        show lyblabla normal
        lyblabla "Дэкс сказал, что уходит. Ведь его любимый проект отдали перехватчикам."
        show lap norm with dissolve
        lap "Вот оно значит как..."
        lap "Знаете... Я его, пожалуй, догоню!"
        show lap angry with dissolve
        lap "Ну я ему сейчас устрою!"
        hide lap with moveoutleft
        
        jump shrineend



label shrineend:
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2 
    scene black with squares
    centered "У каждого свои воспоминания" with dissolve
    centered "Воспоминания бывают хорошие, бывают плохие... Разные!" with dissolve
    centered "И ведь на самом деле не важно, какие воспоминания" with dissolve
    centered "Важно то, что они есть!" with dissolve
    #centered "И у меня они были именно такие"
    scene bg Shrine with squares
    
    show Bench:
        xalign 0.93 yalign 0.76
    show bab norm at right with dissolve
    show ded norm with dissolve:
        xalign 0.9 yalign 1.0
    show BookLay with dissolve:
        xalign 0.67 yalign 0.83
    ded "Даа... Весёленькая у нас была молодость!"
    ded "Хорошо, что ты меня тогда догнала..."
    ded "А то молодой был, вспыльчивый... Кто его знает, что мог натворить..."
    show bab smile with dissolve
    bab "Да уж, было времечко. Сколько лет-то уже прошло?"
    show ded think with dissolve
    ded "Вроде бы, 40."
    show ded norm with dissolve
    show bab norm with dissolve
    bab "40 лет... Как же много. А кажется, будто всё было вчера."
    show bab smile with dissolve
    bab "А помнишь что ты мне в тот же день наговорил?"
    show ded think with dissolve
    ded "Может, лучше не надо об этом?"
    bab "Надо, надо!"
    show ded norm with dissolve
    if lap_sex:
        bab "Пошлости всякие начал говорить!"
        show bab norm with dissolve
        bab "Знаешь, как я тогда засмущалась?"
        bab "Говорить такое..."
        show bab smile with dissolve
        bab "А ведь ты мне уже тогда нравился!"        
    else:
        bab "Я же тогда красавица была!"
        show bab norm with dissolve
        bab "А ты мне тут бац такое. Мол не интересуешь совсем."
        show bab smile with dissolve
        bab "Вот тогда-то ты мне и понравился!"
    show ded think with dissolve
    ded "Да? А я и не догадывался даже!"
    show ded norm with dissolve
    ded "Эх, молодость, молодость..."
    $ renpy.pause(1)
    show ded echi with dissolve
    ded "О! Смотри какая красотка идёт!"
    show bab angry with dissolve
    show Anger:
        xalign 0.83 yalign 0.15
        alpha 0.2 zoom 0.3
        linear 0.5 alpha 1.0 zoom 0.8
        linear 0.5 alpha 0.4 zoom 0.4
        linear 0.5 alpha 1.0 zoom 1.0
    $ renpy.pause(2)
    show bab fight with dissolve
    $ renpy.pause(0.5)
    play sound "sound/ekokubza123_punch.ogg"
    show black with hpunch
    hide Anger
    hide BookLay
    show ded echiflip:
        xalign 0.6 yalign 1.0
    $ renpy.pause(0.5)    
    hide black with dissolve
    ded "Ты совершенно не изменилась за 40 лет!"
    show bab angry with dissolve
    bab "Ты тоже..."
    $ renpy.pause(0.5)
        
    
    scene black
    if not persistent.shrineEnd:
        $ achId = "shrine"
        $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
        $ achText = __("\"Дожить до старости\"")
        call showAchiv
    $ persistent.shrineEnd = True
    centered "{size=36}{b}КОНЕЦ{/b}{/size}" with wipeleft
    jump titles
    return



label photoend:
    $ goodEnd = True
    call ending_photo
    scene black with fade
    if not persistent.photoEnd:
        $ achId = "photo"
        $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
        $ achText = __("\"Общее фото\"")
        call showAchiv
    $ persistent.photoEnd = True
    centered "{size=36}{b}ХОРОШАЯ КОНЦОВКА{/b}{/size}" with wipeleft
    jump titles
    return

label ending_photo:
    play music "Music/PopRock4v7.OGG" fadeout 1 fadein 2
    scene bg SchoolDaySakura with fade
    show lyblabla helmet with dissolve:
        xalign 0.4 yalign 0.8
    lyblabla "Так! Народ, фотографируемся на память!"
    
    show dexp laugh behind lyblabla with easeinright:
        xalign 0.6 yalign -0.2
    dexp "Так?"
    lyblabla "Дэкс! А ну не паясничай и встань нормально!"
    show lyblabla helsilent
    show dexp think with dissolve
    
    show lap joy  behind lyblabla with easeinleft:
        xalign 0.25 yalign 0.6
    lap "Сфоткаемся!"
    
    show lin laugh behind dexp with easeinright:
        xalign 0.8 yalign 1.9
    lin "Меня, меня не забудьте!"
    show lin norm
    
    show mala work behind lap with easeinleft:
        xalign 0.05 yalign 0.6
    mala "А? Что, уже фотографируемся?"
    show mala norm with dissolve
    
    show azyki norm behind lin with easeinleft:
        xalign -0.15 yalign 0.7
    lyblabla "Азуки, ты там не смотришься! Стань рядом с Лин!"
    show azyki laugh with easeinleft:
        xalign 0.9 yalign 0.7
    azyki "Океей!"
    
    show lexa attention with easeinright:
        xalign 1.3 yalign 0.7 # x 1.2
    lexa "Пожалуй, тоже сфотографируюсь!"
    lyblabla "Сядь лучше вниз вторым рядом."
    hide lexa with easeoutbottom
    show lexa norm with easeinbottom:
        xalign 0.3 yalign 24.0
    #lexa "Вот."
    
    show carry spy with easeinleft:
        xalign -0.45 yalign 0.7
    carry "Эй! Меня не забудьте!"
    hide carry with easeoutleft
    show carry sitdown with easeinleft:
        xalign 0.53 yalign 1.05
    carry "Хе-хей!"
        
    show yana norm behind mala with easeinleft:
        xalign -0.1 yalign 0.3
    yana "Всем привет!"
    
    show andry norm behind azyki with easeinright:
        xalign 1.4 yalign 0.5
    andry "А мне где лучше встать?"
    lyblabla "Да, там, рядом с Азуки."
    show andry bita with dissolve:
        xalign 1.05 yalign 0.0
    #andry "2"
    
    show jess happy with easeinright:
        xalign 0.9 yalign 1.2
    jess "Всем чмоки!"
    
    show prana neko behind yana with easeinbottom:
        xalign 0.25 yalign -0.4
    prana "А как же я?!"
    
    
    
    
    show ulilla camera with easeinleft:
        xalign -0.45 yalign 0.7
    lyblabla "Юль, сфотографируй нас пожалуйста!"
    
    ulilla "Без проблем!"
    hide ulilla with easeoutleft
    
    show ulilla joy at offscreenleft
    #ulilla "Лайби, ты только каску сними!"
    ulilla "Лайби! А ты каску снять забыла!"
    #show lyblabla helmsulk with dissolve
    lyblabla "Ой!"
    
    
    hide lyblabla
    show lyba happynorm behind lexa with dissolve:
        xalign 0.4 yalign 1.1
    
    show addSakura 
    centered ""
    
    show white at center
    play sound "sound/eelke_photo.ogg"
    hide white with dissolve
    
    
    return