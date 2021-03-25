from rest_framework import routers
from .import views

router = routers.SimpleRouter()
router.register("myapi",views.ApiViewSet)
urlpatterns = router.urls