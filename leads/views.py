from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lead
from .forms import LeadForm

@login_required
def leads_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/list.html', {'leads': leads})

@login_required
def lead_add(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            return redirect('leads_list')
    else:
        form = LeadForm()
    return render(request, 'leads/form.html', {'form': form})

@login_required
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads_list')
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads/form.html', {'form': form})