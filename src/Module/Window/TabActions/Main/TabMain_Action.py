import random

from Module.DBData.DBData import DBData
from Module.Window.Keys import TABLE_LABEL
from Module.Window.WindowData import WindowData

old_SelectID: int = -1


def getRandomData():
    global old_SelectID

    # ID一覧を取得
    ids = DBData.db.fetch_all("SELECT ID FROM data")
    id_list = [row[0] for row in ids]

    # ランダムで1つのIDを選択
    random_id = random.choice(id_list)

    # 選択されたIDのデータを取得
    record = DBData.db.fetch_one("SELECT * FROM data WHERE ID = ?", (random_id,))

    now_SelectID: int = int(record[TABLE_LABEL.ID])

    if now_SelectID == old_SelectID:
        return getRandomData()

    old_SelectID = now_SelectID

    return record


def RandomSelect(window: WindowData):
    randomData = getRandomData()

    LABEL_DAY: str = "main_day"
    LABEL_TITLE: str = "main_title"
    LABEL_TECHNOLOGY: str = "main_technology"
    LABEL_BODY: str = "main_body"

    window.setValue(LABEL_DAY, randomData[TABLE_LABEL.DATE])
    window.setValue(LABEL_TITLE, randomData[TABLE_LABEL.TITLE])
    window.setValue(LABEL_TECHNOLOGY, randomData[TABLE_LABEL.TECHNOLOGY])
    window.setValue(LABEL_BODY, randomData[TABLE_LABEL.BODY])
