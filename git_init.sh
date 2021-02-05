rm ./venv -r
rm ./websites_entry -r
rm ./manage.py
rm ./.git -rf
python -m venv venv
pip install -r requirements.txt
git init
git add .
git commit -m "first commit with boilerplate"
git flow init
