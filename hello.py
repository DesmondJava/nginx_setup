from cgi import parse_qs, escape

def app(environ, start_response):
    string = environ['QUERY_STRING']
    
    status = '200 OK'
    
    response_headers = [('Content-Type', 'text/plain')]

    start_response(status, response_headers)
    resp = string.split('&')
    body = ''
    for item in resp:
        body += item + '\n'

    return [body]
