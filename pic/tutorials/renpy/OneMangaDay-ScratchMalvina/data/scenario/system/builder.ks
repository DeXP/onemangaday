;ビルダーでシナリオごとに必ず呼び出されるシステム系のKSファイル

;メッセージウィンドウを非表示にする
[macro name="tb_show_message_window"]
	[layopt  layer="message0"  visible="true"  ]
[endmacro]

;メッセージウィンドウを表示する
[macro name="tb_hide_message_window"]
	[layopt  layer="message0"  visible="false"  ]
[endmacro]

[macro name="_tb_system_call"]
	[call storage=%storage ]
[endmacro]

[macro name="tb_image_show"]
	[image storage=%storage layer=1 page=fore visible=true y=%y x=%x width=%width height=%height time=%time ]	
[endmacro]
	
[macro name="tb_image_hide"]
	[freeimage layer=1 page=fore time=%time]	
[endmacro]

;生ティラノ用のマーカー
[macro name="tb_start_tyrano_code"]
[endmacro]

[macro name="_tb_end_tyrano_code"]
[endmacro]

[macro name="lr"]
[l][r]
[endmacro]


