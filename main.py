from kivy.config import Config
Config.set('graphics', 'fullscreen', 0)
Config.write()
from kivymd.uix.dialog import MDDialog
import requests
import json
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.properties import DictProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.dropdown import DropDown
from kivymd.uix.button import MDFlatButton
from datetime import datetime
import calendar
import timeit
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.clock import Clock, _default_time as time
from kivymd.uix.card import MDSeparator
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivy.uix.recycleview import RecycleView
import re
import time as Time
from kivy.uix.recycleview.views import RecycleDataViewBehavior
#bpvtyt
DOUBLE_TAP_TIME = 0.2   # Change diley time between tap in seconds (for MDCard "work_do")
LONG_PRESSED_TIME = 0.9  # Change time in seconds for long press (for MDCard "work_do")
MAX_TIME = 1/600. #time for bilding dropdown list
MAX_TIME_GROUP = 1/60. # time for bilding work_do list

text_for_app = {'UA': {'calendar_month':{"01":"Январь",
                                        "02": "Февраль",
                                        "03": "Март",
                                        "04": "Апрель",
                                        "05": "Май",
                                        "06": "Июнь",
                                        "07": "Июль",
                                        "08": "Август",
                                        "09": "Сентябрь",
                                        "10": "Октябрь",
                                        "11": "Ноябрь",
                                        "12": "Декабрь"},
                       'currency': 'грн',
                       'change_lang':'Выберите язык',
                       'msg_change_lang':'Перезагрузите приложение',
                       'msg_you_login': 'Вы вошли в систему',
                       'msg_no_connect': 'НЕТ СОЕДИНЕНИЯ',
                       'msg_wrong_login': 'Неверный логин или пароль',
                       'msg_delete_work': 'Удалить запись?',
                       'msg_check_fields': 'Заполните поля красного цвета',
                       'btn_login_enter': 'Войти в систему',
                        'btn_login_exit': 'Выйти',
                       'btn_create_work': 'Создать работу',
                       'btn_save': 'Сохранить',
                       'btn_cansel': 'Отменить',
                       'btn_ok': 'OK',
                       'btn_CANSEL': 'ОТМЕНА',
                       'title_login':'Авторизируйтесь',
                       'title_done_work': 'Выполненные работы',
                       'title_count_for': 'Сумма за',
                       'title_no_link_server': 'Нет соединения с сервером',
                       'title_calendar_choose': 'ВЫБЕРИТЕ ПЕРИОД',
                        'title_unit_name': 'Единица измрения',
                       'title_price': 'Стоимость',
                        'title_info_type_work': 'Инф. типа работы',
                       'title_work_type_list': 'Cписок работ',
                       'title_count': 'Расчет',
                       'title_settings': 'Настройки',
                       'title_info': 'Информация',
                       'title_work': 'Работы',
                       'title_server_adress': 'Адрес сервера',
                       'title_server_help': 'Введите адрес сервера',
                       'title_port': 'Порт серера',
                       'title_port_help': 'Введите порт сервера',
                       'title_username': 'Имя пользователя',
                       'title_username_help': 'Введите имя пользователя',
                       'title_password': 'Пароль',
                       'title_password_help': 'Введите пароль',
                       'title_amount': 'Колличество',
                       'space_amount': ' ',
                       'title_amount_info': 'Введите колличество',
                       'title_wired': 'Кабель',
                       'space_wired': '           ',
                       'title_object': 'Объект',
                       'space_object': '          ',
                       'title_object_help': 'Выберите объект',
                       'title_choose_workers': 'Выберите напарника',
                       'title_work_type': 'Тип работы',
                       'title_work_type_info': 'Выберите тип работы',
                       'title_date': 'Дата',
                       'space_date': '               ',
                       'title_complex': 'Сложность',
                       'space_complex': '   ',
                       'title_complex_info': 'Выберите сложность',
                       'title_equipment': 'Оборудование',
                       'title_equipment_info': 'Выберите оборудование',
                       'title_bonus': 'Премия',
                       'space_bonus': '          ',
                       'title_workers': 'Монтажники',
                       'space_workers': '',
                       'title_notes': 'Примечания',
                       'space_notes': ' ',
                       'title_notes_info': 'Опишите примечание к работе',
                       'title_choose_year': 'Выберите год',
                       'title_choose_month': 'Выберите месяц',
                       'info_wrong_login': 'Неверный логин или пароль...',
                       'info_login_systems': 'Войдите в систему...',
                       'info_1': 'Перед началом работ зайдите в пункт меню "Настройки" и введите адрес сервера, логин и пароль и нажмите кнопку "Войти в систему" ',
                       'info_2': '- Кнопка групировки по объектам',
                       'info_3': 'При запуске программы показывается режим сортировки по дате добавления, если хотите переключить в режим группировки работ по объектам нажмите кнопку "Групировка по объктам". Чтобы переключиться обратно в режим сортировки по дате - нажмите еще раз эту кнопку',
                       'info_4': '- Фильтр по дате',
                       'info_5': 'Если хотите просмотреть работы за прошлые месяци нажмите кнопку "Фильр по дате" выберите дату начала и дату окончания в пределах одного месяца. Если, ввели не то - просто нажмите ОТМЕНА и попробуйте заново',
                       'info_6': '- Добавить новую работу',
                       'info_7': 'Нажмите эту кнопку если хотите добавить новую выполненую работу. Учтите есть поля обязательные для заполнения, если вы их не введете они обозначаться красным подчеркиванием, введите в них данные и сохраните',
                       'info_8': 'Редактирование записи',
                       'info_9': ' - Для редактирование добавленых работ нажмите три раза на нужную рработу',
                       'info_10': 'Удаление записи',
                       'info_11': ' - Для удаления добавленой работы нажмите и удерживайте палец над нужной работой в течении 3с'
                        },

                'BG': {'calendar_month':{"01": "Януари",
                                        "02": "Февруари",
                                        "03": "Март",
                                        "04": "Април",
                                        "05": "Май",
                                        "06": "Юни",
                                        "07": "Юли",
                                        "08": "Август",
                                        "09": "Септември",
                                        "10": "Октомври",
                                        "11": "Ноември",
                                        "12": "Декември"},
                       'change_lang':'Изберете език',
                       'msg_change_lang': 'Рестартирайте приложението',
                       'currency': 'лев',
                       'msg_you_login': 'Вие сте влезли в системата',
                       'msg_no_connect': 'БЕЗ ВРЪЗКА',
                       'msg_wrong_login': 'Неправилно име или парола',
                       'msg_delete_work': 'Изтриване на записа?',
                       'msg_check_fields': 'Попълнете всички полета, отбелязани със звездичка',
                       'btn_login_enter': 'Влезте в системата',
                       'btn_login_exit': 'Выйти',
                       'btn_create_work': 'Создать работу',
                       'btn_save': 'Запазете',
                       'btn_cansel': 'Отмени',
                       'btn_ok': 'OK',
                       'btn_CANSEL': 'ОТМЕНИ',
                       'title_login': 'Оторизиране на',
                       'title_done_work': 'Извършена работа',
                       'title_count_for': 'Сумата за',
                       'title_no_link_server': 'Няма връзка със сървъра',
                       'title_calendar_choose': 'Изберете период',
                       'title_unit_name': 'Мерна единица',
                       'title_price': 'Цена',
                       'title_info_type_work': 'Инф. вид работы',
                       'title_work_type_list': 'Списък на работните',
                       'title_count': 'Изчисление',
                       'title_settings': 'Настройки',
                       'title_info': 'Информация',
                       'title_work': 'Работы',
                       'title_server_adress': 'Адрес на сървъра',
                       'title_server_help': 'Въведете адреса на сървъра',
                       'title_port': 'Порт сървъра',
                       'title_port_help': 'Въведете порт сървъра',
                       'title_username': 'Потребителско име',
                       'title_username_help': 'Въведете потребителско име',
                       'title_password': 'Парола',
                       'title_password_help': 'Въведете парола',
                       'title_amount': 'Брой',
                       'space_amount': '              ',
                       'title_amount_info': 'Въведете броя',
                       'title_wired': 'Кабел',
                       'space_wired': '            ',
                       'title_object': 'Обект',
                       'space_object': '            ',
                       'title_object_help': 'Избиране на обект',
                       'title_choose_workers': 'Изберете партньор',
                       'title_work_type': 'Вид работа',
                       'title_work_type_info': 'Изберете вида работа',
                       'title_date': 'Дата',
                       'space_date':'               ',
                       'title_complex': 'Сложност',
                       'space_complex': '     ',
                       'title_complex_info': 'Изберете трудността',
                       'title_equipment': 'Оборудование',
                       'title_equipment_info': 'Изберете оборудването',
                       'title_bonus': 'Награда',
                       'space_bonus': '        ',
                       'title_workers': 'Монтажисти',
                       'space_workers': '',
                       'title_notes': 'Забележки',
                       'space_notes': '   ',
                       'title_notes_info': 'Опишете служебната бележка',
                       'title_choose_year': 'Изберете година',
                       'title_choose_month': 'Изберете месец',
                       'info_wrong_login': 'Неправилно име или парола...',
                       'info_login_systems': 'Влезте в системата...',
                       'info_1': 'Преди да започнете работа, отидете в менюто "Настройки", въведете адреса на сървъра, потребителското име и паролата и натиснете бутона "Влезте в системата" ',
                       'info_2': ' - Бутон за групиране по обекти',
                       'info_3': 'Когато стартирате програмата, тя показва режим на сортиране по дата на добавяне, ако искате да преминете към групиране на дейностите по обекти, натиснете бутона "Групиране по обекти". Ако искате да се върнете към сортиране по дата, натиснете отново този бутон.',
                       'info_4': '- Фильтр по дате',
                       'info_5': 'Ако искате да видите работата от миналия месец, натиснете бутона "Филтриране по дата" и изберете желания месец и година. Натиснете бутона OK',
                       'info_6': '- Добавяне на ново работно',
                       'info_7': 'Натиснете този бутон, ако искате да добавите ново завършено задание. Моля, обърнете внимание, че има задължителни полета, отбелязани със звездичка *, ако не ги въведете, те са отбелязани с червено подчертаване, въведете данните в тях и ги запазете.',
                       'info_8': 'Редактиране на запис',
                       'info_9': ' - За да редактирате добавена задача, щракнете три пъти върху въпросната задача.',
                       'info_10': 'Изтриване на запис',
                       'info_11': ' - За да изтриете добавено задание, натиснете и задръжте пръста си върху желаното задание за 3 сек.'
                       }
                }
#class for connect with CRM rukovoditel
class rkv_api:
    def __init__(self, app_instance):
        super().__init__()
        self.Flag_config = False
        self.Flag_connection = False
        self.Flag_authent = False
        self.Login = 0
        self.Password = 0
        self.user_id = 0
        self.user_secondname = 0
        self.app_instance = app_instance
        self.srv_adress = ''
        self.port = 0
        now = datetime.now()
        self.date_now = now.strftime("%Y-%m-%d")
        self.date_start = now.strftime("%Y-%m-") + '01'
        self.date_end = f'{now.strftime("%Y-%m-")}{calendar.monthrange(now.year, now.month)[1]}'
        self.work_list = 0
        self.do_work_list = 0
        self.equipment_list = 0
        self.object_list = 0
        self.users_on_object_list = 0
        self.users_list = 0
        self.last_id_work = 0
        self.last_id_do_work = 0
        self.complex_list = 0
        self.new_do_work = 0
        self.many_for_pay = ''
        self.app_type = ''
        self.conf_serv = 0

    def init(self):
        try:
            f = open('config.txt', 'r')
        except:
            return ('no_config')
        else:
            conf_str = f.read()
            if conf_str != '':
                self.Flag_config = True
                conf = conf_str.split(',')
                self.srv_adress = conf[2]
                self.port = conf[3]
                url = self.srv_adress + 'get_work_list(1).php'
                try:
                    res = requests.post(url, timeout=2.5, data={"login": conf[0], 'pass': conf[1]})
                except:
                    self.Login = conf[0]
                    self.Password = conf[1]
                    self.conf_serv = self.get_conf_serv(off_line=True)
                    self.users_list = self.get_users_list(off_line=True)
                    self.work_list = self.get_work_list(off_line=True)
                    self.do_work_list = self.get_do_work_list(self.date_start, self.date_end, off_line=True)
                    self.object_list = self.get_object(off_line=True)
                    self.equipment_list = self.get_equipment_list(off_line=True)
                    self.complex_list = self.get_complex_list(off_line=True)
                    # self.users_on_object_list = self.get_users_on_object('41')
                    return ('ok')
                else:
                    self.Flag_connection = True
                    answer = json.loads(res.text)
                    if answer['status'] == 'success':
                        self.Flag_authent = True
                        self.Login = conf[0]
                        self.Password = conf[1]
                        self.users_list = self.get_users_list()
                        self.conf_serv = self.get_conf_serv()
                        self.work_list = self.get_work_list()
                        self.do_work_list = self.get_do_work_list()
                        self.object_list = self.get_object()
                        self.equipment_list = self.get_equipment_list()
                        self.complex_list = self.get_complex_list()
                        return ('ok')
                    else:
                        self.Login = conf[0]
                        self.Password = conf[1]
                        return ('bad_login')
            f.close()

    def count_many(self, get_do_work_list = 0):
        if self.Flag_config:
            self.many_for_pay = 0
            if get_do_work_list == 0:
                do_work_list = self.do_work_list
            else:
                do_work_list = get_do_work_list
            for work in do_work_list['data']:
                if work['254'] == 'да':
                    self.many_for_pay += float(work[self.conf_serv])*float(work['224'])
            return str(self.many_for_pay)
        else:
            return '0'

    def login(self, login=0, password=0, srv_adress=0, port=38654, lang='UA', Log_in=True):
        if Log_in:
            self.srv_adress = 'http://'+srv_adress+':'+ port + '/'

            url =  self.srv_adress  + 'get_work_list(1).php'
            try:
                res = requests.post(url, timeout=2.5, data={'login': login,
                                               'pass': password,
                                               'srv_adress': srv_adress
                                               }
                                    )
            except:
                print('нет соединения регистрация')
            else:

                self.Login = login
                self.Password = password
                self.conf_serv=0
                self.work_list = 0
                self.do_work_list = 0
                self.equipment_list = 0
                self.object_list = 0
                self.users_on_object_list = 0
                self.users_list = 0
                all_conf_serv = self.get_conf_serv(conf_all=True)


                self.conf_serv = all_conf_serv['price_field']
                self.Flag_connection = True
                answer = json.loads(res.text)
                if answer['status'] == 'success':
                    self.Flag_authent = True
                    with open('config.txt', 'w', encoding="utf-8") as f:
                        f.write(f"{login},{password},{self.srv_adress},{port},{self.conf_serv},{lang}")
                    self.Flag_config = True
                    self.init()
                    p = requests.get(all_conf_serv['logo_img'])
                    out = open("logo.png", "wb")
                    out.write(p.content)
                    out.close()
                else:
                    print('error_login')
        else:
            with open('config.txt', 'w', encoding="utf-8") as f:
                f.write('')
            self.Flag_config = False
            self.Flag_connection = False
            self.Flag_authent = False

    def get_conf_serv(self, off_line=False, conf_all=False):
        if self.conf_serv == 0:
            url = self.srv_adress + 'get_conf_serv.php'
            if off_line:
                with open('config.txt', 'r', encoding="utf-8") as f:
                    conf_str= f.read()
                serv_conf = conf_str.split(',')
                return serv_conf[4]
            else:
                try:
                    res = requests.post(url, timeout=2.5, data={'login': self.Login,
                                                   'pass': self.Password})
                except:
                    with open('config.txt', 'r', encoding="utf-8") as f:
                        serv_conf = json.loads(f.read())
                    if conf_all:
                        return {'price_field':'', 'logo_img':''}
                    else:
                        print('111111111')
                        return serv_conf[4]
                else:
                    serv_conf = json.loads(res.text)
                    if conf_all:
                        return serv_conf
                    else:
                        print('111111111')
                        return serv_conf['price_field']
        else:
            return self.conf_serv


    def get_work_list(self, find_word='', off_line=False):
        if self.work_list == 0:
            url = self.srv_adress + 'get_work_list.php'
            if off_line:
                with open('work_list.txt', 'r', encoding="utf-8") as f:
                    return json.loads(f.read())
            else:
                try:
                    res = requests.post(url, timeout=3, data={'find_word': find_word,
                                                   'login': self.Login,
                                                   'pass': self.Password
                                                   })
                except:
                    with open('work_list.txt', 'r', encoding="utf-8") as f:
                        return json.loads(f.read())
                else:
                    with open('work_list.txt', 'w', encoding="utf-8") as f:
                        f.write(res.text)
                    return json.loads(res.text)
        else:
            return self.work_list

    def add_new_do_work(self, array_id_for_new, array_text_for_new):
        url = self.srv_adress + 'add_new.php'
        try:
            res = requests.post(url, timeout=3, data={'223': array_id_for_new['223'],
                                           '239': array_id_for_new['239'],
                                           '224': array_id_for_new['224'],
                                           '237': array_id_for_new['237'],
                                           '252': array_id_for_new['252'],
                                           '267': self.date_now,
                                           '253': array_id_for_new['253'],
                                           'parent_item_id': array_id_for_new['parent_item_id'],
                                           'login': self.Login,
                                           'pass': self.Password
                                           })
        except:
            return {'status': 'no_link'}
        else:
            return json.loads(res.text)

    def update_work_do(self, array_for_update, id_update_item):
        json_array_for_update = json.dumps(array_for_update)
        url = self.srv_adress + 'update_item.php'
        try:
            res = requests.post(url, timeout=3, data={'id': id_update_item,
                                           'data': json_array_for_update,
                                           'login': self.Login,
                                           'pass': self.Password
                                           })
        except:
            return 'no_link'
        else:
            status = json.loads(res.text)
            return status['status']

    def remove_work_do(self, id_remove_item):
        url = self.srv_adress + 'remove_item.php'
        try:
            res = requests.post(url, timeout=2.5, data={'id': id_remove_item,
                                           'login': self.Login,
                                           'pass': self.Password
                                           })
        except:
            return 'no_link'

        else:
            status = json.loads(res.text)
            return status['status']

    def get_do_work_list(self, date_start=0, date_end=0, object=0, reload=False, off_line = False):
        if date_start == 0:
            date_start = self.date_start
            date_end = self.date_end
        if self.do_work_list == 0 or date_end != self.date_end or reload:
            url = self.srv_adress + 'get_work_do.php'
            if off_line:
                with open('do_work_list.txt', 'r', encoding="utf-8") as f:
                    return json.loads(f.read())
            else:
                try:
                    res = requests.post(url, timeout=2.5, data={'object': object,
                                                   'date_start': date_start,
                                                   'date_end': date_end,
                                                   'login': self.Login,
                                                   'pass': self.Password,
                                                   'user_id': self.user_id
                                                   })
                except:
                    self.app_instance.info_msg.text = self.app_instance.text_for_app['msg_no_connect']
                    self.app_instance.info_msg.open()
                    with open('do_work_list.txt', 'r', encoding="utf-8") as f:
                        return json.loads(f.read())
                else:
                    self.last_id_do_work = 0
                    with open('do_work_list.txt', 'w', encoding="utf-8") as f:
                        f.write(res.text)
                    return json.loads(res.text)
        else:
            return self.do_work_list

    def get_equipment_list(self, off_line=False):
        if self.equipment_list == 0:
            url = self.srv_adress + 'get_equipment.php'
            if off_line:
                with open('equipment_list.txt', 'r', encoding="utf-8") as f:
                    return json.loads(f.read())
            else:
                try:
                    res = requests.post(url, timeout=2.5, data={
                        'login': self.Login,
                        'pass': self.Password
                    })
                except:
                    with open('equipment_list.txt', 'r', encoding="utf-8") as f:
                        return json.loads(f.read())
                else:
                    with open('equipment_list.txt', 'w', encoding="utf-8") as f:
                        f.write(res.text)
                    return json.loads(res.text)
        else:
            return self.equipment_list

    def get_complex_list(self, off_line=False):
        if self.complex_list == 0:
            url = self.srv_adress + 'get_complex.php'
            if off_line:
                with open('complex_list.txt', 'r', encoding="utf-8") as f:
                    return json.loads(f.read())
            else:
                try:
                    res = requests.post(url, timeout=2.5, data={'find_word': ''
                                                   })
                except:
                    with open('complex_list.txt', 'r', encoding="utf-8") as f:
                        return json.loads(f.read())
                else:
                    with open('complex_list.txt', 'w', encoding="utf-8") as f:
                        f.write(res.text)
                    return json.loads(res.text)
        else:
            return self.complex_list

    def get_object(self, off_line=False):
        if self.object_list == 0:
            url = self.srv_adress + 'get_object_for_user.php'
            if off_line:
                with open('object_list.txt', 'r', encoding="utf-8") as f:
                    return json.loads(f.read())
            else:
                try:
                    res = requests.post(url, timeout=2.5, data={'login': self.Login,
                                                   'pass': self.Password
                                                   })
                except:
                    with open('object_list.txt', 'r', encoding="utf-8") as f:
                        return json.loads(f.read())
                else:
                    with open('object_list.txt', 'w', encoding="utf-8") as f:
                        f.write(res.text)
                    return json.loads(res.text)
        else:
            return self.object_list

    def get_users_list(self, off_line=False):
        url = self.srv_adress + 'get_user_list.php'
        if off_line:
            with open('users_list.txt', 'r', encoding="utf-8") as f:
                users_list = json.loads(f.read())
            for user in users_list['data']:
                if user['12'] == self.Login:
                    self.user_id = user['id']
                    self.user_secondname = user['8']
                    self.app_type = user['270']
            return users_list
        else:
            try:
                res = requests.post(url, timeout=2.5, data={
                    'login': self.Login,
                    'pass': self.Password
                })
            except:
                with open('users_list.txt', 'r', encoding="utf-8") as f:
                    users_list = json.loads(f.read())
                for user in users_list['data']:
                    if user['12'] == self.Login:
                        self.user_id = user['id']
                        self.user_secondname = user['8']
                        self.app_type = user['270']
                return users_list
            else:
                with open('users_list.txt', 'w', encoding="utf-8") as f:
                    f.write(res.text)
                users_list = json.loads(res.text)
                for user in users_list['data']:
                    if user['12'] == self.Login:
                        self.user_id = user['id']
                        self.user_secondname = user['8']
                        self.app_type = user['270']
                return users_list

    def get_users_on_object(self, id_object):
        for on_object in self.object_list['data']:
            if on_object['id'] == id_object:
                users_on_object = on_object['161'].split(',')
                break
        user_list_with_id = {'data': []}
        for user_on_object in users_on_object:
            for user in self.users_list['data']:
                if user_on_object.lstrip()[2:] == user['8']:
                    user_list_with_id['data'].append({'id': user['id'], '8': user['8']})
        return user_list_with_id

#kivy widgets modifiy-------------------------------------------------------------------------------------------------
class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    toolbar = ObjectProperty()
    new = ObjectProperty()


class AddNewWork(MDBoxLayout):
    text = ObjectProperty()


#class CustomDropDown(DropDown):
#    pass


class ItemForDropDown(Button):
    name_item = StringProperty()
    id_item = StringProperty()

class Calendar (MDBoxLayout):
    pass


class SwipeToDeleteItem(MDCard):
    work_do = ObjectProperty()
    object_name = StringProperty()
    unit_name = StringProperty()
    salary = StringProperty()
    def __init__(self, **kwargs):
        super(SwipeToDeleteItem, self).__init__(**kwargs)
        self.start = 0
        self.press_state = False
        self.register_event_type('on_double_press')
        self.register_event_type('on_long_press')

    def on_touch_down(self, touch):
        if touch.is_touch:
            if not touch.is_mouse_scrolling:

                if self.collide_point(touch.x, touch.y):
                    self.start = timeit.default_timer()

                    if touch.is_double_tap:
                        self.press_state = True
                        self.dispatch('on_double_press')
                    else:
                        return super(SwipeToDeleteItem, self).on_touch_down(touch)
                else:
                    return super(SwipeToDeleteItem, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.is_touch:
            if not touch.is_mouse_scrolling:

                if self.press_state is False:
                    if self.collide_point(touch.x, touch.y):
                        stop = timeit.default_timer()
                        awaited = stop - self.start
                        if awaited > LONG_PRESSED_TIME and awaited < 5:
                            self.dispatch('on_long_press')
                            self.start = 0
                        else:
                            return super(SwipeToDeleteItem, self).on_touch_up(touch)
                    else:
                        return super(SwipeToDeleteItem, self).on_touch_up(touch)
                else:
                    #return super(SwipeToDeleteItem, self).on_touch_up(touch)
                    self.press_state = False

    def on_double_press(self):
        pass

    def on_long_press(self):
        pass


class Object_Conteiner(MDBoxLayout):
    object_name = StringProperty()


class Content_do_work(MDLabel):
    work_do = ObjectProperty()
    object_name = StringProperty()
    unit_name = StringProperty()
    salary = StringProperty()

class WorkTypeCard(MDLabel):
    work_list = DictProperty()
    work_name = StringProperty()


class Worker_item(MDBoxLayout):
    name_worker = StringProperty()
    id_worker = StringProperty()


class Button_ok(MDFlatButton):
    instance = ObjectProperty()
class Button_cancel(MDFlatButton):
    instance = ObjectProperty()

class Button_calendar_ok(MDFlatButton):
    pass
class Button_calendar_cancel(MDFlatButton):
    pass


#kivy widgets modifiy-------------------------------------------------------------------------------------------------
class DropDown (RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.win = None
        self.attach_to = None
        self._touch_started_inside = None
    def _reposition(self, *largs):
        widget = self.attach_to
        win = widget.get_parent_window()
        self.children[0].default_size = widget.size
        wx, wy = widget.to_window(*widget.pos)
        wright, wtop = widget.to_window(widget.right, widget.top)
        h_bottom = win.height - (win.height - wtop)
        h_top = win.height - wy
        if h_bottom > (win.height/3):
            print(1)
            self.height = win.height - (win.height - wy)
            self.top = wy
            self.x = wx
        elif h_top < h_bottom:
            print(2)
            self.height = win.height - (win.height - wy)
            self.top = wy
            self.x = wx
        else:
            if self.children[0].height == 0:
                self.height = 0
            def top(*largs):
                print(3)
                self.y = wtop
                self.x = wx
                if (win.height - wtop)>self.children[0].height and self.children[0].height != 0:
                    print(31)
                    self.height = self.children[0].height
                else:
                    print(32)
                    self.height = win.height - wtop
            Clock.schedule_once(top, 0.2)


    def open(self, widget):
        self.attach_to = widget

        Window.bind(on_motion=self._reposition)
        win = widget.get_parent_window()
        win.add_widget(self)
        self._reposition()
        Clock.schedule_once(self._reposition, 0.2)

    def _real_dismiss(self,*largs):
        if self.parent:
            self.parent.remove_widget(self)
        Window.unbind(on_motion=self._reposition)
    def dismiss(self):
        Clock.schedule_once(self._real_dismiss, 0.2)
    def on_touch_down(self, touch):
        self._touch_started_inside = self.collide_point(*touch.pos)
        if self._touch_started_inside:
            super(DropDown, self).on_touch_down(touch)
        return True

    def on_touch_move(self, touch):
        if self._touch_started_inside:
            super(DropDown, self).on_touch_move(touch)
        return True

    def on_touch_up(self, touch):
        # Explicitly test for False as None occurs when shown by on_touch_down
        if self._touch_started_inside is False:
            self.dismiss()
        else:
            super(DropDown, self).on_touch_up(touch)
        self._touch_started_inside = None
        return True

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prev_screen = 'scr1'
        self.last_item = 0
        self.theme_cls.theme_style = "Light"
        self.dialog = None
        self.Flag_AddNew = 0
        self.Height = 0
        self.Flag_Update_List = False
        self.Flag_Reload_List = False
        self.Flag_group_by_object = True
        self.rkv = rkv_api(self)
        self.dropdown = None
        self.activ_text_field = 0
        self.loop = 0   # for store schedule_interval of object Clock for dropdown list
        self.loop_work_do = 0 # for store schedule_interval of object Clock for work_do list
        self.item_for_builder = []  #array for builder dropdown list
        self.Flag_color = False
        self.item_for_groupe_bilder = {} #array for builder work_do list
        self.last_object_group_bilder=0
        self.count = 0 #caunt what times build item for bulding list
        self.scroll =0 #Link for scroll view (work_do list)
        self. date_of_view = ''
        self.info_msg = Snackbar(
                    text="",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_x=(Window.width - (10 * 2)) / Window.width)

        self.lang = 'UA'
        try:
            f = open('config.txt', 'r')
        except:
            pass
        else:
            conf_str = f.read()
            if conf_str != '':
                conf = conf_str.split(',')
                self.lang = conf[5]
            f.close()
        self.text_for_app = text_for_app[self.lang]
# method for chaing position scroll view on first item, when window was restore
    def win(self,*args):
        var = len(self.root.ids.md_list.children)
        self.root.ids.scroll_do_work.do_scroll_y = True
        try:
            self.root.ids.scroll_do_work.scroll_to(self.root.ids.md_list.children[var-1], padding=10, animate=False)
        except:
            pass

    def Android_back_click(self, window, key, *largs):
        if key == 27:
            if self.prev_screen=="scr 1":
                if self.root.ids.screen_manager.current!='scr 1':
                    self.button_back()
            else:
                self.button_back_from_WL()


    def on_start(self):
        Window.bind(on_restore=self.win)
        Window.bind(on_keyboard=self.Android_back_click)
        print(self.root.ids.toolbar.right_action_items)
        self.rkv.init()
        if self.rkv.Flag_config:
            self.root.ids.adress.text = self.rkv.srv_adress[7:20]
            self.root.ids.port.text = self.rkv.port
            self.root.ids.login.text = self.rkv.Login
            self.root.ids.password.text = '11111111'
            self.root.ids.singup_btn.text = self.text_for_app['btn_login_exit']

            if self.rkv.Flag_connection:
                self.load_items(self.rkv.work_list, self.rkv.do_work_list)
                if not self.rkv.Flag_authent:
                    button = Button(opacity=0.5, background_normal='', color=(0, 0, 0, 1), text=self.text_for_app['info_wrong_login'],
                                    size_hint=(None, None),
                                    size=(Window.width, Window.height - self.root.ids.toolbar.height),
                                    pos_hint={"center_x": .5, "center_y": .5})
                    self.root.ids.md_list.add_widget(button)
                    def scr(self):
                        self.root.ids.screen_manager.current = 'scr 3'
                        self.root.ids.toolbar.title = self.text_for_app['title_login']
                    button.bind(on_press=lambda x: scr(self))
                    self.root.ids.screen_manager.current = "scr 3"
                    self.root.ids.singup_btn.text = self.text_for_app['btn_login_enter']
                    self.root.ids.password.text = self.rkv.Password
            else:
                self.load_items(self.rkv.work_list, self.rkv.do_work_list)
        else:
            self.root.ids.toolbar.title = self.text_for_app['title_login']
            button = Button(opacity=0.5,background_normal='',color=(0,0,0,1),text=self.text_for_app['info_login_systems'],size_hint=(None, None) ,size=(Window.width,Window.height-self.root.ids.toolbar.height), pos_hint={"center_x": .5, "center_y": .5})
            self.root.ids.md_list.add_widget(button)
            def scr(self):
                self.root.ids.screen_manager.current='scr 3'
                self.root.ids.toolbar.title = self.text_for_app['title_login']
            button.bind(on_press=lambda x: scr(self))
            self.root.ids.screen_manager.current = "scr 3"
        if self.rkv.app_type == '':
            self.root.ids.nav_drawer.children[0].ids.menu_list.remove_widget(
                self.root.ids.nav_drawer.children[0].ids.count_maney)
        self.dropdown = DropDown()
        #self.dropdown.open(self.root.ids.lang_btn)
        #self.dropdown.dismiss()

    def button_login(self, instance, instence_adress,instance_port, instance_login, instance_password):
        if instance.text == self.text_for_app['btn_login_enter']:
            self.rkv.login(instance_login.text, instance_password.text, instence_adress.text, instance_port.text)
            if self.rkv.Flag_authent and self.rkv.Flag_config and self.rkv.Flag_connection:
                instance.text = self.text_for_app['btn_login_exit']
                instance.md_bg_color = self.theme_cls.primary_light
                self.load_items(self.rkv.work_list, self.rkv.do_work_list)
                self.root.ids.toolbar.title = self.rkv.count_many() + "грн."
                self.info_msg.text = self.text_for_app['msg_you_login']
                self.info_msg.open()
                self.root.ids.nav_drawer.children[0].ids.logo.source = 'logo.png'
                self.root.ids.nav_drawer.children[0].ids.logo.reload()
                self.root.ids.nav_drawer.set_state("close")
                self.root.ids.screen_manager.current = "scr 1"
                self.root.ids.toolbar.right_action_items = [
                    ["home-city-outline", lambda x: self.group_by_object(self.root.ids.toolbar)],
                    ["calendar", lambda x: self.show_calendar()], ["plus", lambda x: self.add_work()]]
                self.root.ids.toolbar.title = f"{self.rkv.count_many()} {self.text_for_app['currency']}." if self.rkv.app_type != '' else self.text_for_app['title_done_work']
            else:
                if not self.rkv.Flag_connection:
                    self.info_msg.text = self.text_for_app['msg_no_connect']
                    self.info_msg.open()
                else:
                    if not self.rkv.Flag_authent:
                        self.info_msg.text = self.text_for_app['msg_wrong_login']
                        self.info_msg.open()

                instance_password.text = ''
        else:
            self.rkv.login(Log_in=False)
            #instance_login.text = ''
            instance_password.text = ''
            instance.text = self.text_for_app['btn_login_enter']

    def count_many_for_menu(self, instance):
        now = datetime.now()
        date_now = now.strftime("%Y-%m-%d")
        now_date_start = now.strftime("%Y-%m-") + '01'
        now_date_end = f'{now.strftime("%Y-%m-")}{calendar.monthrange(now.year, now.month)[1]}'
        last_mounth = int(date_now[5:7])-1
        befor_m_date_start = f'{now.strftime("%Y-")}{last_mounth:0{2}}-01'
        if (now.month-1)!=0:
            befor_m_date_end = f'{now.strftime("%Y-")}{last_mounth:0{2}}-{calendar.monthrange(now.year, now.month-1)[1]}'
        else:
            befor_m_date_end = f'{int(now.strftime("%Y"))-1}-{12-(now.month-1)}-{calendar.monthrange(now.year-1, 12-(now.month-1))[1]}'
            print(befor_m_date_end)
        if self.rkv.Flag_config:
            if self.rkv.Flag_connection:
                self.root.ids.comon_many_befor.text = f"{self.text_for_app['title_count_for']} {befor_m_date_end[5:7]}.{befor_m_date_end[0:4]} - {self.rkv.count_many(self.rkv.get_do_work_list(date_start=befor_m_date_start, date_end=befor_m_date_end))} {self.text_for_app['currency']}."
                self.root.ids.comon_many_now.text = f"{self.text_for_app['title_count_for']} {now_date_end[5:7]}.{now_date_end[0:4]} - {self.rkv.count_many(self.rkv.get_do_work_list(date_start=now_date_start, date_end=now_date_end, reload=True))} {self.text_for_app['currency']}."
            else:
                self.root.ids.comon_many_befor.text = self.text_for_app['title_no_link_server']
                self.root.ids.comon_many_now.text = self.text_for_app['title_no_link_server']


    def bilder_for_grope_list(self, *args):
        if not self.item_for_groupe_bilder and self.loop_work_do or self.count>=5:
            self.loop_work_do.cancel()
            if self.last_item:
                self.root.ids.scroll_do_work.scroll_to(self.last_item, padding=10,
                                                   animate=False)
        while self.item_for_groupe_bilder and time() < (Clock.get_time() + MAX_TIME_GROUP):
            if self.count<5:
                keys = list(self.item_for_groupe_bilder.keys())
                key_object = keys[0]
                object_name = list(filter(lambda x: x['id'] == key_object,
                                          self.rkv.object_list['data'])).pop()
                if self.item_for_groupe_bilder[key_object]:
                    if self.last_object_group_bilder != key_object:
                        self.last_object_group_bilder = key_object

                        self.root.ids.md_list.add_widget(
                            Object_Conteiner(object_name=object_name['158'])
                        )
                        if self.Flag_color:
                            self.root.ids.md_list.children[0].md_bg_color = (0.95, 0.95, 0.95, 1)
                            self.Flag_color = False
                        else:
                            self.root.ids.md_list.children[0].md_bg_color = (0.80, 0.80, 0.80, 1)
                            self.Flag_color = True

                    else:
                        self.count += 1
                        work_do_item = self.item_for_groupe_bilder[key_object].pop(0)
                        if work_do_item['254'] == 'да' and self.rkv.app_type != '':
                            salary = f" по {work_do_item[self.rkv.conf_serv][0:-1]} = {float(work_do_item[self.rkv.conf_serv])*float(work_do_item['224'])}"
                        else:
                            salary = ''
                        unit_name = list(filter(lambda x: x['id'] == work_do_item['226'],
                                                     self.rkv.work_list['data'])).pop()
                        self.root.ids.md_list.children[0].add_widget(
                            SwipeToDeleteItem(work_do=work_do_item, object_name=object_name['158'], unit_name = unit_name['243'], salary=salary)
                        )

                        if work_do_item['254'] == 'нет':
                            #self.root.ids.md_list.children[0].children[0].md_bg_color = (1, 1, 1, 1)
                            self.root.ids.md_list.children[0].children[0].bind(on_long_press=self.open_remove_dialog)
                            self.root.ids.md_list.children[0].children[0].bind(on_double_press=self.update_item)
                            self.root.ids.md_list.children[0].children[0].remove_widget(self.root.ids.md_list.children[0].children[0].ids.yes)

                else:
                    self.item_for_groupe_bilder.pop(key_object)



    def group_by_object(self, instance, Flag_reload=False):
        instance.ids.right_actions.children[2].theme_text_color="Custom"
        instance.ids.right_actions.children[2].text_color=(0,0,0,0.5)
        if self.Flag_AddNew == 1:
            self.root.ids.new.clear_widgets()
            self.Flag_AddNew = 0
        if self.Flag_group_by_object and self.rkv.Flag_config or Flag_reload:
            self.root.ids.md_list.spacing = 0
            instance.ids.right_actions.children[2].theme_text_color = "Custom"
            instance.ids.right_actions.children[2].text_color = (0, 0, 0, 0.5)
            self.Flag_group_by_object = False
            Flag_color = True
            self.item_for_groupe_bilder = {}
            self.last_object_group_bilder = 0
            for work_item in self.rkv.do_work_list['data']:
                if self.item_for_groupe_bilder.get(work_item['parent_item_id']):
                    self.item_for_groupe_bilder[work_item['parent_item_id']].append(work_item)
                else:
                    self.item_for_groupe_bilder[work_item['parent_item_id']] = []
                    self.item_for_groupe_bilder[work_item['parent_item_id']].append(work_item)
            self.root.ids.md_list.clear_widgets()
            self.count = 0
            self.loop_work_do = Clock.schedule_interval(self.bilder_for_grope_list, 0)
        elif self.Flag_group_by_object == False and self.rkv.Flag_config:
            self.root.ids.md_list.spacing = 10
            instance.ids.right_actions.children[2].theme_text_color = "Custom"
            instance.ids.right_actions.children[2].text_color = (1, 1, 1, 1)
            self.item_for_groupe_bilder = {}
            self.last_object_group_bilder = 0
            if self.loop_work_do:
                self.loop_work_do.cancel()
            self.Flag_group_by_object = True
            self.rkv.last_id_do_work = 0
            self.load_items(0, self.rkv.do_work_list)

    def remove_item(self, instance):
        result = self.rkv.remove_work_do(instance.work_do['id'])
        if result != 'no_link':
            if result != 'error':
                if not self.Flag_group_by_object and len(instance.parent.children)<=2:
                    instance.parent.parent.remove_widget(instance.parent)
                else:
                    instance.parent.remove_widget(instance)
                i = 0
                for work_do in self.rkv.do_work_list['data']:
                    if work_do['id'] == instance.work_do['id']:
                        self.rkv.do_work_list['data'].pop(i)
                    i += 1
                self.dialog.dismiss()
        else:
            self.dialog.text = self.text_for_app['msg_no_connect']

    def open_remove_dialog(self, instance):
        self.dialog = MDDialog(
            text=self.text_for_app['msg_delete_work'],
            buttons=[
                Button_ok(instance=instance),
                Button_cancel(instance=instance),
                ],
            )
        self.dialog.open()


    def update_item(self, instance):
        instance_root = instance
        id_work_do = instance_root.work_do['id']
        amount = instance_root.work_do['224']
        object = list(filter(lambda x: x['id'] == instance_root.work_do['parent_item_id'], self.rkv.object_list['data'])).pop()
        if instance_root.work_do['252']:
            equipment = list(
                filter(lambda x: x['251'] == instance_root.work_do['252'], self.rkv.equipment_list['data'])).pop()
        else:
            equipment = ''
        work_type = list(
            filter(lambda x: x['219'] == instance_root.work_do['223'], self.rkv.work_list['data'])).pop()
        complex = list(
            filter(lambda x: x['name'] == instance_root.work_do['237'], self.rkv.complex_list['data'])).pop()
        if self.dropdown:
            self.dropdown.dismiss()
        worker = instance_root.work_do['239']
        worker_list = list(
            filter(lambda x: instance_root.work_do['239'].find(x['8']) != -1, self.rkv.users_list['data']))
        notes = instance_root.work_do['253']
        if self.dropdown:
            self.dropdown.dismiss()
        if self.Flag_AddNew == 0 and self.rkv.Flag_config:
            if self.rkv.Flag_connection:
                if self.rkv.Flag_authent:
                    instance_root.clear_widgets()
                    instance_root.add_widget(AddNewWork(text='hello'))
                    self.Flag_AddNew = 1
                    #self.dropdown = CustomDropDown()
            else:
                instance_root.clear_widgets()
                instance_root.add_widget(AddNewWork(text='hello'))
                self.Flag_AddNew = 1
                #self.dropdown = CustomDropDown()
        instance_root.unbind(on_long_press=self.open_remove_dialog)
        instance_root.unbind(on_double_press=self.update_item)
        instance_new = instance_root.children[0]
        print(instance_new)
        instance_new.ids.object.text = object['158']
        instance_new.ids.object.name = object['id']
        instance_new.ids.object.parent.name = 'not_edit'

        if equipment:
            instance_new.ids.equipment.text = equipment['251']
            instance_new.ids.equipment.name = equipment['id']
            instance_new.ids.equipment.parent.name = 'not_edit'

        instance_new.ids.amount.text = amount
        instance_new.ids.amount.parent.name = 'not_edit'

        instance_new.ids.work_type.text = work_type['219']
        instance_new.ids.work_type.name = work_type['id']
        instance_new.ids.work_type.parent.name = 'not_edit'

        instance_new.ids.complex.text = complex['name']
        instance_new.ids.complex.name = complex['id']
        instance_new.ids.complex.parent.name = 'not_edit'

        instance_new.ids.notes.text = notes
        instance_new.ids.notes.parent.name = 'not_edit'

        for user in worker_list:
            instance_new.ids.worker.add_widget(
                Worker_item(name_worker=user['8'], id_worker=user['id'])
            )
        if self.dropdown:
            self.dropdown.dismiss()


    def bilder_for_list(self, *args):
        if not self.item_for_groupe_bilder and self.loop_work_do or self.count>=5:
            self.loop_work_do.cancel()

        while self.item_for_groupe_bilder and time() < (Clock.get_time() + MAX_TIME_GROUP):
            if self.count<5:
                self.count += 1
                start = Time.time()
                work_do_item = self.item_for_groupe_bilder.pop(0)
                object_name = list(filter(lambda x: x['id'] == work_do_item['parent_item_id'],
                                          self.rkv.object_list['data'])).pop()
                unit_name = list(filter(lambda x: x['id'] == work_do_item['226'],
                                          self.rkv.work_list['data'])).pop()
                if work_do_item['254'] == 'да' and self.rkv.app_type != '':
                    salary = f" по {work_do_item[self.rkv.conf_serv][0:-1]} = {float(work_do_item[self.rkv.conf_serv]) * float(work_do_item['224'])}"
                else:
                    salary = ''
                end = Time.time()
                t = end - start
                print (f"time: {t}")
                start = Time.time()
                self.root.ids.md_list.add_widget(
                    SwipeToDeleteItem(work_do=work_do_item, object_name=object_name['158'], unit_name=unit_name['243'], salary=salary)
                )
                self.root.ids.md_list.children[0].md_bg_color = (1, 1, 1, 1)
                if work_do_item['254']=='нет':
                    #self.root.ids.md_list.children[0].md_bg_color = (0.9, 0.9, 0.9, 1)
                    self.root.ids.md_list.children[0].bind(on_long_press=self.open_remove_dialog)
                    self.root.ids.md_list.children[0].bind(on_double_press=self.update_item)
                    self.root.ids.md_list.children[0].remove_widget(self.root.ids.md_list.children[0].children[1])
                end = Time.time()
                t = end - start
                print (f"time: {t}")
            #if self.last_item:
                #self.root.ids.scroll_do_work.scroll_to(self.last_item, padding=10,
                                                       #animate=False)
        #if self.last_item:
            #self.root.ids.scroll_do_work.scroll_to(self.last_item, padding=10,
                                                   #animate=False)

    def load_items(self, work_list=0, work_do_list=0):
        if work_do_list != 0:
            if self.loop_work_do:
                self.loop_work_do.cancel()
            self.item_for_groupe_bilder = {}
            self.root.ids.md_list.clear_widgets()
            self.count = 0
            self.item_for_groupe_bilder = work_do_list['data'].copy()
            self.loop_work_do = Clock.schedule_interval(self.bilder_for_list, 0)
            self.last_item = 0

        if work_list != 0:
            work_for_RV = []
            for work_item in work_list['data']:
                work_for_RV.append({'work_list': work_item,
                                    'work_name': work_item['219'],
                                    "height": 140})
            #print(work_for_RV)

            self.root.ids.scroll_m.data = work_for_RV

    def add_work(self):
        if self.Flag_AddNew == 0 and self.rkv.Flag_config:
            if self.rkv.Flag_connection:
                if self.rkv.Flag_authent:
                    self.root.ids.new.padding = 15
                    self.root.ids.new.add_widget(AddNewWork(text='hello'))
                    self.Flag_AddNew = 1
                    button = self.root.ids.new.children[0].children[-2].children[-1].add_widget(
                        Worker_item(name_worker=self.rkv.user_secondname, id_worker=self.rkv.user_id)
                    )
                    self.root.ids.scroll_do_work.scroll_to(self.root.ids.new, padding=10,
                                                           animate=True)
                    #self.dropdown = CustomDropDown()
            else:
                self.root.ids.new.padding = 15
                self.root.ids.new.add_widget(AddNewWork(text='hello'))
                self.Flag_AddNew = 1
                button = self.root.ids.new.children[0].ids.worker.add_widget(
                    Worker_item(name_worker=self.rkv.user_secondname, id_worker=self.rkv.user_id)
                )
                #self.dropdown = CustomDropDown()


    def button_save_new(self, instance):
        Flag_error = False
        if instance.ids.object.name == 'error':
            instance.ids.object.line_color_normal = (1, 0, 0, 1)
            instance.ids.object.text_color_normal = (1, 0, 0, 1)
            instance.ids.object.hint_text_color_normal = (1, 0, 0, 1)#self.theme_cls.primary_palette = "Red"
            #print(instance.ids.object.normal_color)
            Flag_error = True
        if instance.ids.work_type.name == 'error':
            instance.ids.work_type.line_color_normal = (1, 0, 0, 1)
            instance.ids.work_type.text_color_normal = (1, 0, 0, 1)
            instance.ids.work_type.hint_text_color_normal = (1, 0, 0, 1)
            Flag_error = True
        if instance.ids.complex.name == 'error':
            instance.ids.complex.line_color_normal = (1, 0, 0, 1)
            instance.ids.complex.text_color_normal = (1, 0, 0, 1)
            instance.ids.complex.hint_text_color_normal = (1, 0, 0, 1)
            Flag_error = True
        if instance.ids.equipment.name == 'error' and instance.ids.equipment.text != '':
            instance.ids.equipment.line_color_normal = (1, 0, 0, 1)
            instance.ids.equipment.text_color_normal = (1, 0, 0, 1)
            instance.ids.equipment.hint_text_color_normal = (1, 0, 0, 1)
            Flag_error = True
        if instance.ids.amount.text == '' or instance.ids.amount.name == 'error':
            instance.ids.amount.line_color_normal = (1, 0, 0, 1)
            instance.ids.amount.text_color_normal = (1, 0, 0, 1)
            instance.ids.amount.hint_text_color_normal = (1, 0, 0, 1)
            Flag_error = True
        if Flag_error:
            self.info_msg.text = self.text_for_app['msg_check_fields']
            self.info_msg.open()
        if not Flag_error:
            if type(instance.parent).__name__ == 'MDBoxLayout': #if is a new work
                object_name = instance.ids.object.text
                worker_id_list = ''
                worker_name_list = ''
                for worker_item in instance.ids.worker.walk(restrict=True):
                    if type(worker_item).__name__ == 'Worker_item':
                        worker_id_list += f",{worker_item.name}"
                    if type(worker_item).__name__ == 'Button':
                        worker_name_list += f",{worker_item.text}"
                worker_id_list = worker_id_list[1:]
                worker_name_list = worker_name_list[1:]
                array_id_for_new = {'223': instance.ids.work_type.name,
                                    '239': worker_id_list,
                                    '224': instance.ids.amount.text,
                                    '237': instance.ids.complex.name,
                                    '267': '',
                                    '253': instance.ids.notes.text,
                                    '252': instance.ids.equipment.name,
                                    'parent_item_id': instance.ids.object.name}
                array_text_for_new = {'223': instance.ids.work_type.text,
                                      '239': worker_name_list,
                                      '224': instance.ids.amount.text,
                                      '237': instance.ids.complex.text,
                                      '267': self.rkv.date_now,
                                      '253': instance.ids.notes.text,
                                      'parent_item_id': instance.ids.object.name,
                                      'id': '',
                                      '266': '-',
                                      '252': instance.ids.equipment.text}
                result = self.rkv.add_new_do_work(array_id_for_new, array_text_for_new)
                if result['status']=='success':
                    array_text_for_new['id'] = result['data']['id']
                    self.rkv.do_work_list = self.rkv.get_do_work_list(reload=True)
                    child_index_new_work_do = len(self.root.ids.md_list.children)
                    if self.Flag_group_by_object:
                        unit_name = list(filter(lambda x: x['id'] == instance.ids.work_type.name,
                                                self.rkv.work_list['data'])).pop()
                        self.root.ids.md_list.add_widget(
                            SwipeToDeleteItem(work_do=array_text_for_new, object_name=instance.ids.object.text,unit_name=unit_name['243']),child_index_new_work_do)
                        self.root.ids.new.clear_widgets()
                        self.root.ids.new.padding = 0
                        self.root.ids.md_list.children[child_index_new_work_do].bind(on_long_press=self.open_remove_dialog)
                        self.root.ids.md_list.children[child_index_new_work_do].bind(on_double_press=self.update_item)
                        self.root.ids.md_list.children[child_index_new_work_do].remove_widget(self.root.ids.md_list.children[child_index_new_work_do].ids.yes)
                    else:
                        self.rkv.last_id_do_work = 0
                        self.group_by_object(self.root.ids.toolbar, True)
                    self.root.ids.new.clear_widgets()
                else:
                    self.dialog = MDDialog(
                        text=self.text_for_app['msg_no_connect'],
                        buttons=[
                            Button_cancel(instance=instance),
                        ],
                    )
                    self.dialog.open()


            else: #if is update work
                array_for_update = {}
                array_for_card = list(
                    filter(lambda x: x['id'] == instance.parent.work_do['id'], self.rkv.do_work_list['data'])).pop()
                orign_array_for_card = array_for_card.copy()
                object_name = instance.ids.object.text
                if instance.ids.object.parent.name == 'edit':
                    array_for_update['parent_item_id'] = instance.ids.object.name
                if instance.ids.work_type.parent.name == 'edit':
                    array_for_update['field_223'] = instance.ids.work_type.name
                    array_for_card['223'] = instance.ids.work_type.text
                if instance.ids.complex.parent.name == 'edit':
                    array_for_update['field_237'] = instance.ids.complex.name
                    array_for_card['237'] = instance.ids.complex.text
                if instance.ids.equipment.parent.name == 'edit' and instance.ids.equipment.text != '':
                    array_for_update['field_252'] = instance.ids.equipment.name
                    array_for_card['252'] = instance.ids.equipment.text
                if instance.ids.amount.parent.name == 'edit':
                    array_for_update['field_224'] = instance.ids.amount.text
                    array_for_card['224'] = instance.ids.amount.text
                if instance.ids.notes.parent.name == 'edit':
                    array_for_update['field_253'] = instance.ids.notes.text
                    array_for_card['253'] = instance.ids.notes.text
                if instance.ids.worker.parent.name == 'edit':
                    worker_id_list = ''
                    worker_name_list = ''
                    for worker_item in instance.ids.worker.walk(restrict=True):
                        if type(worker_item).__name__ == 'Worker_item':
                            worker_id_list += f",{worker_item.name}"
                        if type(worker_item).__name__ == 'Button':
                            worker_name_list += f",{worker_item.text}"
                    worker_name_list = worker_name_list
                    array_for_update['field_239'] = worker_id_list[1:]
                    array_for_card['239'] = worker_name_list[1:]
                if array_for_update:
                    result = self.rkv.update_work_do(array_for_update, instance.parent.work_do['id'])
                    if result == 'success':
                        FrontBox = instance.parent
                        unit_name = FrontBox.unit_name
                        FrontBox.clear_widgets()
                        FrontBox.add_widget(
                            Content_do_work(work_do=array_for_card, object_name=object_name, unit_name=unit_name)
                        )
                        FrontBox.bind(on_long_press=self.open_remove_dialog)
                        FrontBox.bind(on_double_press=self.update_item)
                    else:
                        instance.parent.work_do = orign_array_for_card
                        for key in array_for_card:
                            array_for_card[key] = orign_array_for_card[key]
                        self.dialog = MDDialog(
                            text=self.text_for_app['msg_no_connect'],
                            buttons=[
                                Button_cancel(instance=instance),
                            ],
                        )
                        self.dialog.open()
                else:
                    instance.parent.work_do = orign_array_for_card
                    for key in array_for_card:
                        array_for_card[key] = orign_array_for_card[key]
                    FrontBox = instance.parent
                    unit_name = FrontBox.unit_name
                    FrontBox.clear_widgets()
                    FrontBox.add_widget(
                        Content_do_work(work_do=array_for_card, object_name=object_name, unit_name=unit_name)
                    )
                    FrontBox.bind(on_long_press=self.open_remove_dialog)
                    FrontBox.bind(on_double_press=self.update_item)
            self.Flag_AddNew = 0


    def button_close_new(self, instance):
        if type(instance.parent).__name__ == 'SwipeToDeleteItem':
            FrontBox = instance.parent
            unit_name = FrontBox.unit_name
            FrontBox.clear_widgets()
            work_do_item = FrontBox.work_do
            if work_do_item.get('254') == 'да':
                salary = f" по {work_do_item[self.rkv.conf_serv][0:-1]} = {float(work_do_item[self.rkv.conf_serv]) * float(work_do_item['224'])}"
            else:
                salary = ''
            FrontBox.add_widget(
                Content_do_work(work_do=work_do_item, object_name=FrontBox.object_name, unit_name=unit_name,
                                  salary=salary)
            )

            if work_do_item.get('254') == 'нет':
                FrontBox.md_bg_color = (1, 1, 1, 1)
                FrontBox.bind(on_long_press=self.open_remove_dialog)
                FrontBox.bind(on_double_press=self.update_item)

        else:
            self.root.ids.new.clear_widgets()
            self.root.ids.new.padding = 0
        self.Flag_AddNew = 0


    def on_text(self, instance, value, item_list, field, drop_down=True, root=0):

        if drop_down and self.dropdown:
            instance.name = 'error'
            instance.parent.name = 'edit'
            self.item_for_builder = []
            if self.dropdown:
                self.dropdown.dismiss()
            reg_str = '[^a-zA-Z0-9a-яА-Я ]'
            text = re.sub(reg_str,' ',instance.text)
            list_str = text.lower().split(' ')
            find_str= ''
            if len(list_str)>1:
                for str in list_str:
                    if str != '':
                        find_str += f'.*{str}'
                find_str += '.*'
            else:
                find_str = text.lower()

            for item in item_list['data']:
                lower = item[field].lower()
                result = re.findall(find_str, lower)
                if result:
                    self.item_for_builder.append({"name_item": item[field], 'id_item': item['id']})

            self.dropdown = DropDown()
            self.dropdown.data = self.item_for_builder
            self.dropdown.open(instance)
        else:
            instance.parent.name = 'edit'
            if root != 0:
                if instance == root.ids.amount:
                    if value != '' and value.isdigit():
                        instance.name = 'not_error'
                    else:
                        instance.name = 'error'


    def on_focus(self, instance, event_focus, item_list, field):
        self.activ_text_field = instance

        if event_focus:
            self.dropdown = DropDown()
            if instance.text:
                self.item_for_builder = []
                reg_str = r'[^a-zA-Z0-9a-яА-Я ]'
                text = re.sub(reg_str,' ', instance.text)
                list_str = text.lower().split(' ')
                find_str = ''
                if len(list_str) > 1:
                    for str in list_str:
                        if str != '':
                            find_str += f'.*{str}'
                    find_str += '.*'
                else:
                    find_str = f'.*{text.lower()}.*'

                for item in item_list['data']:
                    lower = item[field].lower()
                    result = re.findall(find_str, lower)
                    if result:
                        self.item_for_builder.append({"name_item": item[field], 'id_item': item['id']})
                self.dropdown.data = self.item_for_builder
                self.dropdown.open(instance)
            else:
                self.item_for_builder = []
                for item in item_list['data']:
                        self.item_for_builder.append({"name_item": item[field], 'id_item': item['id']})
                self.dropdown.data = self.item_for_builder

                self.dropdown.open(instance)
        else:
            pass
            #self.dropdown.dismiss()



    def remove_worker(self, instance, instance_parent):
        if instance.text != self.rkv.user_secondname:
            instance_parent.parent.parent.name = 'edit'
            instance_parent.parent.remove_widget(instance_parent)


    def click_drop_item(self, text, id_item):
        try:
            test = self.activ_text_field.name
        except:
            self.activ_text_field.text = text
            self.dropdown.dismiss()
            self.lang = text
            self.text_for_app = text_for_app[self.lang]
            self.info_msg.text = self.text_for_app['msg_change_lang']
            self.info_msg.open()
            print(self.text_for_app)
            try:
                f = open('config.txt', 'r')
            except:
                return ('no_config')
            else:
                conf_str = f.read()
                if conf_str != '':
                    conf = conf_str[0:-2]+self.lang
                f.close()
            with open('config.txt', 'w', encoding="utf-8") as f:
                f.write(conf)

        else:
            if self.activ_text_field.name == 'worker':
                self.activ_text_field.parent.name = 'edit'
                self.dropdown.dismiss()
                flag = 0
                for work_item in self.activ_text_field.walk(restrict=True):
                    if type(work_item).__name__ == 'Button' and work_item.text == text:
                        flag = 1
                if flag == 0:
                    self.activ_text_field.add_widget(
                        Worker_item(name_worker=text, id_worker=str(id_item))
                    )
            else:
                self.activ_text_field.text = text
                self.activ_text_field.name = id_item
                self.activ_text_field.parent.name = 'edit'
                self.dropdown.dismiss()

    def show_drop_worker(self, instance, id_object, instance_object):
        if instance_object.text != '':
            self.activ_text_field = instance
            self.item_for_builder = []
            worker_list = self.rkv.get_users_on_object(id_object)
            for worker in worker_list['data']:
                self.item_for_builder.append({"name_item": worker['8'], 'id_item': worker['id']})
            self.dropdown.data = self.item_for_builder
            self.dropdown.open(instance)


    def click_drop_worker(self, text, id_item):
        pass

#start load after event overscroll (start_event_load)
    def start_load(self, scroll):
        if self.Flag_Update_List:
            self.Flag_Update_List = False
            if scroll.name == 'scroll_work':
                self.load_items(self.rkv.work_list)
            elif scroll.name == 'scroll_do_work':
                if self.Flag_group_by_object:
                    if not self.loop_work_do.is_triggered:
                        self.count = 0
                        self.loop_work_do = Clock.schedule_interval(self.bilder_for_list, 0)
                        #self.root.ids.scroll_do_work.do_scroll_y = True
                else:
                    if not self.loop_work_do.is_triggered:
                        self.count = 0
                        self.loop_work_do = Clock.schedule_interval(self.bilder_for_grope_list, 0)
                        #self.root.ids.scroll_do_work.do_scroll_y = True

        elif self.Flag_Reload_List:
            self.Flag_Reload_List = False
            if scroll.name == 'scroll_work':
                self.rkv.last_id_work = 0
                self.load_items(self.rkv.work_list)
                #self.root.ids.scroll_do_work.do_scroll_y = True
            elif scroll.name == 'scroll_do_work':
                print(self.root.ids.new.children)
                if self.Flag_AddNew == 1 and not self.root.ids.new.children:
                    self.Flag_AddNew = 0
                if self.Flag_group_by_object:
                    self.rkv.last_id_do_work = 0
                    self.load_items(0, self.rkv.do_work_list)
                    #self.root.ids.scroll_do_work.do_scroll_y = True
                else:
                    self.rkv.last_id_do_work = 0
                    self.group_by_object(self.root.ids.toolbar,True)
        self.root.ids.spiner.active = False


    # event overscroll for scrollview
    def start_event_load(self, scroll):
        #if scroll.scroll_y< -2.0 or scroll.scroll_y>3.0:
            #self.root.ids.scroll_do_work.do_scroll_y = False

        #if (scroll.children[0].size[1] * scroll.scroll_y) < (scroll.children[0].size[1]/8):
        #    self.Flag_Update_List = True

        if (scroll.children[0].size[1] * scroll.scroll_y) < -200:
            self.Flag_Update_List = True
        elif scroll.scroll_y > 0.9:
            if (scroll.children[0].size[1] / scroll.scroll_y) < scroll.children[0].size[1] - 700:
                self.root.ids.spiner.pos = (self.root.ids.scr1.size[0] / 2, self.root.ids.scr1.size[1] - (
                            (scroll.children[0].size[1] * scroll.scroll_y) - scroll.children[0].size[1]) / 4)
                self.root.ids.spiner.active = True
                self.Flag_Reload_List = True

    def show_calendar(self):
        if self.rkv.Flag_config:
            if self.rkv.Flag_connection:
                if self.rkv.Flag_authent:
                    self.dialog = MDDialog(
                        #title="Выберете период",
                        type="custom",
                        #size_hint=(None, None),
                        #width=1000,
                        #width_offset=5,
                        size_hint_x=0.9,
                        content_cls=Calendar(),
                        buttons=[
                            Button_calendar_ok(),
                            Button_calendar_cancel(),
                        ],
                    )
                    self.dialog.update_width()
                    if self.date_of_view == '':
                        now = datetime.now()
                        year = now.strftime("%Y")
                        month = now.strftime("%m")
                        self.dialog.content_cls.ids.year.text = year
                        self.dialog.content_cls.ids.month.text = self.text_for_app['calendar_month'][month]
                        self.dialog.content_cls.ids.BoxMonth.name = month
                    else:
                        self.dialog.content_cls.ids.year.text = self.date_of_view[0:4]
                        self.dialog.content_cls.ids.month.text = self.text_for_app['calendar_month'][self.date_of_view[5:7]]
                        self.dialog.content_cls.ids.BoxMonth.name = self.date_of_view[5:7]
                    self.dialog.open()
                    self.dialog.update_width()
                    self.dialog.update_height()
            else:
                self.dialog = MDDialog(
                    title=self.text_for_app['title_calendar_choose'],
                    type="custom",
                    # size_hint=(None, None),
                    # width=1000,
                    # width_offset=5,
                    size_hint_x=0.9,
                    content_cls=Calendar(),
                    buttons=[
                        Button_calendar_ok(),
                        Button_calendar_cancel(),
                    ],
                )
                if self.date_of_view == '':
                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    self.dialog.content_cls.ids.year.text = year
                    self.dialog.content_cls.ids.month.text = self.text_for_app['calendar_month'][month]
                    self.dialog.content_cls.ids.BoxMonth.name = month
                else:
                    self.dialog.content_cls.ids.year.text = self.date_of_view[0:4]
                    self.dialog.content_cls.ids.month.text = self.text_for_app['calendar_month'][self.date_of_view[5:7]]
                    self.dialog.content_cls.ids.BoxMonth.name = self.date_of_view[5:7]
                self.dialog.open()
                self.dialog.update_width()
                self.dialog.update_height()

    def save_date(self, instance):
        month = self.dialog.content_cls.ids.BoxMonth.name
        year = self.dialog.content_cls.ids.year.text
        date_start = f"{year}-{month}-01"
        date_end = f"{year}-{month}-{calendar.monthrange(int(year), int(month))[1]}"
        now = datetime.now()
        date_now = now.strftime("%Y-%m-%d")
        if date_end > date_now and date_start <= date_now:
            date_end = date_now
        self.date_of_view = date_start
        self.rkv.last_id_do_work = 0
        self.rkv.do_work_list = self.rkv.get_do_work_list(date_start, date_end, '')
        if self.Flag_group_by_object:
            self.load_items(0, self.rkv.do_work_list)
        else:
            self.Flag_group_by_object = True
            self.group_by_object(self.root.ids.toolbar)
            #self.Flag_group_by_object = True
        if self.rkv.app_type != '':
            self.root.ids.toolbar.title = self.rkv.count_many() + " грн."
        else:
            self.root.ids.toolbar.title = self.dialog.content_cls.ids.month.text
        #self.Flag_group_by_object = True
        self.dialog.dismiss()

    def button_month(self, instance, direct):
        month = instance.ids.BoxMonth.name
        int_month = int(month)
        if direct == 'left' and instance.ids.BoxMonth.name != '01':
            int_month -= 1
        elif direct == 'right' and instance.ids.BoxMonth.name != '12':
            int_month += 1
        month = f"{int_month:0{2}}"
        instance.ids.month.text = self.text_for_app['calendar_month'][month]
        instance.ids.BoxMonth.name = month

    def button_year(self, instance, direct):
        year = instance.ids.year.text
        print (year)
        int_year = int(year)
        if direct == 'left':
            int_year -= 1
        elif direct == 'right':
            int_year += 1
        year = str(int_year)
        instance.ids.year.text = year

    def open_work_info(self, instance):
        self.button_search('close')
        if type(instance).__name__ == 'SwipeToDeleteItem':
            self.prev_screen = self.root.ids.screen_manager.current
            self.root.ids.screen_manager.current = "scr 6"
            work_type = list(
                filter(lambda x: x['219'] == instance.work_do['223'], self.rkv.work_list['data'])).pop()
            self.root.ids.name_work.text = instance.work_do['223']
            self.root.ids.info_box.name = work_type['id']
            self.root.ids.inch.text = f"{self.text_for_app['title_unit_name']} - {instance.unit_name}"
            if self.rkv.app_type != '':
                self.root.ids.coast_work.text = f"{self.text_for_app['title_price']} - {instance.work_do[self.rkv.conf_serv]} {self.text_for_app['currency']}."
            else:
                self.root.ids.coast_work.text = f"{self.text_for_app['title_price']} - {work_type['220']} {self.text_for_app['currency']}."
            self.root.ids.toolbar.right_action_items = [["arrow-u-left-bottom-bold", lambda x: self.button_back()]]
            self.root.ids.toolbar.title = self.text_for_app['title_info_type_work']
        else:
            self.prev_screen = self.root.ids.screen_manager.current
            self.root.ids.screen_manager.current = "scr 6"
            self.root.ids.name_work.text = instance.work_list['219']
            self.root.ids.info_box.name = instance.work_list['id']
            self.root.ids.inch.text = f"{self.text_for_app['title_unit_name']} - {instance.work_list['243']}"
            self.root.ids.coast_work.text = f"{self.text_for_app['title_price']} - {instance.work_list['220']} {self.text_for_app['currency']}."
            self.root.ids.info_work.text = f"{instance.work_list['262']}"
            self.root.ids.toolbar.right_action_items = [["arrow-u-left-bottom-bold", lambda x: self.button_back_from_WL()]]
            self.root.ids.toolbar.title = self.text_for_app['title_info_type_work']




    def button_back(self):
        self.prev_screen='src 1'
        self.root.ids.nav_drawer.set_state("close")
        self.root.ids.screen_manager.current = "scr 1"
        self.root.ids.toolbar.right_action_items = [
            ["home-city-outline", lambda x: self.group_by_object(self.root.ids.toolbar)],
            ["calendar", lambda x: self.show_calendar()], ["plus", lambda x: self.add_work()]]
        self.root.ids.toolbar.title = f"{self.rkv.count_many()} {self.text_for_app['currency']}." if self.rkv.app_type != '' else self.text_for_app['title_done_work']

    def button_back_from_WL(self):
        self.prev_screen = 'src 1'
        self.root.ids.nav_drawer.set_state("close")
        self.root.ids.screen_manager.current = "scr 2"
        self.root.ids.toolbar.right_action_items = [["magnify", lambda x: app.button_search('open')]]
            #["home-city-outline", lambda x: self.group_by_object(self.root.ids.toolbar)],
            #["calendar", lambda x: self.show_calendar()], ["plus", lambda x: self.add_work()]]
        self.root.ids.toolbar.title = self.text_for_app['title_work_type_list']
        self.button_search('open')

    def button_add_from_info(self, instance):
        self.add_work()
        self.button_back()

        self.root.ids.new.children[0].ids.work_type.text = self.root.ids.name_work.text
        if self.dropdown:
            self.dropdown.dismiss()
        self.root.ids.new.children[0].ids.work_type.name = self.root.ids.info_box.name
        self.root.ids.new.children[0].ids.work_type.parent.name = 'edit'
        self.root.ids.scroll_do_work.scroll_to(self.root.ids.new, padding=10, animate=True)
        self.button_search('close')


    def button_search(self, event):
        #self.root.ids.search_box.height = 80
        if event == "open":
            pos_y = Window.height - (self.root.ids.toolbar.height + self.root.ids.text_search.height)/2
        else:
            pos_y = Window.height
        pos_x = (Window.width - self.root.ids.text_search.width) / 2
        print(pos_x)
        self.root.ids.text_search.pos = (pos_x, pos_y)
        #self.root.ids.text_search.pos_hint = {"top": 1}

    def on_text_search(self, value, item_list):
        work_for_RV = []
        reg_str = '[^a-zA-Z0-9a-яА-Я ]'
        text = re.sub(reg_str,' ',value)
        list_str = text.lower().split(' ')
        find_str= ''
        if len(list_str)>1:
            for str in list_str:
                if str != '':
                    find_str += f'.*{str}'
            find_str += '.*'
        else:
            find_str = text.lower()

        for item in item_list['data']:
            lower = item['219'].lower()
            result = re.findall(find_str, lower)
            if result:
                work_for_RV.append({'work_list': item,
                                    'work_name': item['219'],
                                       "height": 140})
        self.root.ids.scroll_m.data = work_for_RV

    def button_lang(self, instance):
        if self.rkv.Flag_config:
            self.activ_text_field = instance
            self.item_for_builder = []
            list_of_lang = text_for_app.keys()
            for lang in list_of_lang:
                self.item_for_builder.append({"name_item": lang, 'id_item': '1'})
            self.dropdown.data = self.item_for_builder
            self.dropdown.open(instance)

    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        #self.theme_cls.font_styles["Weather"] = ["Weather", 16, False, 0.15]
        self.theme_cls.primary_palette = "LightGreen"
        return Builder.load_string(
        """
#:import ScrollEffect  kivy.effects.scroll.ScrollEffect
<ContentNavigationDrawer>

    ScrollView:
        effect_cls: ScrollEffect
        MDList:
            id: menu_list
            OneLineIconListItem:
                #text: "СЕКРЕТ СЕРВИС"
                #bg_color: 0,0.2,0.25,0.6
                Image:
                    id: logo
                    pos_hint: {"center_x": 0.5,"top": 1}
                    source: 'logo.png'
                    size_hint: 0.8,0.8
                    #size: self.texture_size[0]-50, self.texture_size[1]-50
                #FitImage:
                    #source: "logo.png"
                    #size_hint_y: 1
                    #pos_hint: {"top": 1}
                    #radius: 36, 36, 0, 0
                #IconLeftWidget:
                    #icon: "eye"
                    
            OneLineIconListItem:
                text: app.text_for_app['title_done_work']
                font_size: 30
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"
                    root.toolbar.right_action_items = [["home-city-outline", lambda x: app.group_by_object(root.parent.parent.ids.toolbar)], ["calendar", lambda x: app.show_calendar()],["plus", lambda x: app.add_work()]]
                    root.toolbar.title = app.rkv.count_many()+' '+app.text_for_app['currency']+'.' if app.rkv.app_type != '' else app.text_for_app['title_done_work']
                    app.button_search('close')
                IconLeftWidget:
                    icon: "hammer-screwdriver"
                    
            OneLineIconListItem:
                text: app.text_for_app['title_work_type_list']
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
                    root.toolbar.right_action_items = [["magnify", lambda x: app.button_search('open')]]
                    root.toolbar.title = app.text_for_app['title_work_type_list']
                    app.button_search('open')
                IconLeftWidget:
                    icon: "server"
            OneLineIconListItem:
                id: count_maney
                text: app.text_for_app['title_count']
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"
                    root.toolbar.right_action_items = []
                    root.toolbar.title = app.text_for_app['title_count']
                    app.count_many_for_menu(self)
                    app.button_search('close')
                IconLeftWidget:
                    icon: "cash-plus"         
            
            OneLineIconListItem:
                text: app.text_for_app['title_settings']
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
                    root.toolbar.right_action_items = []
                    root.toolbar.title = app.text_for_app['title_settings']
                    app.button_search('close')
                IconLeftWidget:
                    icon: "cog-outline"
                
            OneLineIconListItem:
                text: app.text_for_app['title_info']
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"
                    root.toolbar.right_action_items = []
                    root.toolbar.title = app.text_for_app['title_info']
                    app.button_search('close')
                IconLeftWidget:
                    icon: "information-outline"
            
            
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: "10dp"

        FloatLayout:
            id: search_box
            size_hint_y: None
            #size_hint_x: None
            #width: -30
            height: root.ids.toolbar.height
            
            MDTopAppBar:
                id: toolbar
                pos_hint: {"top": 1}
                #pos: 500,0
                elevation: 20
                title: app.text_for_app['title_work']
                use_overflow: True
    
                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                right_action_items: [["home-city-outline", lambda x: app.group_by_object(self)],["calendar", lambda x: app.show_calendar()],["plus", lambda x: app.add_work()]]

            MDTextFieldRect:
                size_hint_y: None
                height: root.ids.toolbar.height/2
                size_hint_x: 0.75
                pos: 100, Window.height
                id: text_search
                #text_color: 0,0,0,1
                on_text: app.on_text_search(self.text, app.rkv.work_list)
                font_size: Window.width/20
                background_color: app.theme_cls.primary_light
                multiline: False
            MDSpinner:
                id: spiner
                size_hint: None, None
                size: dp(20), dp(20)
                #pos_hint: {'x': .5}
                #pos: 500
                active: False
        MDNavigationLayout:
            x: toolbar.height

            ScreenManager:
                id: screen_manager

                MDScreen:
                    id: scr1
                    name: "scr 1"
                    #size: (self.parent.width, self.parent.height)
                    MDBoxLayout:
                        orientation: "vertical"
                        #spacing: "10dp"
                        #size: (self.parent.width, self.parent.height)
                        MDScrollView:
                            #md_bg_color: (0.92, 0.92, 0.92, 1)
                            #always_overscroll: False
                            id: scroll_do_work
                            name: 'scroll_do_work'
                            #size: (self.parent.width, self.parent.height)
                            on_scroll_move: app.start_event_load(self)
                            on_scroll_stop: app.start_load(self)

                            MDBoxLayout:
                                spacing: 10
                                orientation: "vertical"
                                id: md_list1
                                size_hint_y: None
                                height: self.minimum_height
                                md_bg_color: (0.92, 0.92, 0.92, 1)
                                MDBoxLayout:
                                    padding: 0
                                    orientation: "vertical"
                                    id: new
                                    md_bg_color: (1, 1, 1, 1)
                                    size_hint_y: None
                                    height: self.minimum_height
                                MDBoxLayout:
                                    orientation: "vertical"
                                    spacing: 10
                                    id: md_list
                                    size_hint_y: None
                                    height: self.minimum_height

                MDScreen:
                    name: "scr 2"

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "10dp"


                        RecycleView:
                            id: scroll_m
                            viewclass: 'WorkTypeCard'
                            size_hint_y: None
                            height: self.parent.height
                            do_scroll_x: False
                            key_size: "height"
                            RecycleBoxLayout:
                                id: scroll_m_box
                                #pos: 100,100
                                default_size: None, None
                                default_size_hint: 1, None
                                size_hint_y: None
                                height: self.minimum_height
                                orientation: 'vertical'
                                #spacing: dp(1)
                                #padding: dp(5)


                MDScreen:
                    name: "scr 3"
                    StackLayout:
                        size_hint: 1, 1
                        padding: 5
                        MDTextField:
                            id: adress
                            hint_text: "Multi-line text"
                            #text_color: 0, 0, 0, 1
                            hint_text: app.text_for_app['title_server_adress']
                            helper_text: app.text_for_app['title_server_help']
                            helper_text_mode: "on_focus"
                            icon_right: "web"
                            font_size: Window.width/20
                            #keyboard_mode: 'system'
                        MDTextField:
                            id: port
                            hint_text: "Multi-line text"
                            #text_color: 0, 0, 0, 1
                            hint_text: app.text_for_app['title_port']
                            helper_text: app.text_for_app['title_port_help']
                            helper_text_mode: "on_focus"
                            icon_right: "database-export"
                            font_size: Window.width/20
                            #keyboard_mode: 'system'
                        MDTextField:
                            id: login
                            hint_text: "Multi-line text"
                            #text_color: 0,0,0,1
                            hint_text: app.text_for_app['title_username']
                            helper_text: app.text_for_app['title_username_help']
                            helper_text_mode: "on_focus"
                            icon_right: "account"
                            font_size: Window.width/20
                            #keyboard_mode: 'managed'
                        MDTextField:
                            id: password
                            hint_text: app.text_for_app['title_password']
                            #text: "password"
                            helper_text: app.text_for_app['title_password_help']
                            password: True
                            icon_right: "key-variant"
                            size_hint_x: 1
                            helper_text_mode: "on_focus"
                            font_size: Window.width/20
                            #keyboard_mode: 'managed'
                        BoxLayout:
                            size_hint_y: None
                            height: 10
                        MDRaisedButton:
                            id: singup_btn
                            text: app.text_for_app['btn_login_enter']
                            font_size: Window.width/20
                            size_hint_x: 1
                            height: 90
                            pos_hint: {'top':1}
                            on_release: app.button_login(self, root.ids.adress, root.ids.port, root.ids.login, root.ids.password)
                        BoxLayout:
                            size_hint_y: 0.1
                            #height: 90
                        MDBoxLayout:
                            id: chip_box
                            size_hint_x: 1
                            size_hint_y: None
                            pos_hint: {'top':1}
                            spacing: "8dp"
                            height: self.minimum_height
                            orientation: "horizontal"
                            MDBoxLayout:
                                size_hint_x: 0.7
                                #pos_hint: {'top':1}
                                spacing: "8dp"
                                height: 90
                                SwipeLabel:
                                    pos_hint: {'center_y':0.5}
                                    text: app.text_for_app['change_lang']
                                    size_hint_x: 0.7
                            MDRaisedButton:
                                id: lang_btn
                                text: app.lang
                                font_size: Window.width/20
                                size_hint_x: 0.3
                                height: 90
                                pos_hint: {'top':1, 'right':1}
                                on_release: app.button_lang(self)
                            
            
                MDScreen:
                    name: "scr 4"
                    StackLayout:
                        size_hint: 1, 1
                        padding: 1
                        ScrollView:
                            effect_cls: ScrollEffect
                            do_scroll_y: True
                            
                            StackLayout:
                                size_hint_y: None
                                height: self.minimum_height
                                padding: 3
                                SwipeLabel:
                                    text: app.text_for_app['info_1']
                                OneLineIconListItem:
                                    text: app.text_for_app['info_2']
                                    font_size: Window.width/20#self.parent.parent.width/20
                                    IconLeftWidget:
                                        icon: "home-city-outline"  
                        
                                SwipeLabel:
                                    text: app.text_for_app['info_3']                                         
                                    markup: True
                                OneLineIconListItem:
                                    text: app.text_for_app['info_4']
                                    font_size: Window.width/20#self.parent.parent.width/20
                                    IconLeftWidget:
                                        icon: "calendar"  
                        
                                SwipeLabel:
                                    text: app.text_for_app['info_5']
                                OneLineIconListItem:
                                    text: app.text_for_app['info_6']
                                    font_size: Window.width/20#self.parent.parent.width/20
                                    IconLeftWidget:
                                        icon: "plus"  
                                
                                SwipeLabel:
                                    text: app.text_for_app['info_7']
                                
                                OneLineIconListItem:
                                    text: app.text_for_app['info_8']
                                    font_size: Window.width/20#self.parent.parent.width/20 
                                SwipeLabel:
                                    text: app.text_for_app['info_9']   
                                OneLineIconListItem:
                                    text: app.text_for_app['info_10']
                                    font_size: Window.width/20#self.parent.parent.width/20 
                                SwipeLabel:
                                    text: app.text_for_app['info_11'] 
                MDScreen:
                    name: "scr 5"
                    StackLayout:
                        size_hint: 1, 1
                        padding: 5
                        OneLineIconListItem:
                            id: comon_many_befor
                            text: ''
                            pos_hint: {'top':1}
                            font_size: Window.width/20
                            IconLeftWidget:
                                icon: "cash-check"
                        OneLineIconListItem:
                            id: comon_many_now
                            text: ''
                            pos_hint: {'top':1}
                            font_size: Window.width/20
                            IconLeftWidget:
                                icon: "hammer-screwdriver"
                MDScreen:
                    name: "scr 6"
                    StackLayout:
                        size_hint: 1, 1
                        padding: 1
                        ScrollView:
                            effect_cls: ScrollEffect
                            do_scroll_y: True
                            StackLayout:
                                id: info_box
                                name: ''
                                size_hint_y: None
                                height: self.minimum_height
                                padding: 3
                                StackLayout:
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: 3
                                    SwipeLabel:
                                        id: name_work
                                        text: ''
                                StackLayout:
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: 3
                                    OneLineIconListItem:
                                        text: app.text_for_app['title_unit_name']
                                        font_size: Window.width/20#self.parent.parent.width/20
                                        id: inch
                                    SwipeLabel:
                                        
                                        text: ''
                                StackLayout:
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: 3
                                    OneLineIconListItem:
                                        text: app.text_for_app['title_price']
                                        font_size: Window.width/20#self.parent.parent.width/20
                                        id: coast_work
                                    SwipeLabel:
                                        id: info_work 
                                        text: ''
                                MDRaisedButton:
                                    size_hint_x: 1
                                    #size_hint_y: None
                                    height: Window.width/10
                                    text: app.text_for_app['btn_create_work']
                                    font_size: Window.width/20#self.parent.parent.width/20
                                    on_release: app.button_add_from_info(self)

                                

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
            toolbar: toolbar
            new: new

<Object_Conteiner>
    name: root.object_name
    padding: "3dp"
    spacing: "5dp"
    size_hint_y: None
    height: self.minimum_height
    orientation: "vertical"

    SwipeLabel:
        text: root.object_name
        height: self.texture_size[1]+30
        bold: True
        #size_hint_x: None
        #width: Window.width
        halign: 'center'

<SwipeLabel@MDLabel>
    size_hint_y: None
    #pos_y: -50
    height: self.texture_size[1]
    font_size: Window.width/20#self.parent.parent.width/21
    #valign: 'top'
    pos_hint: {'x': 0, 'y': 1}

<SwipeBox@MDBoxLayout>
    size_hint_y: None
    height: self.minimum_height

<SwipeToDeleteItem>:
    padding: 19
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {"center_x": 0.5}
    size_hint_x: 0.96
    orientation: "vertical"
    MDRelativeLayout:
        id: yes
        padding: -50,0,0,0
        MDIconButton:
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            icon: "check-all"
            pos_hint: {"center_y": 0.6, "center_x": 1}
            
    SwipeLabel:
        id: work_do
        text: f"[ref=work][b]{root.work_do['223']}[/b][/ref]\\n[size={str(self.font_size*0.75)[:2]}][b]{app.text_for_app['space_amount']}{app.text_for_app['title_amount']}: [/b]{root.work_do['224']} {root.unit_name}{root.salary}\\n[b]{app.text_for_app['space_wired']}{app.text_for_app['title_wired']}: [/b]   {root.work_do['252']}\\n[b]{app.text_for_app['space_object']}{app.text_for_app['title_object']}:[/b]   {root.object_name}\\n[b]{app.text_for_app['space_date']}{app.text_for_app['title_date']}:[/b]   {root.work_do['267']}\\n[b]{app.text_for_app['space_complex']}{app.text_for_app['title_complex']}:[/b]   {root.work_do['237']}\\n[b]{app.text_for_app['space_bonus']}{app.text_for_app['title_bonus']}:[/b]   {root.work_do['266']}\\n[b]{app.text_for_app['space_workers']}{app.text_for_app['title_workers']}:[/b]   {root.work_do['239']}\\n[b]{app.text_for_app['space_notes']}{app.text_for_app['title_notes']}:[/b]   {root.work_do['253']}[/size]"
                #text : "[table][tr][td]table cell 1[/td][td]table cell 2[/td][/tr][/table]"
        markup: True
        on_ref_press: app.open_work_info(self.parent)
<Content_do_work>
    size_hint_y: None
    height: self.texture_size[1]
    font_size: Window.width / 20  # self.parent.parent.width/20
    pos_hint: {'x': 0, 'y': 1}
    id: work_type
    text: f"[ref=work][b]{root.work_do['223']}[/b][/ref]\\n[size={str(self.font_size*0.75)[:2]}][b] {app.text_for_app['title_amount']}: [/b]{root.work_do['224']} {root.unit_name}{root.salary}\\n[b]           {app.text_for_app['title_wired']}: [/b]   {root.work_do['252']}\\n[b]          {app.text_for_app['title_object']}:[/b]   {root.object_name}\\n[b]               {app.text_for_app['title_date']}:[/b]   {root.work_do['267']}\\n[b]   {app.text_for_app['title_complex']}:[/b]   {root.work_do['237']}\\n[b]          {app.text_for_app['title_bonus']}:[/b]   {root.work_do['266']}\\n[b]{app.text_for_app['title_workers']}:[/b]   {root.work_do['239']}\\n[b] {app.text_for_app['title_notes']}:[/b]   {root.work_do['253']}[/size]"
                #text : "[table][tr][td]table cell 1[/td][td]table cell 2[/td][/tr][/table]"
    markup: True
    on_ref_press: app.open_work_info(self.parent)

<Worker_item>:
    name: root.id_worker
    size_hint: None, None
    height: self.minimum_height
    width:self.minimum_width
    Button:
        background_normal: ''
        size_hint: None, None
        size: (self.texture_size[0]+10, self.texture_size[1]+5)
        text: root.name_worker
        color: 0,0,0,1
        font_size: Window.width/20#self.parent.parent.width/20
        on_release: app.remove_worker(self, self.parent)
        canvas.before:
            Color:
                rgba: .5, .5, .5, 1
            Line:
                width: 1
                rectangle: self.x, self.y, self.width, self.height

<AddNewWork>:
    id: addwor
    size_hint_y: None
    height: self.minimum_height
    orientation: "vertical"
# Объекты
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        name: 'not_edit'
        MDTextField:
            name: 'error'
            id: object
            multiline: True
            hint_text: "Multi-line text"
            font_size: Window.width/20
            text_color_normal: 0,0,0,1
            hint_text: app.text_for_app['title_object']
            helper_text: app.text_for_app['title_object_help']
            helper_text_mode: "on_focus"
            on_focus: app.on_focus(self, self.focus,app.rkv.object_list, '158')
            on_text: app.on_text(self, self.text, app.rkv.object_list, '158')
# Монтажники
    BoxLayout:
        size_hint: 1, None
        height: self.minimum_height
        name: 'not_edit'

        StackLayout:
            padding: [0,5,0,5]
            id: worker
            name: 'worker'
            size_hint: 0.9, None
            height: self.minimum_height
            orientation: "lr-tb"

        BoxLayout:
            size_hint: 0.1, 1
            Button:
                background_normal: ''
                color: 0,0,0,1
                #background_color: 0,0.2,0.25,0.6
                #adaptive_size: True
                size_hint: 1, 1
                #size: (self.texture_size[0], self.texture_size[1])self.parent.parent.parent.children[3].children[0].name
                text: '+'
                font_size: Window.width/20#self.parent.parent.width/20
                on_release: app.show_drop_worker(root.ids.worker, root.ids.object.name, root.ids.object)
                canvas.before:
                    Color:
                        rgba: .5, .5, .5, 1
                    Line:
                        width: 1
                        rectangle: self.x, self.y, self.width, self.height
                
    MDSeparator:
    MDLabel:
        size_hint_y: None
        text: app.text_for_app['title_choose_workers']
        height: self.texture_size[1]
        font_size: Window.width/23
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 0.5
#Выбор типа работ
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        name: 'not_edit'
        MDTextField:
            name: 'error'
            id: work_type
            multiline: True
            font_size: Window.width/20
            hint_text: "Multi-line text"
            text_color_normal: 0,0,0,1
            helper_text_mode: "on_focus"
            hint_text: app.text_for_app['title_work_type']
            helper_text: app.text_for_app['title_work_type_info']
            on_focus: app.on_focus(self, self.focus,app.rkv.work_list, '219')
            on_text: app.on_text(self, self.text, app.rkv.work_list, '219')

# Блок Колличество и Сложность работ
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: 'horizontal'
            BoxLayout:
                size_hint_y: None
                height: self.minimum_height
                orientation: 'horizontal'
                size_hint_x: 0.4
                name: 'not_edit'
                MDTextField:
                    name: 'error'
                    id: amount
                    font_size: Window.width/20
                    text_color_normal: 0, 0, 0, 1
                    hint_text: app.text_for_app['title_amount']
                    helper_text: app.text_for_app['title_amount_info']
                    helper_text_mode: "on_focus"
                    on_text: app.on_text(self, self.text, 'empty_array', 'ampty_field', False, root)
            BoxLayout:
                size_hint_y: None
                height: self.minimum_height
                orientation: 'horizontal'
                size_hint_x: 0.6
                name: 'not_edit'
                MDTextField:
                    name: 'error'
                    id: complex
                    font_size: Window.width/20
                    text_color_normal: 0, 0, 0, 1
                    hint_text: app.text_for_app['title_complex']
                    helper_text: app.text_for_app['title_complex_info']
                    helper_text_mode: "on_focus"
                    on_focus: app.on_focus(self, self.focus,app.rkv.complex_list, 'name')
                    on_text: app.on_text(self, self.text, app.rkv.complex_list, 'name')
#Выбор оборудования
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            name: 'not_edit'
            MDTextField:
                name: 'error'
                hint_lbl_font_size: 60
                id: equipment
                multiline: True
                font_size: Window.width/18
                hint_text: "Multi-line text"
                text_color_normal: 0,0,0,1
                hint_text: app.text_for_app['title_equipment']
                helper_text: app.text_for_app['title_equipment_info']
                helper_text_mode: "on_focus"
                on_focus: app.on_focus(self, self.focus,app.rkv.equipment_list, '251')
                on_text: app.on_text(self, self.text, app.rkv.equipment_list, '251')

# Примечания
        BoxLayout:
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            name: 'not_edit'
            MDTextField:
                name: 'error'
                id: notes
                multiline: True
                font_size: Window.width/18
                hint_text: "Multi-line text"
                text_color_normal: 0,0,0,1
                hint_text: app.text_for_app['title_notes']
                helper_text: app.text_for_app['title_notes_info']
                helper_text_mode: "on_focus"
                on_text: app.on_text(self, self.text, 'empty_array', 'ampty_field', False)

# Блок кнопок
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        orientation: "horizontal"
        MDRaisedButton:
            size_hint_x: 0.5
            size_hint_y: None
            height: Window.width/10
            text: app.text_for_app['btn_save']
            font_size: Window.width/20#self.parent.parent.width/20
            on_release: app.button_save_new(root)#([root.ids.object, root.ids.work_type, root.ids.complex, root.ids.equipment], [root.ids.amount, root.ids.notes],root.ids.worker)

        MDRaisedButton:
            size_hint_x: 0.5
            height: Window.width/10
            text: app.text_for_app['btn_cansel']
            font_size: Window.width/20#self.parent.parent.width/20
            on_press: app.button_close_new(self.parent.parent)

# Выпадающее меню
<DropDown>
    id: dropdown
    viewclass: 'ItemForDropDown'
    size_hint_y: None
    #height: 100
    RecycleBoxLayout:
        id: drop_down_box
        #pos: 100,100
        #default_size: None, None
        #default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        
        padding: 2,0,0,0

<ItemForDropdown>:
    id: root.id_item
    border: (10,10,10,2)
    background_normal: ''
    text_size: root.width-3, None
    size_hint_y: None
    text: root.name_item
    color: 0,0,0,1
    height: self.texture_size[1]+10
    font_size: Window.width/18
    on_release: app.click_drop_item(root.name_item, root.id_item)
    canvas:
        Color:
            rgba: .5, .5, .5, 1
        Rectangle:
            size: self.width, 2
            pos: self.pos          
        #Line:
            #width: 2
            #rectangle: self.x, self.y, self.width, self.height

#<ItemForDropdown>:
    #padding: "5dp"
    #name: root.id_item
    #spacing: "2dp"
    #size_hint_y: None
    #height: self.minimum_height
    #orientation: "vertical"

    #Button:


# Тип работ
<WorkTypeCard>:
    size_hint_y: None
    padding_x: "5dp"
    height: self.texture_size[1]+30
    font_size: Window.width/20
    #valign: 'top'
    #pos_hint: {'x': 0, 'y': 1}
    text: f"[ref=work_info][b]{root.work_name}[/b][/ref]"#\\nЕдиница измерения: {root.work_list.get('243')}"
    markup: True
    shorten: True
    on_ref_press: app.open_work_info(self)
    canvas:
        Color:
            rgba: .5, .5, .5, 1
        Rectangle:
            size: self.width, 2
            pos: self.pos          
    
<Button_ok>
    text: app.text_for_app['btn_ok']
    on_release: app.remove_item(root.instance)

<Button_cancel>
    text: app.text_for_app['btn_CANSEL']
    on_release: app.dialog.dismiss()
    
<Button_calendar_ok>
    theme_text_color: "Custom"
    text_color: 0,0,0,1
    font_style: "H6"
    text: app.text_for_app['btn_ok']
    on_release: app.save_date(root)

<Button_calendar_cancel>
    theme_text_color: "Custom"
    text_color: 0,0,0,1
    font_style: "H6"
    text: app.text_for_app['btn_CANSEL']
    on_release: app.dialog.dismiss()
    
<Calendar>
    size_hint_y: None
    height: self.minimum_height
    orientation: "vertical"
    spacing: 15
    MDLabel:
        size_hint_y: None
        height: self.texture_size[1]
        font_size: Window.width/17
        halign: "center"
        text: app.text_for_app['title_choose_year']
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style: "H6"
    BoxLayout:
        size_hint_y: None
        height: Window.height/10
        orientation: "horizontal"
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color
            Line:
                width: 1
                rectangle: self.x, self.y, self.width, self.height            
            Rectangle:
                size: self.width-4,self.height-4
                pos: self.x+2, self.y+2
        MDIconButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            icon: "arrow-left-bold-box-outline"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
            on_release: app.button_year(root, 'left')
            user_font_size: "30dp"

        MDLabel:
            id: year
            font_size: Window.width/17
            halign: "center"
            text: ""
        MDIconButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            icon: "arrow-right-bold-box-outline"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
            on_release: app.button_year(root, 'right')
            user_font_size: "30dp"
    MDLabel:
        size_hint_y: None
        height: self.texture_size[1]
        font_size: Window.width/17
        halign: "center"
        text: app.text_for_app['title_choose_month']
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style: "H6"
    BoxLayout:
        size_hint_y: None
        height: Window.height/10
        orientation: "horizontal"
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color
            Line:
                width: 1
                rectangle: self.x, self.y, self.width, self.height            
            Rectangle:
                size: self.width-4,self.height-4
                pos: self.x+2, self.y+2

        #canvas.before:
            #Color:
                #rgba: .5, .5, .5, 1
            #Line:
                #width: 1
                #rectangle: self.x, self.y, self.width, self.height
        MDIconButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            icon: "arrow-left-bold-box-outline"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
            on_release: app.button_month(root, 'left')
            user_font_size: "30dp"
        BoxLayout:
            id: BoxMonth
            name: ''
            size_hint_y: None
            height: Window.height/10
            MDLabel:
                id: month
                font_size: Window.width/17
                halign: "center"
                text: "Ноябырь"
        MDIconButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            icon: "arrow-right-bold-box-outline"
            theme_text_color: "Custom"
            text_color: 0,0,0,1
            on_release: app.button_month(root, 'right')
            user_font_size: "30dp"


        """)
if __name__ == '__main__':
    MyApp().run()
