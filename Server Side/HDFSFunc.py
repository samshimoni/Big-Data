from snakebite.client import Client

client = Client('127.0.0.1', 9000)  # port for comunicating with hadoop

def listFiles(path):  # for example ['/']
    for x in client.ls(path):
        print(x)

def makeFolders(listOfDirs):
    for p in client.mkdir(listOfDirs, create_parent=True):  # for example['/rami_levi', '/yenot_bitan']
        print(p)

def deleteFile(path):  # ['/050519_rl.csv']
    for p in client.delete(path, recurse=True):
        print(p)

def DownloadFile(path_from, path_where_to):  # ['/030719_yb.csv'], '/home/sams/Desktop'
    for f in client.copyToLocal(path_from, path_where_to):
        print(f)

def showText(path):  # ['/030719_yb.csv']
    for l in client.text(path):
        print(l)

def saveFile(path):
    file = client.text(path)
    return file

#file = saveFile(['/030719_yb.csv'])
#for i in file:
    #print(i)

listFiles(['/'])


#lines = sc.textFile("127.0.0.1:9000")

#fileExample =  SparkContext.textFile('hdfs:://127.0.0.0.1:9000/020719_yb.csv','file')
