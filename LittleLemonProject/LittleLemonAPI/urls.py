from django.urls import path
from .views import BookingList, BookingDetail, MenuList, MenuDetail

urlpatterns = [
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('menu/', MenuList.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
]
