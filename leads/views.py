from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lead

@login_required
def dashboard(request):
    leads = Lead.objects.all()
    total = leads.count()
    closed = leads.filter(status__iexact="closed").count()
    open_ = total - closed
    pie_data = {
        "labels": ["Closed", "Open"],
        "values": [closed, open_]
    }
    return render(request, "leads/dashboard.html", {
        "total": total,
        "closed": closed,
        "pie_data": pie_data
    })

@login_required
def leads_list(request):
    query = request.GET.get("q", "")
    leads = Lead.objects.all()
    if query:
        leads = leads.filter(name__icontains=query)
    return render(request, "leads/list.html", {"leads": leads, "query": query})