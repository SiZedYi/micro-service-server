#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
from eureka.eureka import eureka_init, stop_eureka

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_service.settings')
    if os.environ.get('RUN_MAIN'):
        print('run')
        eureka_init()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    stop_eureka()

if __name__ == '__main__':
    main()
