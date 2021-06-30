#data types ชนิดข้อมูล
#age = 25   #integer (int) จำนวนเต็มบวก
#weight = 100.5   #float (float) จำนวนทสนิยม
#first_name = 'worrasak'   #string (str) ตัวอักษร
#has_notebook = true,false   #boolean ตัวแปลถูกหรือผิด?


#operrators เครื่องหมาย
x = 12
y = 2 
a1 = x + y #บวก
a2 = x - y #ลบ
a3 = x * y #คูณ
a4 = x / y #หาร
a5 = x % y #หาเศษจากการหาร
a6 = x ** y #เลขยกกำลัง
a7 = x // y #หารตัดเศษ
a8 = (x + 1) * (y - 1) #หาค่าตามลำดับ


x = 8
x += 3 #หาค่าแบบshortcut
x -= 3
x *= 3
x /= 3


x = 10
y = 5
a1 = x > y  #true เครื่องหมายเปรียบเทียบ
a2 = x >= y #true

a3 = x < y #false
a4 = x <= y #false

a5 = x == y #false ตรวจหาว่าตัวแปลมีค่าเท่ากันหรือไม่
a6 = x != y #true เปรียบเทียบตัวแปลว่ามีค่าไม่เท่ากันหรือไม่


p = True
q = False

a1 = p and q #false
a2 = p or q #true
a3 = not p  #false
a4 = not q #true


#conditions ตรวจสอบเงื่อนไข 
score = 82
# if เงื่อนไข: 
# ...คำสังข้างใน
if score >= 80:
    print('Grade 4')
    print('Nice') #สามารถใส่ข้อความเพื่อให้แสดงผลเพิ่มเติมได้

elif #ใช้ตรวจสอบifด้านบน Note:ถ้าข้างบนตรวจสอบผ่านจะไม่ลงมาตรวจสอบelifจ้างล่างต่อ
# elif(elseif) เงื่อนไข: 
#...คำสังข้างใน
#elif มีได้มากกว่าหนึ่งตัว
score = 75
if score >= 80:
        print ('Greade 4')
        print('Nice')
        elif score >= 70
                print('Grade 3')
                print('lol... you suck')
             
score = 84
if score >= 80:
        print ('Greade 4')
        print('Nice')
elif score >= 70
        print('Grade 3')
        print('lol... you suck')
score = 88
if score >= 80:
        print ('Greade 4')
        print('Nice')
        elif score >= 70
           print('Grade 3')
          print('lol... you suck')
        elif score >= 60
                print('Grade 2')
          print('...')
        elif score >= 50
         print('Grade 1')
         print('you so stupid')
              
else   
#ใช้ตรวจสอบifและelifด้านบนและจะไม่สามารถมีอะไรมาต่อท้ายได้อีก
# else:
#... คำสั่งข้างใน
score = 84
if score >= 80:
        print ('Greade 4')
        print('Nice')
        elif score >= 70
         print('Grade 3')
         print('lol... you suck')
score = 88
if score >= 80:
        print ('Greade 4')
        print('Nice')
        elif score >= 70
          print('Grade 3')
          print('lol... you suck')
        elif score >= 60
           print('Grade 2')
           print('...')
        elif score >= 50
          print('Grade 1')
          print('you so stupid')
        else score <=49
            print('Grade 0')
           print('hmm...')
    
    
    
#loops วนลูป เป็นการใช้คำสั่งเพื่อให้ทำงานวนลูปซ้ำเรื่อยๆโดยที่สามารถกำหนดการวนลูปได้
number = 1
double = number * 2
print( = number * 2)

number = 2
double = number * 2
print( = number * 2)

number = 3
double = number * 2
print( = number * 2)
    
for 
# for ตัวแปล in ชุดข้อมูล:
#...คำสั่งด้านใน
for i in range(3): #range จะสร้างลำดับข้อมูลแบบตัวเลขขึ้นมาโดยที่สามารถกำหนดจำนวนได้ Note.ค่าสุดท้ายจะน้อยกว่าลิมิต 
    print(i)

for i in range(1, 3): #range(ค่าเริ่มต้น, ลิมิต) Note.ค่าสุดท้ายจะน้อยกว่าลิมิต
    print(i)
    
for i in range(1, 13):
    double = i * 2 #doubleในที่นี้ใช้ในการหาสมการคูณสอง
    print(double) 
    
#continue ใช้ข้าม loop รอบนั้น Note.ใช้ได้เฉพาะในloopเท่านั้น
for i in range(1, 15):
    if i  % 3 == 0:
        continue
    print(i)
    
#break ใช้ออกจาก loop จะทำให้หยุดการทำงานของ loop นั้นทันที Note.ใช้ได้เฉพาะในloopเท่านั้น
for i in range(1, 15):
    if i  % 3 == 0:
        break
    print(i)
    
    
#functions ใช้ในการรวมชุดคำสั่งไว้ในที่เดียว
 #def ชื่อฟังกืชั่น():
 #...คำสั่งข้างใน
 
 def get_box_area():
         width = 10 
         length = 15
         height = 12
         box_area = width * length * height
         print(box_area)
 
 #perimeter เป็นการกำหนดตัวแปลส่งให้pythornคำนวนเองทั้งหมด
 def ชื่อฟังก์ชั่น(perimeter1, perimeter2, perimeter3):
         ...คำสั่งข้างใน
 def get_box_area (width, length, height):
         box_area = width * length * height
         print(box_area)
         
get_box_area (4, 4, 2)
get_box_area(2, 1, 2)
get_box_area(width=1, length=2, heigth=3)

def get_box_area (width, length, height):
         box_area = width * length * height
         return box_area
box1 = get_box_area (4, 4, 2)
box2 = get_box_area(2, 1, 2)
print(box1)

def get_box_area (width, length, height):
        if width < 0 or length < 0 or height < 0:
                return 0
         box_area = width * length * height
         return box_area
 
modules #แบ่งโค้ดเป็นส่วนย่อยๆ
import shape as s
circle = s.get_circle_area(10)
print(circle)

triangle = s.get_triangle_area(10, 6)
print(triangle)

tkinter #library for build gui