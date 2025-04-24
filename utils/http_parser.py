def parse_request(request_data):
    """Parseia os dados brutos da requisição HTTP"""
    if not request_data:
        return None
        
    # Decodifica os bytes para string
    try:
        decoded_data = request_data.decode('utf-8')
    except UnicodeDecodeError:
        return None
    
    lines = decoded_data.split('\r\n')
    request_line = lines[0].split()
    
    # Verifica se a linha de requisição tem os componentes mínimos
    if len(request_line) < 3:
        return None
    
    method, path, http_version = request_line
    
    # Extrai headers
    headers = {}
    for line in lines[1:]:
        if not line:
            break
        if ': ' in line:
            key, value = line.split(': ', 1)
            headers[key] = value
    
    # Corpo da requisição (para POST)
    body = None
    if '\r\n\r\n' in decoded_data:
        body = decoded_data.split('\r\n\r\n')[1]
    
    return {
        'method': method,
        'path': path,
        'version': http_version,
        'headers': headers,
        'body': body
    }