# for Viewset
from .view_sets import EmailViewSet
from rest_framework.routers import DefaultRouter

# View set routers

router = DefaultRouter()
router.register(r'api/v1/emails', EmailViewSet, basename='email')
urlpatterns = router.urls