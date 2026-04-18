# Kiwi CMS

A lightweight blog CMS built with Django, designed for Persian-language content with full Jalali calendar support.

## Stack

| Layer | Technology |
| --- | --- |
| Runtime | Python 3.12 |
| Framework | Django 5.2 LTS |
| Database | SQLite (dev) |
| Editor | CKEditor 5 |
| Tagging | django-taggit |
| Calendar | django-jalali + jdatetime |
| Server | Gunicorn |

## Features

- Blog posts with categories and tags
- Rich text editing via CKEditor 5 with image upload
- Jalali (Persian) date display throughout
- Comment system with admin moderation
- Static pages (About, Contact, etc.) with navbar management
- User registration, login, and logout
- Pagination
- reCAPTCHA support on public forms
- Site-wide settings (title, footer, post count, maintenance mode)
- Full Django admin interface

## Requirements

- Python 3.12+
- [mise](https://mise.jdx.dev/) (recommended for Python version management)

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd Kiwi-CMS

# Set Python version (if using mise)
mise install

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure settings
cp Kiwi/settings_sample.py Kiwi/settings.py
# Edit Kiwi/settings.py — set SECRET_KEY and optionally reCAPTCHA keys

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## URL Structure

| URL | Description |
| --- | --- |
| `/` | Homepage with paginated posts |
| `/post/<slug>/` | Single post |
| `/category/<slug>/` | Posts by category |
| `/tag/<name>/` | Posts by tag |
| `/<slug>/` | Static page |
| `/page/<n>/` | Pagination |
| `/user/register/` | User registration |
| `/user/login/` | Login |
| `/user/logout/` | Logout |
| `/admin/` | Django admin |

## Configuration

All configuration lives in `Kiwi/settings.py` (not tracked by git). Key settings:

```python
SECRET_KEY = '...'          # Change before any deployment

RECAPTCHA_SECRET_KEY = ''   # Google reCAPTCHA v2 keys
RECAPTCHA_PUBLIC_KEY = ''

DEBUG = True                # Set to False in production
ALLOWED_HOSTS = []          # Add your domain in production
```

## Production Notes

- Switch `DATABASES` to PostgreSQL
- Set `DEBUG = False` and configure `ALLOWED_HOSTS`
- Run `python manage.py collectstatic`
- Serve with Gunicorn behind Nginx
- Use a proper secret key and store it in an environment variable

## License

MIT
