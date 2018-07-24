from django.conf import settings

def version(request):
    return {'version': "1.4"}