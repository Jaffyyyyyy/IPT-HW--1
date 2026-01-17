import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'connectly_project.settings')
django.setup()

print("Django setup complete. Now importing models...")

from posts.models import User, Post

print(f"User: {User}")
print(f"Post: {Post}")
print("Success!")
