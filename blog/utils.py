from django.conf import settings
import requests

def reCAPTCHA_is_valid(request):
    ''' reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    data = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()

    if result['success']:
        return True
    else:
        return False

def reCAPTCHA_Public_Key():
    return settings.RECAPTCHA_PUBLIC_KEY

def reCAPTCHA_Script():
    script = """
        <script src='https://www.google.com/recaptcha/api.js?hl=fa'></script>
        <div class="g-recaptcha" data-sitekey="{}"></div>
    """.format(settings.RECAPTCHA_PUBLIC_KEY)
    return script