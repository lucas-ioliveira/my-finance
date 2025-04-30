from django.contrib.auth.models import User

from accounts.models import ContactDetails


class AccountRepository:
    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def get_contact_details(user):
        return ContactDetails.objects.filter(user=user).first()

    @staticmethod
    def update_user(user_id, nome, sobrenome, email):
        user = User.objects.get(id=user_id)
        user.first_name = nome
        user.last_name = sobrenome
        user.email = email
        user.save()

    @staticmethod
    def update_contact_details(user, telefone, cep, logradouro, numero, bairro, cidade, estado, complemento):
        try:
            data_db = ContactDetails.objects.get(user__id=user.id)
        except ContactDetails.DoesNotExist:
            data_db = None

        contact_details = {
            'phone': telefone,
            'cep': cep,
            'address': logradouro,
            'number_address': numero,
            'district': bairro,
            'city': cidade,
            'state': estado,
            'complement': complemento
        }

        if data_db:
            return ContactDetails.objects.filter(user__id=user.id).update(**contact_details)
        else:
            return ContactDetails.objects.create(user=user, **contact_details)
