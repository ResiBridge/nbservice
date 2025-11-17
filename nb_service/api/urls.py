from django.urls import path
from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()

router.register('ic', views.ICViewSet)
router.register('service', views.ServiceViewSet)
router.register('application', views.ApplicationViewSet)
router.register('relation', views.RelationViewSet)
router.register('pentest', views.PenTestViewSet)

urlpatterns = router.urls + [
    path('graph/', views.GrafanaNodeGraphView.as_view(), name='grafana-graph'),
]

app_name = 'nb_service-api'