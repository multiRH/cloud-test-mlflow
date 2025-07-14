# vpc with mlflow and nginx

## installation guide


```
mlflow_project/
│── docker-compose.yml
│── nginx.conf
│── mlflow/
│   ├── artifacts/            # Stores MLflow artifacts
│   ├── mlflow.db             # SQLite database for MLflow (if using SQLite)
│── logs/                     # Logs for debugging
```


in the vpc:

```
sudo apt update && sudo apt install -y docker.io docker-compose

sudo systemctl enable --now docker
```


docker-compose.yml
```
version: '3'

services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.10.2
    container_name: mlflow_server
    ports:
      - "5000:5000"
    environment:
      - MLFLOW_TRACKING_URI=http://0.0.0.0:5000
      - MLFLOW_ARTIFACT_ROOT=/mlflow/artifacts
    volumes:
      - ./mlflow_data:/mlflow
    command: mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db

  nginx:
    image: nginx:latest
    container_name: nginx_proxy
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - mlflow
```

nginx.conf
```
events {}

http {
    server {
        listen 80;
        
        location /mlflow/ {
            proxy_pass http://mlflow:5000/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```

start docker:
```
docker-compose up -d
```

create network for nginx and mlflow:

```
docker network create mlflow_project_default
```

to check if the network exists:
```
docker network inspect mlflow_project_default
```

to delete all containers, images, volumes:

```
docker system prune -a
```

## Docker commands

to delete all:
```
docker system prune -a --volumes
```

to build the container:
```
docker-compose build
```

to start the container:
```
docker-compose up -d
```

## Troubleshooting

```
# Check if Docker is running
sudo systemctl enable --now docker 

# List running containers
docker ps 

# Stop and remove containers, networks, images, and volumes defined in the docker-compose.yml file
docker-compose down 

# Stop the nginx container
docker stop nginx-container

# Remove the mlflow container
docker rm nginx-container 

# Start the containers in detached mode
docker-compose up -d 

# List running containers
docker ps 
```

## VIM Basics Commands
```
Mode Switching:
i - Insert mode (before cursor)
a - Insert mode (after cursor)
Esc - Return to Normal mode

Navigation:
h, j, k, l - Left, down, up, right
w - Next word
b - Previous word
0 - Beginning of line
$ - End of line

Save and Exit:
:w - Save
:q - Quit
:wq - Save and quit
:q! - Quit without saving

Editing:
dd - Delete entire line
x - Delete character
u - Undo
yy - Copy line
p - Paste

Search:
/text - Search for "text"
n - Next search result
N - Previous search result

Lines:
:number - Jump to line (e.g. :10)
G - Go to end of file
gg - Go to beginning of file
Additional useful commands:
o - New line below cursor
O - New line above cursor
A - End of line and insert mode
dw - Delete word
D - Delete to end of line
yw - Copy word
r - Replace character


```