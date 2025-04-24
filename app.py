import socket
from config import HOST, PORT
from utils.http_parser import parse_request
from utils.request_handler import handle_request

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor rodando em http://{HOST}:{PORT}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conexão estabelecida com {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                
                # Processar a requisição
                response = handle_request(data)
                conn.sendall(response)
                conn.close()

if __name__ == "__main__":
    run_server()