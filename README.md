# Test task for abz.agency
> :dancers: It is online service where you can see hierarchy of employees in the company. 
> *You can see hierarchy of employees in tree view, search any employee, authorized users can edit information about employees.*
### Author
Sofia Anokhovskaya
____
### Backend development technologies
- Python 3.7
- Django 2.2.19
____
### Launching project in dev mode
- Install and activate the virtual environment
- Install dependencies from the file requirements.txt
```bash
pip install -r requirements.txt
``` 
- In the file folder manage.py run the command:
- You need to make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
- You need to create admin user
```bash
python manage.py createsuperuser
```
- You need to collect static
```bash
python manage.py collectstatic
```
- Run project
```bash
python3 manage.py runserver
```