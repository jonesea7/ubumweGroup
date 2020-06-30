from django.urls import path

from .views import (
    HomeView,
    MainView,
    MembersListView,
    MemberDetailView,
    ContributionsDashboardView,
)

app_name = 'ubumwe_app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('main', MainView.as_view(), name='main'),
    path('dashboard', ContributionsDashboardView.as_view(), name='dashboard'),
    path('members', MembersListView.as_view(), name='members'),
    path('member/<slug>/', MemberDetailView.as_view(), name='member'),
]
