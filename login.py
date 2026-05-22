
def login(username, password):
    # 登录验证逻辑 - main 分支版本
    if username == "admin" and password == "123456":
        return True
    return False
def logout():
    # 清理会话
    clear_session()
def clear_session():
    pass
