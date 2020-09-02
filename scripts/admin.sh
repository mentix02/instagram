#!/usr/bin/env bash

echo "from django.contrib.auth import get_user_model; User = get_user_model();
User.objects.create_superuser('admin', 'admin@admin.com', 'abcd', first_name='Mr.', last_name='Admin')" \
| $(command -v python3) manage.py shell
