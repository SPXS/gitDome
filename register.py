
def register(username, email, password):
    # main 分支：添加密码强度检查
    if len(password) < 6:
        return False
    create_user(username, email, password)
    return True
def send_verification_email(email):
    pass


