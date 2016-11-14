from cgi import parse_qs, escape

def app(environ, start_response):
    qs = environ['QUERY_STRING']
    response_status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]

    start_response(status, response_headers)
    response = qs.split('&')
    body = ''
    for item in response:
        body += item + '\n'

    return [body]
