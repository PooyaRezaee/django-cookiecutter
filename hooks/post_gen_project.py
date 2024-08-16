import os
import shutil

project_directory = os.path.realpath(os.path.curdir)

def remove_path(path):
    """Remove a file or directory."""
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)
    else:
        print(f"Don't exist {path}")

def move_files(src_dir, dest_dir):
    """Move files from src_dir to dest_dir, replacing existing files if necessary."""
    if os.path.exists(src_dir):
        for item in os.listdir(src_dir):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dir, item)
            if os.path.isfile(s):
                shutil.move(s, d)
    else:
        print(f"Don't exist path {src_dir}")

development_mode = '{{ cookiecutter.development_mode }}'
redis_use = True if '{{ cookiecutter.cache_system }}' == 'redis' or '{{ cookiecutter.use_celery }}' == 'y' else False
# Handling development_mode

if development_mode == 'template':
    paths_to_remove = [
        os.path.join(project_directory, 'apps/api/'),
        os.path.join(project_directory, 'apps/account/api/'),
        os.path.join(project_directory, 'apps/sample/api/'),
        os.path.join(project_directory, 'config/settings/other/cors.py'),
        os.path.join(project_directory, 'config/settings/other/drf.py'),
        os.path.join(project_directory, 'config/settings/other/jwt.py'),
        os.path.join(project_directory, 'config/settings/other/spectacular.py'),
    ]
    for path in paths_to_remove:
        remove_path(path)

elif development_mode == 'api':
    api_dirs = {
        os.path.join(project_directory, 'apps/account/api/'): os.path.join(project_directory, 'apps/account/'),
        os.path.join(project_directory, 'apps/sample/api/'): os.path.join(project_directory, 'apps/sample/')
    }
    for src, dest in api_dirs.items():
        move_files(src, dest)
        
    remove_path(os.path.join(project_directory, 'apps/account/api/'))
    remove_path(os.path.join(project_directory, 'apps/sample/api/'))
    remove_path(os.path.join(project_directory, 'apps/account/templates/'))

# Handling use_ckeditor
use_ckeditor = '{{ cookiecutter.use_ckeditor }}'.lower()
if use_ckeditor != 'y':
    remove_path(os.path.join(project_directory, 'config/settings/other/ckeditor.py'))

# Handling use_cloud_storage
use_cloud_storage = '{{ cookiecutter.use_cloud_storage }}'.lower()
if use_cloud_storage != 'y':
    remove_path(os.path.join(project_directory, 'config/settings/other/cloud_storage.py'))

# Handling use_celery
use_celery = '{{ cookiecutter.use_celery }}'.lower()
if use_celery != 'y':
    paths_to_remove = [
        os.path.join(project_directory, 'apps/tasks/'),
        os.path.join(project_directory, 'apps/sample/tasks.py')
    ]
    for path in paths_to_remove:
        remove_path(path)

def create_env_file():
    import secrets
    secret_string = f"qwertyuiop[]';lkjhgfdsazcxvbnm,./QWERTYUIOPASDFGHJKLMNBVCXZ:|?><!@$%^&*()_+1234567890-="
    path = os.path.join(project_directory, '.env')
    random_secretkey = ''.join(secrets.choice(secret_string) for _ in range(64))
    
    redis_env = "REDIS_LOCATION=\n" if redis_use else ""

    with open(path,"w") as EnvFile:
        EnvFile.write(f"DJANGO_SECRET_KEY={random_secretkey}\nDEBUG=True\nDJANGO_SETTINGS_MODULE=config.settings.local\nDATABASE_URL=\nAWS_S3_ACCESS_KEY_ID=\nAWS_S3_SECRET_ACCESS_KEY=\nAWS_STORAGE_BUCKET_NAME=\n{redis_env}")

create_env_file()