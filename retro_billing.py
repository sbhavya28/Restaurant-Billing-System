from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing System")
        title=Label(self.root,text="OG Restro",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.corn=IntVar()
        self.noodles=IntVar()
        self.roll=IntVar()
        self.chilli=IntVar()
        self.sandwitch=IntVar()
        self.manchurian=IntVar()
        self.dragon=IntVar()
        self.kulche=IntVar()
        self.shahi=IntVar()
        self.pulao=IntVar()
        self.naan=IntVar()
        self.malaayi=IntVar()
        self.dal=IntVar()
        self.kadhi=IntVar()
        self.ice=IntVar()
        self.berry=IntVar()
        self.muffin=IntVar()
        self.pastries=IntVar()
        self.pudding=IntVar()
        self.pie=IntVar()
        self.waffles=IntVar()
        self.total_sta=StringVar()
        self.total_main=StringVar()
        self.total_dess=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()

        #================================================GUI Design=============================================================
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)
        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
        
        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)
        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
        
        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)
        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================starters label frame=================================================================
        starters=LabelFrame(self.root,text="Starters",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        starters.place(x=5,y=180,height=380,width=325)
        
        item1=Label(starters,text="Crispy Corn()",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.corn).grid(row=0,column=1,padx=10)

        item2=Label(starters,text="Hakka Noodles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=10)

        item3=Label(starters,text="Spring Roll",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.roll).grid(row=2,column=1,padx=10)

        item4=Label(starters,text="Chilli Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.chilli).grid(row=3,column=1,padx=10)

        item5=Label(starters,text="Sandwitch",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.sandwitch).grid(row=4,column=1,padx=10)

        item6=Label(starters,text="Manchuria",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.manchurian).grid(row=5,column=1,padx=10)

        item7=Label(starters,text="Draogn Vegetables",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(starters,borderwidth=2,width=15,textvariable=self.dragon).grid(row=6,column=1,padx=10)
        #===================================Maincourse label frame=====================================================================================
        maincourse=LabelFrame(self.root,text="Maincourse",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        maincourse.place(x=340,y=180,height=380,width=325)

        item8=Label(maincourse,text="Chhole Kulche",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.kulche).grid(row=0,column=1,padx=10)

        item9=Label(maincourse,text="Shaahi Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.shahi).grid(row=1,column=1,padx=10)

        item10=Label(maincourse,text="Pulaao",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.pulao).grid(row=2,column=1,padx=10)

        item11=Label(maincourse,text="Butter naan",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.naan).grid(row=3,column=1,padx=10)

        item12=Label(maincourse,text="Malaayi Roti and Chilly Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.malaayi).grid(row=4,column=1,padx=10)

        item13=Label(maincourse,text="Daal Makhani",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=10)

        item14=Label(maincourse,text="Fried rice and Kadhi",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(maincourse,borderwidth=2,width=15,textvariable=self.kadhi).grid(row=6,column=1,padx=10)
        #========================================Dessert frame label===============================================================================
        dessert=LabelFrame(self.root,text="Dessert",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        dessert.place(x=677,y=180,height=380,width=325)

        item15=Label(dessert,text="Ice-cream",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.ice).grid(row=0,column=1,padx=10)

        item16=Label(dessert,text="Berry Cheesecake",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.berry).grid(row=1,column=1,padx=10)

        item17=Label(dessert,text="Chocolate Muffins",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.muffin).grid(row=2,column=1,padx=10)

        item18=Label(dessert,text="Pastries",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.pastries).grid(row=3,column=1,padx=10)

        item19=Label(dessert,text="Pudding",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.pudding).grid(row=4,column=1,padx=10)

        item20=Label(dessert,text="Apple Pie",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.pie).grid(row=5,column=1,padx=10)

        item21=Label(dessert,text="Waffles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(dessert,borderwidth=2,width=15,textvariable=self.waffles).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)
        
        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)
        
        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)
        
        total_starters=Label(billing_menu,text="Total starters Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_starters_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sta).grid(row=0,column=1,padx=10,pady=7)
        
        total_maincourse=Label(billing_menu,text="Total maincourse Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_maincourse_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_main).grid(row=1,column=1,padx=10,pady=7)

        
        total_dessert=Label(billing_menu,text="Total Beauty & dessert Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_dessert_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_dess).grid(row=2,column=1,padx=10,pady=7)

        tax_starters=Label(billing_menu,text="starters Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_starters_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
        
        tax_maincourse=Label(billing_menu,text="maincourse Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_maincourse_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)

        
        tax_dessert=Label(billing_menu,text="Beauty & dessert Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_dessert_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)
        
        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)

#=====================================================================Functionning===========================================================================
def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
   
   #calculating total starters' price
    self.co=self.corn.get()*80
    self.no=self.noodles.get()*90
    self.ro=self.roll.get()*120
    self.ch=self.chilli.get()*110
    self.sa=self.sandwitch.get()*100
    self.ma=self.manchurian.get()*89
    self.dr=self.dragon.get()*100
    total_starters_price=(
                self.co+
                self.no+
                self.ro+
                self.ch+
                self.sa+
                self.ma+
                self.dr)          
    self.total_sta.set(str(total_starters_price)+" Rs")
    self.a.set(str(round(total_starters_price*0.05,3))+" Rs")
    
    #calculating total maincourse price
    self.ku=self.kulche.get()*42
    self.sh=self.shahi.get()*120
    self.pu=self.pulao.get()*113
    self.na=self.naan.get()*160
    self.mal=self.malaayi.get()*55
    self.da=self.dal.get()*480
    self.ka=self.kadhi.get()*76
    total_maincourse_price=(
        self.ku+
        self.sh+
        self.pu+
        self.na+
        self.mal+
        self.da+
        self.ka)
    self.total_main.set(str(total_maincourse_price)+" Rs")
    self.b.set(str(round(total_maincourse_price*0.01,3))+" Rs")

    #calculating total dessert price
    self.ic=self.ice.get()*30
    self.be=self.berry.get()*180
    self.pa=self.pastries.get()*130
    self.mu=self.muffin.get()*500
    self.pu=self.pudding.get()*100
    self.pi=self.pie.get()*100
    self.wa=self.waffles.get()*20
    
    total_dessert_price=(
        self.ic+
        self.be+
        self.pa+
        self.mu+
        self.pu+
        self.pi+
        self.wa)
    self.total_dess.set(str(total_dessert_price)+" Rs")
    self.c.set(str(round(total_dessert_price*0.10,3))+" Rs")
   
   #calculating total price
    self.total_all_bill=(total_starters_price+
                total_maincourse_price+
                total_dessert_price+
                (round(total_maincourse_price*0.01,3))+
                (round(total_dessert_price*0.10,3))+
                (round(total_starters_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)


#==================================================================Content of Billing Area=========================================================
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO OG RESTRO\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.corn.get()!=0:
        self.txtarea.insert(END,f"Corn\t\t {self.corn.get()}\t{self.co}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.roll.get()!=0:
        self.txtarea.insert(END,f"SpringRoll\t\t {self.roll.get()}\t{self.ro}\n")
    if self.chilli.get()!=0:
        self.txtarea.insert(END,f"ChilliPaneer\t\t {self.chilli.get()}\t{self.ch}\n")
    if self.sandwitch.get()!=0:
        self.txtarea.insert(END,f"Sandwitchs\t\t {self.sandwitch.get()}\t{self.sa}\n")
    if self.manchurian.get()!=0:
        self.txtarea.insert(END,f"Manchurian\t\t {self.manchurian.get()}\t{self.ma}\n")
    if self.dragon.get()!=0:
        self.txtarea.insert(END,f"dragon\t\t {self.dragon.get()}\t{self.dr}\n")
    if self.kulche.get()!=0:
        self.txtarea.insert(END,f"Kulche\t\t {self.kulche.get()}\t{self.ku}\n")
    if self.shahi.get()!=0:
        self.txtarea.insert(END,f"ShahiPaneer\t\t {self.shahi.get()}\t{self.sh}\n")
    if self.pulao.get()!=0:
        self.txtarea.insert(END,f"Pulaao\t\t {self.pulao.get()}\t{self.pu}\n")
    if self.naan.get()!=0:
        self.txtarea.insert(END,f"Naan\t\t {self.naan.get()}\t{self.na}\n")
    if self.malaayi.get()!=0:
        self.txtarea.insert(END,f"MalaayiRoti\t\t {self.malaayi.get()}\t{self.mal}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.kadhi.get()!=0:
        self.txtarea.insert(END,f"Kadhi\t\t {self.kadhi.get()}\t{self.ka}\n")
    if self.ice.get()!=0:
        self.txtarea.insert(END,f"IceCream\t\t {self.ice.get()}\t{self.ic}\n")
    if self.berry.get()!=0:
        self.txtarea.insert(END,f"Cheesecake\t\t {self.berry.get()}\t{self.be}\n")
    if self.pastries.get()!=0:
        self.txtarea.insert(END,f"Pastries\t\t {self.pastries.get()}\t{self.pa}\n")
    if self.muffin.get()!=0:
        self.txtarea.insert(END,f"Muffin\t\t {self.muffin.get()}\t{self.mu}\n")
    if self.pudding.get()!=0:
        self.txtarea.insert(END,f"Pudding\t\t {self.pudding.get()}\t{self.pu}\n")
    if self.pie.get()!=0:
        self.txtarea.insert(END,f"Pie\t\t {self.pie.get()}\t{self.pi}\n")
    if self.waffles.get()!=0:
        self.txtarea.insert(END,f"Waffles\t\t {self.waffles.get()}\t{self.wa}\n")
        
    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total starters Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Maincourse Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Dessert Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")




#==================================================Defining Functionality of Clear Button======================================================================
def clear(self):
        self.txtarea.delete(1.0,END)
        self.corn.set(0)
        self.noodles.set(0)
        self.roll.set(0)
        self.chilli.set(0)
        self.sandwitch.set(0)
        self.manchurian.set(0)
        self.dragon.set(0)
        self.kulche.set(0)
        self.shahi.set(0)
        self.pulao.set(0)
        self.naan.set(0)
        self.malaayi.set(0)
        self.dal.set(0)
        self.kadhi.set(0)
        self.ice.set(0)
        self.berry.set(0)
        self.muffin.set(0)
        self.pastries.set(0)
        self.pudding.set(0)
        self.pie.set(0)
        self.waffles.set(0)
        self.total_sta.set(0)
        self.total_main.set(0)
        self.total_dess.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()
            
root=Tk()         #root being the object of Tk class
obj=Bill_App(root)
root.mainloop()    #helps in viewing the window
    
