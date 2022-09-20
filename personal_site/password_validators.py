from django.core.exceptions import ValidationError


class EndsWith123Validator:
    def validate(self, password, user=None):
        if not password.endswith('123'):
            raise ValidationError(
                'Пароль должен заканчиваться на "123"',
                code="password doesn't end with '123'",
            )

    def get_help_text(self):
        return "Все стандартные валидаторы отключены. Есть один кастомный -  пароль должен заканчиваться на \"123\". " \
               "Всё очень просто."
