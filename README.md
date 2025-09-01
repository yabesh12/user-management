# {{project_name}}

FastAPI Microservice Template

## How It Works

Clone repo with microservice name:

```bash
git clone https://github.com/yabesh12/microservice-template.git {{project_name}}
cd {{project_name}}
```

`.env.example` picks up `PROJECT_NAME={{project_name}}` automatically (or defaults to folder name).

## Run Service

```bash
docker-compose up --build
```

## Health Check Endpoint

```
GET http://localhost:8000/v1/health
```

Response:
```json
{
  "status": "ok",
  "service": "{{project_name}}"
}
```
