# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin



class TweetCreateView(FormUserNeededMixin, CreateView):
	# queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = '/tweet/create/'
	# login_rul = '/admin/'

	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated():
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD__ERRORS] = ErrorList(["user must be logged in to continue!"])
	# 		return self.form_invalid(form)
			

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

	def get_object(self):
		return Tweet.objects.get(id=1)


class TweetListView(ListView):
	queryset = Tweet.objects.all()
	template_name = 'tweets/list_view.html'

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context



# def tweet_detail_view(request, id=1):
# 	obj = Tweet.objects.get(id=id)
# 	print(obj)
# 	context = {
# 		"object": obj
# 	}
# 	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	print(queryset)
# 	for obj in queryset:
# 		print(obj.content)
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, "tweets/list_view.html", context)