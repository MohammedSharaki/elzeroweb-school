print("information")
#Operator[+/-/*/=/%]
#[=]Equal 
#[!=]noEqual 
#
#
#
#
#الملاحظه فوق الكلمه 
#لو عاوز تبحث وتعرف فيه كام قيمه في المتغير
#print(len)
print("_______________typs_______________")
print(type(10)) #ارقام عاديه او ارقام صحيحه 
print(type(100.9)) #رقم عشري 
print(type("hollo world")) #النص اللي بنتعامل معاه 
print(type([1,2,3,])) #نوع من انواع الليست 
print(type({"one": 1,"two": 2,"three": 3}))#وصف الكلمه
print((2==2))#لمعرفه هل المعادله صحيحه
print("_______________________words__________________________")
name ="mohammed sharaki" #single word =normal
myname="mohammed sharaki" #two word =camel case
my_name="mohammed sharaki" #two word =snake_caes
print(name) #single
print(my_name) #snak_ qutes
print(myname) #camel qutes
print("_________________back___slash____________________________")
#\n new line   ======بيعمل سطر جديد في قلب الكود
print("name is \n mohammed")
#علشان تعمل علامه الباك سلاش في الرن تعمل اتنين باك سلاش 
print ("i love backshash\\")
#لو انت عاوز تقول كلمه جوا علامه تعمل ايه 
print('ilove backslash \'teast\'')
#لوعاوز تجيب مكان حروف بدل اماكن 
print('mohammed\rmostafa')
#تعمل 4 مساطر 
print("mohammed\tmostafa")
#__________________concatenation__________________
print("__________concatenation__________")
#ربط بين سلسلتين 
a = '''mostafa
mohammed "asslam" 'amira'
sharaki'''

b ="""c
a
d"""    
#لو عاوز تحط كلمه جوا علامه بدون اي خاجه /لو انت بتعمل بدبل كود اعكس /والعكس صحيح
print(a+" "+b)    
print("_________________index_________slicing____________________________")
#[index]هو البحث في الكلمه عن مكان حرف
#[slicing]هو قطع الجمله من بدايه الي نهايه ولزم يكون عندي بدايه ونهايه
m ="mohammed sharaki "
#لمعرفه اول حرف 
print(m[0])
#لمعرفه مكان الحرف بس من ورا 
print(m[-6])
#هيقطع الكلمه 
print(m[7:16])
#هيبدا من الاول الي للسبعه 
print(m[:7])
#هيبدا من خمسه الي النهايه 
print(m[5:])
#هيجيبها كلها 
print(m[:])
#___________stips_______________
print("___________stips_______________")
#هيجيب كل حرفين مع بعض يعني هيسيب حرف وياخد حرف
print(m[::2])
m= "my name is mohammed"

#rstrip()بيشيل المسافات من علي اليمين 
r="     my name is mohammed        "
#strip ()بيشيل المسافات من علي اليمنين والشمال
print(r.strip())
#rstrip()بيشيل المسافات من علي اليمين 
print(r.rstrip())
#lstrip()بيشيل المسافات من الشمال فقط
print(r.lstrip())

#__________________________نفس اللي فوق__________________________)

r="#@#@#@#@#@#@#@#my name is mohammed#@#@#@#@#@#@#"
#strip ()بيشيل المسافات من علي اليمنين والشمال
print(r.strip("#@"))
#rstrip()بيشيل المسافات من علي اليمين 
print(r.rstrip("#@"))
#lstrip()بيشيل المسافات من الشمال فقط
print(r.lstrip("#@"))
print("_____________________-methods-string-__________________")
#title __يخلي وال الكيمه كابيتل وبعد الارقام برضو 
#capitaleize __يخلي اول الكلمات كابيتل 
#zfill
c,v,b,f ="1","22","444","7777"
print(c.zfill(4))
print(b.zfill(4))
print(v.zfill(4))  
print(f.zfill(4))
print("________________________________________")
#['i', 'love', 'python', 'and', 'php']هتيقي كده 
m="i love python and php"
print(m.split())
m="i-love-python-and-php-and-sql"
print(m.split("-"))
#اخر اتنين  بتعمل كده "-"
m="i-love-python-and-php-and-sql"
print(m.rsplit("-",2))
#center#
e="mohammed"
#هنا هيحط مسافات قبل وبعد الكلمه لحد ماتوصل الي 10 احرف 
print(e.center(10)) 
#هنا هيحط علامه الدولار قبل وبعدالكلمه لحد ماتوصل الي 10 ارقام 
print(e.center(10 , "$" )) #
#هنا هيحط علامه النجمه لحد ماتوصل الي 10 ارقام 
print(e.center(10 , "*" )) 
print ("_________________________________________________________________________________________________________________________________")
#count 
print (e.count("m"))#بيعد من اول الجمله الي الاخر وممكن يبقي فيه بدايه ونهايه زي الايند دكسي

#swapcase
#بيحول الكبير الي الصغير 
g = "I Love Python"
h = "i lOVE pYTHON"
i = "I Love Python"
#startwith
#هل بيبداالحرف الاول ب كذا
print(i.startswith("I"))
print(i.startswith("S"))
#دي هتبده من رقم 7
print(i.startswith("P", 7, 12))
j = "I Love Python"
#هل بينتهي الحرف الاخير بكذا 
print(j.endswith("n"))
print(j.endswith("S"))
#ده هيبدا من رقم 2
print(j.endswith("e", 2, 6))

print(g.swapcase())
print(h.swapcase())

m="my name is mohammed"
print(m.index("i")) 
#لمعرفه اين يقع الحرث رقم 3
print(m[0])
#هيبحث علي الحرف رقم صفر في الجمله
#print(m.index("i",1,4))
print(m.find("d"))
#دي للبحث برضو
print(m.find("d",1,20))
print(m.find("d",5,20))
print("_________________________________________----------------------")
#rjust
m="mohammed"
print(m.rjust(10))
#بيعمل مسافات من علي لاليمين 
#الكلام يبقي من علي اليمين والعلامات من علي الشمال 
#ljust
print(m.ljust(10,"$"))
#بيعمل علامه الدولار من علي الشمال 
#الكلام يبقي علي الشمال والعلامات من علي اليمين 
e = """First Line
Second Line
Third Line"""
print (e.splitlines())
#حولها الي قائمه 
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#expadtaps
#تقدر تتحكم بالبعد بين التابات 
e="my \tname \tis \tmohammed \tand \tlove \tpyghon"
print (e.expandtabs(8))
#is title
O="I Love Python And 3g"
e="I Love Python And 3G"
print (e.istitle())
print (O.istitle())
#بيسال وبيقول هل هو مابيتل
m="y "
print(m.isspace())
#بيال عن هل هي فيه مسافات في قلب الكلمه 
print("_________________string formatting_______o_____l____d__")
name = "mohammed" 
age =15
rank = 10
print("my name is "+name)
#print("i have a "+age)#خطا هنا لا مفيش استرنج مع رقم 
#print("my rank a"+rank) #نفس الحكايه 
print("my name is %s"%name)
print ("my name is %s and my age is %s"%(name,age))
print("my naem is %s and my age is %d and my rank is %f"%(name, age, rank))
# %S =>string
# %D =>number
# %f =>float
name = "mohamed"
l = "python"
y =10
print("my name is %s and iam %s devolper with %d years exp"%(name ,l, y))
number = 15
print("my number is %d" % number)
print("my number is %.5f"% number)
mylongstring = "hello peaples of elzero web scool"
print(" %.6s"%mylongstring)#دي علشان تطلع كل الاعداد اللي انا عاوزها
print("/_____________string formatting___n___e____W_____\ ")
print("my name is {:s} and my age is {:d} and my rank is {:f}".format(name,age,rank))
# {:s} =>string
# {:d} =>number
# {:f} =>float
print("my name is {:s} and iam {:s} devolper with {:d} years exp".format(name ,l, y))
print("my number is {:d}" .format(number))
print("my number is {:.4f}".format(number))
nmoney= 309303000
print("my money in bank is  {:,d}".format(nmoney) )
a, b, c = "one","two","three"
print("hello {1} {2} {0}".format(a ,b ,c))
print("hello {} {} {}".format(a ,b ,c))
#ده لو انت عاوز تغير الاماكن للكلمات 
x ,y ,z=10 ,30 ,94
print("hello {1:d} {2:d} {0:.2f} ".format(x,y,z))
#formate in verison 3.6
name="mohammed"
age=35
print(f"my name is : {name}and my age {age}")
#java script
print("__________________numbers__________________")
#int
print(type(100))
print(type(100))
print(type(1))
print("_______________________________________________________________________")
#float
print(type(10.4))
print(type(5.5))
#complex
complex=100+10j
print(type(complex))
print("my complex number {}".format(complex.real))
print("my number complex is {}".format(complex.imag))
#int to float to complex
#complex cant change any thing
print(100)
print("hsfgfjkgdfkjgkjfhgk fhgkdfhgklj")
print(float(100))

print("____________lists____________")
# ____________lists____________
# [1]تقدر تحط بيانات  مع اي حاجه  
# [2]العناصر ملهاش ستايل معين 
# [3]مرنه يعني تقدر تضيف او تحذف او تعدل
# [4]العناصر مرتبه وتقدر توصل اليها عن طريق index
# [5] diffrint deta typs
mylist=["one","two","1","true","100.4"]
print(mylist)
print(mylist[1])#acces
print(mylist[0:3])#سلايس
print(mylist[::1])
print(mylist[::2])
#سهله انك تعدل عليها مش زي tubles
#edit
mylist[1]=2
print(mylist)
mylist[0:3]=["a","c","d","r"]
print(mylist)
print("_____________________-methods-lists-__________________")
#_____________________-methods-lists-__________________
#append
#ممكن تضيف اي حاجه مش لازم حهاجه محدده

myfamily=["amira","mostafa"]
print(myfamily)
mybrother=["omar","mohammed","aasem","aslam"]
myfamily.append(mybrother)
print(myfamily[1])
print(myfamily[2][3])
#extend
#نفس اللي فوقها بس لو بتضيف ليست بتبقي كامله
mohammed = [1,2,3,4]
aasem = ["a","b","c"]
alsam=["two","one"]
mohammed.extend(aasem)
mohammed.extend(alsam)
print(mohammed)
#ramove
#تح1ف الكلمه الكرره مره واحده فقط او اي كلمه 
x=["mohammed","aasem","mohammed","aasem","mohammed","aasem","mohammed"]
x.remove("mohammed")
x.remove("aasem")
x.remove("mohammed")
print(x)
#sort
#لترتيب الالرقام من الاصغر الي لااكبر 
#مينفعش تحط رقم مع استؤنج
y=[10,4,-9,-62,100,190]
print(y)
y.sort()
print(y)
#sort(reverse=True)
#علشان يرتبها عادي من لالصغير الي الكبر 
#sort(reverse=false)
#علشان ترتبها من الكبير الي الصغير
#reverse
#بيعكس بس مش بيععمل حاجه تاني الاول يبقس الاخير والاخير الاول 
l=[1,2,3,4,5,"mohammed"]
l.reverse()
print(l)
#عسكت الكلمات من اليميمن الي الشمال


#clear
z=[1,2,3,4]
z.clear()
print(z)



#copy
m=[1,2,3,4,5,6,7]
b=m.copy()
print(b)
#كوبي بتاخد نسخه من الليست اللي فوق 
# بس ملهاش دعوه باللي بعدها 

#count
#لمعرفه كم مره العددد اتكرر كام مره في الليست
r=[1,9,3,2,0,8,7,2,3,1,9,7,9,5,7,9,1,2,6,7,2,2,9,0,2,1,9,0,2,4,9,8,5,8,4,3,5,7,2,3,8,4,6,9,0,5,3]
print(r.count(1))
print("__________________________________tuble__________________________________")
#[1]ممكن تحط قوسين 
#[2]وممكن لا
#[3]عناصر مؤتبه
#[4]index
#[5]متقدرش تعدل فيها 
#[6]تقدر تحط اي قيمه عادي 

tuple1="mohamemd","aasem"
tuple2=("aasem",10)
print(type(tuple1))
print(type(tuple2))
tuple3=("1,2,3,4,5")
#tuple3[0]="6" #متقدرش تعدل عليها 
print("___________________________________________________________________________________________")
print("__________________________________  tuple__________________________________")
#concatenation
n=[1,2,3,4]
n1=[6,7,8,9]
c = n+n1
#list,string,tuple,rebeat
mystrig="mohammed"
mylist=[1,2]
mytuple="mohammed","ahmed"
print(mystrig*2)
print(mytuple*2)
print(mylist *2)
print("__________________________________ methods tuple__________________________________")
#methods>= count()
mohamemd=(1,2,3,4,4)
print(mohammed.count(8))
# ___________________________
# methodes >= index
print(mohamemd[0])









print('___________________ set___________________')
#set
#{}بتتفتح كده \
#كمش مرتبه خالص
#مفيش فيها index
#مفيش فيها سليس
#ممكن تخزن فيها [numbers string  tuple ] #not list dic 
#بتحذف اي حاج مكرره 
mysetone={"mohamemd"}
print(mysetone)
mysettwo={"mohamemd",100}
print(mysettwo)
print("___________________ set methods ___________________")
#clear()
a={1,2,3,4,5,6}
a.clear()
print(a)
#union
print(a.union(b))#تقدر تحط اكتر من حاجه 
a={1,2,3,4,5,6}
#add
a.add(9) 
print(a)
#copy()
r={1,2,3,4,5}
f=r.copy() #shall oand copy 
#يعني مش هتعرف تعمل اي حاجه 
print(r)
print(f)
r.add(44)
print(r)
print(f)

#remove
r.remove(5)
print(r)#حذفت الخمسه بس لو اديتها رقم مش موجود هتعمل ايرور
#r.remove(10)
print(r)
#discard
h={1,2,3,4}
h.discard(1)
h.discard(10)
print(h)
#pop[دي بطلع قيمه عشوائيه ]
h={True,"a",1,10}
#h.pop()[كده هتطلع قيمتين]
print(h.pop())#كه هتطلع قيمه واحده 


#.update()دي بتعمل تحديث للعنصر مع حاجه تانيه وبتشيل المككرر
j={1234}
k={"mohamemd","aaesm"}
k.update([1,2,3,4])
k.update(j)
print(k)
print("="*50)
#difference[بيحط المكرر ويحطه في القنصل]
a={1,2,3,4}
b={1,2,"mohamemd","omar"}
print(a)
print(a.difference(b))#a-b
print(a)
print("="*10)
#الفرق بينdifference//difference_updateانها بتعمل ابديت  و 
print(a)
a.difference_update(b)
print(a)
print("="*50)
#intersection[ده بيحط الارقام المككره القنصل]
e={1,2,3,4,7}
r={6,7,"mohammed","aassem"}
print(e)
print(r)
print(r.intersection_update(e))
print(r)
#symmetric_difference[دي بتعمل لاعناصر المش مكرره]
i={1,2,3,4,5,"X"}
j={"osama","zero",1,2,4}
print(i.symmetric_difference_update(j))
print(i)
#issuperset[دي بتسال هل كل اللي في الول في التاني ]
r={1,2,3,4,5,6,7}
t={1,4,5,7}
print(r.issuperset(t))
#issubset
a={1,2,3,4}
m={1,2,3,4,5,6}
print(a.issubset(m))
print("="*100)
#diffrunt of issuperset issubset  
#issuperset start from back to face 
#issubset start from face to back
r={1,2,3,4,5,6,7}
t={1,4,5,7}
print(r.issuperset(t))
a={1,2,3,4}
m={1,2,3,4,5,6}
print(a.issubset(m))

#dictionary
# [1] cerly bracts {}
# [2] iteams are contain key : valu
# [3] ky need immutable valu (string,number,bool,tuple )dont allowed list
# [4] unique
# [5] dosent have order and dont can to do index
# [6] index by callled key







#dictionary
user={
    "name"   : "mohammed",
    "age"    :  15,
    "contry" : "egypt",
    "brother": ["omar","mohamemd","aasem"]

}
#لو انت عاوز تبحث علي كلمه مثلا هتبقي كده 
print(user)
print(user["brother"])
print(user.get("brother"))

#two dimensional  dictianary

lang={
    "front end":{
        "html" : "hyper text markup languge",
        "css"  : " style sheet "
    },
    "back end":{
        "name":"python"
    }
}
print(lang)#دي الكل 
print(lang["front end"])# دي الالفرونت اند بس
print(lang["back end"]["name"]) # دي الباك اند والجواها الاسم 
print(len(lang))#للبحث هيا فيها كام قيمه 
print(len(lang["back end"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allfarmework ={
    "one":frameworkOne,
    "two":frameworkTwo,
    "three":frameworkThree
}
print(allfarmework)


print("----------methods--------Dictionary-----------------")
#clear()
user={
    "name":"mohamemd"
}
user.clear()
print(user)



#update
member={
    "name":"mohammed"
}

print(member)
member["age"]=15#دي اضاهف عنصر برضو
print(member)
member.update({"con":"egypt"}) #طبعا دي باضافه العناصر بالميثودث

#copy

main={
    "name":"mohamemd"
}
print("="*100)
b=main.copy()
print(b)
main.update({"age":"15"})
print(main)
print(b)

print("="*100)

#setdefult
#دي بتضيف عنصر علي العناصر
mohammed={
    "name":"mohammed"
}
print(mohamemd)
print(mohammed.setdefault("age",15))#د يضافت عنصر علي اللي فوق بيس لو حطيط ايحاجه غير اللي ات عاوزهزا مش متغيرها
print(mohamemd)

#popitem
lesson={
    "name":"mohammed",
    "age":15
}

print(lesson)
lesson.update({"schools":"height"})
print(lesson)
print(lesson.popitem())

print("="*100)

#.fromkey()دي بتركب الاتنين علي بعض 
l=("my skils","my name","my learning")
p="front end","mohamemd"
print(dict.fromkeys(l,p))


print("="*20,"boolan operaor","="*20)
#========boolan =======
#and 
# or 
# not بتقلب الصح غلط
#
#age=int(input("age : "))
contrey = "egypt"
rank = 10
#print(age>=21 and contrey=="egypt"and rank>5.5)

#age >16 العمر اكبر من 16
#print(age>=21 )

#print("="*20,"# -- Assignment Operators --","="*20)
#=================# -- Assignment Operators --=========
# =
# +=
# -=
# *=
# **=
# /=
# %=
# //=


fa=4
la=20
'''
de=fa+la
print(de)
fa = fa+la
print(fa)
'''
#fa += la
#print(fa)
fa/=la
print(fa)


#comparison - operator

# [=]
# [!=]
# [>] اكبر من 
# [<] اصفر من 
# [>=]
# [<=]
#[=]
print(100==100)
print(100==200)
print(100==100.00)
#[!=]
print("0"*19)
print(100!=100)
print(100!=200)
print(100!=100.00)
#[>]
print("0"*19)
print(100>100)
print(100>200)
print(100>100.00)
print(100>39)

print("0"*19) 


#=========type conversion========
#str()
o=1
print(o)
print(type(str(o)))
print(" == type == conversion == ")
#tuble()
p="mohammed","aasem"
k={"mohamemd",111}
h={"mohammed":"aasem","omar":"mmoo"}
l="mohammed"
#print(p)
#print(type (p))
print( (tuple(p)))
print( (tuple(k)))
print(  (tuple(h)))
print(  (tuple(l)))
#ونفس الحاجات دي بتطبق غلي كل حاجه

#د يكل حاجه ماعدا القاموس
# str[مش بيقبل انها تتحول الي قاموس ]
# tuple[]
# 
# #

p=(("a",1),("b",2),("c",3))
k={"mohamemd",111}
h=[["mohammed","aasem"],["omar","mmoo"]]#لازم تحط ليست جةوا ليست 
l="mohammed"
#print(p)
print( (dict(p))) # to change (("a":1),("b":2),("c":3)) change to dict
#print(  (dict(k)))#مش بتتحول خلاص
print( (dict(h)))
print(dict(l))


