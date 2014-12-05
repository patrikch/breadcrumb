from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"projects",views.ProjectViewSet)
router.register(r"waves",views.WaveViewSet)
router.register(r"shops",views.ShopViewSet)
