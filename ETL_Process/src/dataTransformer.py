import 

'''Read data from file into pandas dataframe'''
def readJSON(filename):
    '''Read json file to list of json'''
    import pandas as pd
    import json

    jobsList = []
    try:
        with open(filename, 'r', encoding='utf-8') as fin:
            for line in fin:
                lineJson = json.loads(line, encoding='utf-8')
                jobsList.append(lineJson)
        return jobsList
    except:
        raise

def cleanData(inputDict):
    '''From input dict, chop into necessary fields'''
    outputDict = {}
    outputDict['jobtitle'] = get_jobtitle(inputDict)
    outputDict['ostarnetid'] = get_ostarnetid(inputDict)
    #outputDict['postdate'] = get_postdate(inputDict)
    #outputDict['amount'] = get_amount(inputDict)
    #outputDict['idcompany'] = get_idcompany(inputDict)
    #outputDict['age_low'] = get_agelow(inputDict)
    #outputDict['age_high'] = get_agehigh(inputDict)
    #outputDict['exp_low'] = get_explow(inputDict)
    #outputDict['exp_high'] = get_exphigh(inputDict)
    #outputDict['no_position'] = get_noposition(inputDict)

    return outputDict

def get_jobtitle(inputDict):
    key = ['func', 'pos', 'pos2', 'posth']
    try:
        title = " ".join([item2 for item2 in [inputDict.get(item) for item in key] if item2 != None])
    except:
        raise
    return title

def get_ostarnetid(inputDict):
    ## map to ostarnet in the database
    import random
    ostartnetid = random.randint(1,4)
    return ostarnetid

def get_postdate(inputDict):
    ## see if the later dicts has the same structure or not
    try: 
        monthdict = {"January":1, "February":2, "March":3, "April":4, "May":5,
                "June":6, "July":7, "August":8, "September":9, "October":10,
                "November":11, "December":12}
        date = inputDict.get('pdate').split("-")
        date = "20"+date[2]+"-"+"0"*(2-len(str(monthdict.get(date[1]))))+str(monthdict.get(date[1]))+"-"+date[0]
    except:
        raise
    return date

def get_amount(inputDict):
    try:
        ## wait for p'pyle
        import random
        amount = random.randint(1,3)
    except:
        raise
    return amount

        













