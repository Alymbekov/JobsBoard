from django.urls import path

from jobs_board_main.views import get_jobs, get_job, subscribe

urlpatterns = [
    # All jobs
    path('jobs/', get_jobs, name="jobs_view"),
    path('jobs/<int:id>/', get_job, name="job_view"),
    path('jobs/<int:id>/subscribe', subscribe, name="subscribe_view"),
]
