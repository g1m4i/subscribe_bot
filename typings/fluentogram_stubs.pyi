from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    expense: Expense
    add_job_post: Add_job_post

    @staticmethod
    def error_when_getting_data() -> Literal["""Сталася помилка при запиті, повторіть дію"""]: ...

    @staticmethod
    def cant_get_job_by_url() -> Literal["""Не можу отримати інформацію про Job Post, можливо силка невірна або Jop Post прихований"""]: ...

    @staticmethod
    def start() -> Literal["""Для взаємодії з ботом, використовуй меню нижче."""]: ...

    @staticmethod
    def adding() -> Literal["""Додаю..."""]: ...


class Expense:
    select_category: ExpenseSelect_category
    add_description: ExpenseAdd_description

    @staticmethod
    def enter_sum() -> Literal["""Введіть суму витрат:"""]: ...

    @staticmethod
    def select_wallet() -> Literal["""Оберіть гаманець:"""]: ...

    @staticmethod
    def check_data(*, sum, wallet, category) -> Literal["""Перевірте введені дані:
Сума: { $sum } грн.
Гаманець: { $wallet }
Категорія: { $category }"""]: ...

    @staticmethod
    def write_description() -> Literal["""Введіть опис витрати:"""]: ...

    @staticmethod
    def check_data_description(*, sum, wallet, category, description) -> Literal["""Перевірте введені дані:
Сума: { $sum } грн.
Гаманець: { $wallet }
Категорія: { $category }
Опис: { $description }"""]: ...

    @staticmethod
    def added(*, created_time, sum, wallet, category, description) -> Literal["""✅ Витрату додано ✅
Дата: { $created_time }
Сума: { $sum } грн.
Гаманець: { $wallet }
Категорія: { $category }
Опис: { $description }"""]: ...

    @staticmethod
    def add_expense_error(*, created_time, sum, wallet, category, description) -> Literal["""⚠️ Помилка при додавані витрати ⚠️
Дата: { $created_time }
Сума: { $sum } грн.
Гаманець: { $wallet }
Категорія: { $category }
Опис: { $description }"""]: ...


class ExpenseSelect_category:
    @staticmethod
    def __call__() -> Literal["""Оберіть категорію:"""]: ...

    @staticmethod
    def button() -> Literal["""Обрати"""]: ...


class ExpenseAdd_description:
    @staticmethod
    def button() -> Literal["""📝 Додати опис"""]: ...


class Add_job_post:
    @staticmethod
    def input_job_post_url() -> Literal["""Ви в меню додавання Job Posts. Надішліть мені посилання для додавання його в CRM.

Для виходу з меню, натисніть &#34;❌&#34;"""]: ...

    @staticmethod
    def job_added(*, url) -> Literal["""Job Post 
{ $url }
Успішно додано ✅"""]: ...

