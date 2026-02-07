# Connectly API - Quick Start Guide

✓ **HTTPS/SSL Support Verified and Working**

This guide will help you set up and run the Connectly API with HTTPS support in under 10 minutes.

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd IPT-HW--1
```

### 2. Create Virtual Environment
```bash
python -m venv env
```

### 3. Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\env\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
.\env\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source env/bin/activate
```

**Note:** You should see `(env)` at the beginning of your command prompt.

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

**Included packages:**
- Django & Django REST Framework
- JWT authentication
- HTTPS/SSL support (pyOpenSSL, cryptography, werkzeug)
- Password hashing (Argon2, BCrypt)
- CORS headers
- Django extensions

**If you encounter issues, try updating pip first:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Setup Database
```bash
cd connectly_project
python manage.py migrate
```

### 6. Create Test Data (Optional)
```bash
# Create a superuser for admin access
python manage.py createsuperuser

# Follow prompts to enter username, email, and password
```

### 7. Generate SSL Certificates (Required for HTTPS)
```bash
# Go back to project root
cd ..

# Generate certificates
python generate_cert.py

# You should see success messages
```

### 8. Run the Server

**Option A: HTTPS (Recommended for full testing)**
```bash
cd connectly_project
python manage.py runserver_plus --cert-file ../cert.pem --key-file ../key.pem
```

**Note:** If you get an OpenSSL error, see the "pyOpenSSL Import Error" section in Troubleshooting below.

**Option B: HTTP (Simpler, for basic testing)**
```bash
cd connectly_project
python manage.py runserver
```

### 9. Access the API

**HTTPS:** https://127.0.0.1:8000/api/
- Your browser will show a security warning (normal for self-signed certificates)
- Click "Advanced" → "Proceed to 127.0.0.1 (unsafe)" to continue
- ✓ **If you can access the API, HTTPS is working correctly!**

**HTTP:** http://127.0.0.1:8000/api/

**Admin Panel:** 
- HTTPS: https://127.0.0.1:8000/admin/
- HTTP: http://127.0.0.1:8000/admin/

**Success Indicators:**
- Server running without errors
- HTTPS lock icon in browser (with warning for self-signed cert)
- API endpoints responding correctly
- All tests passing

## Available Endpoints

### Authentication
- `POST /api/register/` - Register new user
- `POST /api/login/` - Login user
- `GET /api/protected/` - Test protected endpoint (requires token)

### Users
- `GET /api/users/` - List all users
- `POST /api/users/` - Create user

### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create post
- `GET /api/posts/<id>/` - Get post detail

### Comments
- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create comment

### Tasks (Factory Pattern)
- `GET /api/tasks/` - List all tasks
- `GET /api/tasks/?type=priority` - Filter tasks by type
- `POST /api/tasks/create/` - Create task (uses TaskFactory)
- `GET /api/tasks/<id>/` - Get task detail
- `PUT /api/tasks/<id>/` - Update task
- `DELETE /api/tasks/<id>/` - Delete task

## Testing with Postman

1. Import the collection: `Connectly API Security Tests.postman_collection.json`
2. Update the base_url variable:
   - For HTTPS: `https://127.0.0.1:8000/api`
   - For HTTP: `http://127.0.0.1:8000/api`
3. Run the collection tests

## Running Unit Tests
```bash
cd connectly_project
python manage.py test posts.tests -v 2
```

Expected: 23 tests should pass

## Troubleshooting

### Virtual Environment Not Activating
- **PowerShell:** May need to enable script execution:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- **Git Bash:** Use PowerShell or CMD instead

### Cryptography Module Not Found
```bash
# Make sure virtual environment is activated first
pip uninstall cryptography -y
pip install cryptography

# Verify installation
python -c "import cryptography; print(cryptography.__version__)"
```

### SSL Certificate Issues
```bash
# Regenerate certificates
cd <project-root>
python generate_cert.py
```

### pyOpenSSL Import Error (Windows)

If you get this error when running `runserver_plus` with HTTPS:
```
CommandError: Python OpenSSL Library is required to use runserver_plus with ssl support.
```

Even though `pip install pyOpenSSL` shows it's already installed, try this:

**Option 1: Automated Fix (Recommended)**
```powershell
# Make sure virtual environment is activated
.\env\Scripts\Activate.ps1

# Run the automated fix script
python fix_openssl.py
```

**Option 2: Manual Fix**
```powershell
# Uninstall and reinstall packages
pip uninstall pyopenssl cryptography cffi -y
pip cache purge
pip install --no-cache-dir cffi cryptography pyopenssl

# Verify it works
python -c "import OpenSSL; print('OpenSSL version:', OpenSSL.__version__)"
```

**Option 3: Test First**
```powershell
# Run diagnostic test
python test_openssl.py
```

**Common Causes:**
- Virtual environment not properly activated (make sure you see `(env)` in your prompt)
- Corrupted installation or cached files
- DLL loading issues on Windows
- Antivirus blocking DLL files

**After fixing:** Restart your terminal/IDE and try running the server again.

For detailed troubleshooting, see `FIX_OPENSSL.md`.

### Port Already in Use
```bash
# Use a different port
python manage.py runserver 8001

# Or find and kill the process using port 8000
```

### Database Errors
```bash
# Reset migrations
python manage.py migrate --run-syncdb

# Or delete db.sqlite3 and run migrations again
rm db.sqlite3
python manage.py migrate
```

## Design Patterns Implemented

### Singleton Pattern
1. **ConfigManager** - Centralized configuration settings
   - Location: `connectly_project/singletons/config_manager.py`
   - Provides: DEFAULT_TASK_PRIORITY, ENABLE_NOTIFICATIONS, RATE_LIMIT

2. **LoggerSingleton** - Centralized logging
   - Location: `connectly_project/singletons/logger_singleton.py`
   - Logs all API operations to console

### Factory Pattern
1. **TaskFactory** - Standardized task creation
   - Location: `connectly_project/factories/task_factory.py`
   - Creates: regular, priority, recurring tasks
   - Validates: type-specific metadata requirements

## Security Features
- ✓ HTTPS with self-signed certificates
- ✓ Password encryption (Argon2, PBKDF2, BCrypt)
- ✓ Token-based authentication
- ✓ Role-based access control (RBAC)
- ✓ Secure cookie flags
- ✓ HSTS headers
- ✓ Input validation
- ✓ Relational data validation

## Project Structure
```
IPT-HW--1/
├── connectly_project/
│   ├── connectly_project/     # Django settings
│   ├── posts/                  # Main app
│   ├── singletons/            # Singleton patterns
│   ├── factories/             # Factory patterns
│   ├── manage.py
│   └── db.sqlite3
├── env/                        # Virtual environment
├── generate_cert.py           # Certificate generator
├── requirements.txt           # Python dependencies
├── QUICK_START.md            # This file
└── Connectly API Security Tests.postman_collection.json
```

## Support
For issues or questions, refer to:
- `SETUP_GUIDE.md` - Detailed setup instructions
- `DEBUGGING_GUIDE.md` - Debugging common issues
- `TEST_CREDENTIALS.md` - Testing credentials
- `TESTING_GUIDE.md` - Testing guide
- `FIX_OPENSSL.md` - OpenSSL/HTTPS troubleshooting

## Helper Scripts
- `test_openssl.py` - Test OpenSSL installation
- `fix_openssl.py` - Automatically fix OpenSSL issues
- `generate_cert.py` - Generate SSL certificates
