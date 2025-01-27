import requests

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
        data_db = ContactDetails.objects.get(user=user)
        contato = {
            'cep': data_post.get('cep', data_db.cep),
            'address': data_post.get('logradouro', data_db.address),
            'number_address': data_post.get('numero', data_db.number_address),
            'district': data_post.get('bairro', data_db.district),
            'city': data_post.get('cidade', data_db.city),
            'state': data_post.get('estado', data_db.state),
            'complement': data_post.get('complemento', data_db.complement),
            'phone': data_post.get('telefone', data_db.phone),
        }
        return ContactDetails.objects.filter(user=user).update(**contato)
