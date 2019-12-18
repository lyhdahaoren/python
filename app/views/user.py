import os
import time
from flask import Blueprint, current_app, redirect, url_for, flash, request, jsonify
from flask_restful import Api,Resource
from app.models import Qy_login
from app.extensions import db

# 创建蓝本对象
qy = Blueprint('qy', __name__)

api_qy_login = Api(qy)


class qyRegister(Resource):
    def post(self):
        requestData = request.form
        try:
            username = requestData.get('username')
            password = requestData.get('password')
            mobile = requestData.get('mobile')
            mobiles = Qy_login.query.filter_by(mobile=mobile).first()
            if mobiles is None:
                if mobiles.username == username:
                    return jsonify({'code': '400015', 'msg': '该用户已存在，请登录', 'data': ''})
                u = Qy_login(username=username, password=password, mobile=mobile)
                db.session.add(u)
                db.session.commit()
            else:
                return jsonify({'code': '400015', 'msg': '该用户已存在，请登录', 'data': ''})
        except:
            # print("{} User add : {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"),requestData['username']))
            print('failure')
            db.session.rollback()
            return False
        else:
            # print("{} User add : {} success...".format(time.strftime("%Y-%m-%d %H:%M:%S"),requestData['username']))
            print('success')
            return jsonify({'code': '200', 'msg': '注册成功', 'data': ''})
        finally:
            db.session.close()

api_qy_login.add_resource(qyRegister, '/register', endpoint= 'register')