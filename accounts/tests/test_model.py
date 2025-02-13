from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import ContactDetails


class ContactDetailsModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.contact_details = ContactDetails.objects.create(
            user=self.user,
            phone='1234567890',
            cep='12345678',
            address='Rua Teste',
            number_address='123',
            district='Bairro Teste',
            city='Cidade Teste',
            state='SP',
            complement='Complemento Teste',
            active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def test_contact_details_creation(self):
        contact_details = ContactDetails.objects.get(user=self.user)
        
        self.assertEqual(contact_details.user, self.user)
        self.assertEqual(contact_details.cep, '12345678')
        self.assertEqual(contact_details.address, 'Rua Teste')
        self.assertEqual(contact_details.number_address, '123')
        self.assertEqual(contact_details.district, 'Bairro Teste')
        self.assertEqual(contact_details.city, 'Cidade Teste')
        self.assertEqual(contact_details.state, 'SP')
        self.assertEqual(contact_details.complement, 'Complemento Teste')
        self.assertTrue(contact_details.active)

    def test_contact_details_count(self):
        self.assertEqual(ContactDetails.objects.count(), 1)
