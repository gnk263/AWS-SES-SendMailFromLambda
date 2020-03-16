import boto3
from email.header import Header

SENDER_ADDRESS = 'no-reply@example.com'
SENDER_NAME = '私だ'

ses = boto3.client('ses', region_name='eu-west-1')


def lambda_handler(event, context):
    to_address = 'hoge@example.com'
    subject = 'テストメール'
    body = 'これはテストメールです。'
    send(to_address, subject, body)


def send(to_address, subject: str, body: str):
    display_name = '{0}<{1}>'.format(
        Header(SENDER_NAME, 'utf-8').encode(),
        SENDER_ADDRESS
    )

    ses.send_email(
        Source=display_name,
        Destination={
            'ToAddresses': [to_address],
            'CcAddresses': [],
            'BccAddresses': []
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
