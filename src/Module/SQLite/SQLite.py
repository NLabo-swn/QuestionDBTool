import sqlite3
from typing import List, Tuple, Any


class SQLite:
    """
    SQLiteデータベース操作を扱うクラス。Create, Read, Update, Delete (CRUD) 操作をサポートします。

    Attributes:
        db_name (str): SQLiteデータベースファイルの名前。
    """

    def __init__(self, db_name: str):
        """
        指定されたデータベース名でSQLiteDatabaseを初期化します。

        Args:
            db_name (str): SQLiteデータベースファイルの名前。
        """
        self.db_name = db_name

    def execute_query(self, query: str, params: Tuple = ()) -> None:
        """
        結果を返さない単一のクエリを実行します。

        Args:
            query (str): 実行するSQLクエリ。
            params (Tuple, optional): SQLクエリに渡すパラメータ。デフォルトは空のタプル。
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

    def fetch_all(self, query: str, params: Tuple = ()) -> List[Tuple[Any, ...]]:
        """
        クエリを実行し、すべての行をタプルのリストとして返します。

        Args:
            query (str): 実行するSQLクエリ。
            params (Tuple, optional): SQLクエリに渡すパラメータ。デフォルトは空のタプル。

        Returns:
            List[Tuple[Any, ...]]: クエリで返されたすべての行のリスト。
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetch_one(self, query: str, params: Tuple = ()) -> Tuple[Any, ...]:
        """
        クエリを実行し、単一の行をタプルとして返します。

        Args:
            query (str): 実行するSQLクエリ。
            params (Tuple, optional): SQLクエリに渡すパラメータ。デフォルトは空のタプル。

        Returns:
            Tuple[Any, ...]: クエリで返された単一の行。
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()

    def create_table(self, table_name: str, columns: str) -> None:
        """
        指定された名前と列でテーブルを作成します。

        Args:
            table_name (str): 作成するテーブルの名前。
            columns (str): テーブルに作成する列とそのデータ型。
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_query(query)

    def insert(self, table_name: str, columns: str, values: Tuple) -> None:
        """
        指定されたテーブルに新しい行を挿入します。

        Args:
            table_name (str): 挿入するテーブルの名前。
            columns (str): 値を挿入する列。
            values (Tuple): 列に挿入する値。
        """
        placeholders = ", ".join(["?" for _ in values])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, values)

    def update(
        self, table_name: str, set_values: str, condition: str, params: Tuple
    ) -> None:
        """
        条件に一致する指定されたテーブルの行を更新します。

        Args:
            table_name (str): 更新するテーブルの名前。
            set_values (str): 設定する列とその新しい値。
            condition (str): 行を一致させるための条件。
            params (Tuple): SQLクエリに渡すパラメータ。
        """
        query = f"UPDATE {table_name} SET {set_values} WHERE {condition}"
        self.execute_query(query, params)

    def delete(self, table_name: str, condition: str, params: Tuple) -> None:
        """
        条件に一致する指定されたテーブルの行を削除します。

        Args:
            table_name (str): 削除するテーブルの名前。
            condition (str): 行を一致させるための条件。
            params (Tuple): SQLクエリに渡すパラメータ。
        """
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_query(query, params)

    def select_all(self, table_name: str) -> List[Tuple[Any, ...]]:
        """
        指定されたテーブルからすべての行を選択します。

        Args:
            table_name (str): 選択するテーブルの名前。

        Returns:
            List[Tuple[Any, ...]]: テーブル内のすべての行のリスト。
        """
        query = f"SELECT * FROM {table_name}"
        return self.fetch_all(query)

    def select_where(
        self, table_name: str, condition: str, params: Tuple
    ) -> List[Tuple[Any, ...]]:
        """
        条件に一致する指定されたテーブルの行を選択します。

        Args:
            table_name (str): 選択するテーブルの名前。
            condition (str): 行を一致させるための条件。
            params (Tuple): SQLクエリに渡すパラメータ。

        Returns:
            List[Tuple[Any, ...]]: 条件に一致する行のリスト。
        """
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        return self.fetch_all(query, params)
