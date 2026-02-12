# Check App Tutorial

Welcome to **Check**, a simple and robust checklist application built with **FastAPI** (backend) and **SolidJS** (frontend).

This guide will walk you through setting up, running, and using the application.

## Prerequisites

- **Python 3.11+**
- **Node.js 18+** (for building frontend)

## 1. Installation

Clone the repository and install dependencies.

```bash
git clone https://github.com/hal2142pal/check.git
cd check

# Install Backend Deps
pip install fastapi uvicorn pydantic

# Install Frontend Deps
cd frontend
npm install
```

## 2. Building the Frontend

Before running the app, compile the SolidJS interface:

```bash
cd frontend
npm run build
cd ..
```

This creates a `dist/` directory which the backend will serve.

## 3. Running the App

Start the server:

```bash
uvicorn main:app --reload
```

Open your browser to: **http://127.0.0.1:8000**

---

## 4. User Guide

### The Interface

When you open the app, you will see a clean, minimalist interface.

```text
+---------------------------------------+
|               Checklist               |
|                                       |
|  [ Add a new task...      ] [ Add ]   |
|                                       |
+---------------------------------------+
```

### Adding a Task

1.  Click the input field.
2.  Type your task (e.g., "Buy milk").
3.  Press **Enter** or click **Add**.

```text
+---------------------------------------+
|  [ Buy milk               ] [ Add ]   |
+---------------------------------------+
|  [ ] Buy milk                         |
+---------------------------------------+
```

### Completing a Task

Click the checkbox next to a task to mark it as done.

```text
+---------------------------------------+
|  [x] Buy milk                         |
+---------------------------------------+
```

The text will strike through, indicating completion.

### Data Persistence

Currently, data is stored in memory. If you restart the server, the list will reset.

---

## Troubleshooting

- **"Vite not found":** Ensure you ran `npm install` inside the `frontend` directory.
- **"404 Not Found":** Make sure you ran `npm run build` so the `dist/` folder exists.
