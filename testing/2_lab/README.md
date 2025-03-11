## Створення середовища
```bash

poetry env remove --all
poetry config virtualenvs.in-project true

poetry install

poetry shell
python program/main.py
python -m unittest -v ./tests/main.py 
exit
```

----
## Запуск Юніт-тестів
```bash
# Ми перевірили що всі функції та клас починаються з test 
# Також ми перевірили що файл з тестами починається з слова test
# А також папка з файлами називається tests 
poetry run python -m unittest -v
```

---
## Використання PyTest
```bash
poetry add pytest black flake8 --dev 
poetry install --with dev
poetry run pip list

poetry run python -m unittest -v
poetry run pytest tests/ -v
poetry run pytest -v

poetry run python program/main.py
poetry run python program/bank.py

poetry run pytest program/bank.py -v

poetry run flake8 tests/test_units.py
```

## Запуск програми
```
export PYTHONPATH=./
poetry run python program/main.py
```