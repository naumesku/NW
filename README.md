Онлайн платформа торговой сети электроники

Веб-приложение, с API интерфейсом и админ-панелью.
Реализована модель сети по продаже электроники. Сеть представляет собой иерархическую структуру из 3 уровней:

Завод;
Розничная сеть;
Индивидуальный предприниматель.
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья - её уровень - 1.

В админ-панели созданных объектов На странице объекта сети добавлены:

ссылка на «Поставщика»;
фильтр по названию города;
«admin action», очищающий задолженность перед поставщиком у выбранных объектов.
CRUD для всех моделей (запрещено обновление через API поля «Задолженность перед поставщиком»);

Добавлена возможность фильтрации объектов по определенной стране.

Настроены права доступа к API так, чтобы только активные сотрудники имели доступ к API.

Инструкция по запуску проекта

1. Создать админа и модератора
python manage.py csu

2. Запустить сервер
python manage.py runserver