from django.conf.urls import include, url
from .views import fbMssngrView
urlpatterns = [
    url(r'^66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/?$', fbMssngrView.as_view()) #A REVISAR EL r', esto se debio sacar de fbdeveloper 
]

#TOKEN CLIENTE: 4b319908429fe442b2894a6e5ab5c13e
