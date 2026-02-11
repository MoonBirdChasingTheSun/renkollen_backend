import os
from dotenv import load_dotenv

# 加载 .env 文件里的变量
load_dotenv()

class Config:
    # 格式: mysql+pymysql://用户名:密码@地址:端口/数据库名
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:@localhost:3306/renkollen'

    # 禁用一个不需要的追踪功能，节省内存
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 密钥（随便写一串乱码，用于安全）
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key'