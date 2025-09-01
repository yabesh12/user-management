# {{project_name}}

FastAPI Microservice Template

## How It Works

Clone repo with microservice name:

```bash
git clone <repo-url> user-management
cd user-management
```

`.env.example` picks up `PROJECT_NAME=user-management` automatically (or defaults to folder name).

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
  "service": "user-management"
}
```
