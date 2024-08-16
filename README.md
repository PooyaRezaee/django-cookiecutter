# Django Template with Cookiecutter

This project is a Django template built using Cookiecutter

<p align="center">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" alt="Django">
    <img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django Rest Framework">
    <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx">
    <img src="https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4" alt="celery">
    <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="redis">
    <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="postgresql">
</p>

## Usage
```bash 
pip install cookiecutter
cookiecutter https://github.com/PooyaRezaee/django-cookiecutter.git
cd project_name

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements_dev.txt
python manage.py makemigrations # after fill .env file
```
After setting the contents of .env now you can develop the project. To see the instructions for executing and managing the project, you can see the readme.md file inside the project.


## TODO
- [ ] find bugs