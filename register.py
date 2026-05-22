def register(username, email, password):
    # main 分支：添加密码强度检查
    if len(password) < 6:
        return False
    # feature-auth 分支：添加邮箱验证
    if not is_valid_email(email):
        return False
    create_user(username, email, password)
    return True

def send_verification_email(email):
    pass
