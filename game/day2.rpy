label day2:
    scene black with fade
    
    centered "День 2"
    
    #centered "Первый день был непростым, но..."
    #centered "Работа начинается именно сегодня!"
    centered "В бой!" 
    #play music "Music/Reju_-_The_Source_Of_The_Rejuvenescence.ogg" fadeout 1
    #play music "Music/PopRock2.OGG" fadeout 1 fadein 3
    play music "Music/ePop.OGG" fadeout 1 fadein 3

    
    scene bg TeachersRoom with fade
    show dexp norm at center 
    dexp "(зевает) Увааах!"
    dexp "Доброе утро!"
    show dexp laugh
    dexp "Неплохо вчера погуляли, да?"
    show dexp norm
    
    if met == "malya":
        show mala work with dissolve:
            xalign 0.15 yalign 1.0
        mala "Привет, Дэкс!"
        mala "Я за вчера перевела главу, но там есть кое-какие вопросы... Не поможешь?"
    if met == "azyki":
        show azyki norm with dissolve:
            xalign 0.15 yalign 1.0
        azyki "Привет, Дэкс!"
        show azyki angry with dissolve:
            xalign 0.2 yalign 1.0
        azyki "Скоро уже перевод там доделаешь? Уже нужно!"
    if met == "lyba":
        show yana norm with dissolve:
            xalign 0.2 yalign 0.8
        yana "Привет, Дэкс!"
        yana "Тут по твоему переводу несколько вопросов. Ты сейчас занят?"
    
    show carry normflip with dissolve:
        xalign 0.85 yalign 1.0
    carry "О! А чего это вы тут собрались? Гы!"
    
    dexp "Так, не мешайте! Дайте с человеком договорить!"
    if met == "malya":
        hide mala with dissolve
    if met == "azyki":
        hide azyki with dissolve
    if met == "lyba":
        hide yana with dissolve
    hide carry with dissolve
    dexp "Вот вечно так: если навалятся проблемы - то все сразу..."
    dexp "Ах да. Тебя хотела видеть Лайби. Подойди к ней, пожалуйста."
    
    menu:
        "Где искать Лайби?"
        "На крыше":
            #dexp "Нету её там с утра!"
            scene bg Roof with fade
        "В столовой":
            scene bg Dinning1 with fade
            pass
        "В учебном классе":
            scene bg EmptyClass42 with fade
            pass
        "В коридоре":
            scene bg Hallway1 with fade
            pass
            
    show lyblabla normal at center with dissolve
    lyblabla "Тебе повезло, я уже собиралась уходить."
    lyblabla "Так, стажёр, ты ведь у нас [prof_str]."
    lyblabla "Отлично! На новый проект как раз тебя и не хватало!"
    show lyblabla sulk
    lyblabla "Конечно, к проекту уже приписан [prof_str], но он очень перегружен."
    lyblabla "Так что если сможешь взять на себя часть работы, то сможем делать релизы чаще."
    
    show lyblabla normal 
    lyblabla "В общем, начинай работать. Если что-нибудь будет непонятно - спрашивай у кого-нибудь из команды."
    
    play music "Music/eDance1.OGG" fadein 3
    #scene bg Schoolyard with fade
    scene bg SchoolDaySakura with fade
    show drakoha norm with dissolve
    drakoha "Привет! Ты тоже недавно в команде?"
    drakoha "Ну и как оно? Здесь классно!"
    drakoha "Я - Дракоша, новый тайпер. В команде я совсем недавно."
    drakoha "Ой, забыла. Мне срочно нужно за хлебом!"
    drakoha "Ну, ещё поговорим. Пока-пока!"
    hide drakoha with dissolve
    "" "И что это только что было? ..."
    
    scene bg Classroom44 with fade
    show dexp joybig with moveinleft
    dexp "А мы уже сегодня виделись!"
    menu:
        ""
        "Помочь Дэксу с Лап":
            $ lap_points += 2
            show dexp thinkbig
            dexp "А? Что? Лап? Да, она мне давно нравится."
            dexp "Но я всё никак не могу добиться взаимности..."
            
            scene bg ChurchDream with zoomout
            show lap bride at center with dissolve
            show dexp norm at left with dissolve            
            "" "... Объявляю вас мужем и женой! Жених, можете поцеловать невесту!"
            hide lap
            hide dexp
            with moveoutright
            play sound "sound/gflower__perfect-kiss.ogg"
            
            scene bg Classroom44 with squares
            show dexp thinkbig at center with dissolve
            dexp "Эхх... Вот бы это когда-нибудь сбылось!"
            pass
        "Пойти дальше":
            pass
    
    #"" "Мда. Пойду ка я дальше..."
    
    scene bg Classroom49 with fade
    show lin normbig at center with dissolve
    lin "Привет!"
    
    menu:
        ""
        "Помочь Лин с Лап":
            show lin laughbig
            lin "А? Что? Лап? Да, она мне давно нравится."
            lin "Но я всё никак не могу добиться взаимности..."
            
            scene bg ChurchDream with zoomout
            show lin bride at center with dissolve
            show lap norm at left with dissolve            
            "" "... Объявляю вас мужем и женой! Жених, можете поцеловать невесту!"
            hide lin
            hide lap
            with moveoutright
            play sound "sound/gflower__perfect-kiss.ogg"
            
            scene bg Classroom49 with squares
            show lin normbig at center with dissolve
            lin "Эхх, мечты-мечты..."
            pass
        "Пойти дальше":
            pass
            
    scene bg Shop with fade
    show lap norm at center  with dissolve
    lap "Ох, какие люди!"
    lap "Голова после вчерашнего не болит? Классно оторвались!"
    
    menu:
        ""
        "Помочь Лап с Лёхой":
            show lap joy at center
            lap "Лёша? Да, настолько яркие чувства я испытываю впервые!"
            lap "Но, кажется, его не очень интересуют девушки..."
            
            scene bg ChurchDream with zoomout
            show lexa bride at center with dissolve
            show lap norm at left with dissolve  
            if not config.has_voice:
                play sound "sound/mattskydoodle_censor-beep.ogg"
            lexa "Сволочи!"
            lexa "Куда вы меня тащите?!"
            lexa "Отпустите меня!!!"
            "" "... Объявляю вас мужем и женой! Жених, можете поцеловать невесту!"
            hide lexa
            hide lap
            with moveoutright
            play sound "sound/gflower__perfect-kiss.ogg"
            
            scene bg Shop with squares
            show lap bigquestion at center  with dissolve
            lap "Но захочет ли он..."
            pass
        "Пойти дальше":
            pass
    
    play music "Music/Fast.OGG" fadein 3
    scene bg Office with fade
    
    if text_team:
        show dexp norm with dissolve:
            xalign 0.1 yalign 1.0
        show mala angry at center with dissolve
        mala "А я тебе говорю, что не так оно переводится!"
        dexp "Всё так, я 3 раза проверил."
        show carry norm with moveinright:
            xalign 1.4 yalign 0.8
        show lexa attention at right with moveinright
        lexa "Дэкс, проверь-ка свой перевод ещё раз!"
        lexa "Только теперь бери тексты не непонятно откуда, а из официального источника!"
        show dexp angry with dissolve
        dexp "Да надёжный там источник!"
        dexp "Я оттуда всегда тексты беру!"
        dexp "И раньше всегда прокатывало!"
        mala "Да ё-моё! Дэкс, не прав ты!"
        show lexa norm with dissolve
        lexa "О! А вот и наш новенький член команды!"
        lexa "Нам нужна помощь в разрешении данного конфликта. Поможешь?"
        menu:
            "Кто прав?"
            "Прав Дэкс.":
                pass
            "Права Маля.":
                pass
            "Прав Лёха.":
                pass
            "Все по-своему правы.":
                pass
        dexp "Ага, нашёл кого спрашивать, новичка!"
        show dexp norm with dissolve
        dexp "Ты б лучше сам головой подумал, что нам с этим текстом делать..."
        show prana norm with moveinleft:
            xalign -0.2 yalign 0.8
        prana "Ну и чего вы тут ругаетесь?"
        play music "Music/PopRock2.OGG" fadein 3
        prana "Всё просто же!"
        prana "Да, Дэкс допустил некоторую неточность в переводе."
        prana "Но и остальные тоже не правы!"
        prana "Маля, ты вообще предложение не заметила."
        prana "Лёша, а ты правда не знал, что Дэкс собирает тексты из многих источников?"
        prana "Предлагаю выбрать нечто среднее, и более литературный вариант!"
        show dexp laugh with dissolve
        dexp "Спасибо тебе, Пряня!"
        show mala norm with dissolve
        mala "Ого! Так вот оно как. Спасибо!"
        show prana neko with dissolve
        prana "Не за что!"
        prana "На этом рабочее совещание можно считать законченным?"
        
    if pic_team:
        show dexp norm with dissolve:
            xalign 0.1 yalign 1.0
        show azyki angry at center with dissolve
        azyki "Дэкс! Что ты там вчера насканировал? А нормально сделать не мог?"
        dexp "Да всё я нормально сделал."
        show carry norm with moveinright:
            xalign 1.4 yalign 0.8
        show lexa attention at right with moveinright
        lexa "Проверь ка настройки сканирования ещё раз!"
        show dexp angry with dissolve
        dexp "Да все настройки правильные!"
        dexp "Всегда так делал, и никаких проблем не было!"
        azyki "Дэкс, не прав ты!"
        show lexa norm with dissolve
        lexa "О! А вот и наш новенький член команды!"
        lexa "Нам нужна помощь в разрешении данного конфликта. Поможешь?"
        menu:
            "Кто прав?"
            "Прав Дэкс.":
                pass
            "Права Азуки.":
                pass
            "Прав Лёха.":
                pass
            "Все по-своему правы.":
                pass
        dexp "Ага, нашёл кого спрашивать, новичка!"
        show dexp norm with dissolve
        dexp "Ты б лучше сам головой подумал, что нам с этими сканами делать..."
    
    
    
    scene black with fade
    centered "Вот и прошёл ещё один день..."
    centered "Но много ли было сделано?"
    centered "Но ведь ещё не вечер!"
    centered "Хотя нет, как раз таки вечер..." with dissolve
    
    play music "Music/eDance1.OGG" fadein 3
    scene bg SchoolyardNight with fade
    show dexp norm at center with dissolve
    show andry norm at right with dissolve
    show lexa norm at left with dissolve
    
    dexp "Пацаны!"
    show dexp laugh
    dexp "Говорят, что Лап спит в миленькой ночнушке!"
    dexp "Пошли подглядывать!"
    
    scene bg HomeDoorNight with fade
    show andry shy at right 
    show dexp think at center 
    show lexa norm at left
    with moveinleft
    lexa "Что-то я очкую!"
    andry "Ага, боязно как-то... Может, ну его нафиг?"
    show dexp norm with dissolve
    dexp "Да не бойтесь! Я сто раз так делал!"
    andry "Ну... раз ты так говоришь... Ладно!"
    hide andry
    hide dexp
    hide lexa
    with moveoutright
    
    play music "Music/Dubstep1.OGG" fadeout 1 fadein 2
    scene bg HomeCorridor with fade
    show lap sleepy at center with dissolve
    lap "(зевает) Увааах!"
    lap "А вы не подскажете, как пройти в библиотеку?"
    show dexp norm at offscreenleft
    
    dexp "Прямо по коридору, затем направо."
    lap "Спасибо."
    hide lap with moveoutright
    show dexp laugh
    dexp "И смыть не забудь!"
    
    show dexp nya at right with dissolve
    show lap angry with moveinright
    play music "Music/Fast.OGG" fadein 1
    lap "Эй! А вы здесь что забыли!"
    show dexp think
    lap "А ну пошли вооон!"
    lap "А то сейчас Лайби вызову!!!"
    dexp "Пацаны! Нас поймали! Сваливаем!"
    hide dexp with moveoutright
    hide lap with moveoutright
    play sound "sound/ekokubza123_punch.ogg"
    show dexp fearbig at offscreenright with vpunch
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Уй!" with hpunch
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Ай!" with vpunch
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Лап! Мы честно-честно больше так не будем!"  with hpunch
    
    scene black with fade
    centered "И долго ещё крики боли и страха доносились в ночи..."
    centered "Но это уже совсем другая история!"
    
    
        
    #play music "Music/EuroDance2.OGG" fadeout 1 fadein 2
    jump day3            
    return
