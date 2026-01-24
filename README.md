# Autonomous AI Business Operations Manager

An intelligent, autonomous system that acts as a comprehensive Business Operations Manager. It ingests business data, performs multi-agent analysis, assesses risks, makes strategic decisions, and generates execution plans with professional PDF reports.

## 🚀 Features

- **Autonomous Agents**: 5-stage AI pipeline (Analysis, Risk, Decision, Execution, Reporting).
- **Premium Dashboard**: "Cyber-Corporate" UI with animated backgrounds and glassmorphism.
- **Data Ingestion**: Support for CSV data and qualitative operational notes.
- **PDF Reporting**: Auto-generated executive summaries.
- **Secure**: Local environment variable management for API keys.

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, OpenAI SDK (GitHub Models).
- **Frontend**: React, Vite, Lucide React, Recharts.
- **Styling**: Pure CSS (Variables, Flexbox/Grid, Animations).

## 📋 Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **GitHub Account** (for GitHub Models Token)

## ⚙️ Setup & Installation

### 1. Clone & Configure Backend

```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

**Environment Setup:**
1. Rename `.env.example` to `.env`.
2. Open `.env` and add your GitHub Token:
   ```
   OPENAI_API_KEY=github_pat_...
   OPENAI_BASE_URL=https://models.inference.ai.azure.com
   OPENAI_MODEL_NAME=gpt-4o
   ```

### 2. Configure Frontend

```bash
cd ../frontend
npm install
```

## 🏃‍♂️ How to Run Locally

### Step 1: Start Backend Server
In the `backend/` directory:
```bash
python -m uvicorn app.main:app --reload
```
*Server will start at `http://localhost:8000`*

### Step 2: Start Frontend Dashboard
In the `frontend/` directory (open a new terminal):
```bash
npm run dev
```
*Dashboard will open at `http://localhost:5173`*

## 💡 Usage

1. **Open Dashboard**: Go to `http://localhost:5173`.
2. **Upload Data**: Use the provided `sales_data.csv` in `sample-data/`.
3. **Add Context**: Paste the content of `operational_notes.txt` into the text area.
4. **Run Analysis**: Click the "Run AI Analysis" button.
5. **Explore**:
   - **AI Insights**: View trends and anomalies.
   - **Risk Assessment**: Check potential risks and severity.
   - **Execution Plan**: See the step-by-step roadmap.
   - **Reports**: Download the PDF Executive Summary.

## ☁️ Deployment (Vercel)

This project is configured for Vercel deployment.

1.  **Push to GitHub**.
2.  **Import Project in Vercel**.
3.  **Environment Variables**: Add `OPENAI_API_KEY`, `OPENAI_BASE_URL`, and `OPENAI_MODEL_NAME` in Vercel Project Settings.
4.  **Deploy**: Vercel will automatically build the React frontend and serverless Python backend.

## 📁 Project Structure

```
├── backend/
│   ├── app/
│   │   ├── agents/      # AI Agent Logic
│   │   ├── core/        # Config & Security
│   │   ├── models/      # Pydantic Models
│   │   ├── prompts/     # System Prompts
│   │   ├── routes/      # API Endpoints
│   │   └── services/    # LLM & PDF Services
│   ├── main.py          # Entry Point
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/  # Reusable UI Components
│   │   ├── pages/       # Dashboard Pages
│   │   ├── styles/      # CSS Themes
│   │   └── main.jsx     # Logic Entry
│   └── package.json
└── sample-data/         # Test files
```
