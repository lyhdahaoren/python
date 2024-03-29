#扩展

#bootstrap
#from flask_bootstrap import Bootstrap

#sql
from flask_sqlalchemy import SQLAlchemy

#数据库扩展
from flask_migrate import Migrate

#电话邮件插件
from flask_mail import Mail

#日期时间处理插件
from flask_moment import Moment

#登录系统插件
#from flask_login import LoginManager

#上传file插件
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class

#debug插件
from flask_debugtoolbar import DebugToolbarExtension

#富文本插件
#from flask_ckeditor import CKEditor

#缓存插件
from flask_cache import Cache

# 创建对象
#bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
moment = Moment()
#login_manager = LoginManager()
#上传
photos = UploadSet('photos',IMAGES)
#调试工具
toolbar = DebugToolbarExtension()
#富文本
#ckeditor = CKEditor()
#缓存页面
# cache=Cache()

# 初始化
def config_extensions(app):
    #bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    #login_manager.init_app(app)
    toolbar.init_app(app)
    # cache.init_app(app,config={'CACHE_TYPE':'redis'})

    # ckeditor.init_app(app)
    #一些图片上传的配置
    #configure_uploads(app,photos)
    #设置上传文件大小
    #patch_request_class(app,size=None)

    #指定登录的端点
    #login_manager.login_view = 'users.login'

    #需要登录时的提示信息
    #login_manager.login_message = '需要先登录'
    # 设置session保护级别
    # None：禁用session保护
    # 'basic'：基本的保护，默认选项
    # 'strong'：最严格的保护，一旦用户登录信息改变，立即退出登录
    #login_manager.session_protection = 'strong'

