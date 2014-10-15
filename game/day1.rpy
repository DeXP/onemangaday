label day1:    
    stop music
    play sound "sound/cocoricosound_cock-a-doodle-doo.ogg"
    scene bg Forest41 with fade
    show Sunshine at topright with moveintop
    show Shtab at left with moveinleft
    #play music "Music/Juanitos_-_El_Loco_Boogaloo.mp3" fadeout 1
    play music "Music/eDance1.OGG" fadein 3
    show lyblabla helmet at center with dissolve

    "???" "Приветствую тебя, новобранец!"
    "???" "Ты попал в штаб-квартиру. Мы переводим мангу."
    show lyblabla helmsulk at center
    "???" "И мы должны переводить её быстрее и качественнее вероятного противника!"
    "???" "Ты хочешь переводить мангу вместе с нами?"
    show lyblabla helsilent at center 
    
    menu:
        #"Переводить мангу?" #Название вопроса
        ""
        "Конечно, хочу. Я с Вами!":  
            show lyblabla helmet at center
            "???" "Ну и отлично. Работы непочатый край, рабочие руки всегда нужны."        
        "Нет, спасибо. Я так, мимо прохожу.":
            $ scan_points = -2
            $ klin_points = -2
            $ translate_points = -2
            $ korrekt_points = -2
            $ type_points = -2
            $ beta_points = -2
            
            show lyblabla helmet at center
            "???" "Не важно! Работы слишком много, и тебе придётся её делать. Родина тебя не забудет!"
    
    show lyblabla helmsulk at center
    lyblabla "Кстати, меня зовут Лайби. Я главный координатор команды."
    lyblabla "А вон идёт Дэкс, один из переводчиков с английского."
    
    show lyblabla helsilent at center 
    show dexp laugh at left with dissolve
    dexp "Привееет! А мы тут переводами манги балуемся..."
    #dexp_en "Hellooo! We are the manga translators! Yeeah!"
    #hide dexp
    
    show dexp nya at right with dissolve:
        xalign 1.0 yalign 1.0
    #play sound "sound/DeXP_nya.ogg"
    play sound "sound/ecfike_chuckle-1.ogg"
    dexp "Да пребудет с тобой великий кавай! Ня!"
    hide dexp with moveoutright
    
    show lyblabla helmet at center
    lyblabla "Он вообще-то нормальный парень, но периодически совсем неадекват..."
    show lyblabla helmsulk at center
    lyblabla "Ну... В штаб-квартиру тебе пока ещё рано. Так что пойдём, я покажу тебе учебную базу. Заодно и с остальной командой познакомишься!"
    
    #hide lyblabla
    hide Shtab with moveoutleft
    hide Sunshine with moveouttop
    
    scene bg EmptyClass42 with fade 
    show lyblabla normal at center with dissolve
    lyblabla "Вот, это наше учебное помещение. Иногда оно же рабочее, оно же столовая, оно же... Хотя нет, про остальные возможные применения помещения узнаешь в процессе!"
    lyblabla "Лап, подойди сюда, пожалуйста."
    
    show lap norm at right with moveinright
    show lyblabla silent at center
    lap "Да, Лайби. Зачем я тебе понадобилась?"
    hide lyblabla
    show lyblabla silent at left
    #hide lap
    
    play sound "sound/andrutzab_Surprise.ogg"
    show lap surprized at center with moveinright
    lap "Ой, а ты новенький, да? Рада с тобой познакомиться!"
    show lap joy at center
    lap "Ну, теперь работать станет чуточку легче, и мы сможем делать релизы чаще."
    show lap norm at center
    lap "Кстати, а как ты относишься к креативному экзистенциализму в контексте бренности бытия?"
    
    menu:
        "Креативный экзистенциализм?"                
        "Эээ...":  
            pass      
        "Ну... Как бы сказать...":
            pass
        "Креативному чего-чего?":
            pass
    
    show lap angry at center
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lap "Ай, ну вас всех. Только \"хи-хи\" да \"ха-ха\". А на серьёзные темы и поговорить не с кем..."
    hide lap with moveoutleft
    #hide lyblabla
    show lyblabla normal at center with dissolve
    play sound "sound/madamvicious_female-ehem.ogg"
    lyblabla "Мда. Придётся всё-таки мне лично показать тебе основные этапы перевода манги."
    lyblabla "Или ты и так знаком с основными этапами перевода манги?"
    
    show lyblabla silent at center 
    menu:
        ""#"Этапы перевода манги?" #Название вопроса                 
        "Нет, расскажи пожалуйста!":
            show lyblabla normal at center 
            lyblabla "Сначала оригинал манги сканируется и переводится в цифровой вид. За это отвечает сканировщик."
            show lyblabla sulk
            lyblabla "Дальше изображение надо очистить от мусора и старых надписей. Этим занимается клинер."
            show lyblabla normal
            lyblabla "Параллельно со сканированием и клином можно осуществлять непосредственно перевод манги с одного языка на другой. Обычно переводчик выдаёт результат своей деятельности в виде текстового файла."
            lyblabla "Каждый перевод потом вычитывается на лексические, орфографические и прочие ошибки. Этим занимается корректор."
            show lyblabla sulk
            lyblabla "Когда есть очищенные сканы и вычитанный перевод, то перевод можно нанести на подготовленные изображения. Этим занимается тайпер."
            lyblabla "Ну а когда текст нанесён на изображения остаётся проверить общее качество всей выполненной работы. Этим занимается бэта-ридер."
            show lyblabla normal
            pass      
        "Да, я всё знаю. Перейдём к делу.":
            pass
            
    scene bg Hallway1
    show lyblabla normal at center 

    lyblabla "Ну хорошо. Пройдись по коридору, выбери себе занятие по душе."
    lyblabla "Но помни, что можешь пройти обучение только у трёх учителей!"
    
    #play music "Music/Bars_Beats_Studio_-_Sunshine.ogg" fadeout 1
    #play music "Music/ePop.OGG" fadeout 1
    play music "Music/PopRock2.OGG" fadeout 1 fadein 3
    $ learn_cnt = 0
    jump domenu
    
    #lyblabla "Хорошо. Ну а теперь..."
    
    #scene black with fade
    #play music "Music/Merl_Beatz_-_A_soir_on_fuck_instrumental.ogg"
    #centered "Продолжение следует..."
    return


label domenu:
    $ learn_cnt += 1
    if learn_cnt > 3:
        jump after_learn
    scene bg Hallway1
    #show lyblabla silent at center
    hide lyblabla
    menu:
        "" #"\n\n\nНа какой из этапов пройти обучение?"                
        "Сканировщик":  
            if scan_learned:
                show lyblabla normal at center 
                lyblabla "Люк! Дао сканирования познаётся лишь однажды! Познай другую сторону силы."
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump scan     
        "Клинер":  
            if klin_learned:
                show lyblabla normal at center 
                lyblabla "Чисто-чисто-чисто в доме трубочиста!"
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump kliner 
        "Переводчик":  
            if translate_learned:
                show lyblabla normal at center 
                lyblabla "Не, не! Элиру эл ци тие!"
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump translator
        "Корректор":
            if korrekt_learned:
                show lyblabla normal at center 
                lyblabla "Текст после релиза не корректируют! Не судьба..."
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump korrektor
        "Тайпер":  
            if type_learned:
                show lyblabla normal at center 
                lyblabla "Да даже газету не печатают дважды! А ты два раза на тайп хочешь..."
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump typer
        "Бэта-ридер":
            if beta_learned:
                show lyblabla normal at center 
                lyblabla "Альфа, бэта, гамма, дзетта и газета!"
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump betareader
        "Пойти в столовую":
            if dinning_learned:
                show lyblabla normal at center 
                lyblabla "Хватит есть! Так и потолстеть недолго..."
                $ learn_cnt -= 1
                jump domenu
            else:
                hide lyblabla
                jump dinning_masta
        "Не собираюсь я работать!":
            show lyblabla normal at center 
            lyblabla "Работать - нужно!"
            $ learn_cnt += 1
            jump domenu
            #jump badend
    return


label scan:
    scene bg TeachersRoom with fade
    $ scan_learned = True
    
    $ scan_points += 10
    $ klin_points += 5
    $ type_points += 2
    $ beta_points += 2
    
    show dexp norm at center with dissolve
    dexp "Привет. Мы уже знакомы. Однако я не только переводчик, но и сканировщик."
    dexp "Казалось бы, что там сложного в этом сканировании? Берёшь бумажки, кладёшь на сканер, жмёшь кнопку."
    show dexp laugh
    dexp "Но всё не так просто..."
    show dexp norm
    dexp "Во-первых, томики манги - это не подготовленные единичные странички, а именно цельные книги."
    dexp "Чтобы расклеить мангу на листки, необходимо разогревать утюгом корешок. Что бы при этом мангу не сжечь, необходимо греть аккуратно, через марлю."
    show dexp think
    dexp "При этом следует помнить, что разогретый жидкий клей любит марать всё, на что только не попадёт!"
    dexp "Далее надо провести непосредственно сканирование полученных страничек. Сотни их, сотни..."
    show dexp norm 
    dexp "Каждая страничка сканируется индивидуально. Ведь если есть бумажный источник, то надо сделать максимально качественные сканы, чтобы облегчить работу клинеру."
    
    dexp "Есть 2 типа сканеров: CIS и CCD. CIS-сенсор обычно стоит в дешёвых сканерах и МФУ, CCD - в более дорогих моделях."
    
    show cis1 at topleft
    show cdd1 at topright
    dexp "Вот картинки с CIS (слева) и CDD-сканера (справа)."
    show dexp think
    dexp "И какая же из картинок лучше?"
    menu:
        "Какая картинка лучше?"                
        "Левая, она выглядит более чистой.":  
            pass      
        "Правая, на ней больше информации.":
            pass
    #" Левая выглядит более чистой. Неужели дешёвый CIS-сенсор лучше? Посмотрим под увеличением!"
    show dexp norm
    dexp "Левая, правая... Непонятно! Лучше посмотрим под увеличением!"
    hide cis1
    hide cdd1
    
    show cis2 at topleft
    show cdd2 at topright
    show dexp laugh
    dexp "Вот теперь разница видна. CIS-сканер просто не увидел текстуру, в то время как на CCD-изображении при желании можно разобрать даже фактуру бумаги."
    dexp "Особенно это видно на белом поле правее руки."
    hide cis2
    hide cdd2
    
    show dexp norm
    dexp "Также разница в типах сенсора сканера очень видна при деформациях. Например, если не расшивать книгу. Вот для примера деформированный лист:"
    
    show cis3 at center
    dexp "Это изображение получено на CIS-сканере. Размытие в области деформаций ужасно!"
    hide cis3

    show dexp think
    show cdd3 at center
    dexp "А это получено на CDD-сканере. Деформация примерно одинакова, но какова разница в результирующей картинке!"
    hide cdd3
    
    dexp "Как видно, на сгибе разница очень значительна."
    #dexp "Так же серьёзно отличается чувствительность сенсоров. Это видно при значительном увеличении:"

    
    show dexp norm 
    dexp "Ещё при сканировании следует не забывать следить за именованием файлов и за ориентацией сканов."
    
    dexp "Ну... Я рассказал тебе о сканировании всё, что знаю. Дальше поможет только практика."
    
    show lap norm at left with moveinright
    dexp "Ой, Лап! Ты такая милая! Иди сюда, пообщаемся."
    show lap angry at left with dissolve
    lap "Это что, домогательство? Нарываешься, да?!?"
    
    hide dexp with moveoutright
    hide lap  with moveoutright
    
    jump domenu
    return
    
    
label kliner:
    $ klin_learned = True
    
    $ klin_points += 10
    $ type_points += 5
    $ scan_points += 5
    $ beta_points += 2
    
    scene bg Shop with fade
    
    show Server at left with dissolve
    
    show lexa lookdown at left with dissolve
    "???" "Мда, ну и как поставить PHP под FreeBSD? Ууу! Сервера - зло!"
    play sound "sound/ecfike__sigh-1.ogg"
    "???" "Да и как-то кривоват сервер-то... Наверное, не следовало собирать его из подручного мусора..."
    
    
    show lexa norm at center with dissolve
    lexa "А, привет! Я энжынегр-зубр. Можно просто \"Лёха\". Я тут иногда клиню."
    lexa "Но всё чаще пытаюсь разрулить выдуманные проблемы с несуществующим сервером!"
    
    show dexp fearbig at offscreenleft
    dexp "Лёша, зараза, сделай клин, а?"
    
    lexa "Вернёмся к нашим баранэссам. Эээ, кхм, я имел ввиду, девушкам."
    hide Server with dissolve
    
    show cdd2 at left
    show klin0 at right
    lexa "Слева изображение после сканера. Справа - правильное изображение после клина."
    show lexa attention
    lexa "Разница видна в уровнях шума, в цветах и текстурах. Ну а теперь рассмотрим самые распространённые ошибки:"
    
    show lexa norm
    hide cdd2 with moveoutleft
    #hide klin0
    show klin0 at left with moveinright
    show klin_dark at right with moveinright
    lexa "Вот. Слева нормальный клин. Справа - с преувеличенным количеством чёрного. Так быть не должно."
    hide klin_dark with moveoutright

    show klin_light at right with moveinright
    lexa "А теперь правый клин пересветлён. Тоже плохо."    
    hide klin_light with moveoutright
    
    show lap norm at right with moveinright
    lap "Ах, Лёша, ты сегодня такой милый!"
    show lap joy at right
    lap "Не поможешь мне немного?"
    show lexa attention
    show lap norm at right
    lexa "Не видишь, я занят!"
    show lap angry at right
    lap "Ну вот всегда так..."
    hide lap with moveoutright
    show lexa norm
    
    show klin_overlevel at right with moveinright
    show lexa attention
    play sound "sound/ecfike_heh.ogg"
    lexa "Теперь у нас переклин. В данном случае изображение перечищено: потеряны текстуры, некоторые цвета. Так тоже делать нельзя."
    
    show lexa attention
    hide klin_overlevel with moveoutright
    hide klin0 with moveoutleft
    lexa "Ну? Всё ясно?"
    
    show lexa norm with hpunch
    lexa "(сейчас что-то будет!)"
    
    show lexa norm at right with moveinright
    show lyba angry at left #with hpunch
    lyba "Лёха, блин! Когда уже клин доделаешь!"
    lexa "Я занят."
    lyba "Все заняты! Но все - делают!"
    
    show carry norm at center with moveinright
    play sound "sound/madamvicious__stupid-witch.ogg"
    carry "Гы-гы! Ой ну вообще! Ну просто вообще! Гыыыы!"
    lyba "Кэрри, а ты чего ржёшь! У тебя долгов по работе на полгода вперёд!"
    hide lyba
    show lyblabla normal at left
    lyblabla "И вообще, Кэрри, что ты здесь делаешь?"
    
    show carry surprised
    show lyblabla silent
    stop sound
    carry "Как что? Я клинер вообще-то..."
    
    play music "Music/Dubstep1.OGG" fadeout 1 fadein 2
    show carry question
    stop sound
    carry "О! Точно! Пойду-ка я поиграюсь!"
    hide carry with moveoutright
    hide lexa with moveoutright
    
    hide lyblabla 
    show lyba angry at left    
    show lyba angry at center with moveinleft
    lyba "Вот и как с такими людьми работать, а?"
    hide lyba with moveoutright
    
    #hide lexa with fade
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    
    jump domenu
    return
    
    

label translator:
    $ translate_learned = True
    
    $ translate_points += 10
    $ korrekt_points += 5
    $ beta_points += 2
    $ type_points += 2
    
    scene bg Hallway41 with fade
    play sound "sound/ripper351_whistle.ogg"
    show dexp nya at center with dissolve
    dexp "Прости! Сие тайна великая есть!"
    hide dexp with moveoutleft
    
    scene bg Classroom44 with fade
    show dexp joybig at center with moveinleft
    dexp "Да уж, от тебя и не убежишь... Ладно, расскажу тебе про основы!"
    show dexp joybig at left with dissolve
    show lin normbig at right with moveinright
    lin "Эй, Дэкс! Для тебя тут дело есть!"
    dexp "А, что? Я вообще-то тут человеку объясняю..."
    lin "Да ладно. Заодно на примере и покажешь! Переведи, пожалуйста, фразу: \"Ne, ne! Eliru el ci tie!\""
    
    show dexp fearbig
    play sound "sound/ecfike_hey-1.ogg"
    dexp "Эй! Она же не на английском!"
    show lin angrybig
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lin "Ну и что?! Ты же переводчик! Делай давай!"
    show lin laughbig
    lin "Спасибо тебе большое!"
    hide lin with moveoutright
    
    #hide dexp
    show dexp thinkbig at  center with moveinleft
    dexp "Вот и как так работать?"
    dexp "И вообще, на каком языке фраза?!"
   
    menu:
        "\"Ne, ne! Eliru el ci tie!\""
        "Испанский":
            pass
        "Итальянский":
            pass
        "Латынь":
            pass
        "Эсперанто":
            $ translate_points += 2
            pass
    show dexp fearbig
    dexp "Ааа! Фиг разберёшься..."
    
    #hide dexp
    show dexp joybig at left with moveinright
    
    show lap bigquestion at right
    play sound "sound/andrutzab_Hm.ogg"
    lap "Кстати, Дэкс, вот тебе ещё фразочка:"
    lap "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
    
    show dexp fearbig
    play sound "sound/ecfike_growl-2.ogg"
    dexp "Ааа! За что мне всё это?!?"
    hide lap with moveoutright
    
    dexp "Великая Пряня-сэмпай! Спаси-помоги-объясни!"
    show prana clouds at topright with moveintop
    prana "Вижу, твоё отчаяние достигло крайней точки."
    show dexp joybig
    prana "Так и быть, помогу!"
    prana "Первая фраза на эсперанто, вторая - на латыни!"
    
    show dexp fearbig
    #play sound "sound/ecfike_growl-2.ogg"
    play sound "sound/ecfike__sigh-1.ogg"
    dexp "Ааа!"
    prana "И да пребудет с тобой Poogle!"
    hide prana with moveouttop
    
    play sound "sound/ecfike_computer-error.ogg"
    centered "{size=104}{b}{color=#11e}P{/color}{color=#e11}o{/color}{color=#ff1}o{/color}{color=#11e}g{/color}{color=#1e3}l{/color}{color=#e11}e{/color}{/b}{/size}" with dissolve
    
    
    hide dexp with fade
    jump domenu
    return
    
    

label korrektor:
    $ korrekt_learned = True
    
    $ korrekt_points += 10
    $ translate_points += 5
    $ beta_points += 2

    scene bg Classroom49 with fade
    show lin normbig at center with dissolve
    lin "Привет! Я Лин, главный корректор."
    lin "И я сейчас покажу тебе на примере, что такое редактирование текста!"
    lin "Пускай у нас есть текст \"Он был умный, был красивый, но мы на него ложили!\". Как бы его лучше отредактировать?"
    menu:
        "\"Он был умный, был красивый, но мы на него ложили!\""
        "Был умён, красив, но мы ложили на него!":  
            show lin angrybig
            lin "Ну какое нафиг \"ложили\", а?! Клали. Клали!!!"
            pass      
        "Он был умён, красив, и клали на него не только мы!":
            show lin angrybig
            lin "А откуда \"не только\"? Совсем с дубу рухнул?"
            pass
        "Умнец и красавец, давай-ка свой конец!":
            show lin angrybig
            lin "Ну и кто тут извращенец, а?! Совсем фантазия разыгралась?"
            pass
    show lin normbig
    
    lin "Ну понятно, да? Не всё оно так просто, как казалось..."
    show lin laughbig
    play sound "sound/madamvicious_woman-yandere-laugh.ogg"
    lin "Вобщем: практика, практика и ещё раз практика! Через пару лет и ты сможешь нормально редактировать тексты."
    show lin normbig at left with moveinright
    
    show yana questionbig at right with moveinright
    yana "Лин, не поможешь тут немного с корректом, а то совсем непонятно..."
    
    lin "Хорошо, Янушка, помогу! "
    lin "Пошли."
    
    hide lin with moveoutleft
    hide yana with moveoutleft
    
    jump domenu
    return



label typer:
    $ type_learned = True
    
    $ type_points += 10
    $ beta_points += 5
    $ klin_points += 2
    $ translate_points += 2
    
    scene bg Storage with fade
    
    show andry norm at center with dissolve
    andry "Привет, я Андрей, и я покажу тебе основы тайпа. Только давай быстрее, я занят."
    
    show type_good at topright
    show type_bad at topleft
    show andry shy at center
    andry "Вот. Слева плохой тайп, справа хороший. Всё ясно? Ну я тогда пойду..."
    
    hide type_good
    hide type_bad
    #hide andry
    
    show andry norm at left with moveinright
    show lap surprized at right with moveinright
    play sound "sound/andrutzab_Aah.ogg"
    lap "О! Андрей, всё хотела тебя спросить!"
    show type_china at top
    show lap norm at right
    lap "А не лучше ли тайпить как-то так?"
    
    show andry fight 
    andry "НЕТ! Не лучше!"
    show andry shy 
    andry "Такой шрифт был бы неплох где-нибудь в названии, но не в основном тексте. И строки расположены слишком близко друг другу - такой текст тяжело читать."
    hide type_china
    
    show lap joy
    lap "Ага, спасибо большое! Буду знать. Текст должен хорошо выглядеть, быть расположенным равномерно по облачку, но в то же время хорошо читаться."
    
    show andry chem
    #play music "Music/Bars_Beats_Studio_-_Jump.ogg" fadeout 1
    #play music "Music/eHeavyReggae.OGG" fadeout 1
    play music "Music/Metal1.OGG" fadein 1
    andry "Ну, я побежал? Мне ещё раствор для травления печатных плат делать..."
    hide andry with moveoutleft    
    
    play sound "sound/genelythgow_sshhhhhht.ogg"
    show Smoke2 at center with dissolve
    #stop music fadeout 1.0
    show lap surprized
    lap "Ой! Кажется, мы переборщили с \"Lorem Ipsum\" и призвали что-то ужасное!"
    lap "Бежим отсюда!"
    hide lap with moveoutright
    
    play sound "sound/deganoth_explosion-1.ogg"
    show Explosion at center with dissolve
    show lyba angry at center with hpunch
    lyba "Ууу! Химики-сатанисты хреновы! А убирать кто будет?!"
    
    hide Smoke2
    hide Explosion
    hide lyba with dissolve
    
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    
    jump domenu
    return
    
    
    
label betareader:
    $ beta_learned = True
    
    $ beta_points += 10
    $ type_points += 5
    $ klin_points += 2
    $ korrekt_points += 2
    
    scene bg Roof with fade
    show Sunshine at topright with moveintop
    
    show lyblabla normal with dissolve
    lyblabla "Я иногда делаю бэта-чтение наших переводов."
    show lyblabla sulk
    lyblabla "Но стараюсь делать это на крыше. Успокаивает."
    lyblabla "И мысли о суициде почти не лезут в голову..."
    
    lyblabla "Нет, всё-таки иногда лезут. Так что буду соблюдать технику безопасности!"
    show lyblabla helmet with dissolve
    lyblabla "Вот. Так-то лучше!"
    
    lyblabla "Ну сам посуди, вот изображение готового клина:"
    show klin0 at right with moveinright
    hide lyblabla
    show lyba helangry at center
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lyba "А пятно на воротнике кто убирать будет?!"
    lyba "Я?! Меня на все проекты просто физически не хватит..."
    hide klin0 with moveoutright
    
    hide lyba
    show lyblabla helmsulk
    lyblabla "Вот так и живём. Что не выловит бэта-ридер, то потом вывалят на нас читатели..."
    
    lyblabla "Ай, ну её, эту технику безопасности..."
    show lyblabla silent at left with moveinright
    
    show lin norm at right with moveinright
    play sound "sound/madamvicious_woman-insane-laughter.ogg"
    lin "О! Лайби! А я тебя ищу. Смотри, как наши накосячили!"
    show lin laugh
    lin "Представляешь, там написали не \"клали\", а \"ложили\"! Ложили! Вот умора! Ха-ха-ха!"
    
    hide lyblabla
    show lyba angry at left
    lyba "Лин! Ты ведь сама корректила этот проект! Почему раньше не выловила?!"
    
    show lin norm with dissolve
    stop sound
    lin "Упс."
    hide lin with moveoutright
    
    hide lyba
    show lyblabla normal at left
    show lyblabla normal at center with moveinleft
    lyblabla "Всё ещё есть желание быть бэта-ридером? Если да, то теперь тебе поможет только практика!"
    
    hide lyblabla with dissolve
    jump domenu
    return
    
    
label dinning_masta:
    $ dinning_learned = True
    
    $ scan_points += 4
    $ klin_points += 4
    $ translate_points += 4
    $ korrekt_points += 4
    $ type_points += 4
    $ beta_points += 4
    
    scene bg Dinning1 with fade
    
    show carry surprised at center with moveinright
    carry "О! И ты уже в столовке!"
    show carry norm
    carry "Шустро, шустро!"
    show carry question 
    carry "Если будешь так же быстро делать клин - станешь незаменимой частью команды!"
    hide carry with moveoutleft
    
    show lin norm at left with moveinleft
    show lap norm at center with moveinright
    
    show lap surprized
    lap "Лин, как продвигается корректировка текстов?"
    show lin laugh
    lin "Всё путём! Не забывать удалять лишние повторения - и текст сразу становится более читаемым!"
    show lin norm 
    lin "А ты ведь и клинишь и тайпишь?"
    show lap norm
    lap "Ага! Но пока ещё не совсем чувствую центр массы текста. Надеюсь, придёт с опытом."
    
    lin "Кстати, а что есть-то будем?"
    lap "Ах. Здесь очень вкусные блинчики! Ты как, не против?"
    lin "Ну и отлично, пойдём!"
    hide lin with moveoutleft
    hide lap with moveoutleft
    
    show andry norm at center with moveinright
    andry "Эй! Меня подождите, меня!"
    hide andry with moveoutleft
    
    scene bg Dinning2
    show dexp fearbig at center
    play sound "sound/ecfike_growl-1.ogg"
    dexp "Ну сколько можно про еду говорить, а!?"
    dexp "Я ж худеть пытался..."
    show dexp joybig
    dexp "Ну и фиг с ним! Пойду нажрусь!"
    dexp "Кстати, если будешь сканировать - не забывай расшитые листы класть стопкой рядом со сканером. Тогда получится быстрее!"
    dexp "А если решишься стать переводчиком - то используй несколько словарей, значения слов могут быть разными!"
    hide dexp with moveoutright
    
    scene bg Dinning1
    show lyblabla normal at center with move
    lyblabla "Народ! Может хватит тут жевать?"
    lyblabla "Мангу-то за вас делать никто не будет..."
    lyblabla "Да и при бэта-чтении чем больше народу, тем лучше!"
    
    hide lyblabla with fade
    
    jump domenu
    return
    
    

label after_learn:
    scene bg EmptyClass42 with fade 
    show lyblabla normal at center
    
    lyblabla "Поздравляю! Обучение окончено!"
    lyblabla "Ну, кем ты хочешь стать?"
    show lyblabla silent
    
    $ prof_help = __("И да поможет тебе великий Ктулху!")
    menu:
        ""#"\n\nКем быть?"                
        "Сканировщик": 
            $ profession = "scan"
            $ prof_str = __("сканировщик")
            $ prof_help = __("Этап сканирования наиболее связан с этапами клина и тайпа. Кстати, кого-нибудь из сканировщиков часто можно найти в столовой.")
            $ pic_team = True
            if scan_points >= NEED_POINTS:
                $ prof_success = True
                if not persistent.beenScanner:
                    $ achId = "scanner"
                    $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
                    $ achText = __("\"Сканировщик\"")
                    call showAchiv
                $ persistent.beenScanner = True
            pass
        "Клинер": 
            $ profession = "klin"
            $ prof_str = __("клинер")
            $ prof_help = __("Этап клина связан со сканированием и тайпом. Кроме того, бэта-ридер тоже может вылавливать огрехи клина.")
            $ pic_team = True
            if klin_points >= NEED_POINTS:
                $ prof_success = True
                if not persistent.beenCleaner:
                    $ achId = "cleaner"
                    $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
                    $ achText = __("\"Клинер\"")
                    call showAchiv
                $ persistent.beenCleaner = True
            pass
        "Переводчик": 
            $ profession = "translator"
            $ prof_str = __("переводчик")
            $ prof_help = __("Переводчик теснее всего связан с корректировщиком и тайпером. При тайпе текст не всегда влазит в необходимую область и приходится его сокращать.")
            $ text_team = True
            if translate_points >= NEED_POINTS:
                $ prof_success = True
                if not persistent.beenTranslator:
                    $ achId = "translator"
                    $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
                    $ achText = __("\"Переводчик\"")
                    call showAchiv
                $ persistent.beenTranslator = True
            pass
        "Корректор": 
            $ profession = "korrektor"
            $ prof_str = __("корректор")
            $ prof_help = __("Корректор часто общается с переводчиком, бэта-ридером и иногда тайпером.")
            $ text_team = True
            if korrekt_points >= NEED_POINTS:
                $ prof_success = True
                if not persistent.beenProofreader:
                    $ achId = "proofreader"
                    $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
                    $ achText = __("\"Корректор\"")
                    call showAchiv
                $ persistent.beenProofreader = True
            pass
        "Тайпер": 
            $ profession = "type"
            $ prof_str = __("тайпер")
            $ prof_help = __("Этап тайпа связан как с результатами этапа перевода и корректировки, так и с результатами сканирования и клина.")
            $ pic_team = True
            if type_points >= NEED_POINTS:
                $ prof_success = True
                if not persistent.beenTyper:
                    $ achId = "typer"
                    $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
                    $ achText = __("\"Тайпер\"")
                    call showAchiv
                $ persistent.beenTyper = True
            pass
        "Бэта-ридер":
            $ profession = "beta"
            $ prof_str = __("бэта-ридер")
            $ prof_help = __("Этап бэта-прочтения больше всего связан с этапом тайпа, т.к. при наборе текста ошибки предыдущих этапов частично вылавливаются и остаётся проверить только сам тайп.")
            $ text_team = True
            if beta_points >= NEED_POINTS:
                $ prof_success = True
                if not persistent.beenBetareader:
                    $ achId = "betareader"
                    $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
                    $ achText = __("\"Бэта-ридер\"")
                    call showAchiv
                $ persistent.beenBetareader = True
            pass
            
            
    show lyblabla helmet
    lyblabla "Ну что ж..."
    
    if not prof_success:
        lyblabla "Извини, ты нам не подходишь."
        lyblabla "Тебе не хватает прилежности. Возможно, в следующий раз повезёт больше..."
        lyblabla "[prof_help]"
        lyblabla "Попробуй выбрать более подходящих учителей."
        jump badend
    
    #play music "Music/Bars_Beats_Studio_-_Polaroid.ogg" fadeout 1
    play music "Music/EuroDance2.OGG" fadeout 1 fadein 1
    hide lyblabla
    show Flags at topleft
    show Cracker at topright
    #show lyblabla helmet at center
    show lyba happy at center
    if text_team:
        show dexp laugh at left
        show lin laugh at right
    if pic_team:
        show lap joy at left
        show andry shy at right
    lyba "Поздравляю, кадет! Твоё новое звание: \"[prof_str]\"!"
    
    hide lyba
    if text_team:
        show dexp norm at left
        show lin norm at right
    if pic_team:
        show lap norm at left
        show andry norm at right
    show lyblabla helmsulk
    lyblabla "Конечно, в одиночку вести какой-нибудь проект тебе пока никто не даст."
    lyblabla "Cначала надо набраться опыта. Но ты уже можешь участвовать в реальных проектах, делать перевод манги вместе с нами!"
    lyblabla "А после первого релиза с твоим участием ты станешь полноправным членом команды."
    lyblabla "Но это всё потом, а сейчас..."
    
    
    scene bg Disko with fade
    hide lyblabla
    #show lyba happy at center
    show lyba happy at center with dissolve
    if text_team:
        hide dexp
        show dexp laugh at left with dissolve
        hide lin
        show lin laugh at right with dissolve
    if pic_team:
        hide lap
        show lap joy at left with dissolve
        hide andry
        show andry shy at right with dissolve
    play sound "sound/madamvicious__nyuu-voice.ogg"
    lyba "Вечеринка!!!"
    lyba "Веселись как следует, ведь завтра будет тяжёлый рабочий день, а перед ним нужно хорошо отдохнуть!"
    if profession == "beta":
        lyba "Бэта-ридерам не легко живётся, но именно на нас держится качество выполненной работы!"
    
    hide lyba with moveoutleft
    
    if text_team:
        call text_team_omedeto
        call pic_team_omedeto
    if pic_team:
        call pic_team_omedeto
        call text_team_omedeto
    
    
    "" "От обилия поздравлений стало душно."
    $ disko_goout = False
    menu:
        "Что делать?"
        "Выйти на улицу":
            $ disko_goout = True
            $ met = "malya"
            call disko_yard
            pass
        "Пойти на крышу":
            $ disko_goout = True
            $ met = "lyba"
            call disko_roof
            pass
        "Сходить в столовую":
            $ disko_goout = True
            $ met = "azyki"
            call disko_stolovka
            pass
        "Остаться в зале":
            pass
    
    show lexa norm at center with dissolve
    if disko_goout:
        lexa "А почему я не мог тебя найти?"
        lexa "А, не важно..."
    show lexa attention
    lexa "Поздравляю! И если будут вопросы по схемотехнике - обращайся! ... К Андрею."
    show lexa norm 
    lexa "В любом случае, погуляй по залу, пообщайся с людьми. С нами весело!"
    
    
    #DeXP
    scene bg DiskoStage with fade
    show dexp norm at left with dissolve
    show lap norm at right with dissolve
    dexp "Лап! Я давно хотел сказать тебе..."
    
    show dexp laugh 
    dexp "Ты мне очень-очень нравишься!"
    
    show lap surprized
    play sound "sound/andrutzab_Surprise.ogg"
    lap "Ч... чего?"
    
    show dexp norm
    dexp "Нравишься ты мне, говорю!"
    
    show lap angry
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lap "Ах так, да?!  А ну-ка иди сюда, повтори!"
    
    hide dexp with moveoutleft
    hide lap with moveoutleft
    play sound "sound/ekokubza123_punch.ogg"
    scene bg DiskoStage with vpunch
    
    show dexp fearbig at offscreenleft
    dexp "Ой!"
    play sound "sound/ekokubza123_punch.ogg"
    show dexp fearbig at offscreenleft with hpunch
    dexp "Да чтоб я ещё раз наступил на эти же грабли..."
    
    scene bg Disko with fade
    
    "" "Весело тут..."
    
    
    #Lin
    scene bg DiskoStage with fade
    show lap norm at left with dissolve
    show lin norm at right with dissolve
    lin "Лап! Я давно хотела сказать тебе..."
    
    show lin laugh 
    lin "Ты мне очень-очень нравишься!"
    show lap surprized
    play sound "sound/andrutzab_Surprise.ogg"
    lap "Ч... что, опять?"
    
    show lin norm
    lin "Нравишься ты мне, говорю!"
    "" "(Сговорились они, что ли? Или фраз других нет?)"
    
    show lap angry
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lap "Ах так, да?!  А ну-ка иди сюда, повтори!"
    
    hide lin with moveoutright
    hide lap with moveoutright
    play sound "sound/ekokubza123_punch.ogg"
    scene bg DiskoStage with vpunch

    scene bg Disko with fade
    
    
    "" "Кхм. А вдруг там за кулисами опять что-нибудь интересное?"
    
    #Lap + Zubr
    scene bg DiskoStage with fade
    show lexa norm at left with dissolve
    show lap norm at right with dissolve
    lap "Лёша! Я давно..."
    show lap surprized
    lap "Хотя нет, не буду банальной!"
    
    show lap joy
    lap "Ты самый лучший! Когда вижу тебя, звёзды на небе светят ярче! Хочу быть с тобой!"
    
    #show lap surprized
    play sound "sound/ecfike_heh.ogg"
    lexa "А? Ты что-то говорила? Прости, я задумался!"
    
    show lap norm
    lap "Ты мне нравишься!"
    
    show lexa attention
    lexa "Прости, но мне нравятся только серверы!"
    
    show lap angry
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lap "Ах так, да?!  А ну-ка иди сюда, повтори!"
    
    hide lexa with moveoutleft
    hide lap with moveoutleft
    play sound "sound/ekokubza123_punch.ogg"
    scene bg DiskoStage with vpunch
    
    
    scene bg Disko with fade

    
    
    "" "Мда. Слишком уж тут насыщенная дискотека. Пойду-ка я спать..."

    
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2
    
    scene black with fade
    centered "Так закончился первый день."
    centered "А на следующий - уже началась тяжёлая работа!"
    #jump goodend
    jump day2
    return


label text_team_omedeto:
    show dexp norm at center with moveinleft
    dexp "Поздравляю с поступлением в команду! Хорошо поработаем вместе!"
    if profession == "translator":
        dexp "Переводчикам нелегко живётся, но вместе мы - сила. Удачи тебе, коллега!"
    hide dexp with moveoutleft
    show lin norm at center with moveinleft
    lin "Так держать! Мы - команда!"
    if profession == "korrektor":
        lin "Далеко не все переводчики умеют красиво излагать свои мысли. Наша главная задача как корректоров - донести мысль до читателя!"
    hide lin with moveoutright
    return


label pic_team_omedeto:
    show andry norm at center with moveinleft
    andry "Тебе удалось! Теперь ты с нами. Ура!"
    if profession == "type":
        andry "Набирать текст далеко не так просто. Но мы как тайперы справимся! Так ведь?"
    hide andry with moveoutright
    
    show lap norm at center with moveinright
    lap "Молодчина! Теперь в команде на целого человека больше! Да мы теперь вместе горы свернём!"
    if profession == "klin":
        show lap joy
        lap "Далеко не все картинки после сканера хороши. Но нас это не остановит!"
    hide lap with moveoutleft
    return
    
    
label disko_roof:
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2
    scene bg RoofNight with fade
    
    show lyblabla sulk at center with dissolve
    lyblabla "Что, тоже не любишь шумные сборища?"
    lyblabla "На крыше всегда тихо и свежий воздух."
    lyblabla "Ну, стало легче?"
    lyblabla "Пойдём лучше ко всем, ведь сегодня знаменательный день!"
    
    hide lyblabla
    play music "Music/Dance3.OGG" fadeout 1 fadein 2
    scene bg Disko with fade
    return
    
label disko_yard:
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2
    scene bg SchoolyardNight with fade
    
    show mala norm with dissolve
    "???" "О! Привет! Тоже любишь погулять?"
    mala "Меня Мальвиной зовут. Можно просто Маля."
    show mala work with dissolve
    mala "Я в команде относительно недавно, но сама и перевожу, и клиню, и тайплю."
    mala "У меня не слишком много опыта, но чем смогу - помогу."
    mala "Если будут вопросы - обращайся!"
    show mala norm with dissolve
    mala "А теперь давай вернёмся ко всем. Всё-таки это твой праздник!"
    hide mala with moveoutleft
    
    play music "Music/Dance3.OGG" fadeout 1 fadein 2
    scene bg Disko with fade
    return
    
label disko_stolovka:
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2
    scene bg DinningNight with fade
    
    show dexp norm at center with dissolve
    dexp "(Омноном!)"
    show dexp fearbig
    play sound "sound/ecfike__sigh-1.ogg"
    dexp "Ну вот! Даже ночью поесть спокойно не дают!"
    hide dexp with moveoutright
    
    show azyki norm with dissolve
    play sound "sound/madamvicious_female-ehem.ogg"
    azyki "Ну и зачем надо было его пугать?"
    show azyki laugh
    azyki "За Дэксом так смешно наблюдать, когда он думает, что его никто не видит!"
    show azyki norm
    azyki "Меня зовут Азуки!"
    azyki "Я клинер, и Лайби считает, что очень даже неплохой."
    azyki "Если будут вопросы - обращайся."
    hide azyki with moveoutleft
    
    play music "Music/Dance3.OGG" fadeout 1 fadein 2
    scene bg Disko with fade
    return
    
