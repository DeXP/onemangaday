[_tb_system_call storage=system/_scene1.ks]

[bg  storage="black-800x600.png"  time="0"  ]
*start

[tb_show_message_window  ]
It is not known when this story was there...[p]
But once ... It still happened![p]


[tb_hide_message_window  ]
[bg  time="1000"  method="crossfade"  storage="OneMangaDay-bg.jpg"  ]
[chara_show  name="Dex"  time="1000"  left="-1"  top="0"  ]
[tb_show_message_window  ]
[iscript]
$(".chara_name_area").css({"color":"#999999"});
[endscript]

#Dex
Oh yeah! It looks even better when polished![p]
#


[tb_hide_message_window  ]
[chara_show  name="Malya"  time="1000"  left="460"  top="50"  ]
[tb_show_message_window  ]
[iscript]
$(".chara_name_area").css({"color":"#76e2e4"});
[endscript]

#Malya
Wow! How did you get so big?[p]
Are you sure know how to use it?[p]
#


[iscript]
$(".chara_name_area").css({"color":"#999999"});
[endscript]

#Dex
For sure! You're getting ahead now![p]
#


[tb_hide_message_window  ]
[tb_start_tyrano_code]
[anim name="Malya" left="0" time="1000"]
[wait time=1000]
[anim name="Dex" left="220" time="1000"]
[wait time=1000]
[wa]
[_tb_end_tyrano_code]

[iscript]
$(".chara_name_area").css({"color":"#76e2e4"});
[endscript]

[tb_show_message_window  ]
#Malya
Wow! Indeed, you know how![p]
#


[tb_hide_message_window  ]
[chara_mod  name="Malya"  time="1000"  storage="chara/5/OneMangaDay-Mala-yee.png"  ]
[tb_show_message_window  ]
#Malya
This is awesome! Scratch the back once more, eh?[p]
#


[chara_hide  name="Dex"  time="0"  ]
[chara_hide  name="Malya"  time="0"  ]
[bg  time="0"  method="crossfade"  storage="black-800x600.png"  ]
THE END![p]


[jump  storage="scene1.ks"  target="*start"  cond="1"  ]
[s  ]
