# coding: utf-8
import os
import json

# 定义数据类
class Data():
    def __init__(self,title,url,type):
        self.title = title
        self.url = url
        self.type = type

class DataEncoder(json.JSONEncoder): 
  def default(self, obj): 
    if isinstance(obj, Data): 
      return {
          'title':obj.title,
          'url':obj.url,
          'type':obj.type,
      } 
    return json.JSONEncoder.default(self, obj)        


dataList = []

def getBlog():
    dirName = "markdown\\"
    fileList = os.listdir(dirName)
    for fileName in fileList:
        filePath = os.path.join('%s\%s' % (dirName, fileName))
        oldFile = open(filePath, 'r', encoding='UTF-8')
        fileContent = oldFile.read()+str('''
                        \n
                        <link rel="stylesheet" href="/static/markdeep/journal.css?">
                        <style class="fallback">body{visibility:hidden}</style>
                        <script>markdeepOptions={tocStyle:'long'};</script>
                        <script src="/static/markdeep/markdeep.min.js?" charset="utf-8"></script>
                        ''')         
        newFilePath =  os.path.join('%s\%s' % ("blog\\", fileName+".html"))
        newFile = open(newFilePath, 'w', encoding='UTF-8')
        newFile.write(fileContent)               
        dataList.append(Data(fileName,newFilePath,"blog"))
        oldFile.close()
        newFile.close()
        

def getData():
    dirName = "data\\"
    fileList = os.listdir(dirName)
    for fileName in fileList:
        filePath = os.path.join('%s\%s' % (dirName, fileName))  
        dataList.append(Data(fileName,filePath,"data")) 

def getPhoto():
    dirName = "photo\\"
    fileList = os.listdir(dirName)
    for fileName in fileList:
        filePath = os.path.join('%s\%s' % (dirName, fileName))  
        dataList.append(Data(fileName,filePath,"photo"))                                          


if __name__ == "__main__":
    getBlog()
    getData()
    getPhoto()
#  生成json配置文件
    configFilePath =  os.path.join('%s' % ("config.json"))
    configFile = open(configFilePath, 'w', encoding='UTF-8')
    configFile.write(json.dumps(dataList, cls=DataEncoder))   
    configFile.close() 