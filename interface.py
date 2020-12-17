from models import *


class TableOutput:
    def __init__(self, list_row: list, list_fields: list):
        self.list_row = list_row
        self.list_fields = list_fields

    def __str__(self):
        out_list = ["" for i in range(len(self.list_row) + 1)]
        for i in range(len(self.list_fields)):
            max_len = len(self.list_fields[i])
            for row in self.list_row:
                max_len = max(max_len, len(str(row[i])))
            out_list[0] += str(self.list_fields[i]).ljust((max_len+4)*2, " ")
            for row_index in range(len(self.list_row)):
                out_list[row_index + 1] += str(self.list_row[row_index][i]).ljust((max_len+4)*2, " ")
        return "\n".join(out_list)


class ProcessModel:
    def __init__(self, model: Model):
        self.model = model
        self.show_str = '\n'.join([f'{"%3s. " % str(i)}{self.model.list_fileds[i]}:{self.model.list_types[i]}'
                                   for i in range(len(self.model.list_fileds))])
        self.process_str = '\n'.join(self.show_str.split('\n')[1:])

    def create(self):
        return self.model.create(**self._get_kwargs('создания', self.process_str, False))

    def update(self):
        print("Введите ID: ", end='')
        try:
            id = int(input())
        except:
            raise self.ParseError("Введите ID, он нужен!")
        return self.model.patch(id, **self._get_kwargs('обнавления', self.process_str, False))

    def _get_kwargs(self, description: str, parametrs: str, find_flag: bool = True):
        print(f"Введите через запятую параметры {description} и их значения (a=5,b=2)\n"
              f"{'Оставьте пустым для получения всех записей' if find_flag else ''}\n"
              f"Список параметров: \n"
              f"{parametrs}\n"
              f"$>", end='')
        kwargs = {}
        inp = input() \
            .replace(' ', '') \
            .replace('\n', '') \
            .split(',')
        if inp != ['']:
            for token in inp:
                # Тут нельзя сделать через один try, типы ошибок одинаковые(
                try:
                    field, arg = token.split('=')
                except:
                    raise self.ParseError("Параметры пишутся через =.")

                try:
                    t_i = self.model.list_fileds.index(field)
                except:
                    raise self.ParseError(f"У модели {self.model.table_name} нет поля {field}.")

                try:
                    kwargs.update({
                        field: self.model.list_types[t_i](arg)
                    })
                except:
                    raise self.ParseError(
                        f"Введенное поле {field} не соответствует типу {self.model.list_types[t_i]}.")
        return kwargs

    def read(self):
        return self.model.filter(**self._get_kwargs("поиска", self.show_str))

    def delete(self):
        return self.model.delete(**self._get_kwargs("поиска", self.show_str))
    class ParseError(Exception):
        pass


models = {
    1: OrganizationType,
    2: TypeOfEvent,
    3: TypeOfWindow,
    4: TypeOfWall,
    5: TypeOfResource,
    6: MeterModel,
    7: Address,
    8: Manager,
    9: EObject,
    10: Vehicle,
    11: Event,
    12: Building,
    13: Resource,
    14: Consumption,
    15: Meter
}
if __name__ == "__main__":
    while (True):
        print("Выберите таблицу для работы")
        print("  0. Выход")
        for id, model in models.items():
            print(f"{'%3s. ' % id}{str(model).split('.')[1][:-2]}")

        print("$> ", end='')
        run_flag = int(input())
        if not run_flag:
            break

        model = models[run_flag]()
        processor = ProcessModel(model)
        while (True):
            print("Выберите действие\n"
                  "0 - выбрать другую таблицу\n"
                  "1 - create\n"
                  "2 - update\n"
                  "3 - filter\n"
                  "4 - delete\n"
                  "$> ", end='')
            f = int(input())
            try:
                if f == 0:
                    break
                elif f == 1:
                    list_row = processor.create()
                elif f == 2:
                    list_row = processor.update()
                elif f == 3:
                    list_row = processor.read()
                elif f == 4:
                    list_row = processor.delete()
                print(TableOutput(list_row, model.list_fileds))
            except Exception as e:
                print(e)
