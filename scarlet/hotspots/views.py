from django.http import JsonResponse, HttpResponseBadRequest
from django.views.generic import View
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin


from . import models, cms_forms


class HotSpotsGetData(LoginRequiredMixin, View):
    """
    Getting hotspots for given module
    """
    login_url = '/'
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        hotspot_module = None
        hotspots = []
        fields = ''

        try:
            hotspot_module = models.HotSpotModule.objects.get(pk=kwargs.get('slug'))
        except models.HotSpot.DoesNotExist:
            return HttpResponseBadRequest()

        for item in hotspot_module.hotspots.all().order_by('order'):
            hotspots.append({
                'x': item.x_cord,
                'y': item.y_cord,
                'label': item.label,
                'order': item.order,
            })

            form = cms_forms.HotSpotForm(instance=item, auto_id='%s-input-{0}-{1}'.format(item.x_cord, item.y_cord))

            print form.instance.order

            if form.instance.image:
                print form.instance.image.file.url

            context = {
                'x': item.x_cord,
                'y': item.y_cord,
                'form': form,
            }

            fields += render_to_string('hotspots/fieldsets.html', context)

        fields = fields.replace('\n', '')

        empty_fields = render_to_string('hotspots/fieldsets.html', {'form': cms_forms.HotSpotForm()})

        return JsonResponse({'hotspots': hotspots, 'fields': fields, 'emptyFields': empty_fields})