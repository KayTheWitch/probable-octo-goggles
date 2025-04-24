def build_response(status_code, content_type, content, extra_headers=None):
    """Constrói uma resposta HTTP básica"""
    status_messages = {
        200: 'OK',
        201: 'Created',
        400: 'Bad Request',
        404: 'Not Found',
        500: 'Internal Server Error'
    }
    
    headers = {
        'Content-Type': content_type,
        'Content-Length': str(len(content)),
        'Connection': 'close',
        'Server': 'MeuServidorHTTP/1.0'
    }
    
    if extra_headers:
        headers.update(extra_headers)
    
    response_line = f"HTTP/1.1 {status_code} {status_messages.get(status_code, '')}\r\n"
    headers_section = ''.join(f"{k}: {v}\r\n" for k, v in headers.items())
    
    return (response_line + headers_section + '\r\n').encode() + content