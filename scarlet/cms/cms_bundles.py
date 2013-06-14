from .internal_tags.forms import TagFilterForm
from .internal_tags import handler

from . import views, bundles, sites
from . import site

class TagListView(views.ListView):
    display_fields = ('name',)
    paginate_by = 100
    filter_form = TagFilterForm


class TagBundle(bundles.Bundle):
    main = TagListView()

    class Meta:
        primary_model_bundle = False
        model = handler.get_model()

class EmbedView(views.CMSView):
    def get(self, request, *args, **kwargs):
        tags = request.GET.get('tags')
        return self.render(request, tags=tags)

class WYSIWYG(bundles.BlankBundle):
    main = EmbedView(default_template='cms/insert_media.html')

site.register('tags', TagBundle(name='tags'), 20)
try:
    site.register('wysiwyg', WYSIWYG(name='wysiwyg'), 21)
except sites.AlreadyRegistered:
    pass
