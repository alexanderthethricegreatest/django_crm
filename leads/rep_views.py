from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead

def is_sales_rep(user):
    return user.groups.filter(name="Sales Reps").exists()

@login_required
@user_passes_test(is_sales_rep)
def rep_home(request):
    leads = Lead.objects.all()
    return render(request, "leads/rep_home.html", {"leads": leads, "user": request.user})

@login_required
@user_passes_test(is_sales_rep)
def rep_add_lead(request):
    if request.method == "POST":
        Lead.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            zip=request.POST.get("zip"),
            country=request.POST.get("country"),
            last_contacted=request.POST.get("last_contacted"),
            next_step=request.POST.get("next_step"),
            status=request.POST.get("status"),
            notes=request.POST.get("notes"),
            created_by=request.user,
        )
        return redirect("rep_home")
    return render(request, "leads/rep_add_lead.html")

@login_required
@user_passes_test(is_sales_rep)
def rep_edit_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)

    if lead.created_by != request.user:
        return render(request, "leads/unauthorized.html", status=403)

    if request.method == "POST":
        for field in ["name", "phone", "email", "address", "city", "state", "zip", "country", "last_contacted", "next_step", "status", "notes"]:
            setattr(lead, field, request.POST.get(field))
        lead.save()
        return redirect("rep_home")

    return render(request, "leads/rep_edit_lead.html", {"lead": lead})
