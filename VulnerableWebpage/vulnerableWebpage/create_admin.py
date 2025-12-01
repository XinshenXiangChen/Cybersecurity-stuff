"""
Simple script to create admin user.
Run: python create_admin.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vulnerableWebpage.settings')
django.setup()

from users_app.models import User

# Create admin user if it doesn't exist
if User.objects.filter(username='admin').exists():
    print('Admin user already exists!')
else:
    User.objects.create(username='admin', password='admin')
    print('Admin user created successfully!')

