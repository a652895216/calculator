# tkinter - 计算器
from  tkinter import *
import time
huaban = Tk()   #root是面板大小
huaban.geometry('250x380')    #!!注意这是 埃克斯x 相当于乘号
huaban.title('辉哥专用')
frame_show=Frame(width=300,height=150,bg='#dddddd')   #这是框架大小
frame_show.pack()

sv = StringVar()  #显示部分
sv.set('0')    #初始化显示一个0
show_label= Label(frame_show,textvariable=sv,bg='yellow',width=13,height=2,font=('宋体',20,'bold'),justify=LEFT,anchor='w')
#anchor 锚点 代表右边
show_label.pack(padx=5,pady=5) #pad是灰色框的厚度
# 第二步
def delete():
    global num1,num2
    if sv.get() == '0':
        sv.set('0')
    else:
        m=len(sv.get())
        mm = len(num1)
        if operator==False and m>1:
            shanchu = sv.get()
            shanchu = shanchu[0:m-1]
            sv.set(shanchu)
            num1 = num1[0:m-1]
        elif operator==True and m>1:
            shanchu = sv.get()
            shanchu = shanchu[0:m - 1]
            sv.set(shanchu)
            num2 = shanchu[mm+1:m]
        else:
            sv.set('0')
            num1=''
            num2=''
def clear():
    global num1,num2,operator
    print('清除')
    sv.set('0')
    num1=''
    num2=''
    operator=False
def fun():
    print('次方')
def sqr2():
    print('根号')

frame_bord = Frame(width=400, height=350,bg='white')
frame_bord.pack(padx=5,pady=5)
#command:当按钮被按下时所调用的一个函数或方法。所回调的可以是一个函数、方法或别的可调用的Python对象。
button_del = Button(frame_bord, text='DEL',width = 5 ,height =2,command=delete)
button_del.grid(row = 0, column=0)
button_clear = Button(frame_bord, text='AC',width = 5 ,height =2,command=clear)
button_clear.grid(row = 0, column=1)
button_fun = Button(frame_bord, text='^n',width = 5 ,height =2,command=fun)
button_fun.grid(row = 0, column=2)
button_ce = Button(frame_bord, text='开根号',width = 5 ,height =2,command=sqr2)
button_ce.grid(row = 0, column=3)

num1 =''
num2 =''
operator= False
def aa(num):
    num=str(num)
    global num1,num2,n
    if  operator == False:
        num1 = num1 + num
        sv.set(num1)
    else:
        num2 = num2 + num
        sv.set(num1+fff+num2)

# 数字按钮建
button_1 = Button(frame_bord,text='1',width = 5 ,height =2,command=lambda :aa(1))
button_1.grid(row=1,column=0)
button_2 = Button(frame_bord,text='2',width = 5 ,height =2,command=lambda :aa(2))
button_2.grid(row=1,column=1)
button_3 = Button(frame_bord,text='3',width = 5 ,height =2,command=lambda :aa(3))
button_3.grid(row=1,column=2)
button_4 = Button(frame_bord,text='4',width = 5 ,height =2,command=lambda :aa(4))
button_4.grid(row=2,column=0)
button_5 = Button(frame_bord,text='5',width = 5 ,height =2,command=lambda :aa(5))
button_5.grid(row=2,column=1)
button_6 = Button(frame_bord,text='6',width = 5 ,height =2,command=lambda :aa(6))
button_6.grid(row=2,column=2)
button_7 = Button(frame_bord,text='7',width = 5 ,height =2,command=lambda :aa(7))
button_7.grid(row=3,column=0)
button_8 = Button(frame_bord,text='8',width = 5 ,height =2,command=lambda :aa(8))
button_8.grid(row=3,column=1)
button_9 = Button(frame_bord,text='9',width = 5 ,height =2,command=lambda :aa(9))
button_9.grid(row=3,column=2)
button_0 = Button(frame_bord,text='0',width = 5 ,height =2,command=lambda :aa(0))
button_0.grid(row=4,column=1)
button_dian = Button(frame_bord,text='.',width = 5 ,height =2,command=lambda :aa('.'))
button_dian.grid(row=4,column=0)

def operation(op):
    global operator,fff,n
    operator = True
    fff=op  # fff为全局符号
    if op in ['+','-','x','/']:
        n = num1 + fff
        sv.set(num1+op)
def equal():
    global num1, num2, operator,ans
    if fff == '+':
        sv.set(float(num1) + float(num2))
        ans = float(num1) + float(num2)
    if fff == '-':
        sv.set(float(num1) - float(num2))
        ans = float(num1) - float(num2)
    if fff == 'x':
        sv.set(float(num1)*float(num2))
        ans = float(num1) * float(num2)
    if fff == '/':
        sv.set(float(num1)/float(num2))
        ans = float(num1) / float(num2)
    num1 =''
    num2 =''
    operator= False
def Ans():
    global num1,num2
    if operator == False:
        num1 = str(ans)
        sv.set('Ans')
    else:
        num2 = str(ans)
        sv.set(num1+fff+'Ans')

button_jia = Button(frame_bord,text='+',width = 5 ,height =2,command=lambda :operation('+'))
button_jia.grid(row=1,column=3)
button_jian = Button(frame_bord,text='-',width = 5 ,height =2,command=lambda :operation('-'))
button_jian.grid(row=2,column=3)
button_chen = Button(frame_bord,text='x',width = 5 ,height =2,command=lambda :operation('x'))
button_chen.grid(row=3,column=3)
button_jian = Button(frame_bord,text='/',width = 5 ,height =2,command=lambda :operation('/'))
button_jian.grid(row=4,column=3)
button_deng = Button(frame_bord,text='=',width = 5 ,height =2,command=lambda :equal())
button_deng.grid(row=5,column=3)
button_ans = Button(frame_bord,text='Ans',width = 5 ,height =2,command=lambda :Ans())
button_ans.grid(row=4,column=2)


huaban.mainloop()