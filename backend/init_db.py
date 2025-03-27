import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # データベース接続の設定
        config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'user',
            'password': 'password'
        }

        # データベースに接続
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # データベースを選択
        cursor.execute("USE koilog")

        # ユーザーテーブルの作成
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)

        # サンプルユーザーの追加
        insert_query = """
        INSERT INTO users (username, email, password_hash)
        VALUES (%s, %s, %s)
        """
        sample_users = [
            ('admin', 'admin@example.com', 'hashed_password_1'),
            ('user1', 'user1@example.com', 'hashed_password_2'),
            ('user2', 'user2@example.com', 'hashed_password_3')
        ]
        cursor.executemany(insert_query, sample_users)

        # 変更を保存
        conn.commit()
        print("データベースとテーブルの初期化が完了しました！")

    except Error as e:
        print(f"エラーが発生しました: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("データベース接続を閉じました。")

if __name__ == "__main__":
    create_database()

import mysql.connector

config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'koilog',
    'user': 'user',
    'password': 'password'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # ユーザーテーブルの内容を表示
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    for user in users:
        print(f"ID: {user[0]}")
        print(f"Username: {user[1]}")
        print(f"Email: {user[2]}")
        print(f"Created at: {user[4]}")
        print("---")

except mysql.connector.Error as err:
    print(f"エラーが発生しました: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

import mysql.connector

config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'koilog',
    'user': 'user',
    'password': 'password'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # 新しいユーザーの追加
    insert_query = """
    INSERT INTO users (username, email, password_hash)
    VALUES (%s, %s, %s)
    """
    new_user = ('newuser', 'newuser@example.com', 'hashed_password_4')
    cursor.execute(insert_query, new_user)
    
    # 変更を保存
    conn.commit()
    print("新しいユーザーが追加されました！")

except mysql.connector.Error as err:
    print(f"エラーが発生しました: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close() 