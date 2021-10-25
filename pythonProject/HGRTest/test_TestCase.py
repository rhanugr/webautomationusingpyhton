import json
import requests

from HGRTest.DataDrivenTest import Library


def test_add_multiple_students():
    api_url = 'http://www.thetestingworldapi.com/api/studentsDetails'
    f = open('C:/Hanamanta_Data/Datadriven/student.json')
    json_request = json.loads(f.read())
    obj = Library.Lib(FilePath='C:/Hanamanta_Data/testdata.xlsx', SheetName="Sheet1")
    row1 = obj.fetch_row_count()
    col1 = obj.fetch_column_count()
    keyList = obj.fecth_key_name()

    for i in range(2,row1+1):
        udpated = obj.update_requets_with_data(i,json_request,keyList)
        response = requests.post(api_url,udpated)
        print(response)
        # print(response.text)



