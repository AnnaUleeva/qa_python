import pytest

from main import BooksCollector

@pytest.fixture # фикстура, которая создает коллекцию с набором книг
def default_collector():
    collector = BooksCollector()

    # Без жанра
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    # Фантастика
    collector.add_new_book('Питон за один день')
    collector.set_book_genre('Питон за один день', 'Фантастика')

    # Ужасы
    collector.add_new_book('Зловещие мертвецы')
    collector.add_new_book('Обитель проклятых')
    collector.set_book_genre('Зловещие мертвецы', 'Ужасы')
    collector.set_book_genre('Обитель проклятых', 'Ужасы')

    # Детективы
    collector.add_new_book('Убийство в Восточном экспрессе')
    collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')

    # Мультфильмы
    collector.add_new_book('Красавица и чудовище')
    collector.set_book_genre('Красавица и чудовище', 'Мультфильмы')

    # Избранное
    collector.add_book_in_favorites('Убийство в Восточном экспрессе')
    collector.add_book_in_favorites('Красавица и чудовище')


    return collector