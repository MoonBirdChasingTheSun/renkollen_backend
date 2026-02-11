from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# 1. 用户表 (User) - 对应图中左侧的 User 表
class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(256))  # 密码我改成了储存hash值
    email = db.Column(db.String(50), unique=True)
    admin = db.Column(db.Boolean, default=False)

    # 关系：一个用户可以有多条评论，也可以记录多个事件
    comments = db.relationship('Comment', backref='user', lazy=True)
    recorded_events = db.relationship('ReindeerEvent', backref='recorder', lazy=True)

    # 【新增方法】 密码hash值设置与验证
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.first_name}>'


# 2. 主人表 (Owner) - 对应图中上方的 Owner 表
class Owner(db.Model):
    __tablename__ = 'owner'

    owner_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))  # 图中未标长度，暂设100
    email = db.Column(db.String(100))

    # 关系：一个主人有多只驯鹿
    reindeers = db.relationship('Reindeer', backref='owner', lazy=True)

    def __repr__(self):
        return f'<Owner {self.owner_id}>'


class Reindeer(db.Model):
    __tablename__ = 'reindeer'

    # 【改动】Integer 作为数据库内部的主键（给外键用，速度快）
    reindeer_id = db.Column(db.Integer, primary_key=True)

    # 【新增】农场主使用的“ID”（比如 'F-01-A'），用 String 存
    ear_tag = db.Column(db.String(50), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    owner_id = db.Column(db.String(20), db.ForeignKey('owner.owner_id'))
    mother_owner_id = db.Column(db.String(20))
    birth_year = db.Column(db.Integer)

    # 如果母亲ID也是字母+数字，这里必须用 String
    mother_ear_tag = db.Column(db.String(50))

    comment = db.Column(db.String(500))
    life_slaughter = db.Column(db.Boolean)
    vaja = db.Column(db.Boolean)

    events = db.relationship('ReindeerEvent', backref='reindeer', lazy=True)
    comments = db.relationship('Comment', backref='reindeer', lazy=True)

    def __repr__(self):
        return f'<Reindeer {self.ear_tag}>'


# 4. 评论表 (Comments) - 对应图中下方的 Comments 表
class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)

    # 谁评论的？
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # 评论哪只鹿？
    reindeer_id = db.Column(db.Integer, db.ForeignKey('reindeer.reindeer_id'))

    text = db.Column(db.String(500))
    created_at = db.Column(db.Date, default=datetime.utcnow)
    updated_at = db.Column(db.Date, onupdate=datetime.utcnow)


# 5. 驯鹿事件表 (Reindeer_events) - 对应图中右侧的表
class ReindeerEvent(db.Model):
    __tablename__ = 'reindeer_events'

    reindeer_event_id = db.Column(db.Integer, primary_key=True)
    reindeer_id = db.Column(db.Integer, db.ForeignKey('reindeer.reindeer_id'))

    # 记录员 ID
    recorded_by_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    event_season = db.Column(db.String(64))
    modified_date = db.Column(db.Date)
    weight = db.Column(db.Integer)
    life_slaughter = db.Column(db.Boolean)