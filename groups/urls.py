from django.urls import path
from .views import IndexView, LikeView

urlpatterns = [
    path('', IndexView.as_view()),
    path('like/', LikeView.as_view()),
]
