from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from wallet.models import Category

class CategoryModelTest(TestCase):
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
    
    def test_category_creation(self):
        category = Category.objects.get(user=self.user)
        
        self.assertEqual(category.user, self.user)
        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.description, 'Test Description')
        self.assertTrue(category.active)
    
    def test_category_count(self):
        self.assertEqual(Category.objects.count(), 1)