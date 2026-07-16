'''
#SINGLE INHERITNCE:
class A:
    def printa(self):
        print("parent class-A")
class B(A):
    def printb(self):
        print("child class-B")
a=A()
a.printa()
b=B()
b.printb()
b.printa()



#HIERAICHAL INHERITANCE
class A:
    def printa(self):
        print("parent class-A")
class B(A):
    def printb(self):
        print("child class-B")
class C(A):
    def printc(self):
        print("parent class-C")
class D(A):
    def printd(self):
        print("child class-D")
b=B()
b.printb()
b.printa()
c=C()
c.printc()
c.printa()
d=D()
d.printd()
d.printa()

#MULTIPLE INHERITANCE
class A:
    def printa(self):
        print("parent class-A")
class B:
    def printb(self):
        print("child class-B")
class C:
    def printc(self):
        print("child class-C")
class D(A,B,C):
    def printd(self):
        print("child class-D")

d=D()
d.printd()
d.printa()
d.printb()
d.printc()


#MULTILEVEL INHERITANCE
class A:
    def printa(self):
        print("parent class-A")
class B(A):
    def printb(self):
        print("child class-B")
class C(B):
    def printc(self):
        print("child class-C")
a=A()
b=B()
c=C()
c.printa()
c.printb()
c.printc()

#HYBRID INHERITANCE
class A:
    def printa(self):
        print("parent class-A")
class B:
    def printb(self):
        print("child class-B")
class C(B,A):
    def printc(self):
        print("child class-C")
class D(C):
    def printd(self):
        print("child class-D")
d=D()
d.printa()
d.printb()
d.printc()
d.printd()

#REAL WORLD EXAMPLES
#single inheritance

class InstagramV1:
    def post(self):
        print("you can uplaoad your posts")
    def reel(self):
        print("you can uplaod your reels")
class InstagramV2(InstagramV1):
    def story(self):
        print("you can upload your stories")
    def live(Self):
        print("you can go for the live")
Geetha=InstagramV1()
print("Geetha-InstagramV1")
Geetha.post()
Geetha.reel()


Nithya=InstagramV2()
print("\nNithya -InstgramV2")
Nithya.post()
Nithya.reel()
Nithya.story()
Nithya.live()


#MULTIPLE INHERITANCE
class InstagramV1:
    def post(self):
        print("you can uplaoad your posts")
    def reel(self):
        print("you can uplaod your reels")
class InstagramV2(InstagramV1):
    def story(self):
        print("you can upload your stories")
    def live(Self):
        print("you can go for the live")
class  InstagramV4:
    def note(self):
        print("you can update your note")
class InstagramV5:
    def instants(self):
        print("you can upload your snaps")
class InstagramV3:
    def crossPlatforms(self):
        print("you can upload your same status on whatsapp status")
        print("you can upload your same status on facebook status")
Geetha=InstagramV1()
print("Geetha-InstagramV1")
Geetha.post()
Geetha.reel()


Nithya=InstagramV2()
print("\nNithya -InstgramV2")
Nithya.post()
Nithya.reel()
Nithya.story()
Nithya.live()

Hema=InstagramV3()
print("Hema-InstagramV3")
Hema.post()
Hema.story()
Hema.live()
Hema.crossPlatforms()


lakshmi=InstagramV4()
print("lakshmi-InstagramV4")
lakshmi.post()
lakshmi.story()
lakshmi.live()
lakshmi.crossPlatforms()
lakshmi.note()

vijaya=InstagramV5()
print("vijaya-InstagramV5")
vijaya.post()
vijaya.story()
vijaya.live()
vijaya.crossPlatforms()
vijaya.intsants()
vijaya.intsants()



class InstagramV1:
    def post(self):
        print("You can upload post")

    def reel(self):
        print("You can upload the reels")
        
class InstagramV2(InstagramV1):
    def story(self):
        print("Upload the story")
    def live(self):
        print("Go to Live")

class Whatsapp:
    def status(self):
        print("Upload the status")

class facebook:
    def fbstory(self):
        print("Upload the story")

class InstagramV3(InstagramV2,Whatsapp,facebook):
    def crossplatforms(self):
        print("Upload the same story on your Whatsapp")
        print("Upload the same story on your facebook")

Geetha=InstagramV1()
print("Geetha= Instagram V1")
Geetha.post()
Geetha.reel()

print()

Nithya=InstagramV2()
print("Nithya= Instagram V2")
Nithya.post()
Nithya.reel()
Nithya.live()

print()

Hema=InstagramV3()
print("Hema= Instagram V3")
Hema.post()
Hema.reel()
Hema.story()
Hema.live()      
Hema.crossplatforms()




class A:
    def print(self):
        print("class -A")
class B(A):
    def print(self):
        super().print()
        print("class -B")
b=B()
b.print()



class A:
    def print(self):
        print("class -A")
class B:
    def print(self):
        print("class -B")
class C(A,B):
    def print(self):
        A.print(self)
        B.print(self)
        print("class -C")
c=C()
c.print()

'''

