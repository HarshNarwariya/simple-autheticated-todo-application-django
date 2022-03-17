from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('index/', view=views.index, name="index"),
    path('add_work/', view=views.CreateWork.as_view(), name="add_work"),
    path('work_list/', view=views.WorkList.as_view(), name="work_list"),
    path('work/<int:pk>/update/', view=views.WorkUpdate.as_view(), name='work_update'),
    path('work/<int:pk>/delete/', view=views.WorkDelete.as_view(), name='work_delete'),
]