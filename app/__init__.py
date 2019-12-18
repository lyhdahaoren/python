#引入flask，跟模板
from flask import Flask, jsonify

#引入配置项 -->> config.py
from app.config import config

#引入扩展项 -->> extensions.py
from app.extensions import config_extensions

#引入蓝本配置项 -->> views/_init_.py
from app.api import config_blueprint

from app.error.error import CustomFlaskErr
from app.error.code import Code

def config_errorhandler(app):
    # 如果在蓝本定制，则只针对蓝本的错误有效。
    # 可以使用app_errorhandler定制全局有效的错误显示
    @app.errorhandler(CustomFlaskErr)
    def handle_flask_error(error):
        # response 的 json 内容为自定义错误代码和错误信息
        response = jsonify(error.to_dict())

        # response 返回 error 发生时定义的标准错误代码
        response.status_code = error.status_code

        return response




# 将创建app的动作封装成一个函数
def create_app(config_name):
    # 创建app实例对象
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config.get(config_name) or 'default')
    app.config.from_object(Code)
    # 执行额外的初始化
    config.get(config_name).init_app(app)

    #设置debug=True,让toolbar生效
    app.debug=True

    # 加载扩展
    config_extensions(app)

    # 配置蓝本
    config_blueprint(app)

    # 配置全局错误处理
    config_errorhandler(app)

    # 返回app实例对象
    return app