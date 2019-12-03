from django.shortcuts import render

from jobs_board_main.models import Job, Subscriber, Subscription


def get_jobs(request):
    # get all jobs from the DB
    jobs = Job.objects.all()
    return render(request, 'jobs_board_main/jobs.html', {'jobs': jobs})


def get_job(request, id):
   job = Job.objects.get(pk=id)
   return render(request, 'jobs_board_main/job.html', {'job': job})


def subscribe(request, id):
    job = Job.objects.get(pk=id)
    sub = Subscriber(email=request.POST['email'])
    sub.save()

    subscription = Subscription(user=sub, job=job)
    subscription.save()

    payload = {
        'job': job,
        'email': request.POST['email']
    }
    return render(request, 'jobs_board_main/subscribed.html', {'payload': payload})
