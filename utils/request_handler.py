import os
from utils.http_parser import parse_request
from utils.response_builder import build_response

def serve_static_file(file_path):
    """Serve arquivos estáticos"""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Determina o Content-Type baseado na extensão
        ext = os.path.splitext(file_path)[1].lower()
        content_types = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.ico': 'image/x-icon',
            '.svg': 'image/svg+xml'
        }
        
        return build_response(
            200,
            content_types.get(ext, 'application/octet-stream'),
            content
        )
    except FileNotFoundError:
        return build_response(404, 'text/html', b'<h1>404 Not Found</h1>')
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return build_response(500, 'text/html', b'<h1>500 Internal Server Error</h1>')

def handle_request(request_data):
    """Lida com a requisição HTTP e retorna a resposta apropriada"""
    parsed = parse_request(request_data)
    if not parsed:
        return build_response(400, 'text/html', b'<h1>400 Bad Request</h1>')
    
    path = parsed['path']
    
    # Rota padrão
    if path == '/':
        return serve_static_file('static/index.html')
    
    # Serve arquivos estáticos
    if path.startswith('/static/'):
        file_path = os.path.join(*path.split('/'))  # Mais seguro que path[1:]
        if not os.path.exists(file_path):
            return build_response(404, 'text/html', b'<h1>404 Not Found</h1>')
        return serve_static_file(file_path)
    
    # Exemplo de rota dinâmica
    if path == '/hello':
        return build_response(200, 'text/html', b'<h1>Hello World!</h1>')
    
    # Rota não encontrada
    return build_response(404, 'text/html', b'<h1>404 Not Found</h1>')