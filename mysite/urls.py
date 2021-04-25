
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/',
         UserCreateDoneTV.as_view(), name='register_done'),

    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls'))
]
