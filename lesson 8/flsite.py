import os

from flask import Flask

# config
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'QQL'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))

menu = [
    {"name": 'Установка', "url": 'install-flask'}
    , {"name": 'Первое приложение', "url": 'first-app'}
    , {"name": 'Обратная связь', "url": 'contact'}
    , {"name": 'Авторизация', "url": 'login'}
]


# @app.route('/')
# @app.route('/index')
# def index():
#     print(url_for('index'))
#     return render_template('index.html', menu=menu)
#
#
# @app.route('/about')
# def about():
#     print(url_for('about'))
#     return render_template('about.html', title='О сайте', menu=menu)
#
#
# @app.route('/profile/<username>')
# def profile(username):
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#     return f'Пользователь: {username}'
#
#
# @app.route('/contact', methods=['POST', 'GET'])
# def contact():
#     if request.method == 'POST':
#         if len(request.form['username']) > 2:
#             flash('Сообщение отправлено', category='success')
#         else:
#             flash('Ошибка отправки', category='error')
#
#     return render_template('contact.html', title='Обратная связь', menu=menu)
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if 'userLogged' in session:
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == 'POST' and request.form['username'] == 'qql' and request.form['psw'] == '123':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for('profile', username=session['userLogged']))
#     return render_template('login.html', title='Авторизация', menu=menu)
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page404.html', title='Страница не была найдена', menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
    # session.clear()
