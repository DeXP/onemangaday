label day6:
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2
    scene black with fade
    centered "День 6" with dissolve
    centered "Выходной"
    
    play music "Music/ePop.OGG" fadeout 1 fadein 2
    scene bg Storage with fade
    show andry chem at center with dissolve
    
    show lap norm at right with moveinright
    lap "Привет, Андрей! Что опять химичишь?"
    
    show andry norm with dissolve
    
    show C4 with dissolve:
        xalign 0.3 yalign 0.5
    andry "Да вот, всё изучаю альтернативные способы заработка."
    
    show lap surprized with dissolve
    lap "Ого!"
    lap "А что это за гвоздь в центре?"
    
    show andry shy with dissolve
    andry "О! Это моя новейшая разработка!"
    andry "Таймер обратного отсчёта, работающий на абсолютно новых принципах!"
    andry "Надо вынести устройство на солнце и тень от гвоздя будет показывать точное время!"
    
    show lap norm at left
    lap "Ух ты! Классно!"
    show lap joy with dissolve
    lap "А что это за кнопочка!"
    play sound "sound/ecfike_computer-error.ogg"
    show andry fight with dissolve
    play music "Music/Metal1.OGG" fadein 1
    andry "Ложись! Сейчас всё взорвётся!"
    show lap surprized  with dissolve
    
    show andry liedown with dissolve:
        xalign 0.5 yalign -0.4
    show lap liedown with dissolve:
        xalign 0 yalign -0.9
    
    play sound "sound/daatg_tusss.ogg"
    centered "{b}{color=#060}3{/color}{/b}"
    play sound "sound/daatg_tusss.ogg"
    centered "{b}{size=44}{color=#006}2{/color}{/size}{/b}"
    play sound "sound/daatg_tusss.ogg"
    centered "{b}{size=64}{color=#600}1{/color}{/size}{/b}"
    play sound "sound/daatg_tusss.ogg"
    centered "{b}{size=84}{color=#f00}0{/color}{/size}{/b}"
    show black
    hide black with dissolve
    play sound "sound/daatg_tusss.ogg"
    centered "{b}{size=44}{color=#006}-1{/color}{/size}{/b}"
    play sound "sound/daatg_tusss.ogg"
    centered "{b}{size=44}{color=#006}-2{/color}{/size}{/b}"
    
    show andry norm with dissolve
    andry "Кхм. Я ещё не до конца отладил таймер, он периодически сбоит..."
    andry "Ну... Я пойду?"
    hide andry with moveoutleft
    show lap angry at left with dissolve
    $ lap_kind = False
    menu:
        ""
        "Пойти побить Андрея":
            lap "Сбоит, да? А ну иди сюда!"
            pass
        "Пойти сильно побить Андрея":
            lap "Сбоит, да? Ух, я тебе сейчас уши-то надеру!"
            pass
        "Пойти ОЧЕНЬ сильно побить Андрея!":
            lap "Проверять технику перед использованием надо!"
            lap "Иди сюда, Андрейка, иди сюда!"
            lap "Ух, я тебе сейчас накостыляю!"
            $ penalty += 1
            pass
        "Простить Андрея":
            $ penalty -= 1
            lap "Ах так, да?"
            show lap norm with dissolve
            lap "Ай, ладно. Сегодня живи."
            $lap_kind = True
            pass
    hide C4
    
    if lap_kind == False:
        hide lap with moveoutleft
        show Imp fight at offscreenleft
        play sound "sound/ekokubza123_punch.ogg"
        Imp "Ай!" with vpunch
    else:
        hide lap with moveoutright
    
    
    
    play music "Music/ePop.OGG" fadeout 1 fadein 2
    scene bg EmptyClass42 with fade 
    show yana norm at left
    show dexp maikasad at center with dissolve
    dexp "Уааах. Доброе утро!"
    show dexp maikasad at right with moveinright
    show lyba bath with dissolve
    lyba "О! А что это вы тут делаете?"
    yana "Как это что? Работаем!"
    lyba "Так сегодня ж шестой день, выходной!"
    dexp "Ой. А я и забыл!"
    dexp "Лайби, а ты сама что здесь делаешь?"
    hide lyba
    show lyblabla normal with dissolve
    lyblabla "Как что? Охраняю мобильную штаб-квартиру, конечно же!"
    show lyblabla silent
    dexp "А почему именно ты?"
    show lyblabla normal
    lyblabla "А чтоб никто не догадался!"
    show lyblabla silent
    yana "Мы тогда пойдём!"
    show lyblabla normal
    lyblabla "Идите. Но никому ни слова о новом расположении штаб-квартиры!"
    show lyblabla silent
    
    show black with dissolve
    hide lyblabla
    hide dexp
    hide yana
    show lyba eating at center
    hide black with dissolve
    show ulilla joy at left with moveinleft
    ulilla "Ну что, ушли?"
    lyba "Ушли."
    ulilla "Пошли дальше в карты играть?"
    lyba "Пошли!"
    hide lyba with moveoutright
    hide ulilla with moveoutright
    
    
    
    play music "Music/eDance1.OGG" fadeout 1 fadein 2
    scene bg SchoolDaySakura with fade
    show lin sad at center with dissolve
    lin "Уф, ну и жарища..."
    lin "Собрались же с Лап пройтись по магазинам... И где она?"
    show lin norm with dissolve
    lin "Эхх. Такую юбочку себе вчера присмотрела!"
    
    show black with dissolve
    centered "Спустя некоторое время"
    hide black with dissolve
    
    show lin sad with dissolve
    lin "Кхм. Что-то я замечталась!"
    lin "Лап всё-равно опаздывает, а ждать жарко."
    lin "А что, если я немного разденусь? В этом же нет ничего плохого!"
    
    $ lin_state = 5
    $ lin_readed = False
    $ lin_allowKofta = True
    $ lin_StripMaster = True
    jump lin_nude


label lin_nude:
    
    $ cur_choise = 0
    menu:
        ""
        "Снять кофту" if lin_allowKofta:
            $ lin_allowKofta = False
            $ cur_choise = 5
        "Надеть открытый купальник":
            $ cur_choise = 3
        #"Остаться нагишом":
        "Раздеться догола":
            $ cur_choise = 2
        "Надеть закрытый купальник":
            $ cur_choise = 4
        "Почитать мангу":
            $ cur_choise = 99

            
    if cur_choise == lin_state:
        
        if lin_state == 5:
            lin "Скину-ка я кофту!"
            show lin leto with dissolve
            lin "Вот! Так-то гораздо лучше!"
    
            show black with dissolve
            centered "Спустя ещё некоторое время"
            hide black with dissolve
            
        elif lin_state == 4:
            lin "Всё равно жарко!"
            lin "Пойду надену купальник. Чуть что, скажу, что из бассейна."
            hide lin with moveoutleft
            show lin sexy with moveinleft
            lin "Вот так-то гораздо лучше!"
    
            show black with dissolve
            centered "Спустя ЕЩЁ время"
            hide black with dissolve
            
        elif lin_state == 3:
            lin "Ммм... Хоть и купальник, но всё-равно жарковато."
            lin "О! Идея!"
            hide lin with moveoutright
            show lin swim with moveinright
            lin "Яху!"
            
        elif lin_state == 2:
            lin "Кхм. А что, если..."
            hide lin with moveoutbottom
            jump after_nude
            
        
        $ lin_state -= 1
    elif cur_choise < 6 :
        if cur_choise > lin_state:
            if cur_choise == lin_state+1:
                lin "А сейчас я как одета?!"
            else:
                lin "Я уже давно сняла эту часть одежды!"
        if cur_choise < lin_state:
            lin "Ага! Может ещё и трусики сразу кому-нибудь подарить?!"
        $ lin_StripMaster = False
    else:
        show Book with moveinleft:
            xalign 0.6 yalign 0.3
        if lin_readed:
            lin "Ну и что я тут не видела?"
        else:
            $ lin_readed = True
            lin "О! Интересненько!"
            show black with dissolve
            centered "Через час"
            hide black with dissolve
            lin "Ой! Что-то я увлеклась!"
        hide Book with moveoutleft
    
    jump lin_nude
    
    
label after_nude:
    if lin_StripMaster:
        if not persistent.stripMaster:
            $ achId = "stripMaster"
            $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
            $ achText = __("\"Мастер раздевания\"")
            call showAchiv
        $ persistent.stripMaster = True
        
    show lyba angry at center with dissolve
    lyba "Стоять!"
    show lyba angry at left with moveinright
    show lin swim at right with moveinright
    lin "Да, Лайби, что такое?"
    lyba "Это ты у меня спрашиваешь, что такое?"
    lyba "Нет, это я спрашиваю, что это такое?!"
    lyba "А если Дэкс такое увидит, что тогда будет!"
    show lin swimsad with dissolve
    lin "Да... Об этом я как-то не подумала..."
    lyba "А ну вставай и иди одевайся!"
    lin "Не могу."
    lyba "Почему?"
    play sound "sound/madamvicious_girl-taking-damage.ogg"
    lin "Да радикулит проклятый! Опять спину прихватило..."
    hide lyba
    show lyblabla normal at left behind lin with dissolve
    lyblabla "Ох, горе ты моё луковое..."
    lyblabla "Ладно, пошли, помогу!"
    show lyblabla silent at right with moveinleft
    hide lin with moveoutleft
    hide lyblabla with moveoutleft
    show black
    hide black with dissolve
    show lyblabla normal at right with moveinleft
    show lin norm at left with moveinleft
    lyblabla "Лин, а что ты здесь вообще делала?"
    lin "Да вот, Лап жду. Договорились же с ней по магазинам пройтись..."
    show lyblabla sulk with dissolve
    lyblabla "Кхм. Так вы же вроде с ней на воскресенье договаривались?"
    lin "Ну да."
    lyblabla "А сегодня суббота!"
    show lin sad with dissolve
    lin "Мда... Так Лап и не виновата вовсе, получается..."
    lyblabla "Кстати! А почему купальник надевала? Думала, никто не заподозрит?"
    show lin laugh with dissolve
    lin "Ага! Сказала бы, что только что из бассейна!"
    show lyblabla normal with dissolve
    lyblabla "Но у нас нет бассейна..."
    show lin angry with dissolve
    lin "Да что ж за день такой сегодня?! Не везёт и не везёт..."
    lyblabla "Кстати, что бы охладиться, достаточно съесть мороженое!"
    show lin norm with dissolve
    lin "О! Точно, так и сделаю! Спасибо!"
    
    
    
    
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    scene black with fade
    centered "Немного позже"
    
    scene bg Park with fade
    show Freezer at left with dissolve
    show andry ice at left behind Freezer with dissolve
    andry "Налетай! Торопись! Покупай..."
    andry "Мороженое, соки, напитки, чипсы!"
    
    show lin norm at center with moveinright
    lin "А, Андрей, привет!"
    lin "Ты что это делаешь?"
    show andry norm with dissolve
    andry "Да так, продолжаю исследовать альтернативные методы заработка!"
    show lin laugh with dissolve
    lin "Да какой же этот метод альтернативный? Обычный нормальный заработок."
    show andry shy with dissolve
    andry "Ну не скажи! Здесь я вижу какие люди богаче, какие беднее."
    andry "А те, у кого кошелёк потолще, потом могут стать моими \"клиентами\"!"
    play sound "sound/madamvicious_female-ehem.ogg"
    lin "Так вот оно как..."
    show lin angry with dissolve
    lin "А ну не майся дурью и лучше делом займись!"
    show andry fight with dissolve
    play sound "sound/mattskydoodle_censor-beep.ogg"
    andry "А что мне ещё делать-то, что?! Деньги нужны очень!"
    andry "Иначе я не смогу покупать новые фигурки..."
    lin "Ах фигурки, да..."
    lin "А ну иди сюда!!!"
    
    hide andry with moveoutleft
    hide lin with moveoutleft
    show Imp fight at offscreenleft
    play sound "sound/ekokubza123_punch.ogg"
    Imp "Ай!" with vpunch
    
    show black with dissolve
    centered "Через некоторое время"
    hide black with dissolve
    
    show andry norm at center behind Freezer with moveinright
    andry "Фух! Кажется, оторвался!"
    show andry norm at left with moveinright
    show andry ice with dissolve
    andry "Налетай! Торопись! Покупай..."
    
    
    play music "Music/eDance1.OGG" fadeout 1 fadein 2
    scene bg MalaRoom with fade
    show mala homework at right with dissolve
    show mala homework2 at right with dissolve
    mala "А! Привет!"
    mala "А я тут мангу перевожу, скоро ещё один том выпустим!"
    show mala homework with dissolve
    mala "Тут есть пара моментов сложных, но я справлюсь."
    mala "Читатели же ждут!"
    show mala homework2 with dissolve
    
    menu:
        ""
        "Спросить у Мальвины, почему она не одета":
            mala "А! Так лето же! Жарко."
            mala "А тут ещё кондиционер сломался..."
            mala "В общем, сейчас только так работать и могу."
            pass
        "Пожаловаться на жару":
            show linMouthStern with dissolve:
                xalign 0.455 yalign 0.285
            mala "Ага! Полностью согласна!"
            mala "Я из-за этой жары в купальнике сижу..."
            hide linMouthStern with dissolve
            mala "Дома же можно!"
            pass
        "Отчитать за безнравственное поведение":
            hide mala
            show ChairPink:
                xalign 0.3 yalign 1.2
            show mala angrybig at left with dissolve
            mala "Эй! Ты ведь у меня дома!"
            mala "Со своим уставом в чужой монастырь не суются!"
            hide ChairPink
            show mala homework2 at right with dissolve
    mala "Кстати, сегодня я никуда не пойду."
    mala "Если было желание меня куда-нибудь вытащить - лучше забудь."
    mala "Манга важнее!"
    show mala homework with dissolve
    mala "Да и вечереет уже..."
    
    jump day7