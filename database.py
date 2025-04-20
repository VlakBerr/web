import sqlite3


from article import Article


class Database:
    articles = []
    DB='database.db'
    SCHEMA='schema.sql'

    @staticmethod
    def execute(sql, params=()):
        'подключаемся к бд'
        connection=sqlite3.connect(Database.SCHEMA)

        'получаем курсор'
        cursor = connection.cursor()

        'код'
        cursor.execute(sql, params)
        

        'фиксируем изменения'
        connection.commit()


    def create_table():
        with open(Database.SCHEMA) as schema_file:
            Database.execute(schema_file.read())


    @staticmethod
    def save(article: Article):
       if Database.find_article_by_title(article.title) is not None:
           return False
       
       Database.execute(
            'INSERT INTO articles VALUES (?,?,?)',
            [article.title, article.content ,article.photo]
        )
       return True



    @staticmethod
    def find_article_by_title(title):
        'подключаемся к бд'
        connection=sqlite3.connect(Database.SCHEMA)

        'получаем курсор'
        cursor = connection.cursor()

        'код'
        cursor.execute('SELECT * FROM articles WHERE title = ?', [title])
        articles=cursor.fetchall()

        if len(articles) == 0:
            return None
        
        article = Article(articles[0][0], articles[0][1], articles[0][2], articles[0][3])

        return articles[0]
    

    @staticmethod
    def get_all_articles():
        return Database.articles
    