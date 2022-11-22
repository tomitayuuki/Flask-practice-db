from flask import Blueprint, render_template, url_for, request, redirect
from apps.app import db
from apps.practiceDB.models import User
from apps.practiceDB.forms import UserForm

# 分岐設定
practiceDB = Blueprint(
    "practiceDB",
    __name__,
    template_folder = "templates",
    static_folder = "static"
)

# 初期画面
@practiceDB.route("/", methods=["GET","POST"])
def index():
    # ユーザ情報フォーム
    form = UserForm()
    # 普通に来たら普通に表示
    if request.method != "POST":
        return render_template("practiceDB/index.html", form=form)

    # フォームデータが送られてきたらデータベースに登録
    username=form.username.data
    email=form.email.data
    user = User(
        username=username,
        email=email,
    )
    db.session.add(user)
    db.session.commit()

    userdata = User.query.filter_by(username=username).first()

    return render_template("practiceDB/index.html",
        userdata=userdata, form=form)


# SQL動作確認
@practiceDB.route("/sql")
def sql():
    user = User(
        username="kazuyamishima",
        email="kokogakisamanohakabada@gmail.com"
    )
    db.session.add(user)
    db.session.commit()
    return "コンソールを確認"
