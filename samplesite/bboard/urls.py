from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import index, AdCreateView, edit, add_and_save, AdDetailView, \
    AdListView, AdUpdateView, AdDeleteView, api_rubrics, api_rubric_detail, \
    APIRubrics, APIRubricDetail, APIRubricViewSet

app_name = 'space'

router = DefaultRouter()
router.register('rubrics', APIRubricViewSet)

urlpatterns = [
    path('', index, name='list'),
    path('list/', AdListView.as_view(), name='list-class'),
    path('create/', AdCreateView.as_view()),
    path('create-func/', add_and_save),
    path('edit/<int:pk>', edit),
    path('update/<int:pk>', AdUpdateView.as_view()),
    path('detail/<int:id>/', AdDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='delete'),
    # path('api/rubrics/', APIRubrics.as_view()),
    # path('api/rubrics/<int:pk>/', APIRubricDetail.as_view()),
    path('api/', include(router.urls)),

]
