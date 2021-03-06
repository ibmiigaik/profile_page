from flask_mongoengine import MongoEngine

from werkzeug.security import generate_password_hash


db = MongoEngine()

class Schedule(db.Document):
    check = db.StringField(required=True)

    schedule = db.DictField()

    @staticmethod
    def create_mock_schedules():
        schedules = (
            Schedule(
    check=f"ИБ12020",
    schedule ={
            'monday':{
                'day': 'Понедельник',
                'lessons': {
                    'up':{
                        'first': '',
                        'second': '',
                        'third': '',
                        'fourth': '',
                        'fifth': 'Философия',
                        'sixth': '',
                        'seventh': ''
                        },
                    'down': {
                        'first': '',
                        'second': '',
                        'third': '',
                        'fourth': '',
                        'fifth': '',
                        'sixth': 'Философия',
                        'seventh': ''
                       }
                    }
                },

            'tuesday':{
                'day': 'Вторник',
                'lessons': {
                    'up':{
                        'first': '',
                        'second': 'Основы информационной безопасности',
                        'third': 'Основы информационной безопасности',
                        'fourth': 'Физическая культура',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                        },
                    'down': {
                        'first': '',
                        'second': 'Основы информационной безопасности',
                        'third': 'Основы информационной безопасности',
                        'fourth': 'Физическая культура',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                        }
                    }
                },

            'wednesday':{
                'day': 'Среда',
                'lessons': {
                    'up':{
                        'first': 'Физическая культура',
                        'second': 'Основы геодезии',
                        'third': 'Математический анализ',
                        'fourth': 'Основы геодезии',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                        },
                    'down': {
                        'first': 'Физическая культура',
                        'second': 'Основы геодезии',
                        'third': 'Математический анализ',
                        'fourth': 'Основы геодезии',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                       }
                    }
                },

            'thursday':{
                'day': '',
                'lessons': {
                    'up':{
                        'first': '',
                        'second': '',
                        'third': '',
                        'fourth': '',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                        },
                    'down': {
                        'first': '',
                        'second': '',
                        'third': '',
                        'fourth': '',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                       }
                    }
                },

            'friday':{
                'day': '',
                'lessons': {
                    'up':{
                        'first': '',
                        'second': '',
                        'third': '',
                        'fourth': '',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                        },
                    'down': {
                        'first': '',
                        'second': '',
                        'third': '',
                        'fourth': '',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                       }
                    }
                },

            'saturday':{
                'day': 'Суббота',
                'lessons': {
                    'up':{
                        'first': 'Основы управленческой деятельности',
                        'second': 'Истоия и современная система защиты информации в России',
                        'third': '',
                        'fourth': '',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                        },
                    'down': {
                        'first': 'Основы управленческой деятельности',
                        'second': 'Истоия и современная система защиты информации в России',
                        'third': 'Основы управленческой деятельности',
                        'fourth': '',
                        'fifth': '',
                        'sixth': '',
                        'seventh': ''
                       }
                    }
                }
            }
            ).save()
        )

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    first_name = db.StringField()
    last_name = db.StringField()
    patronymic = db.StringField()
    addmission_year = db.StringField()
    direction = db.StringField()
    group_num = db.StringField()


    role = db.StringField(required=True)

    @staticmethod
    def create_mock_users():

        users=(
            User(
                username=f"test",
                password=generate_password_hash(f"testpassword"),
                first_name = f"testfirst_name",
                last_name = f"testlast_name",
                patronymic = f"testpatronymic",
                addmission_year =f"2020",
                direction = f"ИБ",
                group_num = f"1",
                role="student",
            ).save()
        )
