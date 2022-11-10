from django.urls import path
from .views import index, AdCreateView, edit, add_and_save, AdDetailView, \
    AdListView, AdUpdateView, AdDeleteView

app_name = 'bboard'

urlpatterns = [
    path('', index, name='list'),
    path('list/', AdListView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('create-func/', add_and_save),
    path('edit/<int:pk>', edit),
    path('update/<int:pk>', AdUpdateView.as_view()),
    path('detail/<int:pk>/', AdDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='delete'),
]
