[_tb_system_call storage=system/_preview.ks ]

*start

[bg  storage="black-800x600.png"  time="0"  ]
[tb_show_message_window  ]
Неизвестно, когда случилась эта история...[p]
Но когда-то... Она всё-таки случилась![p]


[tb_hide_message_window  ]
[bg  time="1000"  method="crossfade"  storage="OneMangaDay-bg.jpg"  ]
[chara_show  name="Дэкс"  time="1000"  left="-1"  top="0"  ]
[tb_show_message_window  ]
[iscript]
$(".chara_name_area").css({"color":"#999999"});
[endscript]

#Дэкс
О да! Отполированным он выглядит ещё лучше![p]
#


[tb_hide_message_window  ]
[chara_show  name="Маля"  time="1000"  left="460"  top="50"  ]
[tb_show_message_window  ]
[iscript]
$(".chara_name_area").css({"color":"#76e2e4"});
[endscript]

#Маля
Ого! Он у тебя такой большой![p]
Уверен, что умеешь им пользоваться?[p]
#


[iscript]
$(".chara_name_area").css({"color":"#999999"});
[endscript]

#Дэкс
А то! Становись вперёд![p]
#


[tb_hide_message_window  ]
[tb_start_tyrano_code]
[anim name="Маля" left="0" time="1000"]
[wait time=1000]
[anim name="Дэкс" left="220" time="1000"]
[wait time=1000]
[wa]
[_tb_end_tyrano_code]

[iscript]
$(".chara_name_area").css({"color":"#76e2e4"});
[endscript]

[tb_show_message_window  ]
#Маля
Ого! Действительно, умеешь![p]
#


[tb_hide_message_window  ]
[chara_mod  name="Маля"  time="1000"  storage="chara/3/OneMangaDay-Mala-yee.png"  ]
[tb_show_message_window  ]
#Маля
Кааайф! Почеши спинку ещё, а?[p]
#


[chara_hide  name="Дэкс"  time="0"  ]
[chara_hide  name="Маля"  time="0"  ]
[bg  time="0"  method="crossfade"  storage="black-800x600.png"  ]
КОНЕЦ![p]


[jump  storage="scene1.ks"  target="*start"  cond="1"  ]
[s  ]
