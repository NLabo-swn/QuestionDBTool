from Module.SQLite.SQLite import SQLite


class DBData:
    db: SQLite
    path: str

    def initialize(path: str) -> None:
        DBData.path = path
        DBData.db = SQLite(DBData.path)

    def getDBPath() -> str:
        return DBData.path
