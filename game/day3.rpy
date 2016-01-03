label day3:
    play music "Music/Chillout2.OGG" fadeout 1 fadein 2
    scene black with fade
    
    centered "День 3"
    
    scene bg SeaDream with fade
    
    
    show dexp dreambeach at offscreenleft
    
    dexp "Эхх! Хорошо!"
    dexp "Но жарко..."# И пожрать бы!"
    dexp "Лин! Напитки мне! Немедленно!"
    
    show lin sexytort at right with moveinright
    lin "Да, мой повелитель! Исполнено!"
    show dexpSeaAngryMouth with dissolve:
        xalign 0.111 yalign 0.497
    dexp "Эй! Я заказывал напитки, а не торт!"
    lin "Слушаюсь и повинусь, повелитель!"
    hide lin with moveoutright
    
    dexp "Да ё-моё! Совсем плохая!"
    hide dexpSeaAngryMouth with dissolve
    dexp "Лап! Принеси мне попить! Быстро!"
    show lap sexytort at right with moveinright
    lap "Да, мой господин!"
    show dexpSeaAngryMouth with dissolve:
        xalign 0.111 yalign 0.497
    dexp "Грр!!! Напитки! Слышишь, напитки!!! Не медведя!"
    
    show lap sexytort:
        xalign 0.65 yalign 1.0
    show lin sexytort:
        xalign 1.1 yalign 1.0
    with moveinright
    lap "Прости нас, хозяин! Мы сделаем всё-всё, что ты пожелаешь!"
    hide dexpSeaAngryMouth
    show dexpSeaEvil with dissolve:
        xalign 0.081 yalign 0.48
    dexp "Нуу... Раз уж ВСЁ..."
    
    #scene white with fade
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    
    scene bg DeXPRoom with squares
    show dexp maikasad at center
    dexp "Блин, как всегда, на самом интересном!"
    dexp "Ну вот что, что мне мешало досмотреть сон до конца?!?"
    
    show dexp maikasurprised at center with dissolve
    dexp "А... Это ты, наш новый [prof_str]..."
    dexp "Вот обязательно меня будить было, а?"
    show dexp maikasad at center
    dexp "Кстати, а что ТЫ делаешь у меня дома?!?"
    menu:
        "" #"Почему Дэкс сегодня проснулся не один?"
        "Ну... Мне была нужна помощь...":
            dexp "Ну раз помощь, то ладно. Своих в беде не бросаем!"
            pass
        "А что, нельзя что ли?!?":
            dexp "Хм. Да вроде можно."
            pass
        "Да так. По делам в этот район надо было.":
            dexp "Дела - это важно."
            pass
        "...":
            pass
    
    dexp "Ладно, пошли, уже действительно пора работать..."
    
    
    scene bg Residential_city with fade
    show dexp norm at right with moveinright
    dexp "Вот так вот и живём."
    show dexp laugh at center with moveinright
    dexp "Нам налево. Пройдём ещё пару кварталов и будем на месте."
    hide dexp with dissolve
    
    
    play music "Music/Metal1.OGG" fadein 1
    play sound "sound/ekokubza123_punch.ogg"
    scene bg Residential_gop with hpunch
    show Imp fight at offscreenleft
    play sound "sound/ekokubza123_punch.ogg"
    Imp "Ай!" with vpunch
    play sound "sound/ekokubza123_punch.ogg"
    Imp "Ааа!" with hpunch
    show andry bita at left with dissolve
    show dexp norm at right with dissolve
    dexp "А, Андрей, привет! Чем занимаешься?"
    show andry norm at left with dissolve
    andry "Да так... Исследую альтернативные способы заработка."
    dexp "А, ну ясно. Ладно, мы пойдём. Ты тоже не задерживайся!"
    play music "Music/ePop.OGG" fadeout 1 fadein 3
    andry "Ага, скоро подойду! Тут совсем чуть-чуть осталось!"
    show andry bita at left with dissolve
    hide andry with moveoutleft
    play sound "sound/ekokubza123_punch.ogg"
    Imp "Ай!" with vpunch
    hide dexp with moveoutright
    play sound "sound/ekokubza123_punch.ogg"
    Imp "Уй!" with hpunch
    
    
    #scene bg Hallway1 with fade
    scene bg SchoolDay with fade
    show dexp norm at center with dissolve
    dexp "Хух! Вот мы и пришли!"
    dexp "Ладно, мне идти работать надо, а ты зайди в учебную комнату, с тобой хотела поговорить Лайби."
    

    play music "Music/Metal1.OGG" fadein 1
    scene bg EmptyClass42 with fade 
    show Shtab at left with moveinleft
    show lyblabla helmbinocle at center with dissolve
    #show Binocle:
    #    xalign 0.49 yalign 0.33
    #lyblabla "Прости, я сейчас очень занята. Подойди немного позже."
    lyblabla "У нас возникли некоторые проблемы."
    lyblabla "На одном из проектов были непонятки с лицензированием, этим и воспользовалась вражеская команда!"
    lyblabla "Да что я говорю? Вот, смотри!"
    #hide Binocle
    
    play music "Music/Movie7.OGG" fadein 1
    scene bg Forest41
    show ulilla miltable:
        xalign 0.4 yalign 0.8
    show BinocularMask
    if not config.has_voice:
        play sound "sound/mattskydoodle_censor-beep.ogg"
    lyblabla "Вот! Видишь! Я же говорила!"
    show ulilla miltable2 with dissolve
    lyblabla "Место подобрано очень профессионально! Ещё недавно там находилась наша штаб-квартира."
    lyblabla "Экипировка тоже подобрана на высшем уровне. Начиная с одежды и заканчивая маскировочным стулом!"
    show ulilla miltablesad with dissolve
    if not config.has_voice:
        play sound "sound/andrutzab_Aah.ogg"
    lyblabla "Единственное, что выдаёт противника - красные туфли."
    hide BinocularMask
    hide ulilla
    
    scene bg EmptyClass42 with fade
    show Shtab at left with dissolve
    show lyblabla helmsulk at center with dissolve
    lyblabla "Ну? Теперь понимаешь всю серьёзность ситуации?"
    lyblabla "Как же вовремя мы организовали мобильную штаб-квартиру..."
    lyblabla "Что же будем делать?"

    $ attack_done = False
    jump what_mil_do
    
    #jump goodend
    return
    
    
    
label what_mil_do:
    
    show lyblabla helsilent at center 
    menu:
        "Что делать?"
        "Провести разведку!":
            show lyblabla helmet at center 
            lyblabla "Разведка уже проведена!"
            lyblabla "И нам повезло, что успели заметить противника на ранних этапах!"
            show lyblabla helmsulk at center 
            lyblabla "... да уж, если б не красные туфли - то всё могло бы быть совершенно по-другому..."
            jump what_mil_do
            pass
        "Атаковать первыми! Напасть!":
            if attack_done:
                show lyblabla helmet at center
                lyblabla "Ну атаковали уже. И что изменилось?"
                jump what_mil_do
            else:
                $ attack_done = True
                jump attack_ulilla
            pass
        "Пойти на улицу всё обдумать":
            jump think_ulilla
            pass
    return   
    
    
label attack_ulilla:
    scene bg Forest41 with fade
    show Sunshine at topright with moveintop
    show lyblabla helmsulk at right with moveinright
    show dexp norm at right with moveinright
    show lyblabla helmet at center with moveinright
    
    lyblabla "А ну выходи, подлый трус!"
    
    show lyblabla helmet at left with moveinright
    show dexp think at center with moveinright
    show andry bita at right with moveinright
    
    if not config.has_voice:
        play sound "sound/ecfike_heh.ogg"
    dexp "Кхм. Лайби, здесь никого нет."
    show andry norm at right with dissolve
    lyblabla "Что?"
    lyblabla "А, ну да, точно."
    show lyblabla helmsulk at left
    lyblabla "Ладно. Возвращаемся! Ситуацию нужно обдумать!"
    
    scene bg EmptyClass42 with fade
    show Shtab at left with dissolve
    
    jump what_mil_do
    return
    

label think_ulilla:
    scene bg ShoeLocker with fade
    show ulilla go at left with moveinleft
    
    show lyblabla helsilent at right with moveinright
    show lin sad at right with moveinright
    show lyblabla helsilent at center with moveinright
    show carry flipnorm with moveinright:
        xalign 1.4 yalign 1.1
    
    show lyblabla helmet at center
    lyblabla "Ага! Попалась!"
    show lyblabla helsilent at center
    lin "А ну иди сюда! Сейчас мы с тобой разберёмся!"
    carry "Гыыы! Ну всё теперь!"
    
    centered "{size=52}{color=#11e}{b}ROUND 1{/b}{/color}{/size}"
    play music "Music/Fast.OGG" fadein 1
    centered "{size=62}{color=#e11}{b}FIGHT!{/b}{/color}{/size}"
    
    
    $ r1AllowFirst = True
    $ r1AllowPers = True
    $ r1AllowAllPermiss = True
    $ r1AllowTogether = True
    $ r1AllowGetoff = True
    $ r1AnsCount = 0
    
    jump round1



label round1:
    menu:
        ""
        "Мы первые занялись этим проектом!" if r1AllowFirst:
            $ r1AllowFirst = False
            show lyblabla helmet at center 
            lyblabla "Эй! Ты не права! Это изначально наш проект! Мы первые им занялись!"
            show lyblabla helsilent at center
            show ulilla angry at left with dissolve
            ulilla "Да кто ж спорит? Только обновлений не было уже несколько месяцев!"
            ulilla "Что, читатели и дальше должны мучиться без продолжения?!"
            pass
            
        "Что хотим - то и делаем!" if r1AllowAllPermiss:
            $ r1AllowAllPermiss = False
            $ penalty += 1
            show carry question with dissolve
            carry "А чего мы вообще её слушаем?"
            show carry surprised with dissolve
            carry "Что хотим - то и делаем! Проект наш!"
            ulilla "Не удивительно, что с вами никто общаться даже не хочет!"
            show carry norm with dissolve
            ulilla "С таким-то подходом к делу..."
            pass
    
        "Почему б не переводить всем вместе?" if r1AllowTogether:
            $ r1AllowTogether = False
            $ penalty -= 1
            show ulilla angry with moveinright:
                xalign -0.3 yalign 1.0
            show dexp laugh at left with dissolve
            if not config.has_voice:
                play sound "sound/ecfike_chuckle-1.ogg"
            dexp "Девушки! Вы зачем ругаетесь? А почему б не переводить эту мангу вместе, а?"
            lin "Совсем с дуба рухнул!"
            lyblabla "Ни за что! Это вопрос принципа!"
    
            carry "Ну ты ваще, да!"
            ulilla "Данный вариант не уместен."
    
            show dexp think at left with dissolve
            if not config.has_voice:
                play sound "sound/ecfike__sigh-1.ogg"
            dexp "Эхх..."
            hide dexp with dissolve
    
            show ulilla norm at left with moveinleft
            pass
            
        "Вся команда была занята!" if r1AllowPers:
            $ r1AllowPers = False
            lin "У нас были проблемы с персоналом! Это же не повод перехватывать проект!"
            ulilla "А что повод, если не отсутствие перевода?"
            pass
            
        "Да забирайте вы уже этот долбаный проект!" if r1AllowGetoff:
            $ r1AllowGetoff = False
            $ penalty += 3
            lin "Да забирайте уже этот проект!"
            lin "У нас и так работы валом..."
            hide lyblabla
            show lyba angry at center with dissolve
            lyba "Совсем сдурела?"
            lyba "Проект не отдадим!"
            hide lyba
            show lyblabla normal at center with dissolve
            lyblabla "И вообще. Мы начинали проект не для того, чтобы его потом бросить..."
            show lyblabla sulk at center with dissolve
            lyblabla "Да и мне лично он очень нравится..."
            show lyblabla helsilent at center
            pass
            
    $ r1AnsCount += 1
    if r1AnsCount >= 3:
        jump r1after
    else:
        jump round1


label r1after:
    show lyblabla helmet at center 
    lyblabla "В общем, сейчас мы исчерпали свои аргументы. Но учти, в следующий раз так просто не отделаешься!"
    
    hide carry
    hide lin
    hide lyblabla 
    with moveoutright
    
    hide ulilla with moveoutleft
    
    
    
    
    play music "Music/ePop.OGG" fadein 1
    scene bg EmptyClass42 with fade 
    show Shtab at left
    show lyblabla helmet at center with dissolve
    show lin sad at left with dissolve
    
    lyblabla "Вот такие пироги..."
    lyblabla "Нужно что-нибудь придумать! Иначе так и не вернём себе проект..."
    show lyblabla helsilent at center
    
    show azyki laugh at right with dissolve
    if not config.has_voice:
        play sound "sound/madamvicious_giggling-cutely.ogg"
    azyki "Кушать подано. Идите жрать, пожалуйста!"
    
    show lin norm at left with dissolve
    lin "О! Время обеда! Пойдёмте скорее кушать!"
    
    hide azyki
    hide lyblabla
    hide lin 
    with moveoutright
    
    scene black #with fade
    centered "Но ни в обед и ни в ужин ничего нового придумать так и не удалось..." with dissolve
    centered "Так прошёл ещё один день." with dissolve
    
    jump day4
    return
