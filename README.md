# campus_flow2
# CampusFlow 2

A Python command-line ticket management application with AI-powered troubleshooting suggestions using OpenRouter.

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Lizzyben45/campus_flow2.git
cd campus_flow2
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Ubuntu/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project root.

Add:

```env
OPENROUTER_API_KEY=your_actual_api_key
```

Never upload `.env` to GitHub.

### 6. Run the application

```bash
python main.py
```

## Useful Commands

| Task | Command |
|---|---|
| Check Python version | `python --version` |
| Create virtual environment | `python -m venv .venv` |
| Install dependencies | `python -m pip install -r requirements.txt` |
| Install a new package | `python -m pip install package_name` |
| Save installed packages | `python -m pip freeze > requirements.txt` |
| Run application | `python main.py` |
| Check Git status | `git status` |
| Add changes | `git add .` |
| Commit changes | `git commit -m "Your message"` |
| Push to GitHub | `git push` |
| Pull latest changes | `git pull` |

## Features

- Create support tickets.
- Generate unique ticket IDs.
- Validate ticket information.
- Save and load tickets using JSON.
- View existing tickets.
- Generate AI troubleshooting suggestions.
- Display AI suggestions in the terminal.
- Handle AI service errors.

## Security

- API keys are stored in `.env`.
- `.env` must never be committed to GitHub.
- AI suggestions are temporary and are not saved in tickets.json.