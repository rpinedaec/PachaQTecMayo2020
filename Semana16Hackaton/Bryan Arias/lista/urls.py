from rest_framework.routers import SimpleRouter

from lista.views import ArtistaViewSet

router = SimpleRouter()
router.register('Artista', ArtistaViewSet)
urlpatterns = router.urls


