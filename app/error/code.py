class Code:
    USER_NOT_EXISTS = 500015
    USER_PASSWORD_EXCEOTION = 500016

    J_MSG = {
        USER_NOT_EXISTS : '用户不存在',
        USER_PASSWORD_EXCEOTION : '账号或密码错误'
    }
    @staticmethod
    def init_app(app):
        pass