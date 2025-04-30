import requests
import re

from accounts.repositories.repository import AccountRepository


class AccountService:
    @staticmethod
    def get_cep_info(request):
        try:
            cep = re.sub(r'\D', '', request.GET.get("cep"))
        except Exception:
            raise Exception("CEP inválido.")

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
    def update_user(request):
        user_id = request.user.id
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        AccountRepository.update_user(user_id, nome, sobrenome, email)

    @staticmethod
    def update_contact_details(request):
        user = request.user
        telefone = re.sub(r'\D', '', request.POST.get('telefone'))
        cep = re.sub(r'\D', '', request.POST.get('cep'))
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('uf')
        complemento = request.POST.get('complemento')

        AccountRepository.update_contact_details(user, telefone, cep, logradouro, numero, bairro, cidade, estado, complemento)
