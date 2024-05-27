# belajar_django_modular

## Cara membuat migration
```sh
# format nya
pdm run src/manage.py makemigrations <nama_module> --empty -n <nama_migration>

# contoh execution
pdm run src/manage.py makemigrations app_dashboard --empty -n add_user_group

# apply
pdm run src/manage.py migrate
