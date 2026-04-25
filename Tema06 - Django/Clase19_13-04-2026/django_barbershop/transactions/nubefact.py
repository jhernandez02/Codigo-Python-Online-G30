import requests
from django.conf import settings
from pprint import pprint
from .models import Appointments
from services.models import Services
from .models import Customers
from datetime import datetime

def send_nubefact_invoice(appointment_instance: Appointments):
    url = settings.NUBEFACT.get('URL')
    token = settings.NUBEFACT.get('TOKEN')

    customer: Customers = appointment_instance.customer
    service: Services = appointment_instance.service

    cantidad = 1
    precio_unitario = float(service.price)
    valor_unitario = precio_unitario / 1.18

    total = precio_unitario * cantidad
    subtotal = total / 1.18
    igv = total - subtotal

    payload = {
        'operacion': 'generar_comprobante',
        'tipo_de_comprobante': 1,
        'serie': 'FFF1',
        'numero': 1,
        'sunat_transaction': 1,
        'cliente_tipo_de_documento': 6,
        'cliente_numero_de_documento': customer.document_number,
        'cliente_denominacion': customer.name,
        'cliente_direccion': customer.address,
        'cliente_email': customer.email,
        'fecha_de_emision': datetime.now().strftime('%d-%m-%Y'),
        'moneda': 1,
        'porcentaje_de_igv': 18.0,
        'total_gravada': subtotal,
        'total_igv': igv,
        'total': total,
        'enviar_automaticamente_a_la_sunat': True,
        'enviar_automaticamente_al_cliente': True,
        'items': [
            {
                'unidad_de_medida': 'ZZ',
                'codigo': 'S-001',
                'descripcion': service.name,
                'cantidad': cantidad,
                'valor_unitario': valor_unitario,
                'precio_unitario': precio_unitario,
                'subtotal': subtotal,
                'tipo_de_igv': 1,
                'igv': igv,
                'total': total,
                'anticipo_regularizacion': False,
            }
        ]
    }

    response = requests.post(
        url=url,
        headers={
            'Authorization': token,
            'Content-Type': 'application/json'
        },
        json=payload
    )
    json = response.json()
    status = response.status_code

    if status != 200:
        raise Exception(json['errors'])
    
    return json