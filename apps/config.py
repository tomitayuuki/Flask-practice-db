from pathlib import Path
import os

basedir=Path(__file__).parent.parent

# 共通の設定
class BaseConfig:
    SECRET_KEY='kazuyamishimawins'
    WTF_CSRF_SECRET_KEY='kazuyamishimalose'

# localの設定
class LocalConfig(BaseConfig):
    db_uri = os.environ.get('DATABASE_URL') or "postgresql://postgres:postgres@localhost:5432/flask_practice"
    SQLALCHEMY_DATABASE_URI=db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

# テストの設定
class TestingConfig(BaseConfig):
    db_uri = os.environ.get('DATABASE_URL') or "postgresql://postgres:postgres@localhost:5432/flask_practice"
    SQLALCHEMY_DATABASE_URI=db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

# localとtestの分岐
config = {
    "local":LocalConfig,
    "Testing":TestingConfig,
}
