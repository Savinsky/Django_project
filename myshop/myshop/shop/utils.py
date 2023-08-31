from .models import Category
#t = 'title'
#menu = [ {t:'', 'url_name':''},
#         {t:'', 'url_name':''},
#         {t:'', 'url_name':''},
#         {t:'', 'url_name':''},
#]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all() #annotate(Count('product'))
        # проверка пользователя на авторизацию с ограничением доступа к меню(добавление товаров и т.д)
        # is_authenticated
        #context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context