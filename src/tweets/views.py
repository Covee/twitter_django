from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, DeleteView, ListView, CreateView, UpdateView

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin



class TweetCreateView(FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/update_view.html'
	# success_url = '/tweet/'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
	queryset = Tweet.objects.all()
	template_name = 'tweets/delete_confirm.html'
	success_url = reverse_lazy("tweet:list")
			

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
	template_name = 'tweets/detail_view.html'


class TweetListView(ListView):
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)
				)
		return qs

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