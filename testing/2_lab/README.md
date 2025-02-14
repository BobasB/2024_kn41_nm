```bash

poetry env remove --all
poetry config virtualenvs.in-project true

poetry install

poetry shell
python program/main.py
python -m unittest -v ./tests/main.py 
exit


poetry env remove --all
```

###
----
```bash
# Ми перевірили що всі функції та клас починаються з test 
# Також ми перевірили що файл з тестами починається з слова test
# А також папка з файлами називається tests 
poetry run python -m unittest -v