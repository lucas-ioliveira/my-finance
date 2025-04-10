from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from wallet.models import Revenue, Category


class RevenueModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.category = Category.objects.create(
            user=self.user,
            name='Test Category',
            description='Test Description',
            active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        self.revenue = Revenue.objects.create(
            user=self.user,
            description='Test Rescription',
            notes='Test Notes',
            amount=100.00,
            category=self.category,
            payment_date=timezone.now().date(),
            payment_method='Test Method',
            status='Pendente',
            active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def test_revenue_creation(self):
        revenue = Revenue.objects.get(user=self.user)

        self.assertEqual(revenue.user, self.user)
        self.assertEqual(revenue.description, 'Test Rescription')
        self.assertEqual(revenue.notes, 'Test Notes')
        self.assertEqual(revenue.amount, 100.00)
        self.assertEqual(revenue.category, self.category)
        self.assertEqual(revenue.payment_date, timezone.now().date())
        self.assertEqual(revenue.payment_method, 'Test Method')
        self.assertEqual(revenue.status, 'Pendente')
        self.assertTrue(revenue.active)

    def test_revenue_count(self):
        self.assertEqual(Revenue.objects.count(), 1)
