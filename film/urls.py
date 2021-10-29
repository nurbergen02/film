"""film URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from product.views
from .yasg import urlpatterns as doc_urls
from product.views import ProductReviewViewset, ProductViewset, RatingViewset

router = DefaultRouter()
router.register('reviews', ProductReviewViewset)
router.register('rating', RatingViewset)
router.register('products', ProductViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('account.urls')),
    path('api/v1/bookmark/', include('bookmak.urls'))
    # path('likes/', include('likes.ser'))
    # path('products/<int:pk>/likes/', include('likes.services')),
    # path('api/v1/', include('.urls'))
    # path('api/v1/', include('product.urls')),
    # path('api/v1/', include('order.urls'))
    # 127.0.0.1:8000/api/v1/products/,
]
urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

