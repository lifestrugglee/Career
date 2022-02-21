import os
import re
import time
from random import randint
import requests
import json
from bs4 import BeautifulSoup 

class jsonParser():
    def __init__(self):
        self.json_temp = {
               "@context":"https://schema.org/",
               "@type":"Dataset",
               "name":"",
               "identifier":"",
               "description":"",
               "conditionsOfAccess":"",
               "sameAs":"",
               "keywords":[],
               "additionalType":"Datatype",
               "variableMeasured":[
                  "Variable: What kind of column contains in the data"
               ],
               "isBasedOn":{
                  "@type":"CreativeWork",
                  "sourceOrganization":""
               },
               "inLanguage":"",
               "license":"",
               "hasPart":[],
               "creator":{
                  "@type":"Organization",
                  "employees":{
                     "@type":"Person",
                     "name":""
                  },
                  "name":"",
                  "contactPoint":{
                     "@type":"ContactPoint",
                     "email":""
                  },
                  "location":""
               },
               "publication":{
                  "@type":"publicationEvent",
                  "name":"",
                  "identifier":{
                     "@type":"PropertyValue",
                     "propertyID":[]
                  }
               },
               "author":"authors name",
               "dateCreated":"yyyy-mm-dd",
               "dateModified":"yyyy-mm-dd",
               "distribution":[
                  # {
                  #    "@type":"DataDownload",
                  #    "encodingFormat":"",
                  #    "contentUrl":""
                  # }
               ],
               "spatialCoverage":{
                  "@type":"Place",
                  "address":{
                     "@type":"PostalAddress",
                     "streetAddress":""
                  }
               },
               "locationCreated":{
                  "@type":"Country",
                  "name":""
               },
               "url":"",
               "comment":"",
               "maintainer":{
                  "@type":"Organization",
                  "name":""
               },
               "contentRating":"",
               "rating":{
                  "viewCount":"",
                  "voteCount":"",
                  "usabilityRating":"",
                  "downloadCount":""
               },
               "size":"",
               "totalBytes":"",
               "files":[

               ],
               "isReviewed": "N/A",
               "hasData": "N/A"
            }
    
    def set_Name(self, namestr):
        self.json_temp['name'] = namestr

    def get_Name(self):
        tmpname = self.json_temp['name'].replace('"', '').replace("'", "")
        charc = r'([<>#/\\|\?]+)'
        for i in re.findall(charc, tmpname):
            tmpname = tmpname.replace(i, '_')
        return tmpname

    def set_identifier(self, identifier_str):
        self.json_temp["identifier"] = identifier_str

    def set_description(self, description_str):
        self.json_temp["description"] = description_str

    def set_conditionsOfAccess(self, conditionsOfAccess_str):
        self.json_temp["conditionsOfAccess"] = conditionsOfAccess_str

    def set_sameAs(self, sameAs_str):
        self.json_temp["sameAs"] = sameAs_str

    def set_additionalType(self, additionalType_str):
        self.json_temp["additionalType"] = additionalType_str

    def set_inLanguage(self, inLanguage_str):
        self.json_temp["inLanguage"] = inLanguage_str

    def set_license(self, license_str):
        self.json_temp["license"] = license_str

    def set_url(self, url_str):
        self.json_temp["url"] = url_str

    def set_comment(self, comment_str):
        self.json_temp["comment"] = comment_str

    def set_author(self, author_str):
        self.json_temp["author"] = author_str

    def set_dateCreated(self, dateCreated_str):
        self.json_temp["dateCreated"] = dateCreated_str

    def set_dateModified(self, dateModified_str):
        self.json_temp["dateModified"] = dateModified_str

    def set_size(self, size_str):
        self.json_temp["size"] = size_str

    def set_totalBytes(self, totalBytes_str):
        self.json_temp["totalBytes"] = totalBytes_str

    def set_contentRating(self, contentRating_str):
        self.json_temp["contentRating"] = contentRating_str

    def set_isReviewed(self, isReviewed_str):
        self.json_temp["isReviewed"] = isReviewed_str

    def set_hasData(self, hasData_str):
        self.json_temp["hasData"] = hasData_str

        
    def set_keywords_ls(self, keywords_str):
        self.json_temp["keywords"].append(keywords_str)
        
    def set_hasPart_ls(self, hasPart_str):
        self.json_temp["hasPart"].append(hasPart_str)
        
    def set_files_ls(self, files_str):
        self.json_temp["files"].append(files_str)

    def set_variableMeasured_ls(self, variableMeasured_str):
        self.json_temp["variableMeasured"].append(variableMeasured_str)   
    
    def set_rating_viewCount(self, viewCount_int):
        self.json_temp["rating"]["viewCount"] = viewCount_int
    def set_rating_voteCount(self, voteCount_int):
        self.json_temp["rating"]["voteCount"] = voteCount_int
    def set_rating_usabilityRating(self, usabilityRating_int):
        self.json_temp["rating"]["usabilityRating"] = usabilityRating_int
    def set_rating_downloadCount(self, downloadCount_int):
        self.json_temp["rating"]["downloadCount"] = downloadCount_int 
        
    def set_sourceOrganization(self, sourceOrg_str, atType_str='CreativeWork'):
        self.json_temp["isBasedOn"]['@type'] = atType_str
        self.json_temp["isBasedOn"]['sourceOrganization'] = sourceOrg_str
        
    def set_maintainer_name(self, maintainer_name_str, maintain_type='Organization'):
        self.json_temp['maintainer']['@type'] = maintain_type
        self.json_temp['maintainer']['name'] = maintainer_name_str
    
    def set_location_name(self, location_name_str, location_type='Organization'):
        self.json_temp['location']['@type'] = location_type
        self.json_temp['location']['name'] = location_name_str

    def set_distributionInfo(self,encoding_form, content_url, distr_type = "DataDownload"):
        self.json_temp['distribution'].append(
                {
                    "@type": distr_type,
                    "encodingFormat":encoding_form,
                    "contentUrl": content_url
                }
            )
    def set_spatialInfo(self, address_str, addressType="PostalAddress", spatialType="Place"):
        self.json_temp['spatialCoverage']['@type'] = spatialType
        self.json_temp['spatialCoverage']['address']['@type'] = addressType
        self.json_temp['spatialCoverage']['address']['streetAddress'] = address_str
    
    def set_creatorInfo(self, employeeName, orgName, email, org_loc, creator_type="Organization", contact_type="ContactPoint"):
        self.json_temp["creator"]['employees']['name'] = employeeName
        self.json_temp["creator"]['name'] = orgName
        self.json_temp["creator"]['contactPoint']['email'] = email
        self.json_temp["creator"]['location'] = org_loc

        self.json_temp["creator"]['@type'] = creator_type
        self.json_temp["creator"]['contactPoint']['@type'] = contact_type
            
    def set_publicationInfo(self, publication_name, propertyID, publicType="publicationEvent", identifier_type="PropertyValue"):
        self.json_temp['publication']['@type'] = publicType
        self.json_temp['publication']['name'] = publication_name
        self.json_temp['publication']['identifier']['@type'] = identifier_type
        self.json_temp['publication']['identifier']['propertyID'].append(propertyID)
    
    def saveJSON2file(self, dirpath):
        json_string = json.dumps(self.json_temp)
        filepath = os.path.join(dirpath, f"{self.get_Name()}.json")
        with open(filepath, 'w') as outf:
            json.dump(json_string, outf)
        print(f'Json file is saved at {filepath}')
        


def extract_1note(idnum):
    # idnum = '128303'
    # idnum = idls[0]
    urlf = 'https://www.openicpsr.org/openicpsr/project/{}/view'
    url = urlf.format(idnum)
    print(url)
    jsonbox = jsonParser()

    r1 = requests.get(url, headers=headers)

    content = r1.text
    soup = BeautifulSoup(content, 'html.parser')
    sectionTag = soup.find("section")

    # for set identifier
    jsonbox.set_identifier(idnum)

    # for set license and url
    tmp = sectionTag.find('div', attrs={'class', 'panel-heading'})
    for i in tmp.children:
        if i.name is None:
            i = i.strip()
            if i != '' and 'no more than two line breaks' not in i and 'if it contains multiples' not in i:
                jsonbox.set_description(i)
                # print(repr(i))
                break

    licenseinfo = sectionTag.find('div', attrs={'id':'projectLicense'}).text
    jsonbox.set_license(licenseinfo)
    jsonbox.set_url(url)

    # for set project name, creator name, creator organization, source organization
    tmp = sectionTag.find('div', attrs={'class': 'page-header'}).find('div', attrs={'class':'row'}).children
    tmp = [ i for i in tmp if i != '\n']
    project_name = tmp[0].text.strip()
    jsonbox.set_Name(project_name)

    tmp = [i for i in tmp[1].children if i != '\n']
    createrHtml = tmp[-2]

    tmp_creator = createrHtml.contents[-1].strip()
    try:
        if ',' in tmp_creator:
            name, organization = tmp_creator.split(',')
        else:
            organization = tmp_creator
            name = None
    except:
        name = tmp_creator.replace('\n', '').replace('\t', '').replace('\r', '')
        organization = None
    jsonbox.set_sourceOrganization(organization)
    jsonbox.set_creatorInfo(name, organization, None, None, creator_type="Organization", contact_type="ContactPoint")

    # for set distribution, date created, date modified
    tmp = sectionTag.find('div', attrs={'class': 'asideColumn'}).contents
    tmp = [i for i in tmp if i != '\n']

    # "distribution": [{"@type": "DataDownload",
    #                 "encodingFormat": "ZIP",
    #                 "contentUrl": "https://www.kaggle.com/davidbnn92/weather-data-for-covid19-data-analysis/download"}
    #                 ]
    try:
        distURL = f"https://www.openicpsr.org/{tmp[0].find('a')['href']}"
    except:
        distURL = None
    jsonbox.set_distributionInfo( 'URL', distURL)

    versionInfo = [i.text for i in tmp[2].find_all('a')]

    def getVersionDetail(versionStr):
        # formate = 'V2 [2021-12-17]'
        return re.findall(r'(V[\d]+) \[(.*)\]', versionStr)[0]
        
    vers, vers_date = getVersionDetail(versionInfo[0])
    jsonbox.set_dateModified(vers_date)

    vers, vers_date = getVersionDetail(versionInfo[-1])
    jsonbox.set_dateCreated(vers_date)


    # For Set Files
    # 2021/02/21: further fix for some pages showing more than 5, catch the tage to adjust the url
    def getAdditionDataInfo(target_url):
        data_r = requests.get(target_url, headers=headers)
        if data_r.status_code == 200:
            soup = BeautifulSoup(data_r.text, 'html.parser')
            sectionTag = soup.find("section")
            tbodyls = list(sectionTag.find('table', attrs={'class': 'table table-striped'}).find('tbody').children)
            tbodyls = [ i for i in tbodyls if i != '\n']
            return tbodyls
        else:
            return []

    def getFileInfo_dict(target_tbody_ls, fileInfoDict):
        # Example of fileInfoDict:
        # fileInfoDict: {".csv":{"count": 2,
        #                        "size": 6405552} }
        unitLs = ['KB', 'MB', 'GB', 'TB']
        for tr in target_tbody_ls:
            td_tags = tr.find_all('td')
            fileName = td_tags[0].text.strip()
            fileType = td_tags[1].text.strip()
            fileSize = td_tags[2].text.strip()

            if fileSize == '' and fileType == '':
                appendUrl = td_tags[0].find('a')['href']
                folderUrl = f'{url.split(idnum)[0]}{idnum}/version/{vers}/view{appendUrl}'
                tmp_tbodyls = getAdditionDataInfo(folderUrl)
                getFileInfo_dict(tmp_tbodyls, fileInfoDict)
            else:
                unit_inlist = False
                for idx in range(len(unitLs)):
                    unit = unitLs[idx]
                    if unit in fileSize:
                        fileSize_bytes = float(fileSize.split(' ')[0]) * 1024**(idx+1)
                        unit_inlist = True
                        break
                if unit_inlist is False and 'bytes' in fileSize:
                    fileSize_bytes = float(fileSize.split(' ')[0])

                if fileType not in fileInfoDict.keys():
                    fileInfoDict[fileType] = {'count': 0, 'size': 0}
                fileInfoDict[fileType]['count'] += 1
                fileInfoDict[fileType]['size'] += fileSize_bytes
        return fileInfoDict

    tbodyls = list(sectionTag.find('table', attrs={'class': 'table table-striped'}).find('tbody').children)
    tbodyls = [ i for i in tbodyls if i != '\n']
    fileDict = {}
    fileDict = getFileInfo_dict(tbodyls, fileDict)

    totalBytes = 0
    for fileType in fileDict.keys():
        jsonbox.set_files_ls({"name": fileType, "count": fileDict[fileType]['count'], "size": fileDict[fileType]['size']})
        totalBytes += fileDict[fileType]['size']

    def getCorrectUnit4file(fileBytes):
        unitLs = ['B', 'KB', 'MB', 'GB', 'TB']
        def getCount(filesz, count):
            if filesz//1024**count > 0:
                count += 1
                count = getCount(filesz, count)
            else:
                count -= 1
            return count
        
        times = getCount(fileBytes, 1)
        return f'{fileBytes/1024**times:.1f} {unitLs[times]}'

    jsonbox.set_size(getCorrectUnit4file(totalBytes))
    jsonbox.set_totalBytes(totalBytes)

    return jsonbox


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Dnt": "1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", 
}


def main():
    rooturl = 'https://www.openicpsr.org/openicpsr/search/studies?start=0&ARCHIVE=openicpsr&sort=score%20desc%2CDATEUPDATED%20desc&rows=163&q=%22coronavirus%22%20OR%20tag%3A%22covid%2019%22%20OR%20%22coronavirus%22%20OR%20%22covid-19%22%20OR%20%22sars-cov-2%22'
    r = requests.get(rooturl, headers=headers)

    content = r.text
    manualTarget = ''
    # get target dataset id list
    idls = re.findall(r'"ID":([\d]+)', content)
    idls = idls[65:]
    totalNum = len(idls)
    for idx in range(len(idls)):
        idnum = idls[idx]
        if idnum != manualTarget and manualTarget != '':
            continue
        print(f'Start working on idnum: {idnum} ({idx+1} / {totalNum})')
        jsonObj = extract_1note(idnum)

        save_dir = os.path.join('.', 'json_file')
        if os.path.isdir(save_dir) is False:
            os.mkdir(save_dir)

        jsonObj.saveJSON2file(save_dir)

        if idnum == manualTarget and manualTarget != '':
            break

        sleeptime = randint(10, 15)
        print(f'Sleep for {sleeptime} sec...')
        time.sleep(sleeptime)

        

if __name__ == '__main__':
    main()