# news_paper
02.07.2023 - create views and templates/ join templates in settings and download some templates(with boostap) in views.
У новостного создал представление , осталось их подключить к шаблонам(кстати шаблоны скачал с инета - пока только изучаю фронтенд) и осталось настроить их. Надеюсь к завтра все сделаю. Создал сортировку публикаций по датам осталось их проверить.

03.07.2023 На экран выводитя новости можно поменять в default.html какие еще данные выводить, осталось донастроить вывод новостей по датам. + Добавить вывод каждой отдельной новости

05/07/2023 - Сделал цензор на слова - пока их нужно вручную добавлять в список, но можно прикепить файл и импортировать из него список слов, крч можно доработат функцию(что конечно я не буду пока делать-_-) А так же теперь в новстях указывается дата создания поста.
06.07.2023 - Работал с моделями в django- shell Пришлось удалить  и заново создавать связи в БД. Произошла ошибка при редактировании через админ панель свойства textPost. Проблему надеюсь решить завтра. Проблему решил сегодня: метод __str__ в models.py как свойство с помощью декоратора @property. Метод __str__ не должен быть свойством, это специальный метод в Python, который используется для представления объекта в виде строки. Вместо того, чтобы использовать @property,просто нужно определить метод __str__ как обычный метод, который возвращает строковое представление объекта.
