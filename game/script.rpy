init python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)
    



image bg EmptyClass42 = "bg/EmptyClass42.jpg"
image bg Classroom49 = "bg/Classroom_49.jpg"
image bg Classroom44 = "bg/Classroom_44.jpg"
image bg Forest41 = "bg/Forest_g41.jpg"
image bg Hallway1 = "bg/hallway1.jpg"
image bg Hallway41 = "bg/Hallway41.jpg"
image bg HallwayClean = "bg/HallwayClean.jpg"
image bg Shop = "bg/Shop.jpg"
image bg TeachersRoom = "bg/TeachersRoom.jpg"
image bg Office = "bg/Office.jpg"
image bg Storage = "bg/Storage2.jpg"
image bg Roof = "bg/Roof.jpg"
image bg RoofNight = "bg/RoofNight.jpg"
image bg Schoolyard = "bg/Schoolyard_mm.jpg"
image bg SchoolyardNight = "bg/SchoolyardNight.jpg"
image bg Dinning1 = "bg/Dinning1.jpg"
image bg Dinning2 = "bg/Dinning2.jpg"
image bg DinningNight = "bg/DinningNight.jpg"
image bg Doska = "bg/Doska.jpg"
image bg HomeDoorNight = "bg/HomeDoorNight.jpg"
image bg HomeCorridor = "bg/HomeCorridor.jpg"
image bg ChurchDream = "bg/ChurchDream.jpg"
image bg SeaDream = "bg/SeaDream.jpg"
image bg DeXPRoom = "bg/DeXPRoom.jpg"
image bg MalaRoom = "bg/MalaRoom.jpg"
image bg Residential_city = "bg/Residential_city.jpg"
image bg Residential_gop = "bg/Residential_gop.jpg"
image bg ShoeLocker = "bg/ShoeLocker.jpg"
image bg Staircase = "bg/Staircase.jpg"
image bg Park = "bg/Park.jpg"
image bg Park2 = "bg/Park2.jpg"
image bg Shrine = "bg/Shrine.jpg"


#image bg Stars = "bg/Stars2.jpg"
image bg Stars = Fixed(
    Image("bg/Stars2.jpg"),
    anim.Blink( Image("bg/StarMask.png"), high=0.7, low=0.1 ),
    anim.Blink( Image("items/Star2.png"), high=1.0, low=0.5 ),
    #anim.Blink( Image("items/Star1.png", xalign=0.5, yalign=0.75), high=1.0, low=0.6 ),
)


image dragonWingLeft22:
    "items/DragonWing2.png"
    subpixel True  
    parallel:
        rotate 0
        linear 0.5 rotate 20
        linear 0.5 rotate 0
        repeat
        
image VetkaSakury:
    "bg/Branch_Cherry.png"
    xalign -0.1 yalign 0.0
    subpixel True
    rotate 0
    linear 2 rotate 2
    linear 2 rotate 0
    repeat

image bg SchoolDay = Fixed(
        Image("bg/Schoolyard_mm.jpg"),
        Image("items/Sunshine.png", xalign=1.12, yalign=-0.3),
        Image("items/Manga.png", xalign=0.01, yalign=0.75),
        anim.Blink( Image("bg/Branch_Cherry4_mm.png"), high=1.0, low=0.8 ),
        Image("items/Gate1.png", xalign=1.0, yalign=0.53),
        )


image bg SchoolDaySakura = LiveComposite(
    (960,540),
    (0,0), "bg/Schoolyard_mm.jpg",
    (625,0), anim.Blink( Image("items/Sunshine.png"), high=1.0, low=0.9),
    (40,300), "items/Manga.png",
        #anim.Blink( Image("bg/Branch_Cherry4_mm.png"), high=1.0, low=0.8 ),
    (-370,-320), "VetkaSakury",
    (0,0), SnowBlossom("bg/particle/sak2.png", count=7, xspeed=(15, 40), yspeed=(80, 160), start=0, border=80),
    (691,206), "items/Gate1.png",
    (0,0), SnowBlossom("bg/particle/sak1.png", count=2, xspeed=(30, 60), yspeed=(150, 250), start=0, border=80),
    (0,0), SnowBlossom( Animation("bg/particle/sak2.png", 0.5, "bg/particle/sak3.png", 0.5) , count=5, xspeed=(20, 50), yspeed=(100, 200), start=0, border=80),
        )
image addSakura = SnowBlossom("bg/particle/sak1.png", count=2, xspeed=(30, 60), yspeed=(150, 250), start=0, border=80)


image bg SchoolRain = Fixed(
        Image("bg/Schoolyard_mm.jpg"),
        Image("bg/Branch_Cherry4_mm.png"),
        Image("items/Gate1.png", xalign=1.0, yalign=0.53),
        Animation("bg/Rain1.png", 0.075,
                "bg/Rain2.png", 0.075,
                "bg/Rain3.png", 0.075)
        )

image bg Disko1 = "bg/Disko1.jpg"
image bg Disko = Animation("bg/Disko1.jpg", 0.4,
                "bg/Disko2.jpg", 0.4,
                "bg/Disko3.jpg", 0.4,)
image bg DiskoFade:
    "bg/Disko1.jpg" with Dissolve(.1)
    pause .4
    "bg/Disko3.jpg" with Dissolve(.1)
    pause .4
    "bg/Disko2.jpg" with Dissolve(.1)
    pause .4
    repeat

image bg DiskoStage:
    "bg/DiskoStage1.jpg" with Dissolve(.1)
    pause .4
    "bg/DiskoStage2.jpg" with Dissolve(.1)
    pause .4
    repeat





#image white = "bg/white.png"
image white = Solid("#fff")
image Add3D = "items/Add3D.png"
#image Box = "items/Box.png"
image Shtab = "items/Shtab.png"
image Sunshine = "items/Sunshine.png"
image Smoke2 = "items/Smoke2.png"
image Explosion = "items/Explosion.png"
image Lantern = "items/Lantern.png"
image Cracker = "items/Cracker.png"
image Flags = "items/Flags.png"
image Server = "items/Server.png"
image ServerFlip = im.Flip("items/Server.png", horizontal=True)
image Binocle = "items/Binocle.png"
image BinocularMask = "items/BinocularMask.png"
image StarShip = "items/StarShip.png"
image Bench = "items/Bench.png"
image BranchTopLeft = "items/BranchTopLeft.png"
image Kust = "items/Kust.png"
image C4 = "items/C4.png"
image BentoBox = "items/BentoBox.png"
image Freezer = "items/Freezer.png"
image ChairPink = "items/ChairPink.png"
image Sweat = "items/Sweat.png"
image Punch = "items/Punch.png"
image TopCrack = "bg/topCrack.png"
image Question = "items/Question.png"
image Anger = "items/Anger.png"
image Manga = "items/Manga.png"
image Book = "items/Book.png"
image BookLay = "items/BookLay.png"
#image Seagul = "items/Seagul.png"
#image Seagul:
#    "items/Seagul.png" with Dissolve(.1)
#    pause .4
#    "items/Seagul2.png" with Dissolve(.1)
#    pause .4
image Seagul = Animation("items/Seagul.png", 0.4, "items/Seagul2.png", 0.4)
image SeagulStatic = "items/Seagul.png"
image SeagulShock = LiveComposite(
    (177, 95),
    (0, 0), "items/Seagul.png",
    (140, 28), Image("items/O.png")
    )
image SeagulShockFlip = LiveComposite(
    (177, 95),
    (0, 0), im.Flip("items/Seagul.png", horizontal=True),
    (20, 28), Image("items/O.png")
    )

image dexpSeaAngryMouth = "pers/face/dexp_sea_angry_mouth.png"
image dexpSeaEvil = "pers/face/dexp_sea_evil.png"
image linMouthStern = "pers/face/lin_mouth_stern.png"
image lybaMouthOpen = "pers/face/lyba_mouth_open.png"




#Scan
image cis1 = "scan/cis1.jpg"
image cdd1 = "scan/cdd1.jpg"

image cis2 = "scan/cis2.jpg"
image cdd2 = "scan/cdd2.jpg"

image cis3 = "scan/cis3.jpg"
image cdd3 = "scan/cdd3.jpg"

#Type
image type_good = "type/good.png"
image type_bad  = "type/bad.png"
image type_china= "type/chinac2.png"

#Klin
image klin0 = "klin/cdd2-0.jpg"
image klin_dark = "klin/cdd2-dark.jpg"
image klin_light = "klin/cdd2-light.jpg"
image klin_overlevel = "klin/cdd2-overlevel.jpg"



    
    
# Acievements system    
image Strate = "items/ach/Strate.png"
image b1eAch = "items/ach/b1e.png"
image b4eAch = "items/ach/b4e.jpg"
image photoAch = "items/ach/photo.png"
image shrineAch = "items/ach/shrine.jpg"
image stripMasterAch = "items/ach/linKrol.png"
image seeSeagulAch = "items/ach/seagul.png"
image scannerAch = "items/ach/scanner.png"
image cleanerAch = "items/ach/cleaner.png"
image translatorAch = "items/ach/translator.png"
image proofreaderAch = "items/ach/proofreader.png"
image typerAch = "items/ach/typer.png"
image betareaderAch =  "items/ach/betareader.png"

#$achievement.register("b1e")
#$achievement.register("b4e")
#$achievement.register("photo")
#$achievement.register("shrine")
#$achievement.register("stripMaster")
#$achievement.register("seeSeagul")
#$achievement.register("scanner")
#$achievement.register("cleaner")
#$achievement.register("translator")
#$achievement.register("proofreader")
#$achievement.register("typer")
#$achievement.register("betareader")

transform achieveanim:
    #xalign 1.0  yalign 0.0 alpha 0.0
    easeout 0.5 alpha 1.0
    2.5 # Pause
    linear 3.0 alpha 0.0
    
label showAchiv:
    show Strate at achieveanim with dissolve:
        xalign 1.0 yalign 0.0
    #show arcImgImg at achieveanim:
    #    xalign 0.52  yalign 0.025
    if achId == "b1e":
        show b1eAch at achieveanim:
            xalign 0.52  yalign 0.025    
    if achId == "b4e":
        show b4eAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "photo":
        show photoAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "shrine":
        show shrineAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "stripMaster":
        show stripMasterAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "seeSeagul":
        show seeSeagulAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "scanner":
        show scannerAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "cleaner":
        show cleanerAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "translator":
        show translatorAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "proofreader":
        show proofreaderAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "typer":
        show typerAch at achieveanim:
            xalign 0.52  yalign 0.025 
    if achId == "betareader":
        show betareaderAch at achieveanim:
            xalign 0.52  yalign 0.025 
    $achievement.grant(achId)
    show text "[achievementUlocked]\n[achText]" at achieveanim with dissolve:
        xanchor 0.0 yanchor 0.0
        xpos 560 ypos 10
    return




# Определение персонажей игры.
define dexp = Character(_('Дэкс'), color="#999999", image="dexp", window_left_padding=185)
image dexp norm = "pers/dexp_norm.png"
image side dexp norm = "pers/dexp_side_norm.png"
image dexp fly = "pers/dexp_fly.png"
image side dexp fly = "pers/dexp_side_norm.png"
image dexp laugh = "pers/dexp_happy.png"
image side dexp laugh = "pers/dexp_side_joy.png"
image dexp nya = "pers/dexp_nya.png"
image side dexp nya = "pers/dexp_side_joy.png"
image dexp think = "pers/dexp_think.png"
image side dexp think = "pers/dexp_side_think.png"
image dexp angry = "pers/dexp_angry.png"
image side dexp angry = "pers/dexp_side_angry.png"

image dexp joybig = "pers/dexp_joy_big.png"
image side dexp joybig = "pers/dexp_side_joy.png"
image dexp fearbig = "pers/dexp_fear_big.png"
image side dexp fearbig = "pers/dexp_side_fear.png"
image dexp fearbigflip = im.Flip("pers/dexp_fear_big.png", horizontal=True)
image side dexp fearbigflip = "pers/dexp_side_fear.png"
image dexp thinkbig = "pers/dexp_think_big.png"
image side dexp thinkbig = "pers/dexp_side_think.png"
image dexp thinkbigflip = im.Flip("pers/dexp_think_big.png", horizontal=True)

image dexp maikasad = "pers/dexp_maika_sad.png"
image side dexp maikasad = "pers/dexp_side_maika_sad.png"
image dexp dreambeach  = "pers/dexp_norm.png"
image side dexp dreambeach = "pers/side_smile.png"
image dexp maikasurprised ="pers/dexp_maika_surprised.png"
image side dexp maikasurprised = "pers/dexp_side_maika_sad.png"

image dexp happykust = im.Crop("pers/dexp_happy.png", 175, 30, 200, 390)
image side dexp happykust = "pers/dexp_side_joy.png"

image dexp normhalf = "pers/dexp_norm_half.png"
image side dexp normhalf = "pers/dexp_side_norm.png"



define ded = Character(_('Дэкс'), color="#999999", image="ded", window_left_padding=165)
image ded norm = "pers/ded_norm.png"
image side ded norm = "pers/ded_side_norm.png"
image ded think = "pers/ded_think.png"
image side ded think = "pers/ded_side_norm.png"
image ded echi = "pers/ded_echi.png"
image side ded echi = "pers/ded_side_echi.png"
image ded echiflip = im.Flip("pers/ded_echi.png", horizontal=True)
image side ded echiflip = "pers/ded_side_echi.png"



define lap = Character(_('Лап'), color="#e4c860", image="lap", window_left_padding=160)
image lap norm = "pers/lap_norm.png"
image side lap norm = "pers/lap_side_norm.png"
image lap joy = "pers/lap_joy.png"
image side lap joy = "pers/lap_side_norm.png"
image lap angry = "pers/lap_angry.png"
image side lap angry = "pers/lap_side_angry.png"
image lap fight = "pers/lap_fight.png"
image side lap fight = "pers/lap_side_angry.png"
image lap surprized = "pers/lap_surprized.png"
image side lap surprized = "pers/lap_side_question.png"
image lap bigquestion = "pers/lap_question_big.png"
image side lap bigquestion = "pers/lap_side_question.png"
image lap bigqflip = im.Flip("pers/lap_question_big.png", horizontal=True)
image side lap bigqflip = "pers/lap_side_question.png"
image lap titles =  im.FactorScale(im.Flip("pers/lap_question_big.png", horizontal=True), 0.9)
image lap bride = "pers/lap_bride.png"
image side lap bride = "pers/lap_joy.png"
image lap sleepy = "pers/lap_sleepy.png"
image side lap sleepy = "pers/lap_side_sleepy.png"
image lap sexytort = "pers/lap_tort.png"
image side lap sexytort = "pers/lap_side_sexy.png"
image lap liedown = Transform( Image("pers/lap_angry.png"), rotate=80)
image side lap liedown = "pers/lap_side_angry.png"
image lap normhalf = "pers/lap_norm_half.png"
image side lap normhalf = "pers/lap_side_norm.png"
image lap angryhalf = "pers/lap_angry_half.png"
image side lap angryhalf = "pers/lap_side_angry.png"

image lap cosmo = LiveComposite(
    (530, 530),
    (0, 0), "pers/lap_norm.png",
    (181, 13), Image("items/KosmoShlem.png")
    )
image side lap cosmo = "pers/lap_side_norm.png"

image lap cosmoangry = LiveComposite(
    (530, 530),
    (0, 0), "pers/lap_angry.png",
    (182, 10), Image("items/KosmoShlem.png")
    )
image side lap cosmoangry = "pers/lap_side_angry.png"


define bab = Character(_('Лап'), color="#e4c860", image="bab", window_left_padding=145)
image bab norm = "pers/bab_norm.png"
image side bab norm = "pers/bab_side_norm.png"
image bab angry = "pers/bab_angry.png"
image side bab angry = "pers/bab_side_angry.png"
image bab fight = "pers/bab_fight.png"
image side bab fight = "pers/bab_side_angry.png"
image bab smile = LiveComposite(
    (537, 514),
    (0, 0), "pers/bab_norm.png",
    (279, 112), "pers/face/bab_smile.png"
    )
image side bab smile = LiveComposite(
    (149, 178),
    (0, 0), "pers/bab_side_norm.png",
    (60, 90), "pers/face/lyba_mouth_open.png"
    )



define andry = Character(_('Андрэ'), color="#708384", image="andry", window_left_padding=155)
image andry norm = "pers/andry_lookleft.png"
image side andry norm = "pers/andry_side_norm.png"
image andry shy = "pers/andry_shy.png"
image side andry shy = "pers/andry_side_norm.png"
image andry fight = "pers/andry_fight.png"
image side andry fight = "pers/andry_side_angry.png"
image andry fightflip = im.Flip("pers/andry_fight.png", horizontal=True)
image side andry fightflip = "pers/andry_side_angry.png"
image andry chem = "pers/andry_chem.png"
image side andry chem = "pers/andry_side_funny.png"
image andry ice = "pers/andry_ice.png"
image side andry ice = "pers/andry_side_funny.png"
image andry bita = "pers/andry_bita.png"
image side andry bita = "pers/andry_side_norm.png"
image andry liedown = Transform( Image("pers/andry_fight.png"), rotate=-100)
image side andry liedown = "pers/andry_fight.png"


define lin = Character(_('Лин'), color="#e85859", image="lin", window_left_padding=135)
image lin normbig = "pers/lin_norm_big.png"
image side lin normbig = "pers/lin_side_norm.png"
image lin norm = "pers/lin_norm.png"
image side lin norm = "pers/lin_side_norm.png"
image lin angry = "pers/lin_angry.png"
image side lin angry = "pers/lin_side_angry.png"
image lin angrybig = "pers/lin_angry_big.png"
image side lin angrybig = "pers/lin_side_angry.png"
image lin laughbig = "pers/lin_laugh_big.png"
image side lin laughbig = "pers/lin_side_norm.png"
image lin laugh = "pers/lin_laugh.png"
image side lin laugh = "pers/lin_side_norm.png"
image lin bride = "pers/lin_bride.png"
image lin sexytort = "pers/lin_tort.png"
image side lin sexytort = "pers/lin_side_sexy.png"
image lin leto = "pers/lin_leto.png"
image side lin leto = "pers/lin_side_leto.png"
image lin sexy = "pers/lin_sexy.png"
image side lin sexy = "pers/lin_side_sexy.png"
image lin swim = "pers/lin_swim.png"
image side lin swim = "pers/lin_side_swim.png"
image lin swimsad = LiveComposite(
    (499, 499),
    (0, 0), "pers/lin_swim.png",
    (226, 119), Image("pers/face/lin_swim_eye.png"),
    (244, 140), Image("pers/face/lin_mouth_stern.png")
    )
image side lin swimsad = LiveComposite(
    (127, 244),
    (0, 0), "pers/lin_side_norm.png",
    (57, 137), Image("pers/face/lin_mouth_stern.png")
    )
image lin sad = LiveComposite(
    (562, 563),
    (0, 0), "pers/lin_norm.png",
    (274, 135), Image("pers/face/lin_mouth_closed.png")
    )
image side lin sad = LiveComposite(
    (127, 244),
    (0, 0), "pers/lin_side_norm.png",
    (57, 137), Image("pers/face/lin_mouth_closed.png")
    )



define lexa = Character(_('Лёха'), color="#f6cd61", image="lexa", window_left_padding=135)
image lexa norm = "pers/lexa_norm.png"
image side lexa norm = "pers/lexa_side_norm.png"
image lexa attention = "pers/lexa_attention.png"
image side lexa attention = "pers/lexa_side_norm.png"
image lexa lookdown = "pers/lexa_lookdown.png"
image side lexa lookdown = "pers/lexa_side_norm.png"
image lexa lookdownflip = im.Flip("pers/lexa_lookdown.png", horizontal=True)
image side lexa lookdownflip = "pers/lexa_side_norm.png"
image lexa bride = "pers/lexa_bride.png"
image side lexa bride = "pers/lexa_side_bride.png"
image lexa sit = "pers/lexa_sit.png"
image side lexa sit = "pers/lexa_side_norm.png"



define yana = Character(_('Янушка'), color="#718382", image="yana", window_left_padding=145)
image yana norm = "pers/yana_norm.png"
image side yana norm = "pers/yana_side_question.png"
image yana angry = "pers/yana_angry.png"
image side yana angry = "pers/yana_side_question.png"
image yana questionbig = "pers/yana_question_big.png"
image side yana questionbig = "pers/yana_side_question.png"
image yana down = "pers/yana_down.png"
image side yana down = "pers/yana_side_down.png"
image yana down2 = "pers/yana_down2.png"
image side yana down2 = "pers/yana_side_down.png"
image yana downhappy = LiveComposite(
    (535, 541),
    (0, 0), "pers/yana_down2.png",
    (267, 125), Image("pers/face/yana_happy.png"),
    )
image side yana downhappy = "pers/yana_side_question.png"


define mirei = Character(_('Мирей'), color="#f3964f", image="mirei", window_left_padding=135)
image mirei norm = "pers/mirei_norm.png"
image side mirei norm = "pers/mirei_side_norm.png"


define mala = Character(_('Маля'), color="#76e2e4", image="mala", window_left_padding=175)
image mala norm = "pers/mala_norm.png"
image side mala norm = "pers/mala_side_norm.png"
image mala work = "pers/mala_work.png"
image side mala work = "pers/mala_side_work.png"
image mala homework = "pers/mala_homework.png"
image side mala homework = "pers/mala_side_homework.png"
image mala homework2 = "pers/mala_homework2.png"
image side mala homework2 = "pers/mala_side_homework.png"
image mala angry = "pers/mala_angry.png"
image side mala angry = "pers/mala_side_angry.png"
image mala angrybig = "pers/mala_angry_big.png"
image side mala angrybig = "pers/mala_side_angry.png"
image mala angrybigflip = im.Flip("pers/mala_angry_big.png", horizontal=True)
image side mala angrybigflip = "pers/mala_side_angry.png"
image mala sit = "pers/mala_sit.png"
image side mala sit = "pers/mala_side_norm.png"


define azyki = Character(_('Азуки'), color="#aa7084", image="azyki", window_left_padding=145)
image azyki norm = "pers/azyki_norm.png"
image side azyki norm = "pers/azyki_side_norm.png"
image azyki laugh = "pers/azyki_laugh.png"
image side azyki laugh = "pers/azyki_side_norm.png"
image azyki surprized = "pers/azyki_surprized.png"
image side azyki surprized = "pers/azyki_side_surprized.png"
image azyki angry = "pers/azyki_angry.png"
image side azyki angry = "pers/azyki_side_angry.png"


define prana = Character(_('Пряня'), color="#db7f1e", image="prana", window_left_padding=135)
image prana norm = "pers/prana_norm.png"
image side prana norm = "pers/prana_side_norm.png"
image prana clouds = "pers/prana_clouds.png"
image side prana clouds = "pers/prana_side_attention.png"
image prana neko = "pers/prana_neko.png"
image side prana neko = "pers/prana_side_neko.png"


define carry = Character(_('Кэрри'), color="#ffbeef", image="carry", window_left_padding=125)
image carry norm = "pers/carry_norm.png"
image side carry norm = "pers/carry_side_norm.png"
image carry normflip = im.Flip("pers/carry_norm.png", horizontal=True)
image side carry normflip = "pers/carry_side_norm.png"
image carry fear = "pers/carry_fear.png"
image side carry fear = "pers/carry_side_fear.png"
image carry question = "pers/carry_question.png"
image side carry question = "pers/carry_side_question.png"
image carry surprised = "pers/carry_surprised.png"
image side carry surprised = "pers/carry_side_surprised.png"
image carry sitdown = "pers/carry_sitdown.png"
image side carry sitdown = "pers/carry_side_norm.png"
image carry spy = "pers/carry_spy.png"
image side carry spy = "pers/carry_side_spy.png"
image carry flipnorm = im.Flip("pers/carry_norm.png", horizontal=True)
image side carry flipnorm = "pers/carry_side_norm.png"


define ulilla = Character(_('Юлилла'), color="#c8f6aa", image="ulilla", window_left_padding=165)
image ulilla norm = "pers/ulilla_norm.png"
image side ulilla norm = "pers/ulilla_side_norm.png"
image ulilla joy = "pers/ulilla_joy.png"
image side ulilla joy = "pers/ulilla_side_joy.png"
image ulilla go = "pers/ulilla_go.png"
image side ulilla go = "pers/ulilla_side_norm.png"
image ulilla angry = "pers/ulilla_angry.png"
image side ulilla angry = "pers/ulilla_side_angry.png"
image ulilla miltable = "pers/ulilla_miltable.png"
image side ulilla miltable = "pers/ulilla_side_military.png" 
image ulilla miltablesad = "pers/ulilla_miltablesad.png"
image side ulilla miltablesad = "pers/ulilla_side_military.png" 
image ulilla miltable2 = LiveComposite(
    (428, 428),
    (0, 0), "pers/ulilla_miltable.png",
    (172, 140), "pers/face/ulilla_write_hand.png",
    )
image side ulilla miltable2 = "pers/ulilla_side_military.png" 
image ulilla camera = LiveComposite(
    (504, 504),
    (0, 0), "pers/ulilla_joy.png",
    (190, 210), Image("items/Camera.png"),
    )
image side ulilla camera = "pers/ulilla_side_norm.png"



image dragonWingLeft:
    "items/DragonWing2.png"
    subpixel True  
    parallel:
        rotate 0
        linear 0.5 rotate 20
        linear 0.5 rotate 0
        repeat
        
image dragonWingRight:
    im.Flip("items/DragonWing2.png", horizontal=True)
    subpixel True  
    parallel:
        rotate 0
        linear 0.5 rotate -20
        linear 0.5 rotate 0
        repeat
        

define drakoha = Character(_('Дракоша'), color="#e2d40b", image="drakoha",  window_left_padding=175)
image drakoha norm = LiveComposite(
    (487, 487),
    (50, -10), "dragonWingLeft",
    (160,-5), "dragonWingRight",
    (0, 0), "pers/drakoha_norm.png",
    )
image side drakoha norm = "pers/drakoha_side_norm.png"



define jess = Character(_('Джесс'), color="#ffa659", image="jess", window_left_padding=165)
image jess happy = "pers/jess_happy.png"
image side jess happy = "pers/jess_side_happy.png"
image jess phototop = "pers/jess_phototop.png"
image side jess phototop = "pers/jess_side_photo.png"
image jess funnycard = "pers/jess_funnycard.png"
image side jess funnycard = "pers/jess_side_photo.png"


define Imp = Character('???', image="Imp", window_left_padding=175)
image Imp fight = "pers/side_impact.png"
image side Imp fight = "pers/side_impact.png"


define god = Character('???', image="god", window_left_padding=175)
image god cloud = "pers/god_cloud.png"
image side god cloud = "pers/side_angry.png" #"pers/god_side_cloud.png"


#image parkTrio1 = "pers/parkTrio1.png"
define parkTrio = Character('???', image="parkTrio")
image parkTrio st1 = "pers/parkTrio1.png"
image parkTrio st2 = "pers/parkTrio2.png"
image parkTrio st3 = "pers/parkTrio3.png"
image parkTrio st4 = "pers/parkTrio4.png"



define suomi = Character(_('Незнакомка'), color="#dc4497", image="suomi", window_left_padding=145)
image suomi norm = "pers/suomi_norm.png"
image side suomi norm = "pers/suomi_side_norm.png"
image suomi getin = "pers/suomi_getin.png"
image side suomi getin = "pers/suomi_side_norm.png"
image suomi getout = "pers/suomi_getout.png"
image side suomi getout = "pers/suomi_side_norm.png"
image suomi smallrun = "pers/suomi_smallrun.png"
image side suomi smallrun = "pers/suomi_side_norm.png"
image suomi sirprised = "pers/suomi_sirprised.png"
image side suomi sirprised = "pers/suomi_side_sirprised.png"



define lyba = Character(_("Лайби"), window_left_padding=170, image="lyba")
image lyba angry = "pers/lyba_angry.png"
image side lyba angry = "pers/lyba_side_angry.png"

image lyba pistol1 = "pers/lyba_pistol1.png"
image side lyba pistol1= "pers/lyba_side_angry.png"
image lyba pistol2 = "pers/lyba_pistol2.png"
image side lyba pistol2 = "pers/lyba_side_angry.png"

image lyba zont = "pers/lyba_zont.png"
image side lyba zont ="pers/lyba_side_normal.png"
image lyba angryflip = im.Flip("pers/lyba_angry.png", horizontal=True)
image side lyba angryflip = "pers/lyba_side_angry.png"
image lyba bath = "pers/lyba_bath.png"
image side lyba bath = "pers/lyba_side_bath.png"
image lyba eating = "pers/lyba_eating.png"
image side lyba eating = "pers/lyba_side_normal.png"
image lyba happy = LiveComposite(
    (512, 512),
    (0, 0), "pers/lyba_happy.png",
    (214, 5), im.Flip("items/NekoUho.png", horizontal=True),
    (268, 5), Image("items/NekoUho.png")
    )
image side lyba happy = "pers/lyba_side_happy.png"
image lyba happynorm = "pers/lyba_happy.png"
image side lyba happynorm = "pers/lyba_side_happy.png"

image lyba zontcrazy = LiveComposite(
    (598, 598),
    (0, 0), "pers/lyba_zont.png",
    (290, 176), "pers/face/lyba_zont_crazy.png",
    )
image side lyba zontcrazy ="pers/lyba_side_normal.png"

image lyba helangry = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_angry.png",
    #(217, 11), "items/Kaska.png",
    (210, -12), Transform( Image("items/Kaska.png"), rotate=-4 )
    )
image side lyba helangry = "pers/lyba_side_angry.png"



define lyblabla = Character( _("Лайби"), callback=speaker("lyblabla"), image="lyblabla", window_left_padding=155)
image lyblabla normal = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_boka_empty.png",
    (232, 67), "lyblabla eyes normal",
    #(249, 91), WhileSpeaking("lyblabla", "lyblabla mouth normal", "pers/face/lyba_mouth_closed.png"),
    (249, 91), "lyblabla mouth normal",
    )
image side lyblabla normal = "pers/lyba_side_normal.png"

image lyblabla sulk = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_sulk.png",
    (235, 71), "lyblabla eyes normal",
    #(249, 91), WhileSpeaking("lyblabla", "lyblabla mouth normal", "pers/face/lyba_mouth_closed.png"),
    (252, 95), "lyblabla mouth normal",
    )
image side lyblabla sulk = "pers/lyba_side_happy.png"

image lyblabla silent = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_boka_empty.png",
    (232, 67), "lyblabla eyes normal",
    (249, 91), "pers/face/lyba_mouth_closed.png",
    )
image lyblabla helmet = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_boka_empty.png",
    (232, 67), "lyblabla eyes normal",
    (249, 91), "lyblabla mouth normal",
    (212, 18), "items/Kaska.png",
    )
image side lyblabla helmet = "pers/lyba_side_normal.png"


image lyblabla helmbinocle = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_boka_empty.png",
    (232, 67), "lyblabla eyes normal",
    (249, 91), "lyblabla mouth normal",
    (212, 18), "items/Kaska.png",
    (209, 103), "items/Binocle.png"
    )
image side lyblabla helmbinocle = "pers/lyba_side_normal.png"

image lyblabla helmsulk = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_sulk.png",
    (235, 71), "lyblabla eyes normal",
    #(249, 91), WhileSpeaking("lyblabla", "lyblabla mouth normal", "pers/face/lyba_mouth_closed.png"),
    (252, 95), "lyblabla mouth normal",
    (214, 23), "items/Kaska.png",
    )
image side lyblabla helmsulk = "pers/lyba_side_happy.png"

image lyblabla helsilent = LiveComposite(
    (511, 511),
    (0, 0), "pers/lyba_boka_empty.png",
    (232, 67), "lyblabla eyes normal",
    (249, 91), "pers/face/lyba_mouth_closed.png",
    (212, 18), "items/Kaska.png",
    )
image side lyblabla helsilent = "pers/lyba_side_normal.png"

image lyblabla eyes normal:
    "pers/face/lyba_eyes_open.png" 
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "pers/face/lyba_eyes_semiclosed.png"
    .25
    repeat

image lyblabla mouth normal:
    choice:
        "pers/face/lyba_mouth_open.png" 
    choice:
        "pers/face/lyba_mouth_O.png"     
    .2
    "pers/face/lyba_mouth_closed.png"
    .2
    choice:
        "pers/face/lyba_mouth_O.png"
    choice:
        "pers/face/lyba_mouth_open.png" 
    .2
    "pers/face/lyba_mouth_closed.png"
    .2
    choice:
        .1
    choice:
        .05
    choice:
        .3
    choice:
        1.0    
    repeat



label language_chooser:
    #play music "Music/Chillout5v7.OGG" fadein 1
    play sound "sound/ecfike_computer-error.ogg"
    scene bg SchoolDay
    show dexp thinkbig:
        xalign -0.4 yalign 1.0
    show Question:
        xalign 0.17 yalign 0.0
    
    menu:
        "{image=items/flags/en.jpg}  English language":
            $ renpy.change_language("english")
            if not persistent.chose_voiceover:
                $ config.has_voice = False
            pass
        "{image=items/flags/ru.jpg}  Русский язык":
            $ renpy.change_language(None)
            pass
        "{image=items/flags/pl.jpg}  Język polski":
            $ renpy.change_language("polish")
            if not persistent.chose_voiceover:
                $ config.has_voice = False
            pass
            
    #$ renpy.utter_restart()
    hide Question
    hide dexp with dissolve
    return



label splashscreen:
    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        call language_chooser from _call_language_chooser
    return



# Описание переменных
init: 
    $ profession = "newbie"
    $ prof_str = __("Новичок")
    $ prof_success = False
    
    $ text_team = False
    $ pic_team = False
    
    $ scan_learned = False
    $ klin_learned = False
    $ translate_learned = False
    $ korrekt_learned = False
    $ type_learned = False
    $ beta_learned = False
    $ dinning_learned = False
    
    $ scan_points = 0
    $ klin_points = 0
    $ translate_points = 0
    $ korrekt_points = 0
    $ type_points = 0
    $ beta_points = 0
    
    $ NEED_POINTS = 15
    
    $ goodEnd = False
    $ penalty = 0
    
    $ lap_points = 0
    
    $ met = "none"


# Игра начинается здесь.
label start:   
    scene black
    if config.has_voice:
        centered "Озвучено командой сайта xdub.ru"
    jump day1
