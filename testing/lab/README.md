## Запитання для активності
- Давайте придумаємо назву функції?
> будь-яке довільне імя яке придумаєте
- Який аргумент потрібно передати у тестову функцію?
> У тестовій функції завжди має бути self
- Якою командою ми активовуємо poetry середовище / або запускаємо команду на виконання?
> poetry shell / poetry run
- Чи можемо ми вказати декілька assert у тесті?
> безліч, скільки нам буде потрібно 
- Яку бібліотеку ми використовуємо для написання юніт-тестів?
> використовуємо unittest або pytest
- Чи обов’язково називати функцію тесту з префіксом test_?
> так, це обовязково
- Як ви гадаєте, що буде, якщо тест не пройде?
> у нас буде повідомлення який з тестів не виконався, він буде позначений як Failed
- Чим відрізняється assert у звичайному коді від assert у тестах?
> в програмі assert використовується як преевірка правильності вводу а в тестах для тверджень
- Як ми можемо запустити всі тести в проєкті однією командою?
> `poetry run python -m unittest -v` - він автоматично знайде всі тести у проекті АБО `poetry run pytest tests/ -v`
- Що таке покриття коду тестами?
> це співвідношення запущеного коду за допомогою тестів до всієї кодової бази
- Як гадаєте, чи 100% покриття завжди означає ідеальний код?
> ні, навіть якщо тести покривають весь код, це не означає що тести є якісними та можуть знайти всі недоліки в коді 
- Чому важливо тестувати всі можливі варіанти поведінки функції?
> щоб запобігти винекненню багів та неточностей (це дозволить мінімізувати появу багів)
- Як ви думаєте, чи можна написати тест, який сам по собі буде містити помилку?
> так, тестувальники теж люди і можуть робити помилки в тестах
- Якою командою я можу додати нову бібліотеку до проекту?
> `poetry add` і далі вказуємо назву бібліотеки
- Яку команду потрібно виконати, щоб згенерувати звіт Coverage?
> `poetry run python -m coverage report`
- Де можна переглянути детальний звіт про покриття коду?
> він виведеться у командній стрічці
- Чому деякі рядки коду можуть залишитися не протестованими?
> тому що тест не викликає цей код (можуть бути розгалуження if в які тест ніколи не заходить)
- Що ми можемо зробити, якщо Coverage показує низький рівень покриття?
> написати більше тестів які будуть викликати непокритий код
- Чи можна запускати Coverage разом із pytest?
> так
- Як ми можемо зробити тести більш читабельними та зрозумілими?
> називати тестову функції зрозумілими (нормальними) іменами, або додавати опис до тесту або пропросити АІ додати опис до тесту
- Як правильно називати тестові функції, щоб вони були зрозумілими?
> небоятись давати довгі назви та називати відповідно до того що робити функція, щоб з її назви вже було ясно що вона робить
- Чому важливо ізолювати тестові випадки один від одного?
> щоб код який тестується не конфліктував (наприклад не варто тестувати квадрат і трикутник разом бо їх характеристики є різними)
- Що відбудеться, якщо тестова функція не містить assert?
> тест нічого не буде тестувати (але він запуститься)
- Як ми можемо перевірити, які частини коду не покриті тестами?
> Coverage виділить ці частини кожу червоним
- Чи впливає якість тестів на результати покриття?
> і так і ні, бо може бути мала кількість тестів (якісних) яка покриває лише критичні елементи коду
- Як ви думаєте, що краще: більше тестів чи краща їхня якість?
> краща якість, бо кількість не завжди добре
- Чи можуть автоматизовані тести повністю замінити ручне тестування?
> людина є незамінною
- Що робити, якщо після додавання нового коду покриття впало?
> писати нові тести (бо покриття завжди буде падати при додаванні нового коду)
- Як ми можемо оптимізувати тести, щоб вони виконувалися швидше?
> використвши початкову ініціалізацію пееред тестами за допомогою методу setUp або використавши fixtures
- Чи потрібно тестувати приватні та protected методи класу?
> так 
- Як Coverage визначає, які рядки коду були виконані?
> це ті рядки які викликались у тестах
- Чим відрізняється покриття функцій від покриття гілок?
> не завжди ми можемо покрити всі гілки у функції, один тест може покриту одну функцію, але для покриття всіх гілок на треба багато assetr
- Як можна запустити Coverage разом із pytest?
> `pytest --cov=.`
- На вашу думку, який відсоток покриття вважається прийнятним у реальних проєктах?
> вгадуйте :)
- Чи є способи ігнорувати певні частини коду в Coverage?
> напевно можливо
- Як ви думаєте, чи можливе 100% покриття в реальному проєкті?
> так, якщо в прокеті не дописується новий код
- Що відбудеться, якщо тест очікує один результат, а отримує інший?
> тест зафейлиться
- Як можна перевірити покриття коду у вигляді HTML-звіту?
> згенерувати звіт та відкрити його у браузері
- Чи можна визначити покриття тестами окремого модуля програми?
> так, бо у звіті відображується окриття по окремих файлах
- Як ми можемо перевірити, чи всі функції у нашому модулі протестовані?
> відкривши звіт та зайшовши у файл програми ми можемо перевірити які методи не протестовані 