from pymongo import MongoClient


def con_db():
    conn = MongoClient('1707ff9f.all123.net', 27017)
    db = conn.mydb1
    return db
def save_m4a(s1,s2,s3):
    my_set = con_db().my_set
    users={"name":str(s1),"m4a":str(s2),"number":str(s3)}
    my_set.insert(users)
def delet_set():
    db = con_db()
    db.my_set.remove()

if __name__ == "__main__":
    my_set = con_db().my_set
    #save_m4a(1,2,3)
    db = con_db()
    #delet_set()
    num = 1
    for i in my_set.find({"number":"1"}):
        print(i)
        print num
        num = num + 1