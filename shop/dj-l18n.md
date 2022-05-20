# Django локализация. 
      
## Настройки под локализацию.

Функции для переводов.

    from django.utils.translation import ugettext_lazy as _
    from django.utils.translation import ugettext as _

lasy - ленивый перевод. Это когда переводит каждый раз заново по факту требования. Рекомендуется использовать в формах и моделях т.к. они исполняются один раз при загрузке приложения и нам возможно понадобится в последствии получить разный перевод полей на разных языках.

Переключение локали по дефолту.

    LANGUAGE_CODE = 'ru'

Настройки папки для переводов.

    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

Список языков.

    from django.utils.translation import ugettext_lazy as _

    LANGUAGES = (
        ('ru', _('Russian')),
        ('en', _('English')),
    )

Локализация полей админки.

    from django.utils.translation import ugettext as _

    ... 

    image = models.ImageField(verbose_name=_(u'Image')...

Локализация шаблонов интерфейса.

    {% load i18n %}

    ...

    <title>{% translate "This is the title." %}</title>

Переключение языков.

    from django.utils import translation

    def set_language(request):
        next = request.REQUEST.get('next', None)
        if not next:
            next = request.META.get('HTTP_REFERER', None)
        if not next:
            next = '/'
        response = http.HttpResponseRedirect(next)
        if request.method == 'GET':
            lang_code = request.GET.get('language', None)
            if lang_code and check_for_language(lang_code):
                if hasattr(request, 'session'):
                    request.session['django_language'] = lang_code
                else:
                    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
                translation.activate(lang_code)
        return response

Получение текущего языка в шаблоне.

    {% load i18n %}
    ...
    {% get_current_language as LANGUAGE_CODE %}

Более изыскано через шаблонный процессор.

    def lang_context_processor(request):
        return {'LANG': request.LANGUAGE_CODE}

С последующим включением в настройки.

    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'myproject.myapp.templatecontext.lang_context_processor',
    )


## Инструмент для перевода rosetta

[ссылка на документацию](https://django-rosetta.readthedocs.io/)

Установка

    pip install django-rosetta

Включаем в проект.

    INSTALLED_APPS = [
        ..
        'rosetta',    

Включаем роутинг.

    path('rosetta/', include('rosetta.urls')),
    
Создаем папку locale.

Прописываем путь к локалям

    LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

Генерируем файлы переводов.

    ./manage.py makemessages -l ru

    ./manage.py compilemessages
    
Портируем переводы по дефолту

    

Перевод через яндекс.

    ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
    YANDEX_TRANSLATE_KEY = 'trnsl.1.1.20140521T130035Z.1014ae2799c685e3.97b1345108ab3a8520d96f730016a9dac947049b'
    ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'en'
    ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'English'

## Перевод модели.

[ссылка на документацию](https://django-modeltranslation.readthedocs.io/en/latest/)

Установка.

    pip install django-modeltranslation


Включение ДО django.contrib.admin! 

    INSTALLED_APPS = (
        ...
        'modeltranslation',
        'django.contrib.admin',  # optional
        ....
    )

Должен присутствовать список языков.

    LANGUAGES = (
        ('de', gettext('German')),
        ('en', gettext('English')),
    )
 
Перевод по дефолту.

    MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

### Перевод модели.

Создаем translation.py в папке приложения где подключаем класс перевода к классу существующей модели.

    from modeltranslation.translator import translator, TranslationOptions
    from .models import News

    class NewsTranslationOptions(TranslationOptions):
        fields = ('title', 'text')

    translator.register(News, NewsTranslationOptions)

Интеграция с админкой.

    from django.contrib import admin
    from news.models import News
    from modeltranslation.admin import TranslationAdmin

    class NewsAdmin(TranslationAdmin):
        pass

    admin.site.register(News, NewsAdmin)

Команда заполнения перевода дефолтного языка (перенос из старого поля).

    python manage.py update_translation_fields

Апдейт полей при добавлении нового языка или нового поля для перевода.

    python manage.py sync_translation_fields

Загрузка данных из json.

    python manage.py loaddata --populate=all fixtures.json



