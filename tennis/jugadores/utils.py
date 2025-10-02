from django.conf import settings
from twilio.rest import Client

def enviar_mensaje_whatsapp(numero, mensaje):
    # Configura las credenciales de Twilio desde settings.py o variables de entorno
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:' + settings.TWILIO_WHATSAPP_NUMBER
    to_whatsapp_number = 'whatsapp:' + numero

    message = client.messages.create(
        body=mensaje,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    return message.sid
