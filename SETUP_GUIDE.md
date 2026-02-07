# Setup Guide for Other Device

## Prerequisites
- Python 3.8+ installed
- Git (optional, for cloning)

## Setup Steps

### 1. Transfer Project Files
Copy the entire `IPT-HW--1` folder to the other device at the same path `C:\IPT-HW--1\`, or choose a different path and adjust the commands below.

### 2. Create Virtual Environment
Open PowerShell or Command Prompt and run:

```powershell
# Navigate to the project
cd C:\IPT-HW--1

# Create virtual environment
python -m venv env

# Activate virtual environment (PowerShell)
.\env\Scripts\Activate.ps1

# OR if using Command Prompt
# .\env\Scripts\activate.bat
```

**Note:** If you get a PowerShell execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies
With the virtual environment activated:

```powershell
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-extensions werkzeug pyopenssl
```

### 4. Copy SSL Certificates
The SSL certificate files (`cert.pem` and `key.pem`) should already be in the `connectly_project` folder. If they're missing, you'll need to:

**Option A:** Copy them from the original device  
**Option B:** Generate new ones (see section below)

### 5. Run the Server
```powershell
cd connectly_project
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```

## Generating SSL Certificates (If Needed)

If the certificate files are missing, generate them:

```powershell
cd C:\IPT-HW--1\connectly_project

# Using OpenSSL (if installed)
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# OR using Python (simpler for development)
python -c "from werkzeug.serving import generate_adhoc_ssl_context; import ssl; generate_adhoc_ssl_context()"
```

For a quick Python script to generate certificates:

```powershell
python generate_cert.py
```

(See `generate_cert.py` file in the project root)

## Troubleshooting

### Path Not Found Error
- Ensure you've copied the project to the correct location
- Use `Test-Path C:\IPT-HW--1\connectly_project` to verify the directory exists

### Python Not Found
- Ensure Python is installed: `python --version`
- If not, download from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Module Not Found Errors
- Ensure virtual environment is activated (you should see `(env)` in your prompt)
- Reinstall dependencies: `pip install -r requirements.txt` (if requirements.txt exists)

### Certificate Errors
- Verify cert.pem and key.pem exist in the connectly_project folder
- Regenerate certificates if needed (see above)

## Quick Start Commands (Summary)

```powershell
cd C:\IPT-HW--1
.\env\Scripts\Activate.ps1
cd connectly_project
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```

The server should start at `https://127.0.0.1:8000/`
