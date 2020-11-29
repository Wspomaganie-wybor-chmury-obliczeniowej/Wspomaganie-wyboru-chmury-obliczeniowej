"""PycharmProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from Rekomender import views 
app_name = 'Rekomender'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create, name='create'), #mozliwosc stworzenia nowego pytania
    path('answers/', views.answers, name='answers'), # rezultal, jaki provider 
    path('user_questions/', views.user_questions, name='user_questions'),
    # path('questionnaire/', views.questionnaire, name='questionare'),# pytajnik
    path('questionnaire/<question_id>/', views.questionnaire, name='questionnaire'),
    path('identyfyUser/<question_id>/',views.identyfyUser, name='identyfyUser'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.home, name='home'),
]
