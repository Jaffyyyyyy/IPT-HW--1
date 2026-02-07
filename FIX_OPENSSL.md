# Fixing "Python OpenSSL Library is required" Error

## The Problem

You're getting this error even though `pip install pyOpenSSL` shows it's already installed:
```
CommandError: Python OpenSSL Library is required to use runserver_plus with ssl support.
```

## Why This Happens

This usually occurs when:
1. The OpenSSL module can't be imported despite being installed
2. There's a corruption in the installation
3. DLL dependencies aren't properly loaded on Windows
4. The virtual environment isn't properly activated

## Quick Fix Steps

### Option 1: Run the Automated Fix Script (RECOMMENDED)

1. Make sure you're in the virtual environment:
   ```powershell
   .\env\Scripts\Activate.ps1
   ```

2. Run the fix script:
   ```powershell
   python fix_openssl.py
   ```

   This will automatically:
   - Uninstall and reinstall pyOpenSSL and its dependencies
   - Clear the pip cache
   - Verify the installation works

### Option 2: Manual Fix

1. **Activate your virtual environment:**
   ```powershell
   .\env\Scripts\Activate.ps1
   ```

2. **Test if OpenSSL can be imported:**
   ```powershell
   python test_openssl.py
   ```

3. **If the test fails, reinstall the packages:**
   ```powershell
   pip uninstall pyopenssl cryptography cffi -y
   pip cache purge
   pip install --no-cache-dir cffi cryptography pyopenssl
   ```

4. **Verify it works:**
   ```powershell
   python -c "import OpenSSL; print('OpenSSL version:', OpenSSL.__version__)"
   ```

### Option 3: Force Reinstall

If the above doesn't work:

```powershell
pip install --upgrade --force-reinstall --no-cache-dir pyopenssl cryptography cffi
```

## Important Notes

### ⚠️ Don't Run Python Code Directly in PowerShell

**WRONG:**
```powershell
import OpenSSL; print('OpenSSL version:', OpenSSL.__version__)
```

This won't work because PowerShell can't execute Python code directly!

**CORRECT:**
```powershell
python -c "import OpenSSL; print('OpenSSL version:', OpenSSL.__version__)"
```

### ✓ Make Sure Virtual Environment is Activated

Your prompt should show `(env)` at the beginning:
```powershell
(env) PS C:\Users\...\IPT-HW--1>
```

If you don't see `(env)`, activate it:
```powershell
.\env\Scripts\Activate.ps1
```

## After Fixing

Once OpenSSL is working, you can run:

```powershell
cd connectly_project
python manage.py runserver_plus --cert-file ../cert.pem --key-file ../key.pem
```

## Still Not Working?

1. **Restart your terminal/PowerShell** - Sometimes DLLs need a fresh shell
2. **Restart VS Code** - Python interpreter might need to reload
3. **Check antivirus** - Some antivirus software blocks DLL files
4. **Rebuild virtual environment:**
   ```powershell
   deactivate
   Remove-Item -Recurse -Force env
   python -m venv env
   .\env\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

## Files Created to Help You

- `test_openssl.py` - Tests if OpenSSL can be imported properly
- `fix_openssl.py` - Automatically fixes the installation
- `FIX_OPENSSL.md` - This file with instructions
