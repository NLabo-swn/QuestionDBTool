import PySimpleGUI as sg
import datetime

today = datetime.datetime.today()

TITLE_SIZE: int = 12

# メインレイアウト
MainTabLayout = [
    [sg.Text("出題日", size=TITLE_SIZE), sg.Text("-", key="main_day")],
    [sg.Text("")],
    [sg.Text("タイトル", size=TITLE_SIZE), sg.Text("-", key="main_title")],
    [sg.Text("")],
    [sg.Text("使用する技術", size=TITLE_SIZE), sg.Text("-", key="main_technology")],
    [sg.Text("")],
    [sg.Text("問題内容")],
    [sg.Multiline(size=(100, 24), disabled=True, key="main_body")],
    [sg.Text("")],
    [sg.HorizontalSeparator()],
    [sg.Text("")],
    [sg.Button("ランダム選択", size=100, key="main_randomSelect")],
]


# 登録画面
RegistrationTabLayout = [
    [
        sg.Text("問題タイトル", size=TITLE_SIZE),
        sg.Input(size=100, focus=True, key="reg_title"),
    ],
    [sg.Text("")],
    [
        sg.Text("使用する技術", size=TITLE_SIZE),
        sg.Input(size=100, key="reg_technology"),
    ],
    [sg.Text("")],
    [sg.Text("問題内容")],
    [sg.Multiline(size=(100, 27), key="reg_body")],
    [sg.Text("")],
    [sg.HorizontalSeparator()],
    [sg.Text("")],
    [sg.Button("登録", size=100, key="register")],
]

MainLayout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("メイン", MainTabLayout),
                    sg.Tab("登録画面", RegistrationTabLayout),
                ]
            ]
        )
    ]
]
