import base64

def encrypt_password(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

if __name__ == '__main__':
    print("Encrypted password is",encrypt_password("hello world"))