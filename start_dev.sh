# sh VCPFrontend/build.sh
export VCP_BACKEND_SERVER=DEV
python manage.py collectstatic
python manage.py makemigrations vcp_backend
python manage.py migrate
#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@vcp', 'password')" | python manage.py shell
python manage.py runserver 0:8000
#python manage.py test