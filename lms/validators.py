import re
from rest_framework.serializers import ValidationError


class LinkValidator:
    """
    Video Tutorial Link Validator
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field).strip()
        if not re.match("https://www.youtube.com/watch", tmp_val[:29]) or len(tmp_val) <= 29:
            raise ValidationError(
                'Unfortunately, the link does not comply with the rules. '
                'Please enter the link that starts with "https://www.youtube.com/watch"')