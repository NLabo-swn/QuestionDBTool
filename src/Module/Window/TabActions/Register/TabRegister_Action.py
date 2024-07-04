import PySimpleGUI as sg

from datetime import datetime

from Module.DBData.DBData import DBData
from Module.Window.WindowData import WindowData


def addRecord(title: str, technology: str, body: str) -> None:

    # 現在の日付と時刻を取得
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 挿入するデータの定義
    insert_data = (current_date, title, technology, body)

    # データの挿入
    DBData.db.insert("data", "Date, Title, Technology, body", insert_data)


def reg_button(window: WindowData):
    LABEL_TITLE: str = "reg_title"
    LABEL_TECHNOLOGY: str = "reg_technology"
    LABEL_BODY: str = "reg_body"

    title: str = window.getValue(LABEL_TITLE)
    technology: str = window.getValue(LABEL_TECHNOLOGY)
    body: str = window.getValue(LABEL_BODY)

    if title == "":
        sg.popup_error("タイトルを入力してください", title="エラー")
        return
    if technology == "":
        sg.popup_error("使用する技術を入力してください", title="エラー")
        return
    if body == "":
        sg.popup_error("問題内容を入力してください", title="エラー")
        return

    addRecord(title, technology, body)

    window.setValue(LABEL_TITLE, "")
    window.setValue(LABEL_TECHNOLOGY, "")
    window.setValue(LABEL_BODY, "")

    sg.popup_notify("データを登録しました")
