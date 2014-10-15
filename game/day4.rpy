label day4:
    #play music "Music/Chillout2.OGG" fadeout 1 fadein 2
    scene black with fade
    
    centered "День 4"
    
    play music "Music/Dubstep3cosmo.OGG" fadeout 1 fadein 2
    scene bg Stars with fade
    show lap cosmo at left with dissolve
    
    lap "Ух! Как тут красиво!"
    show lap cosmo at center with moveinleft
    lap "Всегда мечтала побывать в космосе..."
    
    show StarShip with moveinleft:
        xalign 0.05 yalign 0.3
    lap "Спасибо большое Андрею, что собрал для меня космический корабль!"
    
    
    show god cloud with moveinright:
        xalign 1.1 yalign 1.3
    
    god "Девочка! Ты зачем засоряешь мой космос всяким хламом?!?"
    show lap cosmoangry at center with dissolve
    lap "Это не хлам! Это мой космический корабль!"
    god "Но выглядит как хлам!"
    lap "Может и выглядит, но Андрей же старался!"
    
    show lap cosmo at center with dissolve
    lap "И ведь это всё не важно! А я давно хотела спросить!"
    
    $ godAnsCount = 0
    $ godKarma = 0
    
    $ godAllow1 = True
    $ godAllow2 = True
    $ godAllow3 = True
    $ godAllow4 = True
    $ godAllow5 = True
    $ godAllow6 = True
    
    jump godQuestions
 

label godQuestions:
    menu:
        #"\nЧто же хотела спросить Лап?"
        ""
        "Как быстро похудеть?" if godAllow5:
            $ godAllow5 = False
            $ godKarma -= 1
            god "Кушать меньше не пробовала?"
        "Есть ли справедливость?" if godAllow1:
            $ godAllow1 = False
            $ godKarma += 2
            god "Спроси что-нибудь полегче, а?"
        "Как понять женщину и своё руководство?" if godAllow2:
            $ godAllow2 = False
            $ godKarma -= 1
            god "А я тут причём? Я женщина, что ли?"
        "Почему наши проекты всё время перехватывают?" if godAllow3:
            $ godAllow3 = False
            $ godKarma += 2
            $ penalty -= 1
            god "Переводить вовремя не пробовали?"
        "Где взять много денег?" if godAllow4:
            $ godAllow4 = False
            $ godKarma -= 1
            god "Работать, так понимаю, не вариант?"
        "Где взять свободное время?" if godAllow6:
            $ godAllow6 = False
            $ godKarma += 2
            god "Как насчёт меньше маяться дурью?"
            
    $ godAnsCount += 1
    if godAnsCount >= 3:
        if godKarma >= 3:
            jump day4afterGod
        else:
            jump godBadEnd
    else:
        jump godQuestions
            
            
label day4afterGod:
    lap "Скажи, а..."
    god "Кхм. Эй, эй, полегче!"
    lap "А ещё я хотела бы узнать..."
    god "Ой. Я тут вспомнил. У меня тут срочные дела! До свидания!"
    
    hide god with moveoutright
    show lap cosmoangry at center with dissolve
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lap "Куда?!? А ну стоять! Я ещё не всё спросила!"
    hide lap with moveoutright
    hide StarShip with moveoutright
    
    
    
    
    scene bg Classroom49 with squares
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    show andry shy:
        xalign -0.14 yalign 1.0
    show lap norm:
        xalign 0.9 yalign 0.7
    
    andry "Эй! Лап! Ты меня слушаешь? Я тебе уже целый час объясняю!"
    show lap surprized with dissolve
    play sound "sound/andrutzab_Surprise.ogg"
    lap "Ой, я, кажется, немножко отвлеклась... Так что ты там говорил?"
    show andry norm with dissolve
    andry "Вот, слушай..."
    
    
    scene bg Staircase with fade
    show carry spy at left with dissolve
    carry "Да. Все секретные данные у меня."
    carry "Да, при ближайшей оказии я передам Вам документы..."
    
    show lexa norm at right with moveinright
    lexa "О, Кэрри! Привет."
    lexa "А что это ты такое делаешь?"
    play sound "sound/madamvicious_female-ehem.ogg"
    carry "Упс."
    hide carry with moveoutleft
    show carry norm at left with easeinleft
    carry "Да так, ничего. Гы-гы."
    carry "Не говори никому, что меня видел, ладно?"
    lexa "Да без проблем..."
    
    
    scene bg Dinning1 with fade 
    show lyblabla helmbinocle at center with dissolve
    lyblabla "Итак, товарищи! Вчера мы так ничего и не решили!"
    lyblabla "Всё-таки, у кого какие будут предложения?"
    play sound "sound/andrutzab_Hm.ogg"
    lyblabla "И где Дэкс?!"
    
    scene black with fade
    play music "Music/EuroDance2.OGG" fadeout 1 fadein 2
    centered "В то же время" with dissolve
    
    scene bg Park with fade
    show Bench:
        xalign 0.93 yalign 0.73
    show lexa sit with dissolve:
        xalign 1.0 yalign 1.0
    show mala sit with dissolve:
        xalign 0.6 yalign 1.0
    
    
    mala "Лёша... Я очень любопытная..."
    show Kust with moveinleft:
        xalign 0 yalign 0.7
    mala "И давно хотела спросить у тебя..."
    
    show dexp happykust behind Kust with moveinleft:
        xalign 0.15 yalign 0.3
    dexp "(Ухх! Сейчас что-то будет!)"
    
    play sound "sound/andrutzab_Aah.ogg"
    mala "Я, правда, немного стесняюсь такое спрашивать..."
    show dexp happykust behind Kust with moveinleft:
        xalign 0.28 yalign 0.3
    dexp "(Ну же! Ну же!)"
    
    show BranchTopLeft at topleft with dissolve
    show jess phototop behind BranchTopLeft at topleft with moveintop
    jess "Ага! Попались! Всех сфотографирую!"
    show white at center
    play sound "sound/eelke_photo.ogg"
    hide white with dissolve

    menu:
        "Что делать Дэксу?"
        "Панически скрыться!":
            hide dexp
            show dexp fearbig at center #with dissolve
            dexp "О нет! Мы попались! Бежииим!!!"
        "Отступить с чувством достоинства":
            hide dexp
            show dexp thinkbig at center
            dexp "Я так думаю, нас ведь уже всё равно сфотографировали? Так что пойду-ка я."
        "Обратить всё в шутку":
            hide dexp
            show dexp joybig at center
            dexp "Ахаха! Вот умора-то! Ахаха!"
    
    
    hide dexp with moveoutright
    hide jess with moveouttop
    show mala angrybig at center with dissolve
    play sound "sound/mattskydoodle_censor-beep.ogg"
    mala "Ах! Так он, значит, за нами всё это время подсматривал!!!"
    mala "Ну пускай только мне попадётся!"
    mala "Из-за него я так и не узнала, почему Лёша носит с собой эту чёртову клавиатуру!"
    hide mala with moveoutright
    hide lexa with dissolve
    
    
    
    
    
    scene black with fade
    centered "Чуть позже"
    
    scene bg Dinning1 with fade
    play music "Music/PopRock2.OGG" fadeout 1 fadein 2
    show lyblabla helsilent at center with dissolve
    show jess funnycard behind lyblabla at left with moveinleft
    jess "Лайби! Смотри, что у меня есть!"
    lyblabla "Что это?"
    jess "Пара пикантных фоток Дэкса, Мали и Лёхи!"
    show lyblabla normal with dissolve
    lyblabla "Молодец, молодец. Делай ещё фотки!"
    show jess happy with dissolve
    show lyblabla silent
    jess "Хе хе!"
    
    show dexp norm behind jess at right with easeinright
    dexp "И что здесь происходит?"
    show dexp laugh with dissolve
    dexp "О! Довольная Джесс!"
    
    show dexp laugh with easeinright:
        xalign 0.03 yalign 0.5
    show dexp maikasurprised with dissolve
    
    show lyblabla normal
    play sound "sound/andrutzab_Aah.ogg"
    lyblabla "Кхм..."
    lyblabla "Дэкс, стесняюсь спросить..."
    lyblabla "Но что ты делаешь так близко к Джесс?"
    hide lyblabla
    show lyba angryflip with dissolve
    play sound "sound/mattskydoodle_censor-beep.ogg"
    lyba "И КАКОГО ЧЁРТА ТЫ БЕЗ ШТАНОВ?!?"
    dexp "Так жарко же."
    lyba "Всё равно! Надень штаны! Ты на официальном мероприятии!"
    show dexp norm at left with dissolve
    dexp "Ну ладно..."
    hide lyba
    show lyblabla normal with dissolve
    lyblabla "Ну и хорошо..."
    show lyblabla silent
    hide jess with moveoutleft
    
    show drakoha norm behind lyblabla at right with moveinright
    drakoha "Всем привет! Я вернулась!"
    show dexp think with dissolve
    dexp "Ну ни фига себе за хлебушком сходила..."
    drakoha "Ой. Соль забыла. Я сейчас, 5 минут!"
    hide drakoha with easeoutright
    
    show mala norm at right with moveinright
    show lexa norm with moveinright:
        xalign 1.4 yalign 1.0
    mala "Всем привет! А что здесь происходит?"
    
    show lyblabla normal
    lyblabla "Ага! Вот и остальные проштрафившиеся появились!"
    lyblabla "Мы тут общим собранием решаем, что с конфликтом делать, а они гуляют!"
    show lyblabla sulk
    lyblabla "В наказание сегодня сами пойдёте говорить с вражеской командой!"
    lyblabla "Шагом марш!"
    show lyblabla silent
    
    show mala work with dissolve
    mala "Ну надо, значит надо..."
    
    hide lexa with moveoutright
    hide mala with moveoutright
    hide dexp with moveoutright
    
    
    
    
    scene black with fade
    centered "И пошли они в бой." with dissolve
    centered "И... "
    centered "Да что ж такое?!?"
    
    scene bg Dinning1 with fade 
    show lyblabla silent at center with dissolve
    show mala work at left with moveinright
    show dexp think at right with moveinright
    
    dexp "Эмм. Лайби, мы тут подумали..."
    mala "В общем, вечер уже, пора ужинать."
    dexp "Может, мы сначала поедим, а завтра уже утром на свежую голову будем разборки устраивать?"
    
    show lyblabla normal
    lyblabla "Ужин - святое. Кушайте на здоровье."
    
    
    scene bg Dinning2 with fade
    show dexp joybig at center with moveinleft
    dexp "Да уж. Война войной, а еда по расписанию!"
    show dexp joybig at left with moveinright
    
    play music "Music/Metal1.OGG" fadein 1
    show mala angrybigflip at right with moveinright
    mala "Ах, вот ты где!"
    mala "Ты почему за нами в парке подглядывал?!"
    
    
    show dexp fearbig with dissolve
    dexp "Я просто посмотреть хотел, честно!"
    
    show mala angrybigflip at center with easeinright
    mala "Ах, посмотреть, да? А ну иди сюда!"
    hide dexp with easeoutleft
    hide mala with moveoutleft
    
    play sound "sound/ekokubza123_punch.ogg"
    show dexp fearbig at offscreenleft with hpunch
    play sound "sound/ekokubza123_punch.ogg"
    dexp "Ай!" with vpunch
    
    scene black with fade
    play music "Music/Chillout5v7.OGG" fadeout 1 fadein 2
    centered "Вот так и закончился ещё один день..." with dissolve
    centered "Выживут ли наши герои, или всё будет плохо?" with dissolve 
    
    jump day5


label godBadEnd:
    $ goodEnd = False
    god "Девочка!"
    god "Ты задаёшь неправильные вопросы!"
    god "И теперь ты навсегда останешься у меня!!!"
    scene black with fade
    centered "И ведь не существует спасения от вечности..." with dissolve
    centered "А вечность заставляет задуматься" with dissolve
    centered "Задуматься... О душе?" with dissolve
    centered "Жадность, насилие, деньги - для этого ли живём?" with dissolve
    centered "{size=36}{b}ПЛОХАЯ КОНЦОВКА{/b}{/size}" with wipeleft
    if not persistent.bad4end:
        $ achId = "b4e"
        $ achievementUlocked = __("{size=20}Достижение разблокировано{/size}")
        $ achText = __("\"Потеряться в космосе\"")
        call showAchiv
    $ persistent.bad4end = True
    centered "( P.S.  Не забудьте найти другие концовки! )" with irisout
    jump titles
    return
