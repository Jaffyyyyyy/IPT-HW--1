import sys
import os

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(__file__))

print("Testing imports...")

try:
    print("\n1. Importing posts.models...")
    from posts import models
    print(f"   Success! User: {models.User}, Post: {models.Post}")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

try:
    print("\n2. Importing posts.views...")
    from posts import views
    print(f"   Success! Views: {dir(views)}")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

try:
    print("\n3. Importing posts.urls...")
    from posts import urls
    print(f"   Success! urlpatterns type: {type(urls.urlpatterns)}")
    print(f"   urlpatterns: {urls.urlpatterns}")
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

print("\nDone!")
