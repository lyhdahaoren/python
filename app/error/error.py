class CustomFlaskErr(Exception):
    # 默认的返回码
    status_code = 200

    # 自己定义了一个 return_code，作为更细颗粒度的错误代码
    def __init__(self, return_code=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict(self.payload or ())

        # 增加 dict key: return code
        rv['return_code'] = self.return_code

        # 增加 dict key: message, 具体内容由常量定义文件中通过 return_code 转化而来
        rv['message'] = J_MSG[self.return_code]

        # 日志打印
        logger.warning(J_MSG[self.return_code])

        return rv