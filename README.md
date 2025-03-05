# vpc with mlflow and nginx

## installation guide


'''
mlflow_project/
│── docker-compose.yml
│── nginx.conf
│── mlflow/
│   ├── artifacts/            # Stores MLflow artifacts
│   ├── mlflow.db             # SQLite database for MLflow (if using SQLite)
│── logs/                     # Logs for debugging
'''


in the vpc:

'''
sudo apt update && sudo apt install -y docker.io docker-compose
sudo systemctl enable --now docker
'''


docker-compose.yml
'''
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
'''

nginx.conf
'''
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

'''

create network for nginx and mlflow

'''
docker network create mlflow_project_default
'''

to check if the network exists:
'''
docker network inspect mlflow_project_default
'''