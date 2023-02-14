'''
    взаимодействие с пользователем

'''

class UserIterface:

    # Отображает пользовательское меню
    #   menu_dict - словарь с пунктами меню формата {int => str, ... }
    #   где ключевые значения соответствуют еомеру, заправшиваемому у пользователя
    #   если будет введено значение вне диапазока ключей - вернет 0
    def show_menu(self, menu_dict:dict):
        for i in menu_dict.keys():
            print(i, " - ", menu_dict[i])

        menu = int(input("> "))

        if menu in menu_dict.keys():
            return menu

        return 0


    # запрашивает строковое значенееи у пользователя
    #      message - сообщенеи для пользователя
    def ask_str(self, message):
        return input(message)

    # заправшивает целочисленное значение у пользователя
    #   message - сообщенеи для пользователя
    def ask_int(self, message):
        pass

    # запращивает дату у пользователя в формате ДД.ММ.ГГГГ
    #   message - сообщенеи для пользователя
    def ask_date(self, message):
        pass


    # запрашивает время у пользователя в формате ЧЧ:ММ
    #   message - сообщенеи для пользователя
    def ask_time(self, mesage):
        pass


