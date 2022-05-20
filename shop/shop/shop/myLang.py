from django.utils import translation
from .settings import LANGUAGE_CODE

class LangBasedOnSettingMiddleware(object):
    def process_request(self, request):
        language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()