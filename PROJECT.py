import mysql.connector
obj=mysql.connector.connect(host="localhost",database="student",user="root",password="19feb001")
c=obj.cursor()
n=eval(input("enter no of customers"))
for i in range(n):
    
    q1="INSERT INTO CUSTOMER VALUES(%s,%s,%s,%s,%s,%s,%s)"
    ccode=eval(input("ccode"))
    cname=input("cname")
    phone=input("number")
    dop=input("date of purchase")
    fname=input("flower name")
    q=eval(input("quantity bought"))
    p=eval(input("SP"))
    
    t=(ccode,cname,phone,dop,fname,q,p)
    c.execute(q1,t)
    obj.commit()

    


print("1.To display the names of flowers in high demand")
print("2.To display the names of flowers in low demand")
print("3.discount for bulk purchase")
print("4.refund")
print("5.add new stock")
print("6.display remaining stock ")
print("7.display bill")
while True:   
    x=eval(input("choice"))
    if x==1:
        c.execute("SELECT FLOWERNAME FROM CUSTOMER WHERE QTY=(SELECT MAX(QTY) FROM CUSTOMER)")
        l=c.fetchall()
        for i in l:
            m=i[0]
        print("The flowers in high demand are:",m)
        print("\n")
    elif x==2:
        c.execute("SELECT FLOWERNAME FROM CUSTOMER WHERE QTY=(SELECT MIN(QTY) FROM CUSTOMER)")
        l=c.fetchall()
        for i in l:
            m=i[0]
        print("The flowers in low demand are:",m)
        print("\n")
            
        
    elif x==3:
        c.execute("UPDATE CUSTOMER SET TOTAL=TOTAL-(0.1*TOTAL) WHERE QTY>100")
        obj.commit()
        print("The customers purchasing more than 100 flowers have been given a 10% discount")
        print("\n")
    elif x==4:
        q1="UPDATE CUSTOMER SET TOTAL=TOTAL-%s WHERE PHONENO=%s"
        m=eval(input("cash to be refunded"))
        
        p=eval(input("phoneno"))
        
        t=(m,p)
        c.execute(q1,t)
        obj.commit()
        print(m,"is refunded to the customer")
       
        
        q2="UPDATE STOCK SET STOCK=STOCK-%s WHERE FNAME=%s"
        s=eval(input("stock returned"))
        f=input("name of flower")
        t=(s,f)
        c.execute(q2,t)
        print("\n")
    elif x==5:
        q="UPDATE STOCK SET STOCK=STOCK+%s WHERE FNAME=%s"
        a=eval(input("enter stock to be added"))
        b=input("enter name of flower")
        t=(a,b)
        c.execute(q,t)
        obj.commit()
        print(a,"is added to the stock for the flower",b)
        print("\n")
    elif x==6:
        c.execute("SELECT STOCK,FNAME FROM STOCK GROUP BY FNAME ")
        print("STOCK :")
        l=c.fetchall()
        for i in l:
            print(i[0],i[1])
        print("\n")
            
    elif x==7:
        p=eval(input("Enter phone no"))
        t=p,
        q="SELECT * FROM CUSTOMER WHERE PHONENO=%s"
        c.execute(q,t)
        print("The customer's bill is as follows:")
        l=c.fetchall()
        for i in l:
            print("BILL OF CUSTOMER")
            print("\n")
            print("Customer code:",i[0])
            print("Name of customer:",i[1])
            print("Date of purchase:",i[3])
            print("Name of flower purchased:",i[4])
            print("Quantity purchased:",i[5])
            print("Total price paid by the customer:",i[6])
            
    
        
        
    
        

