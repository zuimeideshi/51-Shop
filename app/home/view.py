from . import home
from app import db
from app.home.forms import LoginForm,RegisterForm,PasswordForm
from app.models import User ,Goods,Orders,Cart,OrdersDetail
from flask import render_template, url_for, redirect, flash, session, request,make_response
from werkzeug.security import generate_password_hash
from functools import wraps
import random
import string
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


@home.route("/")
def index():
    '''
    首页
    '''

    # 渲染模板
    return render_template('home/index.html')

@home.route("/register/", methods=["GET", "POST"])
def register():
    """
    注册功能
    """
    if "user_id" in session:
        return redirect(url_for("home.index"))
    form = RegisterForm()           # 导入注册表单
    if form.validate_on_submit():   # 提交注册表单
        data = form.data            # 接收表单数据
        # 为User类属性赋值
        user = User(
            username = data["username"],            # 用户名
            email = data["email"],                  # 邮箱
            password = generate_password_hash(data["password"]),# 对密码加密
            phone = data['phone']
        )
        db.session.add(user) # 添加数据
        db.session.commit()  # 提交数据
        return redirect(url_for("home.login"))  # 登录成功，跳转到首页
    return render_template("home/register.html", form=form) # 渲染模板