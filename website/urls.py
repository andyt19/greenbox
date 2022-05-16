from django.contrib import admin
from django.urls import path
from website import views
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.viewall),
    path('viewall', views.viewall),
    path('addproduct', views.addproduct),
    path('addwarehouse', views.addwarehouse),
    path('update/<str:table>/<int:id>', views.update),
    path('edit/<str:table>/<int:id>', views.edit),
    path('delete/<str:table>/<int:id>', views.delete),
]
