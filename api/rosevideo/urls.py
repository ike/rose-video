from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rosevideo.dvdrental import views as dvdviews
from rosevideo.welcome import views as welcomeviews

class RoseVideoDvdRental(routers.APIRootView):
    """
    Rose Video API v1
    """
    pass

class DocumentedRouter(routers.DefaultRouter):
    APIRootView = RoseVideoDvdRental

router = DocumentedRouter()
router.register(r'users', dvdviews.UserViewSet)
router.register(r'groups', dvdviews.GroupViewSet)
router.register(r'rentals', dvdviews.RentalViewSet)
router.register(r'payments', dvdviews.PaymentViewSet)
router.register(r'inventories', dvdviews.InventoryViewSet)
router.register(r'films', dvdviews.FilmViewSet)
router.register(r'renewals', dvdviews.RenewalViewSet)
router.register(r'customers', dvdviews.CustomerViewSet)
router.register(r'staffs', dvdviews.StaffViewSet)
router.register(r'stores', dvdviews.StoreViewSet)

urlpatterns = [
    path('', include(welcomeviews)),
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
