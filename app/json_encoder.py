from json import JSONEncoder

from .models import Contact


class ContactAwareJSONEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, Contact):
            return o.to_dict()

        return super().default(o)
