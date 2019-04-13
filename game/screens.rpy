# Этот файл публично доступен. Модифицируйте его под свои сообственные экраны.

##############################################################################
# Say
#
# Экран отображения ADV-диалога.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Умолчания для side_image и two_window
    default side_image = None
    default two_window = False

    # Решаем, нужен ли нам двухоконный или однооконный вариант.
    if not two_window:

        # Вариант с одним окном.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Вариант с двумя окнами.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Если есть изображение, отобразить его над текстом.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Использовать быстрое меню.
    use quick_menu


##############################################################################
# Choice
#
# Экран для отображения внутриигровых меню.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    
    style.menu_choice_button.ymaximum = 47
    style.menu_choice_button.yminimum = 47
    
    style.menu_choice.size = 25


##############################################################################
# Input
#
# Экран для отображения renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Экран для NVL-диалога и меню.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Отображать диалог.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Отображать меню, если есть.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Экран для отображения главного меню при запуске Ren'Py.
# http://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu:

    # Это заменяет другие меню.
    tag menu

    # Фон главного меню.
    window:
        style "mm_root"
        #Image( _("bg/Title.png"), xalign=0.9, yalign=0.025)
        add __("bg/Title.png") xalign .97 yalign .025
        #add anim.Blink( __("bg/Title.png"), high=0.7, low=1.0  ) xalign .9 yalign .025
        #Animation( _("bg/Title.png"), 0.5, im.FactorScale(_("bg/Title.png"), 0.9), 0.5) 
        #add mmTitle

    # Кнопки главного меню.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Начать игру") action Start()
        #textbutton _("bg/Title.png") action Start()
        textbutton _("Загрузить игру") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Достижения") action ShowMenu("achievements")
        #textbutton _("Help") action Help()
        #textbutton _("Помошь") action ShowMenu("help")
        textbutton _("Выход") action Quit(confirm=False)

init -2 python:

    # Сделать все кнопки главного меню одноразмерными.
    style.mm_button.size_group = "mm"
    #style.mm_button.size = 32
    style.mm_button.ymaximum = 47
    style.mm_button.yminimum = 47




##############################################################################
# Help
screen help: 
    #С помощью этих двух функций мы меняем фон, add можно не использовать 
    tag menu 
    add "bg/Classroom_41.jpg" 
    frame:  
        #Создаем площадь где будет находиться текст, два последних параметра это ширина и высота. 
        area (10,0,800,540)  
        #Делаем вертикальную полосу прокрутки 
        viewport mousewheel True draggable True scrollbars "vertical": 
            has vbox 
            text _("{color=#333333}Краткая информация об игре:{/color}")
            #С помощью этой функции мы опускаем следующий текст на 5 пикселей. 
            null height 5 
            $ fulltext = "{color=#555555}"
            $ fulltext +=__("Эта игра посвящена одному дню из жизни переводчика манги. События и персонажи имеют отношение к реально существующей команде, но все факты жесточайшим образом преувеличены или извращены.\n")
            $ fulltext +=__("Больше информации можно найти в титрах после прохождения игры или на сайте:\n")
            $ fulltext +=__("{a=http://OneMangaDay.dexp.in}http://OneMangaDay.dexp.in{/a}\n")
            $ fulltext +=__("\n")
            $ fulltext +=__("Игра сделана на движке {b}Ren'Py{/b}. Информацию о Ren'Py и о его авторах можно найти на сайте: {a=http://renpy.org}http://www.renpy.org{/a}\n")
            $ fulltext +=__("\n")
            $ fulltext +=__("Графика сделана в {a=http://www.comipo.com/en/}Manga Maker ComiPo!{/a}, с использованием {a=http://gimp.org}GIMP{/a}.\n")
            $ fulltext +=__("Музыка сделана в программе {a=http://magix.com}MAGIX Music Maker 2014{/a}.\n")
            $ fulltext +=__("\n")
            $ fulltext +=__("Звуковые эффекты взяты с сайта {a=http://freesound.org/}http://freesound.org{/a}. Особая благодарность {a=http://www.freesound.org/people/MadamVicious/}MadamVicious{/a} и {a=https://www.freesound.org/people/ecfike/}ecfike{/a} за их прекрасные голоса.\n")
            $ fulltext +=__("\n")
            $ fulltext +=__("Игра выполнена в рамках {a=http://contest.rpgmakerweb.com/}2014 Indie Game Maker Contest{/a}\n")
            $ fulltext +=__("(с) Все права защищены. {a=http://dexp.in}DeXPeriX{/a}, июнь 2014")
            $ fulltext += "{/color}"
            text["[fulltext]"]
            #$ ss = [__("{color=#555555}Эта игра посвящена одному дню из жизни переводчика манги. События и персонажи имеют отношение к реально существующей команде, но все факты жесточайшим образом преувеличены или извращены.\n"
            #     "Больше информации можно найти в титрах после прохождения игры или на сайте:\n"
            #     "{a=http://OneMangaDay.dexp.in}http://OneMangaDay.dexp.in{/a}\n"
            #     "\n"
            #     "Игра сделана на движке {b}Ren'Py{/b}. Информацию о Ren'Py и о его авторах можно найти на сайте: {a=http://renpy.org}http://www.renpy.org/{/a}\n"
            #     "\n"
            #     "Графика сделана в {a=http://www.comipo.com/en/}Manga Maker ComiPo!{/a}, с использованием {a=http://gimp.org}GIMP{/a}.\n"
            #     "Музыка сделана в программе {a=http://magix.com}MAGIX Music Maker 2014{/a}.\n"
            #     "\n"
            #     "Звуковые эффекты взяты с сайта {a=http://freesound.org/}http://freesound.org{/a}. Особая благодарность {a=http://www.freesound.org/people/MadamVicious/}MadamVicious{/a} и {a=https://www.freesound.org/people/ecfike/}ecfike{/a} за их прекрасные голоса.\n"
            #     "\n"
            #     "Игра выполнена в рамках {a=http://contest.rpgmakerweb.com/}2014 Indie Game Maker Contest{/a}\n"
            #     "(с) Все права защищены. {a=http://dexp.in}DeXPeriX{/a}, июнь 2014{/color}")]
    #Здесь создается ссылка на главное меню 
    frame: 
        style_group "mm" 
        xalign .98 
        yalign .98 

        has vbox 

        textbutton _("Вернуться") action Return()
        #textbutton "Главное меню" action ShowMenu("main_menu")
        
        

##############################################################################
# Navigation
#
# Экран, включаемый в другие экраны для отображения навигации и фона.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Фон игрового меню.
    window:
        style "gm_root"

    # Кнопки.
    frame:
        style_group "mm"
        xalign .98
        yalign .98

        has vbox
        
        grid 4 2:
            textbutton _("Вернуться") action Return()
            textbutton _("Главное меню") action MainMenu()
            textbutton _("Достижения") action ShowMenu("achievements")
            textbutton _("Помошь") action ShowMenu("help")
            textbutton _("Сохранить игру") action ShowMenu("save")
            textbutton _("Загрузить игру") action ShowMenu("load")
            textbutton _("Настройки") action ShowMenu("preferences")
            textbutton _("Выход") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"    



##############################################################################
# Achievements
screen achievements: 
    use navigation
    #С помощью этих двух функций мы меняем фон, add можно не использовать 
    tag menu 
    #add "bg/Classroom_41.jpg" 
        
    frame:  
        xalign 0.5
        style_group "ach"
        #style "file_picker_frame"
        #Создаем площадь где будет находиться текст, два последних параметра это ширина и высота. 
        #area (10,0,800,540)  
        #has vbox
        #hbox:
        #    text _(" {color=#113}{size=20}Достижения:{/size}{/color}")
            
        
        $ columns = 2
        $ rows = 6
        
        $ ach_tit = [__("Сканировщик"), __("Клинер"), __("Переводчик"), __("Корректор"), __("Тайпер"), __("Бэта-ридер"), __("Не устроиться на работу"), __("Потеряться в космосе"), __("Дожить до старости"), __("Общее фото"), __("Мастер раздевания"), __("Посмотреть на птичку")]
        $ ach_var = [persistent.beenScanner, persistent.beenCleaner, persistent.beenTranslator, persistent.beenProofreader, persistent.beenTyper, persistent.beenBetareader, persistent.bad1end, persistent.bad4end, persistent.shrineEnd, persistent.photoEnd, persistent.stripMaster, persistent.seeSeagul]
        $ ach_img = ["scanner.png", "cleaner.png", "translator.png", "proofreader.png", "typer.png", "betareader.png", "b1e.png", "b4e.jpg", "shrine.jpg", "photo.png", "linKrol.png", "seagul.png"]

        grid columns rows:
            transpose True
            xfill True
            #style_group "file_picker"
            style_group "ach"
            
            for i in range(0, columns * rows):
                $ curPic = "unk.png"
                $ state = __("Заблокировано")
                if ach_var[i]: 
                    $ curPic = ach_img[i]
                    $ state = __("Открыто")                   
                $ txt = ach_tit[i]
                $ pic = "items/ach/"+curPic
                
                if ach_var[i]: 
                    frame:
                        has hbox
                        #xfill True
                        add Image(pic)
                        text " {color=#333}\"[txt]\"\n  {size=20}[state]{/size}{/color}"
                else: 
                    button:
                        has hbox
                        #xfill True
                        add Image(pic)
                        text " \"[txt]\"\n  {size=20}[state]{/size}"
                

init -2 python:
    style.ach_button.size_group = "ach"
    style.ach_button.xmaximum = 465
    style.ach_button.xminimum = 465
       


##############################################################################
# Save, Load
#
# Экраны для сохранения и загрузки игры.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ибо сохранение и загрузка очень похожи, мы совмещаем их в один экран,
# file_picker. Потом мы используем его из экранов
# загрузки и сохранения.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # Кнопки сверху для выбора страницы.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Пред"):
                action FilePagePrevious()

            textbutton _("Авто"):
                action FilePage("auto")

            textbutton _("Быстро"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("След"):
                action FilePageNext()

        $ columns = 2
        $ rows = 6

        # Отобразить сетку файловых слотов.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Отобразить 10 слотов, с номерами от 1 до 10.
            for i in range(1, columns * rows + 1):

                # Каждый из них - кнопка.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Добавить скриншот.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Пустой Слот."))
                    $ save_name = FileSaveName(i)

                    text " [file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # Это заменяет другие меню.
    tag menu

    use navigation
    use file_picker

screen load:

    # Это заменяет другие меню.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)
    
    style.file_picker_nav_button.ymaximum = 47
    style.file_picker_nav_button.yminimum = 47
    
    style.file_picker_button.ymaximum = 47
    style.file_picker_button.yminimum = 47


##############################################################################
# Preferences
#
# Экран, позволяющий пользователю изменять настройки.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Включить навигацию.
    use navigation

    # Разместить навигационные колонки в сетку шириной 3.
    grid 3 1:
        style_group "prefs"
        xfill True

        # Левая колонка.
        vbox:
            if config.hw_video:
                frame:
                    style_group "pref"
                    has vbox
                    #label _("Озвучка")
                    if config.has_voice:
                        textbutton _("Отключить русскую озвучку") action Function(change_voiceover)
                    else:
                        textbutton _("Включить русскую озвучку") action Function(change_voiceover)
            if config.help != "android":  
                frame:
                    style_group "pref"
                    has vbox
                
                    label _("Отображение")
                    textbutton _("Окно") action Preference("display", "window")
                    textbutton _("Полный экран") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Переходы")
                textbutton _("Все") action Preference("transitions", "all")
                textbutton _("Никаких") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Скорость текста")
                bar value Preference("text speed")

            #if config.help != "android":
            #    frame:
            #        style_group "pref"
            #        has vbox
            #        textbutton _("Джойстик...") action Preference("joystick")
            


        vbox:
            frame:
                style_group "pref"
                has vbox

                #label _("Пропуск")
                textbutton _("Пропуск прочтенных") action Preference("skip", "seen")
                textbutton _("Пропуск всех") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Начать пропуск") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("После выборов")
                textbutton _("Остановить пропуск") action Preference("after choices", "stop")
                textbutton _("Продолжить пропуск") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Ускорить время")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Ждать голос") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Громкость музыки")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Громкость звука")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Тест"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Громкость голоса")
                    bar value Preference("voice volume")

                    textbutton _("Оставлять голос") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Тест"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
                            
            frame:
                style_group "pref"
                has vbox
                
                label _("Язык")
                textbutton "{image=items/flags/en.jpg} "+_("English   ") action Language("english")
                textbutton "{image=items/flags/ru.jpg} "+_("Русский") action Language(None)
                textbutton "{image=items/flags/pl.jpg} "+_("Polski     ") action Language("polish")
                

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0
    
    style.pref_button.ymaximum = 47
    style.pref_button.yminimum = 47

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0
    
init python:
    def change_voiceover():
        persistent.chose_voiceover = True
        if config.has_voice:
            config.has_voice = False
        else:
            config.has_voice = True
            


##############################################################################
# Yes/No Prompt
#
# Экран, спрашивающий у пользователя вопрос да/нет.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action yes_action
            textbutton _("Нет") action no_action

    # Правый щелчок и escape отвечают "нет".
    key "game_menu" action no_action

init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.layout = "subtitle"
    
    style.yesno_button.ymaximum = 47
    style.yesno_button.yminimum = 47


##############################################################################
# Quick Menu
#
# Экран, входящий в экран save и дающий некоторые полезные функции
screen quick_menu:

    # Быстрое внутриигровое меню.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Назад") action Rollback()
        textbutton _("Сохранить") action ShowMenu('save')
        textbutton _("Б.Сохр") action QuickSave()
        textbutton _("Б.Загр") action QuickLoad()
        textbutton _("Пропуск") action Skip()
        textbutton _("Б.Пропуск") action Skip(fast=True, confirm=True)
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Настр") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 16
    if config.help == "android": 
        style.quick_button_text.size = 20
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
