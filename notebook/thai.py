import json
from checklang import isTH
from minedit import levenshtein as lv

def createDictFromFile(filename):
    with open(filename, encoding='utf-8') as fin:
        myjson = json.load(fin, encoding='utf-8')
    return myjson

provCode_postal = createDictFromFile('data/postalToProvCode.json')

def getProvinceCode_postal(postal):
    if(provCode_postal.get(postal)):
        ## return province code
        return provCode_postal.get(postal)
    return None

provCode_provTH = createDictFromFile('data/provTHToProvCode.json')
provCode_provEN = createDictFromFile('data/provENToProvCode.json')
def getProvinceCode_prov(provStr):
    if(isTH(provStr)):
        return provCode_provTH.get(provStr)
    else:
        return provCode_provEN.get(provStr)
    
provEN = provCode_provEN.keys()
provTH = provCode_provTH.keys()
def getProvinceCode_inProv(provStr):
    for item in provTH:
            if(item in provStr):
                return provCode_provTH.get(item)
    for item in provEN:
            if(item in provStr):
                return provCode_provEN.get(item)

districtEN = createDictFromFile('data/districtEN.json')
districtEN_keys = districtEN.keys()
districtTH = createDictFromFile('data/districtTH.json')
districtTH_keys = districtTH.keys()

def getProvinceCode_district(location_str):
    if(isTH(location_str)):
        if(districtTH.get(str) != None):
            ## whole string is district
            return districtTH.get(str)
        else:
            ## search district in the string
            for item in districtTH_keys:
                if(item in location_str):
                    return districtTH.get(item)
    else:
        if(districtEN.get(str) != None):
            return districtEN.get(str)
        else:
            for item in districtEN_keys:
                if(item in location_str):
                    return districtEN.get(item)
    
def getProvinceCode_minEdit(location_str):
    out = []
    if(isTH(location_str)):
        for prov in provTH:
            if(lv(prov, location_str) < 5):
                out.append((prov,location_str, lv(prov, location_str)))
        try:
            return provCode_provTH.get(min(out, key=lambda x: x[2])[0])
        except:
            return None
    else:
        for prov in provEN:
            if(lv(prov, location_str) < 5):
                out.append((prov,location_str, lv(prov, location_str)))
        try:
            return provCode_provEN.get(min(out, key=lambda x: x[2])[0])
        except:
            return None
    
    
    