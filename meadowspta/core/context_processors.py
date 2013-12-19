from django.conf import settings

def view_variables(request):
    return {
        'meadows_site_url': settings.MEADOWS_SITE_URLS[settings.ENVIRONMENT],
        'meadows_map_url': 'https://maps.google.com/maps?q=1101+Helen+Drive+Millbrae,+CA+94030&hl=en&ll=37.602094,-122.418487&spn=0.004573,0.016158&sll=37.269174,-119.306607&sspn=10.362441,16.54541&hnear=1101+Helen+Dr,+Millbrae,+San+Mateo,+California+94030&t=m&z=16&layer=c&cbll=37.602093,-122.418482&panoid=eemM59uql4Hu_seTg4cBUg&cbp=11,217.17,,0,-4.18',
    }