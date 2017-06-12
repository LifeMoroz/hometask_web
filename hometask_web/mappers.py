from collections import OrderedDict

from db.mapper import BaseMapper
from hometask_web.app_models import PC, Adapter, Connection, Configuration, ConfigurationPC


class PCMapper(BaseMapper):
    model = PC
    table_name = 'pc'

    def db_obj_map(self):
        m = OrderedDict()
        # key - db, value - python
        m['id'] = 'id'
        m['title'] = 'title'
        return m


class AdapterMapper(BaseMapper):
    model = Adapter
    table_name = 'adapter'

    def db_obj_map(self):
        m = OrderedDict()
        # key - db, value - python
        m['id'] = 'id'
        m['address'] = 'address'
        m['pc_id'] = 'pc_id'
        return m


class ConnectionMapper(BaseMapper):
    model = Connection
    table_name = 'connection'

    def db_obj_map(self):
        m = OrderedDict()
        # key - db, value - python
        m['id'] = 'id'
        m['from_adapter_id'] = 'from_adapter'
        m['to_adapter_id'] = 'to_adapter'
        return m


class ConfigurationMapper(BaseMapper):
    model = Configuration
    table_name = 'configuration'

    def db_obj_map(self):
        m = OrderedDict()
        # key - db, value - python
        m['id'] = 'id'
        m['title'] = 'title'
        m['start_at'] = 'start_at'
        m['shutdown_at'] = 'shutdown_at'
        m['allow_internet'] = 'allow_internet'
        return m


class ConfigurationPCMapper(BaseMapper):
    model = ConfigurationPC
    table_name = 'configuration_pc'

    def db_obj_map(self):
        m = OrderedDict()
        # key - db, value - python
        m['id'] = 'id'
        m['pc_id'] = 'pc_id'
        m['c_id'] = 'c_id'
        return m
