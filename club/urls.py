
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . views import UserViewSet, send_email
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('contact_us/', include('contact_us.urls')),
    path('service/', include('service.urls')),
    path('account/', include('account.urls')),
    path('banner/', include('banner.urls')),
    # path('blood/', include('blood.urls')),
    path('category/', include('category.urls')),
    path('transaction/', include('transaction.urls')),
    path('people/', include('people.urls')),
    path('post/', include('post.urls')),
    path('notice/', include('notice.urls')),
    path('event/', include('event.urls')),
    # path('message/', include('message.urls')),
    path('send-email/', send_email, name='send_email'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
