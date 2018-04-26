from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
	content = forms.CharField(label='',
				widget=forms.Textarea(
						attrs={'placeholder':'내용을 입력하세요',
								'class':'form-control'}))
	class Meta:
		model = Tweet
		fields = [
			# "user",
			"content",
		]
		# exclude = ['user']     # if i dont want this field, use 'exclude'

	def clean_content(self, *args, **kwargs):
		content = self.cleaned_data.get("content")
		if content == "abc":
			raise forms.ValidationError("cannot be ABC")
		return content