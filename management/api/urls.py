from django.urls import path
from management.api import views
from management.api.views import BookAV, MemberAV, BookDetailAV, homepage, signup, login, logout
# import static
# import mylibrary.settings
urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('book/', BookAV.as_view(), name = 'book'),
    path('book/<int:pk>', BookDetailAV.as_view(), name = 'book-detail'),
    path('member/', MemberAV.as_view(), name = 'member'),
]
# urlpatterns += static(mylibrary.settings.STATIC_URL, document_root=mylibrary.settings.STATICFILES_DIRS)
# if settings.DEBUG:
#     urlpatterns += static(mylibrary.settings.STATIC_URL, document_root=mylibrary.settings.STATICFILES_DIRS)