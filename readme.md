## 🖥️ API1 → API2 via Docker Compose

This project demonstrates two simple FastAPI services (`API1` and `API2`) that communicate with each other via HTTP. The entire system is containerized using Docker Compose.

---

## ✅ Features

* API1 exposes endpoint `/call-api2`
* API1 sends a request to API2's `/hello` endpoint
* API2 returns a JSON message: `"Hello from API 2"`
* API1 returns API2's response to the user
* Both services print logs for incoming requests

---

## 🧱 Project Structure

```
API-hello-test/
├── api1/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── api2/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Setup & Deploy

### 📥 1. Clone the Repository

```bash
git clone https://github.com/Pimnapat25/API-hello-test.git
cd API-hello-test
```

---

### 🐳 2. Install Docker and Docker Compose

* 📦 [Download Docker Desktop](https://www.docker.com/products/docker-desktop) and install
* After installation, open a new terminal and check:

```bash
docker --version
docker compose version
```

If both commands return version numbers, you’re ready.

---

### 🚀 3. Build and Run with Docker Compose

```bash
docker compose up --build
```

This will:

* Build both API containers from their Dockerfiles
* Start the services:

  * `API1` on `http://localhost:8001`
  * `API2` on `http://localhost:8002`

You should see logs similar to:

```
api1-1  | INFO:     API1: Received request from user
api2-1  | INFO:     API2: Received request
```

---

## 🧪 Testing the APIs

### ✅ Test API1 → API2 Call

#### Method 1: Using Browser or Postman

* Open [http://localhost:8001/call-api2](http://localhost:8001/call-api2)
* You should see:

```json
{
  "message_from_api2": {
    "message": "Hello from API 2"
  }
}
```

#### Method 2: Using `curl`

```bash
curl http://localhost:8001/call-api2
```

Expected output:

```json
{"message_from_api2":{"message":"Hello from API 2"}}
```

---

## 📜 Logging Output

Both API containers will print logs to the terminal. Example:

```
api1-1  | INFO:root:API1: Received request from user
api1-1  | INFO:root:API1: Got response from API2: {"message":"Hello from API 2"}
api2-1  | INFO:root:API2: Received request
```

---

## 🔁 Stop the Services

Press `CTRL+C` or run:

```bash
docker compose down
```

---

## 🧩 Troubleshooting

| Problem                         | Solution                                                                 |
| ------------------------------- | ------------------------------------------------------------------------ |
| `docker: command not found`     | Install [Docker Desktop](https://www.docker.com/products/docker-desktop) |
| `docker-compose not recognized` | Use `docker compose` (with space), not `docker-compose`                  |
| Port already in use             | Change ports in `docker-compose.yml` or stop other services              |

