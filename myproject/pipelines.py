from scrapy.exceptions import DropItem
import MySQLdb


class ValidationPipeline(object):
    """
    Itemを検証するPipeline。
    """

    def process_item(self, item, spider):
        if not item['title']:
            # titleフィールドが取得できていない場合は破棄する。
            # DropItem()の引数は破棄する理由を表すメッセージ。
            raise DropItem('Missing title')

        return item  # titleフィールドが正しく取得できている場合。


class MySQLPipeline(object):
    """
    ItemをMySQLに保存するPipeline。
    """

    def open_spider(self, spider):
        """
        Spiderの開始時にMySQLサーバーに接続する。
        itemsテーブルが存在しない場合は作成する。
        """

        settings = spider.settings  # settings.pyから設定を読み込む。
        params = {
            'host': settings.get('MYSQL_HOST', 'localhost'),  # ホスト
            'db': settings.get('MYSQL_DATABASE', 'jpnbooks'),  # データベース名
            'user': settings.get('MYSQL_USER', 'root'),  # ユーザー名
            'passwd': settings.get('MYSQL_PASSWORD', ''),  # パスワード
            'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),  # 文字コード
        }
        self.conn = MySQLdb.connect(**params)  # MySQLサーバーに接続。
        self.c = self.conn.cursor()  # カーソルを取得。
        # itemsテーブルが存在しない場合は作成。
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER NOT NULL AUTO_INCREMENT,
                publisher CHAR(200),
                title CHAR(200) NOT NULL,
                subtitle CHAR(200),
                url CHAR(200),
                imgurl CHAR(200),
                PRIMARY KEY (id)
            )
        ''')
        self.conn.commit()  # 変更をコミット。

    def close_spider(self, spider):
        """
        Spiderの終了時にMySQLサーバーへの接続を切断する。
        """

        self.conn.close()

    def process_item(self, item, spider):
        """
        Itemをitemsテーブルに挿入する。
        """

        self.c.execute('INSERT INTO books (title,url,subtitle,imgurl,publisher) \
               VALUES (%(title)s,%(url)s,%(subtitle)s,%(imgurl)s,%(publisher)s)', dict(item))
        self.conn.commit()  # 変更をコミット。
        return item
