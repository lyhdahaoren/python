# 引入app _init_.py   初始化app的函数
from app import create_app

# flask_script扩展提供向Flask插入外部脚本的功能
from flask_script import Manager

# 处理文件和目录的模块
import os

# flask_migrate主要是扩展数据库表结构
from flask_migrate import MigrateCommand

# 从环境变量中获取config_name
config_name = os.environ.get('FLASK_CONFIG') or 'default'

# 生成app -->>  调用app/_init_.py的create_app方法
app = create_app(config_name)

# flask-scripts只支持传入flask实例 或者函数返回flask实例
manager = Manager(app)

# 挂载数据库迁移脚本
manager.add_command('db',MigrateCommand)
#  python manage.py db init   初始化数据库,会创建一个migations文件夹,并且会在数据库中生成一个alembic_version表
#  python manage.py db migrate  创建迁移历史
#  python manage.py db upgrade  更新数据库

if __name__ == '__main__':
    manager.run()



