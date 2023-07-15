from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    send_mail(
    'Prueba de envio Django',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tempor sollicitudin augue, in finibus tellus tincidunt sed. Mauris fringilla, nulla ac rutrum finibus, ipsum nibh tempor lacus, sit amet gravida arcu massa nec enim. Aliquam erat volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tristique metus nec nisl eleifend, vel pulvinar nisi pellentesque. Integer feugiat sem nec varius malesuada.',
    'djangoexample18@gmail.com',
    ['gabrielsotoccoya@gmail.com'],
    fail_silently=False,
)
    return render(request, 'send/index.html')