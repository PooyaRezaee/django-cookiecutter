import sys

yes_or_no_varibles = [
    "{{ cookiecutter.use_ckeditor }}",
    "{{ cookiecutter.use_cloud_storage }}",
    "{{ cookiecutter.use_celery }}",
]

for field in yes_or_no_varibles:
    if field not in ["y", "n"]:
        print(f"Error: 'use_ckeditor' must be 'n' or 'y' but is {field}")
        sys.exit(1)
