from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class SendEmailView(APIView):
    def post(self, request):
        username = request.data.get('username')
        subject = 'This is drf mail function'
        from_email = settings.EMAIL_HOST_USER
        to = ['labaderavindra1994@gmail.com']
        send_mail(username, subject, from_email, to)

        return Response({'message': 'Email sent successfully'})
