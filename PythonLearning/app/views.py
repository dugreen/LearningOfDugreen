#!coding:utf-8

from flask import render_template,flash,redirect
from app import app
#表单view
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    #return "Hello World~!"
    user = {'nickname':'dugreen'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    #获取客户端发送的数据
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])
