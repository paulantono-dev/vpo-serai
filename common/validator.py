class ValidatorInput:
    def __init__(self,**kwargs):
        self.__string_data = ''
        self.__key_type = ''
        self.__list_numeric = ['1','2','3','4','5','6','7','8','9','0',1,2,3,4,5,6,7,8,9,0]
        self.__list_alpha = [
                'a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t',
                'u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J',
                'K','L','M','N','O','P','Q','R','S','T',
                'U','V','W','X','Y','Z',' '
        ]
        self.__list_alphanumeric = self.__list_numeric+self.__list_alpha
        self._dict_character = {
            'numeric':self.__list_numeric,
            'alpha':self.__list_alpha,
            'alphanumeric':self.__list_alphanumeric,
            'datetime':self.__list_alphanumeric+['-','/',':'],
            'email':self.__list_alphanumeric+['@','.','_'],
        }
        self.__length_character=0
        self.__allowed_character = []
    def __start_check(self):
        if len(self.__string_data)>self.__length_character:
            return {'status':False,'value':self.__string_data,'not_valid_value':f'Panjang Karakter tidak boleh lebih dari {self.__length_character}'}
        for string in self.__string_data:
            if string not in self._dict_character.get(self.__key_type)+self.__allowed_character:
                return {'status':False,'value':self.__string_data,'not_valid_value':string}
        return {'status':True,'value':self.__string_data,'not_valid_value':''}
    def text_numeric(self,stringData,allowed_character=[],length=100):
        self.__string_data=stringData
        self.__allowed_character=allowed_character
        self.__length_character=length
        self.__key_type='alphanumeric'
        return self.__start_check()
    def numeric(self,stringData,allowed_character=[],length=100):
        self.__string_data=stringData
        self.__allowed_character=allowed_character
        self.__key_type='numeric'
        self.__length_character=length
        return self.__start_check()
    def text(self,stringData,allowed_character=[],length=100):
        self.__string_data=stringData
        self.__allowed_character=allowed_character
        self.__key_type='alpha'
        self.__length_character=length
        return self.__start_check()
    def email(self,stringData,allowed_character=[],length=100):
        import re
        self.__string_data=stringData
        self.__allowed_character=allowed_character
        self.__key_type='email'
        self.__length_character=length
        # Make a regular expression
        # for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, stringData)):
            return self.__start_check()
        else:
            return {'status':False,'value':self.__string_data,'not_valid_value':'Not Valid Email Format!'}
        
    def datetime(self,stringData,allowed_character=[],length=10):
        self.__string_data=stringData
        self.__allowed_character=allowed_character
        self.__key_type='datetime'
        self.__length_character=length
        return self.__start_check()