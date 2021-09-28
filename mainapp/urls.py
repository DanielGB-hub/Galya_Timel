from django.urls import path
from Galya_Timel import views

urlpatterns = [
    path('api/category/', views.CategoryListCreate.as_view()),
    path('api/photocard/', views.PhotoCardListCreate.as_view()),
    path('api/textblock/', views.TextBlockListCreate.as_view()),
    path('api/imageblock/', views.ImageBlockListCreate.as_view()),
]