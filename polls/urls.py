from django.urls import path
from django.conf.urls import handler404
from . import views


app_name = "polls"
# handler404 = views.custom_404_view

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("test", views.test, name="test"),

#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),

# ]


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("test", views.test, name="test"),
    # path("test-404/", views.test_404, name="test_404"),
    
]