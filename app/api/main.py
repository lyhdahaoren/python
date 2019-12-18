import os
import time
from flask import Blueprint, current_app, redirect, url_for, flash, request, jsonify
from flask_restful import Api,Resource
# from app.models import Qy_login
from app.extensions import db

# 创建蓝本对象
main = Blueprint('main', __name__)

api_main = Api(main)

@api_main.resource('/a')
class minn(Resource):
    def get(self):
        return jsonify({'code': '400015', 'msg': '该用户已存在，请登录', 'data': ''})
