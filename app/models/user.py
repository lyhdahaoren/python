from flask import current_app
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Qy_login(db.Model):
    __tablename__ = 'qy_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    mobile = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return self.username

    # 密码字段保护
    @property
    def password(self):
        raise AttributeError('密码是不可读属性')

    @password.setter
    def password(self, password):
        # 相当于执行  user.password_hash=password
        self.password_hash = generate_password_hash(password)

    # 密码的校验
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 用户登录生成token
    def generate_activate_token(self, expires_in=84000):
        # 创建用于生成token的类，需要传递秘钥和有效期expires_in默认=3600,expires_in=60
        s = Serializer(current_app.config['SECRET_KEY'], expires_in)
        # 生成包含有效信息(必须是字典数据)的token字符串
        return s.dumps({'id': self.id})