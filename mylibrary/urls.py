"""mylibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
# from django.conf import settings #add this
# from django.conf.urls.static import static #add this
import management.api.urls
import static
from mylibrary import settings

urlpatterns = [
    path('', include(management.api.urls)),
    path('admin/', admin.site.urls),
    path('signup/', include(management.api.urls),),
    path('login/', include(management.api.urls)),
    path('logout/', include(management.api.urls)),
]

# urlpatterns = [
#     path('', include(management.urls)),
#     path('admin/', admin.site.urls),
#     path('signup/', include(management.urls),),
#     path('login/', include(management.urls)),
#     path('logout/', include(management.urls)),
#     path('book/', views.BookView, name='book'),
# ]


# if settings.DEBUG: #add this
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
