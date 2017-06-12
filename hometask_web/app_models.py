import datetime

from db.utils import relationship, many_to_many, set_relationship


class PC:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    adapters = property(relationship('id', 'AdapterMapper', 'pc_id'))
    configuration = property(many_to_many(
        through='ConfigurationPCMapper',
        self_key='id',
        to_mapper='ConfigurationMapper',
        to_key='id',
        on_self='pc_id',
        on_to='c_id',
        single=True))

    @property
    def is_alive(self):
        if self.configuration:
            return self.configuration.start_at < datetime.datetime.now().time() < self.configuration.shutdown_at
        return False


class Adapter:
    def __init__(self, id, address, pc):
        self.id = id
        self.address = address
        self.pc_id = pc

    pc = property(relationship('pc_id', 'PCMapper', 'id', single=True))
    incoming_connections = property(relationship('id', 'ConnectionMapper', 'from_adapter'))
    outgoing_connections = property(relationship('id', 'ConnectionMapper', 'to_adapter'))


class Connection:
    def __init__(self, id, from_id, to_id):
        self.id = id
        self.from_adapter = from_id
        self.to_adapter = to_id

    from_adapter = property(relationship('from_adapter', 'AdapterMapper', 'id', single=True), set_relationship("from_adapter", "id"))
    to_adapter = property(relationship('to_adapter', 'AdapterMapper', 'id', single=True), set_relationship("to_adapter", "id"))


class Configuration:
    def __init__(self, id, title, start_at, shutdown_at, allow_internet):
        self.id = id
        self.title = title
        self.start_at = datetime.time(*[int(x) for x in start_at.split(":")])
        self.shutdown_at = datetime.time(*[int(x) for x in shutdown_at.split(":")])
        self.allow_internet = allow_internet


class ConfigurationPC:
    def __init__(self, id, pc_id, c_id):
        self.id = id
        self.pc_id = pc_id
        self.c_id = c_id


