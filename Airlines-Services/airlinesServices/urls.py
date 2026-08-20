"""
URL configuration for airlinesServices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import sys
sys.dont_write_bytecode = True

from django.contrib import admin
from django.urls import include , path

from airlinesServices.views.views import index , doc
from airlinesServices.views.downloadPdfPresentation import downloadPdfPresentation

urlpatterns = [
    path("airlines/", include("airlines.urls")),
    path("trajectory/", include("trajectory.urls")),

    path('admin/', admin.site.urls),   

    path('doc/' , doc , name='doc'),
    path('', index, name='index')
]

''' view to download a pdf Presentation file '''
urlpatterns += [
    path('pdf/downloadPresentation/', downloadPdfPresentation , name='downloadPdfPresentation'),
]
