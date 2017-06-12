import traceback

from db.condition import Condition


def relationship(self_key, mapper, obj_key, single=False):
    from hometask_web import mappers

    def wrap(self):
        if hasattr(self, self_key + '_id'):
            value = getattr(self, self_key + '_id')
        else:
            value = getattr(self, self_key)
        values = getattr(mappers, mapper)().select(Condition(obj_key, value))
        if values:
            if single:
                return values[0]
            else:
                return values
        else:
            if single:
                return None
            else:
                return []
    return wrap


def many_to_many(through, self_key, on_self, on_to, to_mapper, to_key, single=False):
    from hometask_web import mappers

    def wrap(self):
        if hasattr(self, self_key + '_id'):
            value = getattr(self, self_key + '_id')
        else:
            value = getattr(self, self_key)
        values = getattr(mappers, through)().select(Condition(on_self, value))
        if not values:
            if single:
                return None
            else:
                return []
        try:
            values = getattr(mappers, to_mapper)().select(Condition(to_key, [getattr(v, on_to) for v in values]))
        except Exception as e:
            traceback.print_exc()
            raise

        if values:
            if single:
                return values[0]
            else:
                return values
        else:
            if single:
                return None
            else:
                return []
    return wrap


def set_relationship(pname, obj_key):
    def wrap(self, value):
        if isinstance(value, int):
            setattr(self, pname + "_id", value)
        else:
            setattr(self, pname + "_id", getattr(value, obj_key))
    return wrap
