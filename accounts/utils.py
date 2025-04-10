import requests
import re

from accounts.models import ContactDetails


class Accounts:
    @staticmethod
    def get_cep_info(cep):
        url = f'https://cep.awesomeapi.com.br/json/{cep}'
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            address_dict = {
                'logradouro': data.get('address', ''),
                'bairro': data.get('district', ''),
                'cidade': data.get('city', ''),
                'estado': data.get('state', ''),
                'latitude': data.get('lat', ''),
                'longitude': data.get('lng', ''),
            }
            return address_dict
        else:
            raise Exception(f"Erro externo: {response.status_code} - {response.text}")

    @staticmethod
    def atualizar_info_contato(user, data_post):
        try:
            data_db = ContactDetails.objects.get(user=user)
        except ContactDetails.DoesNotExist:
            data_db = None

        contato = {
            'cep': data_post.get('cep', getattr(data_db, 'cep', None)),
            'address': data_post.get('logradouro', getattr(data_db, 'address', None)),
            'number_address': data_post.get('numero', getattr(data_db, 'number_address', None)),
            'district': data_post.get('bairro', getattr(data_db, 'district', None)),
            'city': data_post.get('cidade', getattr(data_db, 'city', None)),
            'state': data_post.get('uf', getattr(data_db, 'state', None)),
            'complement': data_post.get('complemento', getattr(data_db, 'complement', None)),
            'phone': data_post.get('telefone', getattr(data_db, 'phone', None)),
        }

        contato['cep'] = re.sub(r'\D', '', contato['cep'])
        contato['phone'] = re.sub(r'\D', '', contato['phone'])

        if data_db:
            return ContactDetails.objects.filter(user=user).update(**contato)
        else:
            return ContactDetails.objects.create(user=user, **contato)
