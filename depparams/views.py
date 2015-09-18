from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from depparams.models import Article, ArticleAttribute, CostParam
from django.db.models import ObjectDoesNotExist
from django.contrib import messages
import pdb


def article_creation_home(request):
    return render(request, 'depparams/create_article.html')


class ArticleCreationHomeSave(TemplateView):

    def post(self, request):
        try:
            article_name = request.POST['articlename'].strip()
            try:
                if Article.objects.get(name='%s' % article_name):
                    messages.add_message(request, messages.INFO, "Article name already taken. Please take a different name.")
                    return redirect('article_creation_home')
            except ObjectDoesNotExist:
                pass
            article_description = request.POST['articledescription'].strip()
            article = Article(name=article_name, description=article_description)
            article.save()
        except:
            messages.add_message(request, messages.INFO, 'Something went wrong. Please try again.')
            return redirect('article_creation_home')
        return redirect('article_creation_add_attributes', article_id=article.pk)


def article_creation_add_attributes(request, article_id):
    context = {'article_id': article_id}
    pdb.set_trace()
    return render(request, 'depparams/create_article_add_attributes.html', context)


class ArticleCreationAddAttributeSave(TemplateView):

    def post(self, request):
        try:
            pdb.set_trace()
            attribute_name = request.POST['attributename-0'].strip()
            article_id = request.POST['article-id'].strip()
            description = request.POST['description-attribute-0'].strip()
            try:
                article = Article.objects.get(pk=article_id)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.WARNING, 'Invalid article id.')
                return redirect('article_creation_add_attributes', article_id=article.pk)
            max_value = request.POST['max-value-attribute-0'].strip()
            min_value = request.POST['max-value-attribute-0'].strip()
            article_attribute = ArticleAttribute(name=attribute_name, target_article=article,
                                                 description=description, max_value=max_value, min_value=min_value)
        except:
            messages.add_message(request, messages.INFO, 'Something went wrong. Please try again.')
            return redirect('article_creation_add_attributes', article_id=article.pk)
        return redirect('article_creation_add_depparams', article_id=article_id)


def article_creation_add_depparams(request, article_id):
    return render(request, 'depparams/create_article_add_depparams.html')