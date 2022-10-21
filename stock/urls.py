from rest_framework.routers import DefaultRouter
from .views import (
    CategoryView,
    BrandView,
    ProductView,
    FirmView,
)


router = DefaultRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)
router.register('firm', FirmView)

urlpatterns = router.urls
