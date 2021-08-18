from django.urls import path
from . import views

urlpatterns = [
    path('', views.showReview, name='showReview' ),
    path('delete/<int:pk>', views.deleteReview, name='deleteReview'),
    path('update/<int:pk>', views.updateReview, name='updateReview'),
]