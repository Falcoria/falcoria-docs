# ScanLedger – Installation Guide

ScanLedger is the backend API and data store powering Falcoria's scan ingestion and querying engine.

You can install it using one of the following methods:

- [Virtual Environment (Development Setup)](#1-virtual-environment-development-setup)
- [Docker (Using Public Image)](#2-docker-using-public-image)
- [Docker (Local Build)](#3-docker-local-build)
- [Docker Compose (Recommended for Self-Hosting)](#4-docker-compose-recommended-for-self-hosting)

---

## Installation Methods

### 1. Virtual Environment (Development Setup)

Use this method for development or debugging:

```bash
git clone https://github.com/Falcoria/scanledger.git
cd scanledger

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

cp .env.example .env
nano .env  # Configure DB and tokens

uvicorn app.main:app --host 0.0.0.0 --port 8000
```

API will be available at `https://localhost:8000/docs`.

---

### 2. Docker (Using Public Image)

Generate TLS certificates (optional for HTTPS):

```bash
./generate-tls-bundle.sh
```

Run the container:

```bash
docker run -d \
  --name scanledger \
  -p 443:443 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=changeme \
  -e POSTGRES_DB=falcoriadb \
  -e POSTGRES_HOST=localhost \
  -e ENVIRONMENT=development \
  -e ADMIN_TOKEN=changeme \
  -e TASKER_TOKEN=changeme \
  -v $(pwd)/unit/bundle.pem:/docker-entrypoint.d/bundle.pem:ro \
  ghcr.io/falcoria/scanledger:latest
```

---

### 3. Docker (Local Build)

```bash
git clone https://github.com/Falcoria/scanledger.git
cd scanledger

./generate-tls-bundle.sh

docker build -t scanledger .

docker run -d \
  --name scanledger \
  -p 443:443 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=changeme \
  -e POSTGRES_DB=falcoriadb \
  -e POSTGRES_HOST=localhost \
  -e ENVIRONMENT=development \
  -e ADMIN_TOKEN=changeme \
  -e TASKER_TOKEN=changeme \
  -v $(pwd)/unit/bundle.pem:/docker-entrypoint.d/bundle.pem:ro \
  scanledger
```

---

### 4. Docker Compose (Recommended for Self-Hosting)

```bash
git clone https://github.com/Falcoria/scanledger.git
cd scanledger
cp .env.example .env  # Edit the variables below

docker compose up --build
```

Access: [https://localhost:443](https://localhost:443)

---

## Config Reference

| Variable           | Description |
|--------------------|-------------|
| `POSTGRES_USER`    | Postgres login name |
| `POSTGRES_PASSWORD`| Postgres password |
| `POSTGRES_DB`      | Name of the database used by ScanLedger |
| `POSTGRES_HOST`    | Network host/IP of your Postgres instance |
| `ENVIRONMENT`      | App mode (e.g. `development`, affects error verbosity) |
| `ADMIN_TOKEN`      | Token used to create the default admin user (used for authorization in API calls) |
| `TASKER_TOKEN`     | Token used by the Tasker module (not critical in self-hosted setups) |

---

## API Example

Create a project via curl:

```bash
curl -X POST https://localhost:443/projects \
  -H "Authorization: Bearer <YOUR_ADMIN_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"project_name": "example-project", "comment": "Initial test"}' \
  --insecure
```

Or using `falcli`:

```bash
python3 falcli.py project create example-project
```

---

## License

MIT License – See `LICENSE.md` for full terms.
