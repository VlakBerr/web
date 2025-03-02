from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def ruwiki():
    return render_template("ruwiki.html")

@app.route("/hello")
def hello():
    return 'привет мир'

@app.route("/max")
def find_max():
    a = int(request.args['a'])
    b = int(request.args['b'])
    if a > b: return f'{a}'
    else: return f'{b}'

@app.route("/sonic")
def sonic_article():
    title_article='Ёж Соник'
    text_article='''Ёж Со́ник (яп. ソニック・ザ・ヘッジホッグ Соникку дза Хэдзихоггу, англ. Sonic the Hedgehog) — главный персонаж
    серии видеоигр Sonic the Hedgehog от компании Sega, а также созданных на её основе комиксов, мультсериалов и полнометражных фильмов.
    Соник — синий антропоморфный ёж, созданный художником Наото Осимой, программистом Юдзи Накой и дизайнером Хирокадзу Ясухарой. Во время 
    разработки было предложено множество образов главного героя будущей игры, но разработчики остановились на ёжике синего цвета. Своё имя Соник 
    получил за способность бегать на сверхзвуковых скоростях (англ. sonic — «звуковой; со скоростью звука»). Геймплей за Соника в большинстве игр серии 
    Sonic the Hedgehog заключается в быстром прохождении уровней и битвах с врагами, для атаки которых Соник сворачивается в шар во время прыжка. Немаловажную
    роль для Соника играют золотые кольца, служащие ему в качестве защиты. Главным антагонистом героя является доктор Эггман, который хочет захватить мир и построить 
    свою империю «Эггманленд».После выхода одноимённой игры с его участием Соник быстро стал популярным во всём мире и положил начало крупной медиафраншизе. Персонаж 
    стал талисманом компании Sega, которым остаётся и сейчас, сменив Алекса Кидда, бывшего неофициальным маскотом компании до 1990 года. На ноябрь 2014 года было продано
    свыше 150 миллионов экземпляров игр серии о Сонике[4]. Помимо компьютерных игр, ёж Соник является главным героем комиксов, книг, ряда мультсериалов и полнометражных аниме и фильмов. '''
    article_image_title='Соник'
    article_image_path= 'static/images/Sonic.png'
    return render_template('article.html',
                            title_article=title_article,
                            text_article=text_article, 
                            article_image_title=article_image_title, 
                            article_image_path=article_image_path)


@app.route('/Ехидна_Наклз')
def nacles_article():
    title_article='Ехидна Наклз'
    text_article='''Ехидна Наклз[2] (яп. ナックルズ・ザ・エキドゥナ Наккурудзу дза Экидуна, англ. Knuckles the Echidna) 
    — персонаж видеоигр, телешоу и комиксов серии Sonic the Hedgehog. Его прозвища — «Knuckie», «Rad Red», «Red Storm», 
    «Knux», и «Knucklehead». Создан Такаси Юдой. Первое появление — игра Sonic the Hedgehog 3. Наклз — красная 
    антропоморфная ехидна, чьи иглы похожи на причёску из многочисленных коротких дредов. Можно заметить некоторое 
    различие между игровым и неигровым спрайтами Наклза. В играх играбельный Наклз предстаёт в ярко-красном цвете с 
    зелёными носками, а неиграбельный — как красно-розовый с жёлтыми носками. По официальным данным Наклзу 16 лет.'''
    article_image_title='Ехидна Наклз'
    article_image_path='static/images/Nackles.png'
    return render_template('article.html',
                            title_article=title_article,
                            text_article=text_article, 
                            article_image_title=article_image_title, 
                            article_image_path=article_image_path)







@app.route("/base")
def base():
    return render_template('base.html', title = 'Китайский новый год')

if __name__ == '__main__':
    app.run(debug=True)