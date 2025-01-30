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
pipenv -h

pipenv install requests
pipenv shell
python 1.py

deactivate

