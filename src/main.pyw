import PySimpleGUI as sg
import FileAction

from Module.DBData.DBData import DBData
from Module.Window.TabActions.Main.TabMain_Action import RandomSelect
from Module.Window.TabActions.Register.TabRegister_Action import reg_button
from Module.Window.WindowData import WindowData


DBData.initialize(FileAction.ConvertFileLink("res/data.db"))


def main() -> None:
    window: WindowData = WindowData()

    window.Initialize()

    while True:
        window.read()

        if window.isEvent(sg.WINDOW_CLOSED):
            break
        elif window.isEvent("register"):
            # 登録ボタン
            reg_button(window)
        elif window.isEvent("main_randomSelect"):
            RandomSelect(window)

    window.close()


main()
