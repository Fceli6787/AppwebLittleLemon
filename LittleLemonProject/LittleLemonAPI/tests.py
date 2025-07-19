from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Booking, Menu
import datetime

class BookingViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
        # Create test data
        self.booking = Booking.objects.create(
            user=self.user,
            name='Test Booking',
            no_of_guests=4,
            booking_date=datetime.datetime.now()
        )
        
    def test_get_bookings(self):
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_booking(self):
        url = reverse('booking-list')
        data = {
            'name': 'New Booking',
            'no_of_guests': 2,
            'booking_date': datetime.datetime.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_single_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        data = {'name': 'Updated Booking'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.name, 'Updated Booking')
        
    def test_delete_booking(self):
        url = reverse('booking-detail', args=[self.booking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class MenuViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
        # Create test data
        self.menu = Menu.objects.create(
            title='Test Menu',
            price=12.99,
            inventory=10
        )
        
    def test_get_menu(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_menu(self):
        url = reverse('menu-list')
        data = {
            'title': 'New Menu',
            'price': 9.99,
            'inventory': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_single_menu(self):
        url = reverse('menu-detail', args=[self.menu.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_menu(self):
        url = reverse('menu-detail', args=[self.menu.id])
        data = {'title': 'Updated Menu'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu.refresh_from_db()
        self.assertEqual(self.menu.title, 'Updated Menu')
        
    def test_delete_menu(self):
        url = reverse('menu-detail', args=[self.menu.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
