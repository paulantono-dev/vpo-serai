from common.utils import get_random_string
__DICT_ENV = {
    'LOCAL':{
        'SECRET_KEY':get_random_string(32),
    },
    'STG':{
        'SECRET_KEY':get_random_string(32),
    },
    'PRD':{
        'SECRET_KEY':get_random_string(32),
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