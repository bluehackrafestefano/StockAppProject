from rest_framework.routers import DefaultRouter
from .views import (
    CategoryView,
    BrandView,
    ProductView,
    FirmView,
    StockView,
)


router = DefaultRouter()
router.register('category', CategoryView)
router.register('brand', BrandView)
router.register('product', ProductView)
router.register('firm', FirmView)
router.register('stock', StockView)

urlpatterns = router.urls
