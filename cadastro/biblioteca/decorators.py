import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

def book_registration_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        if isinstance(response, JsonResponse) and response.status_code == 200:
            data = response.json()
            data['message'] = 'Livro cadastrado com sucesso e decorado!'
            new_response = JsonResponse(data, status=200)
            new_response['Custom-Header'] = 'Value'
            logger.info('Livro cadastrado com sucesso!')
            return new_response
        return response
    return wrapper