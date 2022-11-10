
from django.http import HttpResponse, HttpResponseRedirect, \
    HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bboard.forms import AdForm
from bboard.models import Ad, Rubric


def index(request):
    ads = Ad.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'ads': ads})


def edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if request.method == 'POST':
        ad_form = AdForm(request.POST, instance=ad)
        if ad_form.is_valid():
            ad_form.save()
            return redirect('bboard:list')
        else:
            context = {'form': ad_form}
            return render(request, 'bboard/edit.html', context)
    else:
        ad_form = AdForm(instance=ad)
        context = {'form': ad_form}
        return render(request, 'bboard/edit.html', context)


def add_and_save(request):
    if request.method == 'POST':
        ad = AdForm(request.POST)
        if ad.is_valid():
            ad.save()
            return HttpResponseRedirect('/bboard/')
        else:
            context = {'form': ad}
            return render(request, 'bboard/create.html', context)
    else:
        ad = AdForm()
        context = {'form': ad}
        return render(request, 'bboard/create.html', context)


class AdCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = AdForm
    success_url = reverse_lazy('bboard:list')


class AdDetailView(DetailView):
    model = Ad
    template_name = 'bboard/ad_detail_1.html'


class AdListView(ListView):
    template_name = 'bboard/index.html'
    context_object_name = 'ads'
    queryset = Ad.objects.order_by('-published')


class AdUpdateView(UpdateView):
    template_name = 'bboard/create.html'
    form_class = AdForm
    model = Ad
    success_url = reverse_lazy('bboard:list')


class AdDeleteView(DeleteView):
    model = Ad
    success_url = reverse_lazy('bboard:list')