import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'book_name, genre, expect',
        [
            ['Что делать, если ваш кот хочет вас убить', 'Фантастика', 'Фантастика'],
            ['Что делать, если ваш кот хочет вас убить', 'Жанр, которого нет', ''],
            ['Книга, которой нет в колекции', 'Фантастика', None],
            [None, 'Фантастика', None],
            ['', 'Фантастика', None],
        ]
    )
    def test_set_book_genre(self, default_collector, book_name, genre, expect):
        default_collector.set_book_genre(book_name, genre)
        assert default_collector.get_book_genre(book_name) == expect

    @pytest.mark.parametrize(
        'book_name, expect',
        [
            ['Что делать, если ваш кот хочет вас убить', ''],
            ['Питон за один день', 'Фантастика'],
            ['Книга, которой нет в колекции', None],
            [None, None],
            ['', None],
        ]
    )
    def test_get_book_genre(self, default_collector, book_name, expect):
        assert default_collector.get_book_genre(book_name) == expect

    @pytest.mark.parametrize(
        'genre, expect',
        [
            ['', 0],
            [None, 0],
            ['Фантастика', 1],
            ['Жанр, которого нет', 0],
            ['Ужасы', 2]
        ]
    )
    def test_get_books_with_specific_genre(self, default_collector, genre, expect):
        assert len(default_collector.get_books_with_specific_genre(genre)) == expect

    def test_get_books_genre_without_books(self):
        collector = BooksCollector()
        assert len(collector.get_books_genre()) == 0

    def test_get_books_genre_with_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_with_existing_age_rating_collector(self, default_collector):
        assert len(default_collector.get_books_for_children()) == 2

    def test_get_books_for_children_with_only_age_rating_collector(self):
        collector = BooksCollector()

        collector.add_new_book('Зловещие мертвецы')
        collector.set_book_genre('Зловещие мертвецы', 'Ужасы')

        collector.add_new_book('Обитель проклятых')
        collector.set_book_genre('Обитель проклятых', 'Ужасы')

        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')

        assert len(collector.get_books_for_children()) == 0

    @pytest.mark.parametrize(
        'book_name, expect',
        [
            ['', 2],
            [None, 2],
            ['Гордость и предубеждение и зомби', 3],
            ['Убийство в Восточном экспрессе', 2],
        ]
    )
    def test_add_book_in_favorites(self, default_collector, book_name, expect):
        default_collector.add_book_in_favorites(book_name)
        assert len(default_collector.get_list_of_favorites_books()) == expect

    @pytest.mark.parametrize(
        'book_name, expect',
        [
            ['', 2],
            [None, 2],
            ['Гордость и предубеждение и зомби', 2],
            ['Убийство в Восточном экспрессе', 1],
        ]
    )
    def test_delete_book_from_favorites(self, default_collector, book_name, expect):
        default_collector.delete_book_from_favorites(book_name)
        assert len(default_collector.get_list_of_favorites_books()) == expect

    def test_get_list_of_favorites_books_with_existing_favorites_books(self, default_collector):
        assert len(default_collector.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_books_without_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0