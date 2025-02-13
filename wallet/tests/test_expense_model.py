from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from wallet.models import Expense, Category

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

        self.expense = Expense.objects.create(
            user=self.user,
            description='Test Rescription',
            notes='Test Notes',
            amount=100.00,
            category=self.category,
            payment_date=timezone.now().date(),
            due_date=timezone.now().date(),
            payment_method='Test Method',
            status='Pendente',
            active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
    
    def test_expense_creation(self):
        expense = Expense.objects.get(user=self.user)
        
        self.assertEqual(expense.user, self.user)
        self.assertEqual(expense.description, 'Test Rescription')
        self.assertEqual(expense.notes, 'Test Notes')
        self.assertEqual(expense.amount, 100.00)
        self.assertEqual(expense.category, self.category)
        self.assertEqual(expense.payment_date, timezone.now().date())
        self.assertEqual(expense.due_date, timezone.now().date())
        self.assertEqual(expense.payment_method, 'Test Method')
        self.assertEqual(expense.status, 'Pendente')
        self.assertTrue(expense.active)
    
    def test_expense_count(self):
        self.assertEqual(Expense.objects.count(), 1)