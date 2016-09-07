from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
import datetime, json
from .models import Tjros

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    n = 10 #max number of objects to take from the model
    records = Tjros.objects.order_by('time')[:n]
    return render(request, 'graph/index.html', {'records': records})
    #return render(request, 'graph/index.html', {})

def detail(request, time):
    record = get_object_or_404(Tjros, time=time)
    return render(request, 'graph/detail.html', {'record': record})

def record_detail(request, time):
    record = get_object_or_404(Tjros, time=time)
    return render(request, 'graph/record_detail.html', {'record': record})

def chart_data_json(request):
    data = {}
    params = request.GET

    name = params.get('name', '')
    if name == 'water_level':
        data['chart_data'] = ChartData.get_water_level()

    return HttpResponse(json.dumps(data), content_type='application/json')

class LevelChartsView(TemplateView):
    template_name = 'chart/water_level.html'
