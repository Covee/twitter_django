from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='패스워드 확인', widget=forms.PasswordInput)

	def clean_password2(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError("패스워드는 일치해야 아이디 만들어 줄꺼임 훙훙")
		return password2

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username__icontains=username).exists():
			raise forms.ValidationError("유저 이름 딴애가 이미 쓰고있당. 좀 더 창의력을 발휘해보세영")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email__icontains=email).exists():
			raise forms.ValidationError("이미 등록된 이메일이야. 우리의 첫만남을 벌써 잊은거니..?")
		return email