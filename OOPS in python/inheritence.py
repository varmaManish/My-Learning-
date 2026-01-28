
'''class collge:
    mam="supriya" # this is the property of class
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def greet(self):
        print("my mam is"+self.name)
object=collge("Hacking",89)
print(object.name,object.mam ,object.greet())
'''
'''


class Music:
    def __init__(self):
        self.songs=[]
    def add_Song(self,songs):
        self.songs.append(songs)
        print(f"song add '{songs}'")
    def rmv_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
        print(f"removed'{song}")
    def shw_song(self):
        for song in self.songs:
            print(f"songs name:{song}")

player=Music()
player.add_Song("first song")
player.add_Song("second song")
player.add_Song("third song")
player.add_Song("forth song")
player.rmv_song("first song")
player.shw_song()'''


class person:
    def __init__(self,fname,lname,college):
        self.fname=fname
        self.lname=lname
        self.college=college
    def second(self):
         print(f"this is from parent class:{self.fname}")
class student(person):
     def __init__(self,fname,lname,college,id):
        self.college=college
        self.id=id
        super().__init__(fname,lname,college)
     def first(self):
            print(f"first name'{self.fname}'")
            print(f" this is from student{self.college} and id:{self.id}")
y=student("maanish","varma","sdsm",4455)
x=person("maanish","varma","sdsm")
y.first()
x.second()


class Test:
     def __init__(self,x):
         self.x=x
a=Test(10)
print(a.x)