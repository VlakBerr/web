import sqlite3


from article import Article


class Database:
    DB='database.db'
    SCHEMA='schema.sql'

    @staticmethod
    def execute(sql, params=()):
        'подключаемся к бд'
        connection=sqlite3.connect(Database.DB)

        'получаем курсор'
        cursor = connection.cursor()

        'код'
        cursor.execute(sql, params)
        
        'фиксируем изменения'
        connection.commit()

    @staticmethod
    def select(sql, params=()):
        'подключаемся к бд'
        connection=sqlite3.connect(Database.DB)

        'получаем курсор'
        cursor = connection.cursor()

        'выполняем запрос'
        cursor.execute(sql, params)
        
        raw_articles=cursor.fetchall()
        articles=[]
        for id, title, content, photo in raw_articles:
            article = Article(title, content, photo, id)
            articles.append(article)

        return articles
    

    def create_table():
        with open(Database.SCHEMA) as schema_file:
            Database.execute(schema_file.read())


    @staticmethod
    def save(article: Article):
       if Database.find_article_by_title(article.title) is not None:
           return False
       
       Database.execute(
            'INSERT INTO articles (title, content, photo) VALUES (?,?,?)',
            [article.title, article.content ,article.photo]
        )
       return True


    @staticmethod
    def find_article_by_id(id):
        articles = Database.select('SELECT * FROM articles WHERE id = ?', [id])

        if not articles:
            return None
        return articles[0]
    

    @staticmethod
    def delete_article_by_id(id):
        article=Database.find_article_by_id(id)
        if article is None:
            return False
        
        Database.execute('DELETE FROM articles WHERE id = ?', [id])
        return True
    
    
    @staticmethod
    def update_article(id, title, content, photo):
        article=Database.find_article_by_id(id)
        if article is None:
            return False
        
        Database.execute('''
        UPDATE articles
        SET title = ?, content = ?, photo = ?
        WHERE id = ?
        ''', [title, content, photo, id])
        return True



    @staticmethod
    def find_article_by_title(title):
        'подключаемся к бд'
        connection=sqlite3.connect(Database.DB)

        'получаем курсор'
        cursor = connection.cursor()

        'код'
        cursor.execute('SELECT * FROM articles WHERE title = ?', [title])
        articles=cursor.fetchall()

        if len(articles) == 0:
            return None
        
        id, title, content, photo = articles[0]
        article = Article(title, content, photo, id)
        return article
    

    @staticmethod
    def get_all_articles():
        'подключаемся к бд'
        connection=sqlite3.connect(Database.DB)

        'получаем курсор'
        cursor = connection.cursor()

        'код'
        cursor.execute('SELECT * FROM articles')
        raw_articles=cursor.fetchall()

        articles=[]
        for id, title, content, photo in raw_articles:
            article = Article(title, content, photo, id)
            articles.append(article)

        return articles
    