from django.urls import path

from weather import views


app_name = 'weather'


urlpatterns = [
    path('today/', views.CityWeatherView.as_view(), name='today'),
    path('user/city/create/', views.UserCityCreateView.as_view(), name='user_city_create'),
    path('user/city/list/', views.UserCityListView.as_view(), name='user_city_list'),
    path('user/city/delete/', views.UserCityBulkDeleteView.as_view(), name='user_city_delete'),


    path('city_list/', views.CityListView.as_view(), name='city_list_view'),
    path('<slug:slug>/', views.CityDetailView.as_view(), name='city_detail_view')
]
