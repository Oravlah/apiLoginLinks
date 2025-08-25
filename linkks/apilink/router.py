from rest_framework.routers import DefaultRouter
from linkks.apilink.views import LinkViewSet


router_link = DefaultRouter()

router_link.register(prefix='link', basename='link', viewset=LinkViewSet)