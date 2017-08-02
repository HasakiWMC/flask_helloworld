from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Flask Hello World')


@app.route('/services')
def services():
    return 'Service'


@app.route('/about')
def about():
    return 'About'


# int float path路由转换器
@app.route('/user/<int:user_id>')
def user(user_id):
    return 'User %s' % user_id


if __name__ == '__main__':
    app.run(debug=True)  # 不需要重启服务
