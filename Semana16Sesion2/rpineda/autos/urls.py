from rest_framework.routers import SimpleRouter

from autos.views import CarViewSet

router = SimpleRouter()
router.register('cars', CarViewSet)
urlpatterns = router.urls


