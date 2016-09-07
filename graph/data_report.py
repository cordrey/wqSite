from datetime import datetime, timedelta

#Need to change this to get all needed tables - use multiple imports?
from .models import Tjros


class ChartData(object):
    @classmethod
    def get_water_level():
        wq_data = Tjros.objects.order_by('time')

        data = {'dates': [], 'values': []}
        for sample in wq_data:
            data['dates'].append(['time'].strftime('%m/%d/%y %H:%M'))
            data['values'].append(['water_level']))

        return data
