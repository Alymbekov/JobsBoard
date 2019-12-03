from django.urls import path
from jobs_board_main.views import get_jobs

urlpatterns = [
    # All jobs
    path('jobs/', get_jobs, name="jobs_view"),
]

