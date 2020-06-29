from django.urls import path

from .views import (
    HomeView,
    MembersListView,
    MemberDetailView,
    ContributionsDashboardView,
)

app_name = 'ubumwe_app'
urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('dashboard', ContributionsDashboardView.as_view(), name='dashboard'),
    path('members', MembersListView.as_view(), name='members'),
    path('member/<slug>/', MemberDetailView.as_view(), name='member'),
]
