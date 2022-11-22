from flask import Flask
from apps.config import config # 設定を別ファイルからもらう
from flask_sqlalchemy import SQLAlchemy # DB
from flask_migrate import Migrate # DB
from flask_wtf.csrf import CSRFProtect # フォーム
import psycopg2 # postgresqlに必要

# DBインスタンス
db = SQLAlchemy()
# CSRFインスタンス（フォーム用）
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    # 設定の登録
    app.config.from_object(config['Testing'])

    # データベース登録
    db.init_app(app)
    Migrate(app, db)
    # csrf登録
    csrf.init_app(app)

    # アプリ分岐の設定
    from apps.practiceDB import views as practice_view
    app.register_blueprint(practice_view.practiceDB)

    return app
