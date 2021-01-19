import base64
# If You Want
# ctfs = [{'name':'Blue Fish','type':'PWN'},{'name':'CTF2','type':'PWN'},{'name':'CTF3','type':'PWN'},{'name':'CT4','type':'PWN'},{'name':'CTF5','type':'PWN'}]
ctf = {'name':'Blue Fish','type':'PWN'}
flag = 'VVZkYWNHRXlPWFJaVnpVM1dXMTRNVnBXT1cxaFdFNXZXREphZVZwWVRtOWFXRW81'
password = 'QWZpa29tYW57NDQ2ODE2NGZiMzMyOWE1NDlmMzdiM2M5ZTdjZjE3ZjJkMTU1MmY5Y2YzMWQ1ZmNhMjgxNDIyOTA4NjhkZDNlNmM5ZTE4NDU5YmJlZWI1NGQ1YTIwMzZkYTFkZDFiZDdhMWFkMWQ4NDY3NTVkOGI1NWY2YzhkZjdlY2ZlYjlhNGJ9'

def check(user_password):
    base64_bytes = password.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    
    if user_password ==  message:
        return 'Goog Job!\nrfc 3548 rfc 4648! X3'+flag
    else:
        return 'Wrong, Try Again.'