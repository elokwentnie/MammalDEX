from django.contrib import admin
from django.urls import path
from wildlife.views import MammalListView, MammalByRegionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mammals/', MammalListView.as_view(), name='mammal-list'),
    path('mammals/region/<int:region_id>/', MammalByRegionView.as_view(), name='mammals-by-region'),
]
