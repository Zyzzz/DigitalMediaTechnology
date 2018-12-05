import pymysql
from Ui.Libraries.Widgets import SubWindows
class savedata():
    db = pymysql.connect("localhost", "root", "1234", "test")
    data=SubWindows.onedectect()

    def yolo(self,db):
        cursor = db.cursor()

        cursor.execute("insert into algorithmtime(algorithm,time) value('YOLO',data[0];")
        cursor.execute("insert into datalist(pictureName,algorithm,objectList) value('cat','YOLO',data[1];")
    def MaskRCNN(self,db):
        cursor = db.cursor()

        cursor.execute("insert into algorithmtime(algorithm,time) value('MaskRCNN',data[2];")
        cursor.execute("insert into datalist(pictureName,algorithm,objectList) value('cat','MaskRCNN',data[3];")
    def SSD(self,db):
        cursor = db.cursor()

        cursor.execute("insert into algorithmtime(algorithm,time) value('SSD',data[4];")
        cursor.execute("insert into datalist(pictureName,algorithm,objectList) value('cat','SSD',data[5];")
    def FasterRCNN(self,db):
        cursor = db.cursor()

        cursor.execute("insert into algorithmtime(algorithm,time) value('FasterRCNN',data[6];")
        cursor.execute("insert into datalist(pictureName,algorithm,objectList) value('cat','FasterRCNN',data[7];")


