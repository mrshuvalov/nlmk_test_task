from rest_framework.routers import DefaultRouter
from api.views import TableViewSet

router = DefaultRouter()

router.register(r'table', TableViewSet)

urlpatterns = router.urls
