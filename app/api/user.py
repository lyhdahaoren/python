import os
import time
from flask import Blueprint, current_app, redirect, url_for, flash, request, jsonify
from flask_restful import Api,Resource
from app.models import Qy_login
from app.extensions import db

# 创建蓝本对象
qy = Blueprint('user', __name__)

api_qy_login = Api(qy)


@api_qy_login.resource('/register')
class qyRegister(Resource):
    def post(self):
        requestData = request.form
        try:
            username = requestData.get('username')
            password = requestData.get('password')
            mobile = requestData.get('mobile')
            mobiles = Qy_login.query.filter_by(mobile=mobile).first()
            if mobiles is None:
                u = Qy_login(username=username, password=password, mobile=mobile)
                db.session.add(u)
                db.session.commit()
            else:
                return jsonify({'code': '400015', 'msg': '该用户已存在，请登录', 'data': ''})
        except:
            # print("{} User add : {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"),requestData['username']))
            print('failure')
            db.session.rollback()
            return {'code':401}
        else:
            # print("{} User add : {} success...".format(time.strftime("%Y-%m-%d %H:%M:%S"),requestData['username']))
            print('success')
            return jsonify({'code': '200', 'msg': '注册成功', 'data': ''})
        finally:
            db.session.close()


@api_qy_login.resource('/login')
class qyLogin(Resource):
    def post(selfs):
        requestData = request.form;
        username = requestData.get('username')
        password = requestData.get('password')
        human = Qy_login.query.filter_by(username=username).first()
        res = jsonify({'code': '400015', 'msg': '用户名或密码错误'})

        if human is None:
            return res
        else:
            res1 = {
                'code': '200',
                'msg': '登录成功',
                'data': human.username
            }
            print(Qy_login.query.filter_by(username=username).first().username)
            # if human.password != password:
            #     return res
            # else:
            return jsonify(res1)