import psycopg2

DATABASE_NAME = "pes2"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "Sz22177Sz"
DATABASE_HOST = "localhost"


class Model:

    def __init__(self):
        self.conn = psycopg2.connect(dbname=DATABASE_NAME, user=DATABASE_USER,
                                     password=DATABASE_PASSWORD, host=DATABASE_HOST)
        self.conn.set_session(autocommit=True)
        self.cursor = self.conn.cursor()
        self.table_name = "table_name"
        self.list_fileds = ['id']
        self.list_types = [int]

    def _get_arg(self, arg) -> str:
        if type(arg) is str:
            return "'" + arg + "'"
        return str(arg)

    def _get_where_param(self, **kwargs) -> str:
        where_list = []
        for name_arg, value_arg in kwargs.items():
            if name_arg not in self.list_fileds:
                raise self.SQLException(f"У модели {self.table_name} нет поля {name_arg}")
            where_list.append(f"{name_arg}={self._get_arg(value_arg)}")
        if not where_list:
            return "true"
        return " and ".join(where_list)

    def _send_request(self, request: str):
        try:
            self.cursor.execute(request)
        except psycopg2.errors.NotNullViolation as e:
            field = str(e).split('"')[1]
            raise self.SQLException(f"Поле {field} является обязательным.")
        except psycopg2.errors.ForeignKeyViolation as e:
            str_e = str(e)
            fk_table = str_e.split('"')[-2]
            id = str_e.split(')')[-2].split('(')[-1]
            raise self.SQLException(f"Ошибка ограничения целостности.\n "
                                    f"В таблице {fk_table} нет строки с id={id}")
        except psycopg2.InterfaceError as e:
            raise self.SQLException("Нарушено соединение с сервером БД.")
        except Exception as e:
            raise self.SQLException(f"Возникла неизвестная ошибка\n"
                                    f"{str(e)}")

    def delete(self, **kwargs):
        ret = self.filter(**kwargs)
        self._send_request(f'DELETE FROM {self.table_name} '
                           f'WHERE {self._get_where_param(**kwargs)}')
        return ret

    def create(self, **kwargs):
        field_list = []
        arg_list = []
        for field, arg in kwargs.items():
            field_list.append(field)
            arg_list.append(self._get_arg(arg))

        self._send_request(f'INSERT INTO {self.table_name}'
                           f' {"(" + ",".join(field_list) + ")"} '
                           f'VALUES {"(" + ",".join(arg_list) + ")"}')

        return self.filter(**kwargs)

    def patch(self, id: int, **kwargs):
        kwargs = self._get_where_param(**kwargs)
        if kwargs == 'true':
            raise self.SQLException("Укажите хотя бы один параметр для обнавления.")
        self._send_request(f'UPDATE {self.table_name} '
                           f'SET {kwargs.replace(" and ", ",")} '
                           f'WHERE id={id}')
        return self.filter(id=id)

    def filter(self, **kwargs):
        self._send_request(f'SELECT * FROM {self.table_name} '
                           f'WHERE {self._get_where_param(**kwargs)}')
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    class SQLException(Exception):
        pass


class Dict(Model):
    def __init__(self):
        super().__init__()
        self.list_fileds += ['description']
        self.list_types += [str]


class OrganizationType(Dict):
    def __init__(self):
        super().__init__()
        self.table_name = "organizationtype"


class TypeOfEvent(Dict):
    def __init__(self):
        super().__init__()
        self.table_name = "typeofevent"


class TypeOfWindow(Dict):
    def __init__(self):
        super().__init__()
        self.table_name = "typeofwindow"


class TypeOfWall(Dict):
    def __init__(self):
        super().__init__()
        self.table_name = "typeofwall"


class TypeOfResource(Dict):
    def __init__(self):
        super().__init__()
        self.table_name = "typeofresource"


class MeterModel(Dict):
    def __init__(self):
        super().__init__()
        self.table_name = "meter_model"


class Address(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "address"
        self.list_fileds += [
            'index',
            'region',
            'rajon',
            'town',
            'street',
            'building',
            'corpus'
        ]
        self.list_types += [int] + [str for _ in range(6)]


class Manager(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "manager"
        self.list_fileds += [
            'last_name',
            'first_name',
            'patronymic_name',
            'position',
            'phone',
            'email'
        ]
        self.list_types += [str for _ in range(6)]


class EObject(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "eobject"
        self.list_fileds += [
            'type_org',
            'place_adress',
            'director',
            'inn',
            'ogrn',
            'okved',
            'full_name',
            'phone',
            'pes_having'
        ]
        self.list_types += [int for _ in range(4)] + [str for _ in range(4)] + [bool]


class Vehicle(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "vehicle"
        self.list_fileds += [
            'eobject',
            'name',
            'count',
            'carrrying',
            'milleage',
            'fuel_rate'
        ]
        self.list_types += [int, str] + [int for _ in range(4)]


class Event(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "event"
        self.list_fileds += [
            'eobject',
            'type_event',
            'percentage_save',
            'year',
            'cost'
        ]
        self.list_types += [int for _ in range(2)] + [float] + [int for _ in range(2)]


class Building(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "building"
        self.list_fileds += [
            'eobject',
            'type_window',
            'type_wall',
            'name',
            'description',
            'place',
            'square',
            'space',
            'level_count'
        ]
        self.list_types += [int for _ in range(3)] + [str for _ in range(2)] + [int, float, float, int]


class Resource(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "resource"
        self.list_fileds += [
            'eobject',
            'type_resource',
            'name_rso',
            'contract_number',
            'contract_date'
        ]
        self.list_types += [int for _ in range(2)] + [str for _ in range(3)]


class Consumption(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "consumption"
        self.list_fileds += [
            'resource',
            'year',
            'annuale_rate',
            'annuale_cost'
        ]
        self.list_types += [int for _ in range(4)]


class Meter(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "meter"
        self.list_fileds += ['building',
                             'resource',
                             'date_commissioning',
                             'factory_number',
                             'date_verification',
                             'model',
                             ]
        self.list_types += [int for _ in range(2)] + [float] + [int for _ in range(3)]
