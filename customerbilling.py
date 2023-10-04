import math
from tkinter import*
import math,random,os
from tkinter import messagebox
from turtle import right
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,bg=bg_color,relief=GROOVE,font=("Times new roman",30,"bold"),pady=2).pack(fill=X)
        #variable__________
        #------Groccery-------
        self.Bread=IntVar()
        self.Meat=IntVar()
        self.Oils=IntVar()
        self.Rice=IntVar()
        self.Frozen=IntVar()
        self.Spice=IntVar()

        #-------Cosmetics______________
        self.face=IntVar()
        self.cream=IntVar()
        self.wax=IntVar()
        self.deo=IntVar()
        self.shave=IntVar()
        self.serum=IntVar()

        #-------------Clothes------------
        self.Jeans=IntVar()
        self.Shirt=IntVar()
        self.Jacket=IntVar()
        self.Tshirt=IntVar()
        self.Belt=IntVar()
        self.Socks=IntVar()

        #total product price & tax variable--------
        self.groccery_price=StringVar()
        self.cosmetic_price=StringVar()
        self.clothes_price=StringVar()

        self.groccery_tax=StringVar()
        self.cosmetic_tax=StringVar()
        self.clothes_tax=StringVar()

        #customer-------
        self.c_name=StringVar()
        self.c_phn=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
  
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman ",18,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="CustomerName",bg=bg_color,fg="white",font=("ariel",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="CustomerPhone",bg=bg_color,fg="white",font=("ariel",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="CustomerBill",bg=bg_color,fg="white",font=("ariel",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        
        #_____Groccery frame_____#
        F2=LabelFrame(self.root,bd=12,relief=GROOVE,text="Groccery",font=("times new roman ",18,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)
        Bread_lbl=Label(F2,text="Bakery/Bread",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bread_txt=Entry(F2,width=10,textvariable=self.Bread,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
         
        Meat_lbl=Label(F2,text="Meat/Seafood",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Meat_txt=Entry(F2,width=10,textvariable=self.Meat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Oils_lbl=Label(F2,text="Oils/Dairy",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Oils_txt=Entry(F2,width=10,textvariable=self.Oils,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Rice_lbl=Label(F2,text="Rice/Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Rice_txt=Entry(F2,width=10,textvariable=self.Rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Froozen_lbl=Label(F2,text="Froozen",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Froozen_txt=Entry(F2,width=10,textvariable=self.Frozen,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
         
        Spices_lbl=Label(F2,text="Spices",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Spices_txt=Entry(F2,width=10,textvariable=self.Spice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
         #Cosmetic frame_____#

        F3=LabelFrame(self.root,bd=12,relief=GROOVE,text="Cosmetics",font=("times new roman ",18,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        face_lbl=Label(F3,text="Facewash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        face_txt=Entry(F3,width=10,textvariable=self.face,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
         
        cream_lbl=Label(F3,text="cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cream_txt=Entry(F3,width=10,textvariable=self.cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        wax_lbl=Label(F3,text="wax",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        wax_txt=Entry(F3,width=10,textvariable=self.wax,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Deo_lbl=Label(F3,text="Deo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Deo_txt=Entry(F3,width=10,textvariable=self.deo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Shave_lbl=Label(F3,text="Shave",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Shave_txt=Entry(F3,width=10,textvariable=self.shave,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
         
        Serum_lbl=Label(F3,text="Serum",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Serum_txt=Entry(F3,width=10,textvariable=self.serum,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
       #clothes frame___
        F4=LabelFrame(self.root,bd=12,relief=GROOVE,text="Clothes",font=("times new roman ",18,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        Jeans_lbl=Label(F4,text="Jeans",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Jeans_txt=Entry(F4,width=10,textvariable=self.Jeans,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
         
        Shirt_lbl=Label(F4,text="DenimShirt",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Shirt_txt=Entry(F4,width=10,textvariable=self.Shirt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Jacket_lbl=Label(F4,text="Jacket",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        jacket_txt=Entry(F4,width=10,textvariable=self.Jacket,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        TShirt_lbl=Label(F4,text="TShirt",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Tshirt_txt=Entry(F4,width=10,textvariable=self.Tshirt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Belt_lbl=Label(F4,text="Belt",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        belt_txt=Entry(F4,width=10,textvariable=self.Belt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
         
        Socks_lbl=Label(F4,text="Socks",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Socks_txt=Entry(F4,width=10,textvariable=self.Socks,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        # Bill area_________
        F5=Frame(self.root,bd=12,relief=GROOVE)
        F5.place(x=1010,y=180,width=340,height=380)
        Bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #Button frame________
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BillMenu",font=("times new roman ",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        M1=Label(F6,text="Total Groccery Price",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        M1=Entry(F6, width=18,textvariable=self.groccery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        M2=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        M2=Entry(F6, width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        M3=Label(F6,text="Total Clothes Price",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        M3=Entry(F6, width=18,textvariable=self.clothes_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        C1=Label(F6,text=" Groccery Tax",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        C1=Entry(F6, width=18,textvariable=self.groccery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        C2=Label(F6,text=" Cosmetics Tax",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        C2=Entry(F6, width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        

        C3=Label(F6,text=" Clothes Tax",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        C3=Entry(F6, width=18,textvariable=self.clothes_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)


        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetBlue",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="yellow",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="Green",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="Red",fg="white",bd=2,pady=15,width=10,font=("arial 15 bold")).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_Bill()

    def total(self):


        self.g_B_p=self.Bread.get()*40
        self.g_M_p=self.Meat.get()*600
        self.g_O_p=self.Oils.get()*430
        self.g_R_p=self.Rice.get()*1330
        self.g_F_p=self.Frozen.get()*300
        self.g_S_p=self.Spice.get()*230
        
                                     
        self.total_groccery_price=float(
                                    self.g_B_p+
                                    self.g_M_p+
                                    self.g_O_p+
                                    self.g_R_p+
                                    self.g_F_p+
                                    self.g_S_p
                                    )
        
                                 
        
                                    
        
        self.groccery_price.set("Rs"+str(self.total_groccery_price))
        self.g_tax=round((self.total_groccery_price*0.05),2)
        self.groccery_tax.set("Rs."+str(self.g_tax))

        self.c_f_p=self.face.get()*199
        self.c_c_p=self.cream.get()*260
        self.c_w_p=self.wax.get()*50
        self.c_d_p=self.deo.get()*300
        self.c_s_p=self.shave.get()*350
        self.c_se_p=self.serum.get()*230

        
        self.total_Cosmetic_price=float(
                                    self.c_f_p+
                                    self.c_c_p+
                                    self.c_w_p+
                                    self.c_d_p+
                                    self.c_s_p+
                                    self.c_se_p
                                     )
        
        self.cosmetic_price.set("Rs"+str(self.total_Cosmetic_price))
        self.c_tax=round((self.total_Cosmetic_price*0.1),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))


        self.C_j_p=self.Jeans.get()*599
        self.C_s_p=self.Shirt.get()*460
        self.C_J_p=self.Jacket.get()*1500
        self.C_t_p=self.Tshirt.get()*400
        self.C_b_p=self.Belt.get()*350
        self.C_so_p=self.Socks.get()*230

        self.total_clothes_price=float(
                                    self.C_j_p+
                                    self.C_s_p+
                                    self.C_J_p+
                                    self.C_t_p+
                                    self.C_b_p+
                                    self.C_so_p
                                     )
        
        self.clothes_price.set("Rs"+str(self.total_clothes_price))
        self.C_tax=round((self.total_clothes_price*0.05),2)
        self.clothes_tax.set("Rs."+str(self.C_tax))
        self.Total_bill=float(self.total_groccery_price+
                              self.total_Cosmetic_price+
                              self.total_clothes_price+
                              self.g_tax+
                              self.c_tax+
                              self.C_tax)
    
    def welcome_Bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWELCOME WEBFACTORY RETAIL\n")
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number:{self.c_phn.get()}")
        self.txtarea.insert(END,f"\n===================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\tPrice")
        self.txtarea.insert(END,f"\n===================================")
    




    def bill_area(self):
        if self.c_name.get()=="" or self.c_phn.get()=="":
            messagebox.showerror("Error","Customers Details are must")
        elif self.groccery_price.get()=="Rs. 0.0" and self.cosmetic_price.get()=="Rs. 0.0" and self.clothes_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcome_Bill()
        #cosmetics
        if self.Bread.get()!=0:
            self.txtarea.insert(END,f"\n Bread\t\t{self.Bread.get()}\t\t{self.g_B_p}")
        

        if self.Meat.get()!=0:
            self.txtarea.insert(END,f"\n Meat\t\t{self.Meat.get()}\t\t{self.g_M_p}")

        if self.Oils.get()!=0:
            self.txtarea.insert(END,f"\n Oils\t\t{self.Oils.get()}\t\t{self.g_O_p}")

        if self.Rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t{self.Rice.get()}\t\t{self.g_R_p}")

        if self.Frozen.get()!=0:
            self.txtarea.insert(END,f"\n Frozen\t\t{self.Frozen.get()}\t\t{self.g_F_p}")

        if self.Spice.get()!=0:
            self.txtarea.insert(END,f"\n Spice\t\t{self.Spice.get()}\t\t{self.g_S_p}")


        #cosmetics

        if self.face.get()!=0:
            self.txtarea.insert(END,f"\n face\t\t{self.face.get()}\t\t{self.c_f_p}")
        

        if self.cream.get()!=0:
            self.txtarea.insert(END,f"\n cream\t\t{self.cream.get()}\t\t{self.c_c_p}")

        if self.wax.get()!=0:
            self.txtarea.insert(END,f"\n wax\t\t{self.wax.get()}\t\t{self.c_w_p}")

        if self.deo.get()!=0:
            self.txtarea.insert(END,f"\n deo \t\t{self.deo.get()}\t\t{self.c_d_p}")

        if self.shave.get()!=0:
            self.txtarea.insert(END,f"\n shave\t\t{self.shave.get()}\t\t{self.c_s_p}")

        if self.serum.get()!=0:
            self.txtarea.insert(END,f"\n serum\t\t{self.serum.get()}\t\t{self.c_se_p}")

        #clothes

        if self.Jeans.get()!=0:
            self.txtarea.insert(END,f"\n Jeans\t\t{self.Bread.get()}\t\t{self.C_j_p}")
        

        if self.Shirt.get()!=0:
            self.txtarea.insert(END,f"\n Shirt\t\t{self.Shirt.get()}\t\t{self.C_s_p}")

        if self.Jacket.get()!=0:
            self.txtarea.insert(END,f"\n jacket\t\t{self.Jacket.get()}\t\t{self.C_J_p}")

        if self.Tshirt.get()!=0:
            self.txtarea.insert(END,f"\n Tshirt\t\t{self.Tshirt.get()}\t\t{self.C_t_p}")

        if self.Belt.get()!=0:
            self.txtarea.insert(END,f"\n Belt\t\t{self.Belt.get()}\t\t{self.C_b_p}")

        if self.Socks.get()!=0:
            self.txtarea.insert(END,f"\n Socks\t\t{self.Socks.get()}\t\t{self.C_so_p}")

        self.txtarea.insert(END,f"\n------------------------------------")
        if self.groccery_tax.get()!="0.0":
           self.txtarea.insert(END,f"\n Groccery Tax\t\t\t{self.groccery_tax.get()}")

        if self.cosmetic_tax.get()!="0.0":
           self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

        if self.clothes_tax.get()!="0.0":
           self.txtarea.insert(END,f"\n Clothes Tax\t\t\t{self.clothes_tax.get()}")
        
        
        
        self.txtarea.insert(END,f"\n Total Bill: \t\t\t Rs.{str(self.Total_bill)}")
        self.txtarea.insert(END,f"\n------------------------------------")
        self.save_bill()





        pass
        




         
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
         
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END) 
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()   
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfully")      
        else:
            return
    
    def clear_data(self):
        
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        
              
            
            
            
                #------Groccery-------
        self.Bread.set(0)
        self.Meat.set(0)
        self.Oils.set(0)
        self.Rice.set(0)
        self.Frozen.set(0)
        self.Spice.set(0)

        #-------Cosmetics______________
        self.face.set(0)
        self.cream.set(0)
        self.wax.set(0)
        self.deo.set(0)
        self.shave.set(0)
        self.serum.set(0)

        #-------------Clothes------------
        self.Jeans.set(0)
        self.Shirt.set(0)
        self.Jacket.set(0)
        self.Tshirt.set(0)
        self.Belt.set(0)
        self.Socks.set(0)

        #total product price & tax variable--------
        self.groccery_price.set("")
        self.cosmetic_price.set("")
        self.clothes_price.set("")

        self.groccery_tax.set("")
        self.cosmetic_tax.set("")
        self.clothes_tax.set("")

        #customer-------
        self.c_name.set(0)
        self.c_phn.set(0)
        
        self.bill_no.set(0)
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.welcome_Bill()
    
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to Exit?")
        if op>0:
            self.root.destroy()    

root=Tk()
obj= Bill_App(root)
root.mainloop()