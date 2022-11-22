from pathlib import Path

basedir=Path(__file__).parent.parent

# 共通の設定
class BaseConfig:
    SECRET_KEY='kazuyamishimawins'
    WTF_CSRF_SECRET_KEY='kazuyamishimalose'

# localの設定
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@localhost:5432/flask_practice"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

# テストの設定
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

# localとtestの分岐
config = {
    "local":LocalConfig,
    "Testing":TestingConfig,
}
