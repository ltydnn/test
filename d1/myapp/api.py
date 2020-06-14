from django.shortcuts import render

def submit_phone(request):
    '''提交手机号，发送验证码'''
    phone = request.POST.get('phone')
    
    return
def submit_vcode(request):
    '''提交短信验证码，登录'''
    return
def get_profile(request):
    '''获取个人资料'''
    return
def set_profile(request):
    '''修改个人资料'''
    return
def upload_avatar(request):
    '''头像上传'''
    return