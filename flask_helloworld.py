#!usr/bin/env python
# -*- coding:utf-8 _*-

from flask import Flask, render_template
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def hello_world():
    return render_template('index.html', title='Flask Hello World')


@app.route('/services')
def services():
    return 'Service'


@app.route('/about')
def about():
    return 'About'


# int float path 路由转换器
@app.route('/user/<int:user_id>')
def user(user_id):
    return 'User %s' % user_id


@app.route('/regex/<regex("[a-z]{3}"):user_reg>')
def regex(user_reg):
    return 'User %s' % user_reg


if __name__ == '__main__':
    app.run(debug=True)  # 不需要重启服务
