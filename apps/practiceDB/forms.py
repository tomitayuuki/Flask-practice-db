from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# ユーザ情報をもらうフォーム
class UserForm(FlaskForm):
    # ユーザ名
    username = StringField(
        "ユーザ名",
        validators=[
            DataRequired(message="君の名前を教えて"),
            Length(max=30,message="君の名前が長すぎて覚えられないや")
        ],
    )
    # メールアドレス
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="君のメールアドレスを教えて")
        ],
    )
    submit = SubmitField("送信する")
