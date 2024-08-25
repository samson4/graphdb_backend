from django.urls import path

from . import views

app_name = "table"

urlpatterns = [
    path("", views.Customers.as_view(), name="customers_list_api"),
    path("all/", views.CustomersViewSet.as_view(), name="customers"),
    path("graph/", views.GraphView.as_view(), name="graph"),
]
