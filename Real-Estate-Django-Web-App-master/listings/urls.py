from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
      path('listing/<int:listing_id>/', views.listing, name='listing'),
    path('listing/<int:listing_id>/delete/', views.delete_listing, name='delete_listing'),
]