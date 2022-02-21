from django.db.models import Case, When
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from .models import MainCategory, SubCategory, BaseMerchandise, Merchandise
from accounts.tokens import jwt_authorization
from carts.forms import AddMerchandiseForm
from search.documents import MerchandiseDocument
from elasticsearch_dsl import Q


# Create your views here.


class HomeView(ListView):
    
    model = BaseMerchandise
    template_name = 'core/home.html'
    context_object_name = 'merchandises'
    paginate_by = 8
    merchandise_list = BaseMerchandise.objects.all().order_by('id')
    user = None
    search_document = MerchandiseDocument
    
    def __init__(self, **kwargs):
        try:
            self.user = self.request.user
        except:
            pass
        super().__init__(**kwargs)
    
    def get_queryset(self):
        if self.request.method == 'GET':
            if self.request.GET.get('search', ''):
                search_keyword = self.request.GET.get('search', '')
                q = Q(
                    'multi_match',
                    query=search_keyword, 
                    fuzziness='auto', 
                    fields=['name', 'description']
                )
                search = self.search_document.search().query(q)
                search_results = sorted(list(search.execute().to_dict()['hits']['hits']), key=lambda s : s['_score'])
                result_ids = [int(search_result['_id']) for search_result in search_results]
                self.merchandise_list = BaseMerchandise.objects.filter(id__in=result_ids).order_by('id')
        return self.merchandise_list


class MerchandiseDetail(DetailView):
    
    model = BaseMerchandise
    template_name = 'products/merchandise_detail.html'
    context_object_name = 'merchandise'
    
    def get(self, request, *args, **kwargs):
        add_to_cart = AddMerchandiseForm(initial={'quantity':1})
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if request.user:
            context['user'] = request.user
        context['option'] = Merchandise.objects.filter(basemerchandise=self.object)[0] # needs dropdown UI & mechandise loop
        context['add_to_cart'] = add_to_cart
        return self.render_to_response(context)