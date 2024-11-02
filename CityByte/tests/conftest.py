import django

def pytest_configure():
    settings.configure()
    django.setup()
