sudo -u postgres psql -f instalacion/preparacionBD.sql
pip install -r requirements.txt
python manage.py makemigrations productos
python manage.py migrate 