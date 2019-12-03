from django.shortcuts import render

from jobs_board_main.models import Job


def get_jobs(request):
    # get all jobs from the DB
    jobs = Job.objects.all()
    return render(request, 'jobs_board_main/jobs.html', {'jobs': jobs})

