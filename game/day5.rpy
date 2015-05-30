label day5:
    scene black with fade
    centered "День 5" with dissolve
    
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    scene bg EmptyClass42 with fade 
    
    show dexp maikasad at center with dissolve
    dexp "Уааах! Доброе всем утро!"
    
    show mala work at left with moveinleft
    mala "Доброе! Что, спишь ещё? А я уже 10 страниц перевела!"
    dexp "Ага, молодец. Ну что, пойдём воевать?"
    
    show mala norm with dissolve
    mala "Да? А Лёша где?"
    
    show lexa norm at right with moveinright
    lexa "Тут я тут. Ну что, пошли?"
    
    show dexp think with dissolve 
    dexp "Ага, пойдём. А я на ходу обдумаю стратегию!"
    
    show mala angry with dissolve
    mala "Ухх! Ну я им всем покажу!!!"
    hide mala with moveoutleft
    play sound "sound/thefsoundman_punch-02.ogg"
    show mala norm at offscreenleft with hpunch
    
    dexp "Эмм... Мальвин, а ты куда пошла? Там окно..."
    show mala norm at left with moveinleft
    mala "А, ну да. Перепутала, с кем не бывает?"
    
    hide lexa
    hide dexp
    hide mala 
    with moveoutright
    
    
    scene bg Hallway1 with slideleft
    show mala norm:
        xalign -0.35 yalign 0.7
    show dexp think behind mala:
        xalign 0.15 yalign 0.7
    show lexa norm behind dexp:
        xalign 0.63 yalign 0.7
    with moveinleft
    
    lexa "Дэкс, ну что, придумал стратегию?"
    show dexp laugh with dissolve
    dexp "Ага! Там, короче, расставляешь свои войска по всему монитору."
    dexp "Кликаешь мышью, а потом пиу-пиу! Круто, да?"
    show lexa attention with dissolve
    lexa "Кхм.."
    show mala angry with dissolve:
        xalign -0.25 yalign 0.7
    mala "Дэкс! Нам нужна стратегия борьбы с вражеской командой, а не идея для очередной игрушки!!!"
    show lexa norm with dissolve
    show dexp norm with dissolve
    play music "Music/Chillout6v7.OGG" fadein 1
    #dexp "Так это что, получается что я всё это время не над тем думал?"
    dexp "Так это,  получается, я всё время не над тем думал?"
    
    show dexp fearbig at center with dissolve
    dexp "Уаа!! Хны-хны!"
    hide dexp with easeoutright
    mala "Куда?!? Стоять!!!"
    hide mala
    hide lexa
    with dissolve
    
    
    
    play music "Music/EuroDance2.OGG" fadein 1
    scene black with fade
    centered "В это же время"
    scene bg Park2 with dissolve
    show parkTrio st1 at center with dissolve
    show lyba happy at offscreenright
    show lin norm at offscreenright
    show lap joy at offscreenleft
    lyba "А потом представляете, выхожу я такая, а там..."
    show Seagul at topleft with moveinleft
    show Seagul with moveinleft:
        xalign 0.5 yalign -0.1
    show Seagul with moveinleft:
        xalign 0.9 yalign -0.02
    show Seagul with moveinleft:
        xalign 0.93 yalign 0.0
    show Sweat behind Seagul with dissolve:
        xalign 0.84 yalign 0.12
    hide Sweat with moveoutbottom
    hide Seagul with moveoutright
    if not persistent.seeSeagul:
        $ achId = "seeSeagul"
        $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
        $ achText = __("\"Посмотреть на птичку\"")
        call showAchiv
    $ persistent.seeSeagul = True
    #lyba "Там такое, что просто не передать словами!"
    play sound "sound/madamvicious_oh.ogg"
    lyba "Ой! Птичка пролетела... Чуть не попала, зараза!"
    show parkTrio st2 at center with dissolve
    lin "Ага, бывает..."
    lap "Как же всё-таки замечательно, что мы сегодня выбрались на природу!"
    lin "Это точно! А то всё работа, работа... Отдыхать тоже нужно!"
    show parkTrio st1 at center with dissolve
    lyba "Правильный отдых очень важен для продуктивной работы!"
    show parkTrio st2 at center with dissolve
    lap "Ну и отлично!"
    lap "Лин, подай мне, пожалуйста, чипсы!"
    
    menu:
        ""
        "Много есть - вредно для фигуры!":
            pass
        "Самой мало!":
            pass
        "Так чипсы... закончились!":
            pass
    show parkTrio st3 at center with dissolve
    show lin sad at offscreenright
    #lin "Есть много чипсов - вредно для фигуры!"
    show lin norm at offscreenright
    show lap fight at offscreenleft
    lap "Ты меня не беси... Нарываешься?"
    show parkTrio st2 at center with dissolve
    lin "А, нет, ничего. Только не злись!"
    show parkTrio st1 at center with dissolve
    lyba "Зачем ругаетесь? Давайте лучше отдыхать!"
    
    show SeagulStatic at topleft with moveinleft
    lyba "О! На второй круг пошла!"
    show SeagulStatic with moveinleft:
        xalign 0.05 yalign 0.05
    show parkTrio st4 at center with dissolve
    show lyba angryflip at right with dissolve
    show lin angry at center with dissolve
    show lap fight with dissolve:
        xalign 0.0 yalign 0.8
    show SeagulShock with dissolve:
        xalign 0.05 yalign 0.05
    hide SeagulStatic
    lap "Держи его!"
    show SeagulShockFlip with dissolve:
        xalign 0.05 yalign 0.05
    hide SeagulShock
    #lap "123"
    hide SeagulShockFlip with moveoutleft
    hide lap with moveoutleft
    hide lin with moveoutleft
    hide lyba with moveoutleft
    play sound "sound/ekokubza123_punch.ogg"
    show lin norm at offscreenleft with hpunch
    
    
    
    
    
    scene black with fade
    centered "А пока девушки отдыхают..."
    play music "Music/Chillout6v7.OGG" fadein 1
    centered "Давайте вернёмся к нашему \"спецназу\"..." with dissolve
    scene bg SchoolDay with fade
    show dexp norm with dissolve:
        xalign 0.4 yalign 0.7
    dexp "Да уж, подвёл я команду..."
    show dexp think with dissolve
    dexp "И остаётся мне лишь тихо уйти..."
    dexp "Уйти из этой жизни!"
    dexp "Но если я уйду, то кем же я буду?"
    
    menu:
        ""
        "Пойти работать продавцом мороженого":
            show yana angry at right with moveinright
            yana "Чтоб мороженое продавать, надо его где-то брать."
            yana "А у тебя денег нет!"
            show yana norm with dissolve
            yana "Так что не выдумывай.."
            hide yana with moveoutright
            pass
        "Паять электронные схемы":
            show andry fight at left with moveinleft
            andry "Совсем офигел?"
            andry "Мне конкуренты не нужны!"
            hide andry with moveoutleft
        "Сделаться ремонтником компьютеров":
            show lexa attention at left with moveinleft
            lexa "А ты в курcе, что на хорошего компьютерщика надо минимум 5 лет учиться?"
            lexa "Да и есть уже в этом районе компьютерщик..."
            hide lexa with moveoutleft
            pass
        "Профессионально работать фотографом":
            #show BranchTopLeft at topleft with dissolve
            #show jess phototop behind BranchTopLeft at topleft with moveintop
            show jess funnycard with moveinleft:
                xalign -0.2 yalign 1.0
            jess "Угу! Умнее ничего не придумал?"
            jess "Фотографировать тоже уметь надо!"
            #hide jess with moveouttop
            #hide BranchTopLeft with dissolve
            hide jess with moveoutleft
            pass
    
    play music "Music/PopRock2.OGG" fadein 1
    show mala angry:
        xalign 0.8 yalign 0.7
    show lexa norm:
        xalign 1.1 yalign 0.7
    with moveinright
    mala "Совсем больной, да?"
    lexa "Дэкс, я считаю, что ты не прав!"
    mala "Кто ж команду в такой ответственный момент бросает?!"
    show dexp norm with dissolve
    
    show ulilla go with moveinleft:
        xalign -0.1 yalign 0.7
    show ulilla angry with dissolve
    ulilla "Не могли бы вы так не орать? Отвлекаете..."
    
    
    centered "{size=52}{color=#11e}{b}ROUND 2{/b}{/color}{/size}"
    play music "Music/Fast.OGG" fadein 1
    centered "{size=62}{color=#e11}{b}FIGHT!{/b}{/color}{/size}"
    
    $ r2AllowNoAgression = True
    $ r2AllowAlien = True
    $ r2AllowGetoff = True
    $ r2AnsCount = 0
    
    jump round2
    
    
label round2:
    menu:
        ""
        "Нельзя захватывать чужой проект!" if r2AllowAlien:
            $ r2AllowAlien = False
            mala "Ага! Это ты, ты виновата!"
            ulilla "В чём это я виновата?"
            mala "В том, что захватили проект, предварительно не убедившись, что над ним уже кто-то работает!"
            show ulilla norm with dissolve
            ulilla "Признаю свою оплошность."
            show mala norm with dissolve:
                xalign 0.7 yalign 0.7
            pass
        "Нет агрессии!" if r2AllowNoAgression:
            $ r2AllowNoAgression = False
            show lexa attention with dissolve:
                xalign 1.05 yalign 0.7    
            lexa "А ещё сразу заняли агрессивную позицию!"
            show ulilla angry with dissolve
            play sound "sound/mattskydoodle_censor-beep.ogg"
            ulilla "Это кто здесь ещё агрессивный?!?"
            show ulilla norm with dissolve
            ulilla "А, ну да, я..."
            show lexa norm with dissolve:
                xalign 1.0 yalign 0.7
            pass
        "Забирайте проект и делайте его сами!" if r2AllowGetoff:
            $ r2AllowGetoff = False
            $ penalty += 3
            show carry fear with moveinright:
                xalign 1.4 yalign 1.0
            carry "Да заберите этот проект уже к чертям собачьим!"
            carry "Нам и других проектов хватает!!!"
            show mala angry with dissolve
            mala "Кэрри, совсем сдурела?!"
            mala "Такие вещи без разрешения Лайби не делаются!"
            show mala norm with dissolve
            hide carry with moveoutright
            ulilla "Да определитесь вы уже наконец."
    
    $ r2AnsCount += 1
    if r2AnsCount >= 2:
        jump r2after
    else:
        jump round2
        

label r2after:
    show azyki laugh with moveinright:
        xalign 1.3 yalign 0.7
    azyki "Народ! Обедать пора!"
    show azyki surprized with dissolve
    play sound "sound/madamvicious_oh.ogg"
    azyki "Ой..."
    
    ulilla "Эх, а мне далеко идти кушать..."
    show azyki norm with dissolve
    play sound "sound/madamvicious_giggling-cutely.ogg"
    azyki "Да разве ж это проблема? Пойдём поедим с нами!"
    ulilla "А точно можно?"
    show dexp think with dissolve
    dexp "Думаю, проблем не возникнет."
    show ulilla joy with dissolve
    ulilla "Ну, тогда пойдём?"
    
    hide azyki
    hide lexa
    hide mala
    hide dexp
    hide ulilla 
    with moveoutright
    
    
    play music "Music/ePop.OGG" fadein 1
    scene bg Dinning1 with fade
    show dexp norm:
        xalign 0.1 yalign 1.0
    show azyki laugh:
        xalign 0.5 yalign 1.0
    with dissolve
    show ulilla joy with moveinleft:
        xalign -0.37 yalign 1.0
    ulilla "А у вас мило!"
    azyki "Ага, стараемся!"
    show dexp laugh with dissolve 
    dexp "Да ты присаживайся. Сейчас будем есть!"
    
    play music "Music/Movie7.OGG" fadein 1
    show lyblabla helmet behind ulilla with dissolve:
        xalign -0.1 yalign 1.0
    show dexp laugh with moveinleft:
        xalign 0.7
    lyblabla "Это что ж это творится-то, а?"
    show ulilla norm with dissolve
    lyblabla "Вы в нашу святая-святых агента вражеского привели?!"
    show dexp norm with dissolve
    lyblabla "Юлилла, вот и что ты тут делаешь?"
    show azyki surprized with dissolve
    
    ulilla "Ем."
    show lyblabla normal with dissolve
    play music "Music/PopRock2.OGG" fadein 1
    lyblabla "А, ну еда - это святое."
    show azyki laugh with dissolve
    lyblabla "Я с вами!"
    show lyblabla silent with dissolve
    
    
    show dexp laugh behind ulilla with moveinright:
        xalign 0.05
    azyki "Ну и отлично! Я на всех приготовила!"   
    show azyki laugh with moveinright:
        xalign 0.73
    show mala norm with dissolve:
        xalign 0.37 yalign 1.0
    mala "А может, отпразднуем за знакомство?"    
    
    show lexa norm behind azyki with dissolve:
        xalign 0.55
    lexa "О! Еда! Пора б и перекусить!"
    
    show ulilla joy with dissolve
    dexp "Ну что, не жалеешь, что пошла с нами?"
    ulilla "Не жалею. У вас весело!"
    
    show lyblabla helmet with dissolve
    lyblabla "Кому там сильно весело? Сейчас всех работать заставлю!"
    
    hide lyblabla
    #play sound "sound/freesound_Laughs.ogg"
    show lyba happy with dissolve:
        xalign -0.1 yalign 1.9
    show BentoBox with dissolve:
        xalign 0.25 yalign 0.9
    centered ""
    #hide BentoBox
    
    show white at center
    play sound "sound/eelke_photo.ogg"
    hide white with dissolve
    
    
    play music "Music/ePop.OGG" fadein 1    
    scene black with fade 
    centered "А тем временем происходит что-то непонятное!" with dissolve
    
    scene bg HallwayClean with fade
    show suomi getin with dissolve:
        xalign 0.31 yalign 0.99
    suomi "Ура! Открытое окно!"
    suomi "Сегодня я наконец-то сюда заберусь!"
    
    menu:
        "Кого послать разобраться с незнакомцем?"
        "Послать Андрея":
            show andry shy at right with dissolve
            andry "Ты кто такая?"
            show suomi norm with dissolve
            suomi "Ну... Я..."
            show andry bita with dissolve
            andry "Ах так да? Ну теперь держись!"
            show suomi sirprised with dissolve
            suomi "Ты всё не так понял!"
            show andry norm with dissolve
            andry "Да? И что же?"
            show suomi norm with dissolve
            suomi "Я фанатка вашей команды!"
            suomi "И очень-очень люблю ваши переводы! Вы классные!"
            show andry shy with dissolve
            andry "Спасибо! Очень приятно!"
            show andry fightflip with dissolve
            andry "Но шла бы ты лучше подобру-поздорову!"
            show suomi sirprised with dissolve
            suomi "Почему?"
            andry "Ходят тут всякие, а потом вещи пропадают..."
            show andry bita with dissolve
            show suomi getout at center with dissolve
            suomi "Ну я пойду."
            show andry fightflip with dissolve
            show suomi smallrun with dissolve:
                xalign 0.4 yalign 0.42
            andry "И не смей возвращаться!"
            hide suomi with dissolve
            show andry norm with dissolve
            andry "Посторонние на производстве - нарушение техники безопасности!"
            show andry shy with dissolve
            andry "А технику безопасности надо соблюдать!"        
            pass
        "Послать Янушку":
            show yana norm at right with dissolve
            show yana angry with dissolve
            yana "Это что ещё такое!?"
            yana "Ты кто такая? А ну залазь внутрь!"
    
            show suomi norm with dissolve
            suomi "Я фанатка вашей команды!"
            suomi "И очень-очень люблю ваши переводы! Вы классные!"
            show yana norm with dissolve
            yana "Спасибо! Очень приятно!"
            show yana angry with dissolve
            yana "Но это не повод вламываться к нам на учебную базу!"
            show suomi sirprised with dissolve
            suomi "А что, можно было как-то иначе?"
            show yana norm with dissolve
            yana "Конечно, можно!"
            yana "Например, подать заявку, заполнить все формы, дождаться ответа..."
            show suomi norm with dissolve
            suomi "Вот видишь! Почти нереально!"
            suomi "А так хоть на кого-то вблизи посмотрела!"
            show suomi sirprised with dissolve
            suomi "Можно я буду иногда заходить?"
            show yana angry with dissolve
            yana "Нет! Не смей этого делать!"
            suomi "Ладно, ладно..."
            show suomi getout at center with dissolve
            show yana norm with dissolve
            suomi "Ну я пойду."
            show suomi smallrun with dissolve:
                xalign 0.4 yalign 0.42
            yana "Да уж... Случится же такое!"
            hide suomi with dissolve
            yana "Всякие экскурсии - это, конечно, хорошо..."
            show yana angry with dissolve
            yana "Но если только и делать, что экскурсии, то когда работать?"
            pass   
    
    
    scene black with fade 
    #centered "Так и прошёл тот обед" with dissolve
    centered "Вернёмся обратно в столовую." with dissolve
    centered "Обед подходит к концу и плавно перетекает в ужин." with dissolve
    centered "Кто знает, может быть уже зародилась..." with fade
    centered "... дружба?" with dissolve
    #hide black with dissolve
    
    
    scene bg Dinning1 with fade
    show dexp laugh:
        xalign -0.25 yalign 1.0
    show ulilla joy:
        xalign -0.4 yalign 1.0
    show azyki laugh:
        xalign 0.33 yalign 1.0
    show mala norm:
        xalign 0.73 yalign 1.0
    show lexa norm behind azyki:
        xalign 0.55 yalign 1.0
    show lyblabla helsilent:
        xalign 0.1 yalign 1.0
    
    
    ulilla "Спасибо большое. Было очень вкусно!"
    #hide lyba
    hide lyblabla
    #show lyblabla helmet at center with dissolve
    play music "Music/Fast.OGG" fadein 1
    show lyba angry with dissolve:
        xalign 0.1 yalign 1.0
    lyba "Куда?! Не разобрались ещё!"
    
    centered "{size=52}{b}{color=#11e}ROUND {/color}{color=#e11}3{/color}{/b}{/size}"
    show dexp think with dissolve:
        xalign -0.17
    play music "Music/PopRock2.OGG" fadein 1
    dexp "Может, всё-таки попробуем работать вместе?"
    hide lyba
    show lyblabla helsilent with dissolve:
        xalign 0.1 yalign 1.0
    show ulilla norm with dissolve
    ulilla "Ну..."
    show dexp norm with dissolve
    ulilla "Наверное, можно..."
    mala "Да, Лайби, а почему б и нет?"
    show lyblabla helmet with dissolve
    lyblabla "А как же командные принципы?"
    show lyblabla helsilent
    dexp "Какие принципы, когда читатели уже давным-давно ждут продолжения?"
    menu:
        ""
        "Нет! Мы будем бороться до конца!":
            $ penalty += 3
            show lyblabla helmsulk
            lyblabla "Нет, значит нет."
            lyblabla "Проект наш и точка."
        "Сотрудничество - это хорошо":
            show lyblabla helmsulk
            lyblabla "Эхх... Может, вы и правы. Почему б не попробовать?"
    
    
    show black with fade 
    centered "И всё-таки день закончился явно не безрезультатно!" with dissolve
    centered "Неужели команда наконец перестанет заниматься внутренними распрями и начнёт непосредственно переводить?" with dissolve
    
    
    #call ending_photo
    #jump goodend
    #jump photoend
    jump day6
