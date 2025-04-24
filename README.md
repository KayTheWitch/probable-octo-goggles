# HTTP Server

A simple HTTP server implementation in Python that serves static files and handles basic HTTP requests. Written just as a personal project soon to be implemented on my homelab.

## Features

- Serves static files (HTML, CSS, JavaScript, images)
- Handles basic HTTP requests
- Supports common MIME types
- Simple and lightweight implementation
- Built-in error handling (404, 500)

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone https://github.com/StarDropUwU/probable-octo-goggles.git
cd probable-octo-goggles
```

2. No additional dependencies are required as the server uses only Python's standard library.

## Configuration

The server configuration can be modified in `config.py`:

- `HOST`: The host address (default: 'localhost')
- `PORT`: The port number (default: 8000)

## Usage

1. Start the server:
```bash
python app.py
```

2. Access the server in your web browser:
```
http://localhost:8000
```

## Project Structure

```
.
├── server.py          # Main server implementation
├── config.py          # Server configuration
├── static/            # Directory for static files
│   └── index.html     # Default homepage
└── utils/             # Utility modules
    ├── http_parser.py # HTTP request parser
    ├── request_handler.py # Request handling logic
    └── response_builder.py # HTTP response builder
```

## Static Files

Place your static files (HTML, CSS, JavaScript, images) in the `static/` directory. The server will automatically serve these files when requested.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).