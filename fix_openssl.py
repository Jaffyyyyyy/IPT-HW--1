"""
Fix script for OpenSSL import issues on Windows
Run this script to diagnose and fix pyOpenSSL installation problems
"""

import subprocess
import sys

def run_command(command, description):
    """Run a command and return success status"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print('='*60)
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=120
        )
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("="*60)
    print("pyOpenSSL Fix Script for Windows")
    print("="*60)
    print("\nThis script will:")
    print("  1. Check your current Python environment")
    print("  2. Uninstall and reinstall pyOpenSSL and dependencies")
    print("  3. Verify the installation")
    print("\n" + "="*60)
    
    input("Press Enter to continue...")
    
    # Check Python version
    print(f"\nPython version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    # Step 1: Uninstall problematic packages
    print("\n\nSTEP 1: Uninstalling existing packages...")
    packages_to_remove = ['pyopenssl', 'cryptography', 'cffi']
    
    for package in packages_to_remove:
        run_command(
            f'pip uninstall {package} -y',
            f'Uninstalling {package}'
        )
    
    # Step 2: Clear pip cache
    print("\n\nSTEP 2: Clearing pip cache...")
    run_command('pip cache purge', 'Clearing pip cache')
    
    # Step 3: Reinstall packages in correct order
    print("\n\nSTEP 3: Reinstalling packages...")
    packages_to_install = [
        ('pycparser', 'Installing pycparser'),
        ('cffi', 'Installing cffi'),
        ('cryptography', 'Installing cryptography'),
        ('pyopenssl', 'Installing pyopenssl'),
    ]
    
    for package, description in packages_to_install:
        success = run_command(
            f'pip install --no-cache-dir {package}',
            description
        )
        if not success:
            print(f"\n⚠ WARNING: Failed to install {package}")
    
    # Step 4: Verify installation
    print("\n\nSTEP 4: Verifying installation...")
    print("="*60)
    
    try:
        import OpenSSL
        print("\n✓ SUCCESS: OpenSSL imported successfully!")
        print(f"  Version: {OpenSSL.__version__}")
    except ImportError as e:
        print("\n✗ FAILED: Could not import OpenSSL")
        print(f"  Error: {e}")
        print("\n⚠ Additional troubleshooting needed:")
        print("  - Make sure you're in the virtual environment (env)")
        print("  - Try: pip install --upgrade --force-reinstall pyopenssl")
        print("  - Check for antivirus blocking DLL files")
        print("  - Try restarting your terminal/IDE")
        return False
    
    print("\n" + "="*60)
    print("Installation complete!")
    print("="*60)
    print("\nYou can now run:")
    print("  cd connectly_project")
    print("  python manage.py runserver_plus --cert-file ../cert.pem --key-file ../key.pem")
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScript cancelled by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
