from .models import Article
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "body"]
    template_name = "article_new.html"
    success_url = reverse_lazy("article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "body"]
    template_name = "article_update.html"
    success_url = reverse_lazy("article_list")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
