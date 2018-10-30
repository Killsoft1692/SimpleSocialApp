# Social app demo

1. Create virtualenv(Python 3.5.2)
2. Install requirements => pip3 install -U -r requirements.txt
3. python3 manage.py migrate
4. python3 manage.py runserver
5. Credentials: username: admin, password: admin1111,
    usernames: Add, Orest, Bond, Ludmila, John, Katya, Georg, Anatoly, Sergey
    with password: qazwsxedc1111
    login through django admin: http://127.0.0.1:8000/admin/login/?next=/admin/
6. User profiles: http://127.0.0.1:8000/api_v1/profiles/ (friend list included)
7. Groups: http://127.0.0.1:8000/api_v1/groups/
8. Likes functionality: http://127.0.0.1:8000/groups/ 