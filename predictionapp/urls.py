from django.conf.urls import patterns, url

urlpatterns = patterns(
    'predictionapp.views',
    url(r'^$', 'index', name='Index'),
    url(r'^uploadsd/$', 'upload_seed_data', name='upload_seed_data'),
    url(r'^render/graph/$', 'render_graph', name='render_graph'),
)