from .views import view_all,PersonCreatView


from django.urls import path

urlpatterns = [
    path('',view_all,name = 'view_all'),
    # path('create/',PersonCreatView.as_view,name = 'create_person')
]