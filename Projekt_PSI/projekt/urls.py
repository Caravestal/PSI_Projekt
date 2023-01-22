from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from . import views


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onas/', views.onas),
    path('', views.strona),
    url(r'^api-auth/', include('rest_framework.urls')),

    path('Nauczyciele',views.NauczycieleList.as_view(), name=views.NauczycieleList.name),
    path('Nauczyciele/<int:pk>',views.NauczycieleDetail.as_view(), name=views.NauczycieleDetail.name),
    path('LekcjeNauczycieli', views.LekcjeNauczycieliList.as_view(), name=views.LekcjeNauczycieli.name),
    path('LekcjeNauczycieli/<int:pk>', views.LekcjeNauczycieliDetail.as_view(), name=views.LekcjeNauczycieli.name),
    path('Lekcje', views.Lekcje.as_view(), name=views.LekcjeList.name),
    path('Lekcje/<int:pk>', views.LekcjeDetail.as_view(), name=views.LekcjeDetail.name),
    path('LekcjeUczniow', views.LekcjeUczniowList.as_view(), name=views.LekcjeUczniow.name),
    path('LekcjeUczniow/<int:pk>', views.LekcjeUczniowDetail.as_view(), name=views.LekcjeUczniow.name),
    path('Platnosci', views.PlatnosciList.as_view(), name=views.PlatnosciList.name),
    path('Platnosci/<int:pk>', views.PlatnosciDetail.as_view(), name=views.PlatnosciDetail.name),
    path('EgzaminyUczniow', views.EgzaminyUczniowList.as_view(), name=views.EgzaminyUczniowList.name),
    path('EgzaminyUczniow/<int:pk>', views.EgzaminyUczniowDetail.as_view(), name=views.EgzaminyUczniowDetail.name),
    path('Egzaminy', views.EgzaminyList.as_view(), name=views.EgzaminyList.name),
    path('Egzaminy/<int:pk>', views.EgzaminyDetail.as_view(), name=views.EgzaminyDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
