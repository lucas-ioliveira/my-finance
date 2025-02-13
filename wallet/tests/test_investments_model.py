from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from wallet.models import Investments, Category

class ExpenseModelTest(TestCase):
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

        self.investments = Investments.objects.create(
            user=self.user,
            description='Test Rescription',
            notes='Test Notes',
            amount=100.00,
            category=self.category,
            investment_date=timezone.now().date(),
            investment_method='Test Method',
            status='Pendente',
            active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
    
    def test_investments_creation(self):
        investments = Investments.objects.get(user=self.user)
        
        self.assertEqual(investments.user, self.user)
        self.assertEqual(investments.description, 'Test Rescription')
        self.assertEqual(investments.notes, 'Test Notes')
        self.assertEqual(investments.amount, 100.00)
        self.assertEqual(investments.category, self.category)
        self.assertEqual(investments.investment_date, timezone.now().date())
        self.assertEqual(investments.investment_method, 'Test Method')
        self.assertEqual(investments.status, 'Pendente')
        self.assertTrue(investments.active)
    
    def test_investments_count(self):
        self.assertEqual(Investments.objects.count(), 1)