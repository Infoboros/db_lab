import psycopg2

DATABASE_NAME = "pes2"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "Sz22177Sz"
DATABASE_HOST = "localhost"


class Model:

    def __init__(self, table_name: str):
        self.conn = psycopg2.connect(dbname=DATABASE_NAME, user=DATABASE_USER,
                                     password=DATABASE_PASSWORD, host=DATABASE_HOST)
        self.conn.set_session(autocommit=True)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

        self._send_request(f'SELECT column_name, data_type '
                           f'from information_schema.columns '
                           f"where table_schema='public' AND table_name='{table_name}'")
        fields = self.cursor.fetchall()

        self.list_fileds = [el[0] for el in fields]
        self.list_types = [int if el[1] == 'integer' else str
                           for el in fields]

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
        if not field_list:
            raise self.SQLException("Укажите хотя бы одно поле.")
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
    def __init__(self, table_name: str):
        super().__init__(table_name)


class OrganizationType(Dict):
    def __init__(self):
        super().__init__("organizationtype")


class TypeOfEvent(Dict):
    def __init__(self):
        super().__init__("typeofevent")


class TypeOfWindow(Dict):
    def __init__(self):
        super().__init__("typeofwindow")


class TypeOfWall(Dict):
    def __init__(self):
        super().__init__("typeofwall")


class TypeOfResource(Dict):
    def __init__(self):
        super().__init__("typeofresource")


class MeterModel(Dict):
    def __init__(self):
        super().__init__("meter_model")


class Address(Model):
    def __init__(self):
        super().__init__("address")


class Manager(Model):
    def __init__(self):
        super().__init__("manager")


class EObject(Model):
    def __init__(self):
        super().__init__("eobject")


class Vehicle(Model):
    def __init__(self):
        super().__init__("vehicle")


class Event(Model):
    def __init__(self):
        super().__init__("event")


class Building(Model):
    def __init__(self):
        super().__init__("building")


class Resource(Model):
    def __init__(self):
        super().__init__("resource")


class Consumption(Model):
    def __init__(self):
        super().__init__("consumption")


class Meter(Model):
    def __init__(self):
        super().__init__("meter")
