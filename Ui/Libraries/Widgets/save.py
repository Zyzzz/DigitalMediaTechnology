import pymysql

class save():
    db = pymysql.connect("localhost", "root", "123456", "mysql")


    def alt(self,al,ti):

        cursor = self.db.cursor()
        cursor.execute("insert into algorithmtime(algorithm,time) values('%s','%f')" % (al, ti))
        print(13432524354352)
        self.db.commit()

    def dl(self,pic,al,ob):
        cursor =self.db.cursor()

        # cursor.execute("insert into datalist(pictureName,algorithm,objectList) values (pic,al,ob);")
        cursor.execute("insert into datalist(pictureName,algorithm,objectList) values ('%s','%s','%s')" % (pic, al, ob))
        print(1343252435345656354352)
        self.db.commit()
    def close(self):
        self.db.close()



