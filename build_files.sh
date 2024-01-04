echo "Building the project..."

echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
pip install -r requirements.txt 
python3.11 manage.py collectstatic --noinput --clear