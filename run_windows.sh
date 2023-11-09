echo 'sleep 10'
sleep 10

python generate_sql.py

echo 'db script'

echo 'flask init'
flask db init

echo 'stamp head'
flask db stamp head

echo 'flask migrate'
flask db migrate -m 'migracion inicial'

echo 'flask upgrade'
flask db upgrade

echo 'start gunicorn server'

gunicorn app:app --bind 0.0.0.0:5005