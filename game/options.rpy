## Этот файл содержит некоторые опции которые можно изменить для настройки
## вашей игры на Ren'Py. Он содержит только самые часто используемые настройки...
## Их на самом деле гораздо больше.
##
## Строки, начинающиеся с двух знаков '#' являются комментариями, и вы
## не должны их раскомментировать. Строки, начинающиеся с одного
## знака '#' являются закоментированным кодом, и вы можете их
## раскомментировать в подходящих вам ситуациях.

            
init -1 python hide:
    config.help = None
    #style.hyperlink_text.color = "#ddf"
    style.hyperlink_text.color = "#00d"
    style.hyperlink_text.hover_color = "#006"
    
    #config.thumbnail_height = 90
    #config.thumbnail_width = 160
    config.thumbnail_height = 54
    config.thumbnail_width = 96
    
    
    

    ## Включать ли нам инструменты разработчика? Здесь нужно
    ## поставить False перед выпуском игры, чтобы
    ## пользователь не смог мошенничать, используя эти инструменты.

    config.developer = True
    #config.help = "android"
    
    
    build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAim+nfSYGZfSiY+73iyXcx4ZTuFAiEt7tZjRIQQCNqyrFBvMQpiTV+oCweEKCfh8UHPpu9OXkMyLely0AnVUCUa0GzNUSZ3lVSYNw2IR1xl8AVtNgFu7XoAv5hA8JVAgsOElZAqvHyOzTm8Edu34ElB1ZtnaDolVfHvFmbKFtQf1ZRhzcoFsAV5KFyKHmdgfRFyZ/mHZXGPAyNe4Uuo7pfLjs7mXNTt34V5KURlLeRMF+ECQRblQ49yZxh/EayQwXhSAMh9vY7Tam49KEkV+8rQoQnu32Yj/PPtCMxTquH/+iUUM9KMYRFptAK0F2xoDIb+CW95gtVKWHbfFMP0+9+QIDAQAB"
    
    
    if config.help != "android":
        config.mouse = { 'default' : [ ('mouse.png', 0, 0)] }
    config.default_language = "english"
    
    
    ## Эти управляют шириной и высотой экрана.

    config.screen_width = 960
    config.screen_height = 540

    ## Это управляет заголовком окна, когда Ren'Py
    ## запущен в оконном режиме.

    config.window_title = u"OneMangaDay"

    # Эти управляют именем и версией игры, которые указываются
    # в журналах отладки.
    config.name = "OneMangaDay"
    config.version = "1.02"

    #########################################
    # Темы

    ## Затем, мы захотим вызвать функцию темы. theme.roundrect
    ## это тема, поддерживающая круглые прямоугольники.
    ##
    ## Функция темы берет несколько параметров, которые
    ## настраивают цветовую схему.


    theme.marker(
        ## Theme: Marker
        ## Color scheme: Cotton Candy

        ## The color of an idle widget face.
        widget = "#ECC7D0",

        ## The color of a focused widget face.
        widget_hover = "#E1D4C9",

        ## The color of the text in a widget.
        widget_text = "#805C40",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#805C40",

        ## The color of a disabled widget face.
        disabled = "#C8AFA1",

        ## The color of disabled widget text.
        disabled_text = "#E1D4C9",

        ## The color of informational labels.
        label = "#805C40",

        ## The color of a frame containing widgets.
        frame = "#FCF5F2",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.        
        mm_root=Fixed(
        #Image("bg/River_65.jpg"),
        Image("bg/Schoolyard_mm.jpg"),
        Image("items/Sunshine.png", xalign=1.12, yalign=-0.3),
        Image("items/Manga.png", xalign=0.01, yalign=0.75),
        anim.Blink( Image("bg/Branch_Cherry4_mm.png"), high=1.0, low=0.8 ),
        #Transform( Image("bg/Branch_Cherry4_mm.png"), rotate=30, delay=10000.0 ),
        #Animation("bg/Branch_Cherry4_2_mm.png", 1.5,
        #        "bg/Branch_Cherry4_mm.png", 1.5),
        SnowBlossom("bg/particle/sak2.png", count=7, xspeed=(15, 40), yspeed=(80, 160), start=0, border=80),
        
        Animation("pers/gol/g1.png", 0.6,
                "pers/gol/g3.png", 0.15,
                "pers/gol/g2.png", 1.1,
                "pers/gol/g3.png", 0.05
                ),
        Image("items/Gate1.png", xalign=1.0, yalign=0.53),
        Image("bg/team_mm3.png", xalign=0.35, yalign=1.0),
        Animation("pers/face/t.png", 1,
                "pers/face/lyba_eye_wink.png", 2),
        #SnowBlossom("bg/Petal_01.png", count=2, xspeed=(10, 30), yspeed=(50, 70), start=1),
        SnowBlossom("bg/particle/sak1.png", count=2, xspeed=(30, 60), yspeed=(150, 250), start=0, border=80),
        SnowBlossom( Animation("bg/particle/sak2.png", 0.5, "bg/particle/sak3.png", 0.5) , count=5, xspeed=(20, 50), yspeed=(100, 200), start=0, border=80),
        #Image( __("bg/Title.png"), xalign=0.9, yalign=0.025)
        #Animation("bg/Title.png", 1.5,
        #        Transform( Image("bg/Title.png"), zoom=1.1 ), 0.5),
        ),

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        #gm_root = "#b0b8ba",
        gm_root = "bg/Classroom_41.jpg",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )

    config.window_icon = "icon.png"

    #########################################
    ## Эти настройки позволяют вам настроить окно,
    ## содержащее диалоги и текст "от автора", замещая его
    ## изображением.

    ## Фон окна. В Frame, числа символизируют размер
    ## левого/правого и верхнего/нижнего бордюров
    ## соответственно.

    # style.window.background = Frame("frame.png", 12, 12)

    ## Внешние поля - пространство, окружающее окно, на котором
    ## не рисуется фон.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Внутренние поля - пространство внутри окна, где
    ## рисуется фон.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Это минимальная высота окна, включая поля.

    # style.window.yminimum = 250


    #########################################
    ## Это позволит вам изменить расположение главного меню.

    ## Это работает так: мы находим точку-якорь внутри
    ## объекта и точку позиции (pos) на экране.
    ## Затем, мы размещаем объект так, чтобы эти точки совпадали.

    ## Якорь/pos можно задавать как целое или действительное число.
    ## Если целое, оно принимается как кол-во пикселей от
    ## левого верхнего угла. Если действительное, число
    ## принимается как доля размера объекта или экрана.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Это позволяет настроить шрифт текста в Ren'Py.

    ## Файл, содержащий шрифт.

    # style.default.font = "DejaVuSans.ttf"

    ## Размер текста по умолчанию.

    style.default.size = 24

    ## Заметьте, что это изменит стиль лишь некоторого
    ## текста. У других кнопок свои стили.


    #########################################
    ## Эти настройки позволят изменить некоторые звуки
    ## Ren'Py.

    ## Установите False если в игре нет звуковых эффектов.

    config.has_sound = True

    ## Установите False если в игре нет музыки.

    config.has_music = True

    ## Установите True если в игре есть озвучка. 

    config.has_voice = False
    #config.has_voice = True
    #config.auto_voice = "voice/ru/{id}.wav"

    ## Звуки при нажатии на кнопки и imagemap-ы.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Звуки при входе и выходе из игрового меню.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук для проверки громкости.

    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.

    #config.main_menu_music = "Music/Neophyt_-_The_Day_You_Left.mp3"
    #config.main_menu_music = "Music/Juanitos_-_El_Loco_Boogaloo.mp3"
    #config.main_menu_music = "Music/Merl_Beatz_-_A_soir_on_fuck___instrumental.mp3"
    #config.main_menu_music = "Music/Alterlabel_-_ABELCOAST_-_Full_Fun.ogg"
    config.main_menu_music = "Music/PopRock3.OGG"


    #########################################
    ## Справка.

    ## Это позволит настроить опцию справки в меню Ren'Py.
    ## Это могут быть:
    ## - Метка в сценарии. В этом случае эта метка вызывается
    ##   для показа помощи.
    ## - Имя файла отнсоительно основной директории.
    ##   Он будет открыт в веб-браузере.
    ## None. Помощь будет выключена.
    #config.help = "README.html"
    #config.help = None


    #########################################
    ## Переходы.

    ## Используется при входе в игровое меню.
    config.enter_transition = None

    ## Используется при выходе из игрвого меню.
    config.exit_transition = None

    ## Используется между экранами игрового меню.
    config.intra_transition = None

    ## Используется при входе в игровое меню из главного.
    config.main_game_transition = None

    ## Используется при возвращении в главное меню из игры.
    config.game_main_transition = None

    ## Используется при переходе в главное меню из окна загрузки.
    config.end_splash_transition = None

    ## Используется при переходе в главное меню после окончания игры.
    config.end_game_transition = None

    ## Используется при загрузке игры.
    config.after_load_transition = None

    ## Используется при отображении окна.
    config.window_show_transition = None

    ## Используется при скрытии окна.
    config.window_hide_transition = None

    ## Используется при переходе в режим NVL сразу после режима ADV.
    config.adv_nvl_transition = dissolve

    ## Используется при переходе в режим ADV сразу после режима NVL.
    config.nvl_adv_transition = dissolve

    ## Используется при отображении yesno.
    config.enter_yesno_transition = None

    ## Используется при скрытии yesno.
    config.exit_yesno_transition = None

    ## Используется при входе в реплей.
    config.enter_replay_transition = None

    ## Используется при выходе из реплея.
    config.exit_replay_transition = None

    ## Используется при изменении изображения с помощью "say" с изобразительными атрибутами.
    config.say_attribute_transition = None

    #########################################
    ## Имя директории, где хранятся данные игры.
    ## (это необходимо задать рано, чтобы постоянная информация могла быть 
    ## найдена на стадии инициализации.)
python early:
    config.save_directory = "OneMangaDay-1395841743"

init -1 python hide:
    #########################################
    ## Стандартные значения настроек.

    ## Эти опции используются лишь при первом запуске игры.
    ## Чтобы применить их снова, удалите game/saves/persistent.

    ## Запустить в полноэкранном режиме?

    config.default_fullscreen = True

    ## Скорость текста по умолчанию, в знаках в секунду. 0 - бесконечность.

    config.default_text_cps = 0

    ## Время авто-режима по умолчанию.

    config.default_afm_time = 10

    #########################################
    ## Остальные настройки могут быть ниже.
    


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "OneMangaDay-1.02"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "OneMangaDay"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/Music/*.OGG', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    