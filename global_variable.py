__DICT_ENV = {
    'LOCAL':{
        'SECRET_KEY':'SERAITEST',
    },
    'STG':{
        'SECRET_KEY':'SERAITEST',
    },
    'PRD':{
        'SECRET_KEY':'M0V1NGF0RW4RD',
    },
}
DATABASE = {
    'SERAI':{
        'DBNAME':'serai',
        'USER':'serai',
        'PASSWORD':'serai123',
        'PORT':'5432',
        'HOST':'127.0.0.1',

    }
}

ENV = __DICT_ENV['LOCAL']