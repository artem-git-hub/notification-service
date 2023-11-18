from pprint import pprint
import requests

from .models import Message, Dispatch, Client
from notification_service.settings import JWT_TOKEN

def send_message(message_data: dict):
    external_service_url = f"https://probe.fbrq.cloud/v1/send/{message_data.get('id')}"

    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(external_service_url, json=message_data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to external service: {e}")
        return None

def send_messages_for_dispatch(dispatch_id):

    dispatch = Dispatch.objects.get(pk=dispatch_id)

    clients = Client.objects.filter(
        operator_code=dispatch.client_filter_operator_code,
        tag=dispatch.client_filter_tag
    )

    for client in clients:
        message_data = {
            "id": list(clients).index(client),
            "phone": client.phone_number,
            "text": dispatch.message_text,  
        }

        response = send_message(message_data)

        pprint(response)

        Message.objects.create(
            dispatch=dispatch,
            client=client,
            status="success" if response else "failed",
        )
        