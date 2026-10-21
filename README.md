# ⚡ Hackathon-Ready Flask Starter

A lightweight, battle-tested Flask project structure designed specifically for **rapid prototyping**, **team collaboration**, and **speed during hackathons**.

---

## 📁 Project Folder Structure

```text
├── app/
│   ├── __init__.py           # Application Factory (create_app), registers blueprints & DB
│   ├── extensions.py         # SQLAlchemy & CORS instances (prevents circular imports)
│   ├── blueprints/           # Modular route groups (avoids merge conflicts!)
│   │   ├── main/             # Frontend HTML / Jinja views
│   │   │   ├── __init__.py
│   │   │   └── routes.py     # e.g., /, /about
│   │   ├── api/              # RESTful JSON endpoints
│   │   │   ├── __init__.py
│   │   │   └── routes.py     # e.g., /api/projects, /api/health
│   │   └── auth/             # Authentication & user sessions
│   │       ├── __init__.py
│   │       └── routes.py     # e.g., /auth/login, /auth/register
│   ├── models/               # Database tables & schemas
│   │   ├── __init__.py
│   │   └── example.py        # SQLAlchemy models (User, Project)
│   ├── services/             # Core business logic & external integrations
│   │   ├── __init__.py
│   │   └── ai_service.py     # LLM / AI integrations (Gemini, OpenAI, HuggingFace)
│   ├── static/               # Client-side static assets
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   └── templates/            # Jinja2 HTML templates
│       ├── base.html         # Base layout with Bootstrap 5 CDN & flash alerts
│       ├── index.html        # Main landing page & interactive demo
│       ├── 404.html          # Custom error page
│       └── components/       # Reusable UI partials
│           ├── navbar.html
│           └── footer.html
├── instance/                 # Local SQLite database (gitignored)
├── .env                      # Local environment variables (gitignored)
├── .env.example              # Environment template for teammates
├── .gitignore                # Python & virtual environment ignore rules
├── config.py                 # Configuration settings (Dev, Prod, Test)
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
└── README.md                 # Documentation
```

---

## 🚀 Why This Structure Wins at Hackathons

1. **Parallel Teamwork (Zero Merge Conflicts)**:
   - **Frontend Developer**: Works in `app/templates/` and `app/static/`.
   - **API / Backend Developer**: Builds endpoints in `app/blueprints/api/routes.py`.
   - **AI / Integration Engineer**: Adds model logic in `app/services/ai_service.py`.
   - **Database / Auth Developer**: Configures models in `app/models/` and routes in `app/blueprints/auth/`.
2. **Application Factory Pattern (`create_app`)**:
   - Clean, professional architecture that judges appreciate.
   - Prevents hard-to-debug circular import errors common when using a single `app.py`.
3. **Batteries-Included SQLite**:
   - Zero-config local database created automatically on startup inside `instance/dev.db`.
   - No need to configure PostgreSQL or MySQL during the crunch hours.
4. **CORS & Environment Preconfigured**:
   - `flask-cors` is pre-wired if you decide to connect a separate React/Vue/Svelte or mobile frontend.
   - `.env` manages secrets and API keys safely.

---

## ⚡ Quickstart

### 1. Create and Activate Virtual Environment

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Development Server

```bash
python run.py
```

The application will start at `http://localhost:5000` with hot-reloading enabled.

---

## 🔌 Pre-configured Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Home page with UI & interactive demo |
| `GET` | `/api/health` | API health check status |
| `GET` | `/api/projects` | Fetch all project records (JSON) |
| `POST` | `/api/projects` | Create a new project record |
| `POST` | `/api/ai/generate` | Query the AI service helper |
| `POST` | `/auth/login` | Mock authentication endpoint |
| `POST` | `/auth/register` | User registration endpoint |
