import random
import string
from datetime import datetime
from pytz import timezone
from global_variable import ENV
import hashlib


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str.upper()

def generateMd5(prmString):
    rs={'status':False,'md5':'Error generate Hash Text'}
    try:
        datetimeNow = generateDateNow()
        datetimeString = datetimeNow.strftime('%m%d%Y%H%M%S%f')
        vText = prmString+ENV['SECRET_KEY']+datetimeString
        vMd5 = hashlib.md5()
        vMd5.update(vText.encode())
        vConvertText = vMd5.hexdigest()
        rs['status']=True
        rs['md5']=vConvertText
    except Exception as e:
        print(e)
    return rs

def generateDateNow():
    now_utc = datetime.now(timezone('ASIA/JAKARTA'))
    return now_utc

def generateDate():
    date = generateDateNow().strftime("%Y%m%d")
    return date
def generateCurrentTimestamp(string=True):
    now = generateDateNow().strftime("%d-%m-%Y %H:%M:%S")
    if not string:
        now = generateDateNow()
    return now
def toDate(prmStringDate):
    return datetime.strptime(prmStringDate,'%Y-%m-%d')
def generateFileName(prmFileName):
    datetimeNow = generateDateNow()
    datetimeString = datetimeNow.strftime('%m%d%Y%H%M%S%f')
    searchIndexExtension = prmFileName.find('.')
    namefile,ext = os.path.splitext(prmFileName)
    returnFileName = "{}_{}{}".format(namefile,datetimeString,ext)
    return returnFileName

def check_date(prmDate):
    is_valid = False
    to_date = datetime.strptime(prmDate,'%Y-%m-%d %H:%M:%S')
    if to_date.date()<=datetime.now().date():
        is_valid=True
    return is_valid