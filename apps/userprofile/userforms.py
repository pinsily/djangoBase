import re

from django import forms

from front.models import Profile


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, help_text="username")
    email = forms.EmailField(label='email', help_text="email")
    password = forms.CharField(label='password', help_text="password", widget=forms.PasswordInput)
    re_password = forms.CharField(label='password confirmation', help_text="password confirmation",
                                  widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("用户名需大于(包含)3个字符")
        elif len(username) > 20:
            raise forms.ValidationError("用户名需小于(包含)20个字符")
        else:
            filter_result = Profile.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError('该用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = Profile.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("该邮箱已存在")
        else:
            raise forms.ValidationError("请输入正确的邮箱格式")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 3:
            raise forms.ValidationError("密码需大于(包含)3个字符")
        elif len(password) > 20:
            raise forms.ValidationError("密码需小于(包含)20个字符")

        return password

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise forms.ValidationError('两次密码不匹配')

        return re_password


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50, help_text="username or email")
    password = forms.CharField(label='password', widget=forms.PasswordInput, help_text="password")

    # print(username, password)
    # use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if email_check(username):
            filter_result = Profile.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError('该账号不存在')
        else:
            filter_result = Profile.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError('该账号不存在')

        return username
