from django.shortcuts import render
from visits.models import PageVisit


def home(request,*args,**kwargs):
    qs = PageVisit.objects.all()
    PageVisit.objects.create(path=request.path)
    context  = {'page_visits': qs,
                'page_visit_count': qs.count(),
                'page_total_percentage': qs.count() / 100,
                    }
    return render(request,'home.html',context)