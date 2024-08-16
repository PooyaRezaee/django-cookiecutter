import os
import sys
import subprocess

def create_app(app_name, app_type):
    try:
        subprocess.check_call(['django-admin', 'startapp', app_name])
    except subprocess.CalledProcessError as e:
        print(f"Error creating app: {e}")
        sys.exit(1)

    if os.path.exists(app_name):
        os.rename(app_name, os.path.join('apps', app_name))
    else:
        print(f"Folder {app_name} not found.")
        sys.exit(1)

    remove_default_tests_file(app_name)
    create_common_files(app_name)
    if app_type == 'api':
        create_api_files(app_name)
    elif app_type == 'template':
        create_template_files(app_name)
    elif app_type == 'both':
        create_api_files(app_name)
        create_template_files(app_name)
        create_combined_api_files(app_name)

    update_appconfig(app_name)
    print(f"App {app_name} of type {app_type} created successfully.")

def remove_default_tests_file(app_name):
    default_tests_file = os.path.join('apps', app_name, 'tests.py')
    if os.path.exists(default_tests_file):
        os.remove(default_tests_file)

def create_common_files(app_name):
    base_path = os.path.join('apps', app_name)
    os.makedirs(os.path.join(base_path, 'migrations'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'services'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'selectors'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'tests', 'services'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'tests', 'selectors'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'tests', 'models'), exist_ok=True)

    common_files = [
        'models.py',
        'admin.py',
        'urls.py',
        'views.py',
        '__init__.py',
        'services/__init__.py',
        'selectors/__init__.py',
        'tests/__init__.py',
        'tests/services/__init__.py',
        'tests/selectors/__init__.py',
        'tests/models/__init__.py'
    ]

    for file in common_files:
        open(os.path.join(base_path, file), 'a').close()

    create_urls_content(app_name)

def create_api_files(app_name):
    base_path = os.path.join('apps', app_name)
    open(os.path.join(base_path, 'serializers.py'), 'a').close()

def create_template_files(app_name):
    base_path = os.path.join('apps', app_name, 'templates', app_name)
    os.makedirs(base_path, exist_ok=True)

def create_combined_api_files(app_name):
    base_path = os.path.join('apps', app_name, 'api')
    os.makedirs(base_path, exist_ok=True)

    combined_api_files = [
        '__init__.py',
        'urls.py',
        'views.py',
        'serializers.py'
    ]

    for file in combined_api_files:
        open(os.path.join(base_path, file), 'a').close()

def create_urls_content(app_name):
    urls_path = os.path.join('apps', app_name, 'urls.py')
    urls_content = """from django.urls import path
# from .views import ...

urlpatterns = [
    # path("path", CBV.as_view(), name="name"),
]
"""
    with open(urls_path, 'w') as file:
        file.write(urls_content)

def update_appconfig(app_name):
    app_path = os.path.join('apps', app_name, 'apps.py')

    if not os.path.exists(app_path):
        print(f"File {app_path} not found.")
        return

    with open(app_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if line.strip().startswith('name ='):
            line = f'    name = \'apps.{app_name}\'\n'
        new_lines.append(line)

    with open(app_path, 'w') as file:
        file.writelines(new_lines)

    print(f"AppConfig updated for app {app_name}.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        app_name = sys.argv[1]
        try:
            app_type = sys.argv[2].lower()
            if app_type not in ['api', 'template', 'both']:
                print("Error: for <app_type> just select ['api', 'template', 'both']")
                sys.exit(1)
        except IndexError:
            app_type = "{{ cookiecutter.development_mode }}"
    else:
        print("Usage: python create_and_update_app.py <app_name> <app_type>")
        sys.exit(1)


    create_app(app_name, app_type)
