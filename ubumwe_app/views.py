from django.shortcuts import render, get_object_or_404

from .models import Member, Contribution
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


class HomeView(ListView):
    model = Member
    template_name = 'home.html'

    def get(self, *args, **kwargs):
        return redirect('/main')


class MainView(View):

    def get(self, *args, **kwargs):
        total_contributions = 0
        try:
            members = Member.objects.all()

            for member in members:
                total_contributions += member.get_total_saved()

            # contributions = Contribution.objects.all()
            context = {
                'members_object': members,
                'members_count_object': members.count(),
                'contribution_object': f'{total_contributions:,}',
            }
            # print("****** total cont of members: ", members.count())
            return render(self.request, 'home.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "No members in this Kimina yet, please add members and try again.")
            return redirect('/main')


class MembersListView(ListView):
    model = Member
    template_name = 'members_view.html'


class MemberDetailView(DetailView):
    model = Member
    template_name = 'member_details.html'


class ContributionsDashboardView(View):

    def get(self, *args, **kwargs):
        total_contributions = 0
        try:
            members = Member.objects.all()

            for member in members:
                total_contributions += member.get_total_saved()

            # contributions = Contribution.objects.all()
            context = {
                'members_object': members,
                'contribution_object': f'{total_contributions:,}',
            }
            # print("****** total cont: ", total_contributions)
            return render(self.request, 'contributions_dashboard.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "No members in this Kimina yet, please add members and try again.")
            return redirect('/main')


#
#
# @login_required
# def add_to_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order already exists in the cart
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "This item quantity  was updated")
#             return redirect("ubumwe_app:order_summary")
#         else:
#             order.items.add(order_item)
#             messages.info(request, "This item was added to your cart")
#             return redirect("ubumwe_app:order_summary")
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "This item was added to your cart")
#         return redirect("ubumwe_app:order_summary")
#
#
# @login_required
# def remove_from_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order already exists in the cart
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             order.items.remove(order_item)
#             messages.info(request, "This item was removed from your cart")
#             return redirect("ubumwe_app:order_summary")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("ubumwe_app:product", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("ubumwe_app:product", slug=slug)
#
#
# @login_required
# def remove_single_item_from_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order already exists in the cart
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#                 order_item.save()
#             else:
#                 order.items.remove(order_item)
#             messages.info(request, "This item quantity was updated in your cart")
#             return redirect("ubumwe_app:order_summary")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("ubumwe_app:product", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("ubumwe_app:product", slug=slug)
