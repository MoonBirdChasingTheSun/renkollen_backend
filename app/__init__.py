from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from sqlalchemy import text

# 初始化插件
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # 读取刚才写的配置
    app.config.from_object(Config)

    # 绑定插件到 app
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # 【新增】 强制测试数据库连接
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print("\n" + "=" * 40)
            print("✅ 恭喜！数据库连接成功！(配置生效中)")
            print("=" * 40 + "\n")
        except Exception as e:
            print("\n" + "=" * 40)
            print("❌ 警告：数据库连接失败！")
            print(f"错误信息: {e}")
            print("=" * 40 + "\n")
            # 如果你想连接失败直接让程序崩溃退出，可以把下面这行注释取消
            # raise e

    # 注册蓝图
    # from app.api import bp as api_bp
    # app.register_blueprint(api_bp, url_prefix='/api')
    from app import models
    return app