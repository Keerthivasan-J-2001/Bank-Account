import re
def  AcNo_Val(AcNo):
    pattern = r'^[A-Z]{3}\d{3}$'
    if(re.match(pattern,AcNo)):
        return True
    else:
        return False

#print(AcNo_Val('FGH6789'))

def AccHolder_Val(name):
    val = False
    if(name.istitle()):
        if(len(name.split()) == 3):
            for i in name.split():
                if(i.isalpha()):
                    val = True
                else:
                    val = False
                    break
    return val

#print(AccHolder_Val('Mo Naga M'))

def Age_Val(age):
    if(age.isdigit()):
        return True
    return False

def Gender_Val(gen):
    l = ['male','female']
    if(gen.lower() not in l):
        return False
    else:
        return True

#print(Gender_Val('MALE'))

from datetime import datetime
def DOB_Val(date):
    format = '%d-%m-%Y'
    try:
        val = bool(datetime.strptime(date,format))
    except ValueError:
        val = False
    return val

#print(DOB_Val('30-04-1945'))

def City_Val(city):
    if(city.isalpha() and city.istitle()):
        return True
    return False
    
#print(City_Val('Chennai'))

def Bal_Val(bal):
    if(bal < 0):
        return False
    return True

def AccType_Val(AccType):
    t = ('Savings','Current','Joint')
    if(AccType in t):
        return True
    else:
        return False

#print(AccType_Val('Current'))

def PanCard_Val(panno):
    pattern = r"^[A-Z]{5}\d{4}[A-Z]{1}$"
    if(re.match(pattern,panno)):
        return True
    else:
        return False
    
#print(PanCard_Val('APFPJ0567T'))

def Aadhaar_Val(Ano):
    if(Ano.isdigit() and len(Ano) == 12):
        return True
    return False

#print(Aadhaar_Val('209128000071'))