from django.urls import path

from .views import (
    HomeView,
    MemberDetailView,
    ContributionsDashboardView,
)

app_name = 'ubumwe_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard', ContributionsDashboardView.as_view(), name='dashboard'),
    path('member/<slug>/', MemberDetailView.as_view(), name='member'),
]
