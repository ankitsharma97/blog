from django.shortcuts import render
from main import models
# Create your views here.
from django.http import Http404
from django.shortcuts import render,get_object_or_404

def index(request):
    latestArticle=models.Article.objects.all()[:10]
    context={
        "latestArticle":latestArticle
    }
    
    return render(request,'main/index.html',context)


def article(request,pk):
    # try:
    #     article=models.Article.objects.get(pk=pk)
    # except:
    #     raise Http404()
    
    article=get_object_or_404(models.Article,pk=pk)
    context={
        "article":article
    }
    return render(request,'main/article.html',context)



def author(request,pk):
    author=get_object_or_404(models.Article,pk=pk)
    context={
        "author":author
    }
    return render(request,'main/author.html',context)

def create_article(request):
    authors=models.Author.objects.all()
    context={
        "authors":authors
    }
    
    
    if request.method=="POST":
        article_data={
            "title":request.POST['title'],
            "content":request.POST['content'],
            
        }
        article=models.Article.objects.create(**article_data)
        author=models.Author.objects.filter(pk=request.POST['author'])
        article.authors.set(author)
        context["success"]=True
    
    return render(request,'main/create_article.html',context)