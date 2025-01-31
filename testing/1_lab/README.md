## Робота у віртуальних середовищах

- Наступні команди ми виконували у терміналі (Terminal -> New Terminal (Bash terminal))

```bash
pwd
cd testing/1_lab
python -V
pip -V # якщо ця команда не буде працювати
python -m ensurepip --upgrade
pip list # виведе всі глобальні пакети

python -m venv bobas_env

source bobas_env/bin/activate

pip install requests

python 1.py

pip freeze > requirements.txt
pip list
deactivate


pip install pipenv
export PIPENV_VENV_IN_PROJECT=1
pipenv -h

pipenv install requests
pipenv shell
python 1.py

pipenv graph

exit
pipenv --rm

# Встановлення poetry на Windows
curl -sSL https://install.python-poetry.org | python3 -

poetry -h
cd env_with_poetry
poetry init
poetry add numpy
poetry add pandas
poetry shell

pip list
python 1.py
exit
poetry add flake8 --dev
poetry install --with dev
poetry shell

pip list
flake8 .

deactivate
poetry env list
poetry env info
poetry env -h
poetry -h
poetry config -h
poetry show
