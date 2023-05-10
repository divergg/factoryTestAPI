"""
URL configuration for mailingapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Testing API",
        default_version="v1",
        description="Cервис управления рассылками API администрирования и получения статистики\n"
                    "Сущность 'рассылка' имеет атрибуты:\n"
                    "уникальный id рассылки, дата и время запуска рассылки текст сообщения для доставки клиенту\n"
                    "фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)\n"
                    "дата и время окончания рассылки: если по каким-то причинам не успели разослать все сообщения - никакие сообщения клиентам после этого времени доставляться не должны\n"
                    "Сущность клиент имеет атрибуты:\n"
                    "уникальный id клиента,  номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9)\n"
                    "код мобильного оператора, тег (произвольная метка), часовой пояс\n"
                    "Сущность сообщение имеет атрибуты:\n"
                    "уникальный id сообщения, дата и время создания (отправки), статус отправки\n"
                    "id рассылки, в рамках которой было отправлено сообщение, id клиента, которому отправили.",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
