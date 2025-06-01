import sqlite3
import hashlib


from article import Article, User


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
        
        return cursor.fetchall()
    
    @staticmethod
    def convert_to_articles(raw_articles):  
        articles=[]
        for id, title, content, photo in raw_articles:
            article = Article(title, content, photo, id)
            articles.append(article)
        return articles

    def create_table():
        with open(Database.SCHEMA) as schema_file:
            connection = sqlite3.connect(Database.DB)
            cursor = connection.cursor()
            cursor.executescript(schema_file.read())
            connection.commit()
            connection.close()



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
        articles = Database.convert_to_articles(
            Database.select('SELECT * FROM articles WHERE id = ?', [id])
        )

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
    
    @staticmethod
    def register_user(email, phone, password):
        password_hash = hashlib.md5(password.encode()).hexdigest()
        Database.execute(
            "INSERT INTO users (email, phone, password_hash) VALUES (?, ?, ?)",
            [email, phone, password_hash]
        )

    @staticmethod
    def find_user_by_email_or_phone(email_or_phone):
        users = Database.select(
            "SELECT * FROM users WHERE email = ? OR phone = ?",
            [email_or_phone, email_or_phone]
        )
        if not users:
            return None
        
        id, email, phone, password_hash = users[0]
        return User(email=email, phone=phone, id=id)

    @staticmethod
    def can_be_logged_in(email_or_phone, password):
        user = Database.find_user_by_email_or_phone(email_or_phone)
        if user is None:
            return False
        
        password_hash = hashlib.md5(password.encode()).hexdigest()
        real_password_hash = Database.select(
            'SELECT password_hash FROM users WHERE email = ? OR phone = ?',
            [email_or_phone, email_or_phone]
        )[0][0]

        if password_hash != real_password_hash:
            return False
        
        return True
