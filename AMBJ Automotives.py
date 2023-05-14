import mysql.connector as mycon
import datetime
day=datetime.date.today()
time=datetime.datetime.now()
cn = mycon.connect(host='localhost',user='root',password="kelco1941",database="AMBJ_Automotives")
cur = cn.cursor()
print("                                               AMBJ AUTOMOTIVES & SERVICE PARTS PROVIDER")
print(day.day,"/",day.month,"/",day.year,"  ",time.hour,":",time.minute)
print("1.Car Records")
print("2.Spare Parts")
print("3.Customer Details")

choice=int(input("Enter the table you want to edit:"))

if choice == 1 :
    pwd='7000RPM'
    password=input("Enter Password: ")
    def showAll():
        global cn
        global cur
    
        try:
            query="select * from Cars"
            cur.execute(query)
            results = cur.fetchall()
            print("--------------------------------------------------------------------------------------------")
            print('%5s'%"Car_No",'%20s'%'Manufacturing company ','%12s'%'Car','%18s'%'Model','%20s'%'Year of manufacturing','%7s'%'stock')
            print("--------------------------------------------------------------------------------------------")
            count=0
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3],'%20s'%row[4],'%10s'%row[5])

                count+=1
            print("-----------------------------------TOTAL RECORD : ",count,"---------------------------------------")
        except:
            print("Error!!!!!")

        
    def addCar():
              
        global cn,cur
        print("-----------------------------------ADD NEW CAR RECORD-----------------------------------")
        cno = int(input("Enter car number: "))
        mc = input("Enter Manufacturing company: ")
        c = input("Enter car: ")
        m = input("Enter model: ")
        yom = input("Enter year of manufacturing: ")
        stock = int(input("Enter stock available: "))
        query="insert into Cars values("+str(cno)+",'"+mc+"','"+c+"',"+m+","+yom+","+str(stock)+")"
        cur.execute(query)
        cn.commit()
        print("\n -- RECORD ADDED SUCCESSFULLY!!!!! --")

    
    def searchCar():
        global cn,cur
        print("-----------------------------------SEARCH CAR RECORD-----------------------------------")
        cno = int(input("Enter car record number to search :"))
        query="select * from Cars where Car_No="+str(cno)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- SORRY! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("--------------------------------------------------------------------------------------------")
            print('%5s'%"Car_No",'%20s'%'Manufacturing company ','%12s'%'Car','%18s'%'Model','%20s'%'Year of manufacturing','%7s'%'stock')
            print("--------------------------------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3],'%20s'%row[4],'%10s'%row[5])
        print("-"*92)



    def editCar():
        global cn,cur
        print("-----------------------------------EDIT CAR RECORDS-----------------------------------")
        cno = int(input("Enter Car Record no. to edit :"))
        query="select * from Cars where Car_No="+str(cno)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- CHECK THE INPUTTED CAR NUMBER!!!!!! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("--------------------------------------------------------------------------------------------")
            print('%5s'%"Car_No",'%20s'%'Manufacturing company ','%12s'%'Car','%18s'%'Model','%20s'%'Year of manufacturing','%7s'%'stock')
            print("--------------------------------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3],'%20s'%row[4],'%10s'%row[5])
        print("-"*92)
        ans = input("Are you sure to update ? (y/n)")
        if ans=="y" or ans=="Y":
            d = input("Enter new car name to update (enter old value if not to update) :")
            s = input("Enter new model to update (enter old value if not to update) :")
            query="update Cars set Car ='"+d+"',Model="+str(s) + " where Car_No="+str(cno)
            cur.execute(query)
            cn.commit()
            print("\n-- RECORD UPDATED  --")
                
    def delCar():
        global cn,cur
        print("-----------------------------------DELETE CAR RECORD-----------------------------------")
        en = int(input("Enter Car number to delete :"))
        query="select * from Cars where Car_No="+str(en)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- SORRY! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("--------------------------------------------------------------------------------------------")
            print('%5s'%"Car_No",'%20s'%'Manufacturing company ','%12s'%'Car','%18s'%'Model','%20s'%'Year of manufacturing','%7s'%'stock')
            print("--------------------------------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3],'%20s'%row[4],'%10s'%row[5])
        print("-"*92)
        ans = input("Are you sure to delete ? (y/n)")
        if ans=="y" or ans=="Y":
            query="delete from Cars where Car_No="+str(en)
            cur.execute(query)
            cn.commit()
            print("\n-- RECORD DELETED  --")
    def clear():
        for i in range(1,50):
            print()
    while True:
        print("1. SHOW CAR RECORD ")
        print("2. ADD NEW CAR RECORD ")
        print("3. SEARCH CAR RECORD ")
        print("4. EDIT CAR RECORD ")
        print("5. DELETE CAR RECORD ")
        print("0. EXIT")
        ans = int(input("Enter your choice :"))
        if ans==1:
             showAll()
        elif ans==2:
             addCar()
        elif ans==3:
             searchCar()
        elif ans==4:
             editCar()
        elif ans==5:
             delCar()
        elif ans==0:
             print("lIVE THE SPEED!!!!!")
             cn.close()
             break

            

elif choice == 2:
    pwd='KUNAI'
    password=input("Enter Password: ")
    def showAll():
               
               
    
        global cn
        global cur
    
        try:
            query="select * from Spare_Parts"
            cur.execute(query)
            results = cur.fetchall()
            print("------------------------------------------------------------------")
            print('%5s'%"Part_No",'%15s'%'Part ','%31s'%'Stock')
            print("------------------------------------------------------------------")
            count=0
            for row in results:
                print('%5s'%row[0],'%25s'%row[1],'%20s'%row[2])

                count+=1
            print("------------------------TOTAL RECORD : ",count,"------------------------")
        except:
            print("Error!!!!!")

        
    def addpart():
              
        global cn,cur
        print("-------------------------ADD NEW PARTS RECORD-----------------------")
        pno = int(input("Enter Part number: "))
        mc = input("Enter name of the part: ")
        stock = int(input("Enter stock available: "))
        query="insert into Spare_Parts values("+str(pno)+",'"+mc+"',"+str(stock)+")"
        cur.execute(query)
        cn.commit()
        print("\n -- RECORD ADDED SUCCESSFULLY!!!!! --")

    
    def searchpart():
        global cn,cur
        print("---------------------------SEARCH PARTS RECORD-----------------------")
        pno = int(input("Enter car record number to search :"))
        query="select * from Spare_Parts where Part_No="+str(pno)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- SORRY! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("------------------------------------------------------------------")
            print('%5s'%"Part_No",'%15s'%'Part ','%31s'%'Stock')
            print("------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%25s'%row[1],'%20s'%row[2])
        print("-"*92)



    def editpart():
        global cn,cur
        print("-----------------------EDIT SPARE PARTS RECORDS------------------------")
        pno = int(input("Enter Part no. to edit :"))
        query="select * from Spare_Parts where Part_No="+str(pno)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- CHECK THE INPUTTED PART NUMBER!!!!!! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("------------------------------------------------------------------")
            print('%5s'%"Part_No",'%15s'%'Part ','%31s'%'Stock')
            print("------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%25s'%row[1],'%20s'%row[2])
        print("-"*92)
        ans = input("Are you sure to update ? (y/n)")
        if ans=="y" or ans=="Y":
            d = input("Enter new Part name to update (enter old value if not to update) :")
            s = int(input("Enter stock available to update (enter old value if not to update) :"))
            query="update Spare_Parts set Part ='"+d+"',Stock="+str(s) + " where Part_No="+str(pno)
            cur.execute(query)
            cn.commit()
            print("\n-- RECORD UPDATED  --")
                
    def delpart():
        global cn,cur
        print("--------------------DELETE SPARE PARTS RECORD---------------------")
        en = int(input("Enter Part number to delete :"))
        query="select * from Spare_parts where Part_No="+str(en)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- SORRY! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("------------------------------------------------------------------")
            print('%5s'%"Part_No",'%15s'%'Part ','%31s'%'Stock')
            print("------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%25s'%row[1],'%20s'%row[2])
        print("-"*92)
        ans = input("Are you sure to delete ? (y/n)")
        if ans=="y" or ans=="Y":
            query="delete from Spare_Parts where Part_No="+str(en)
            cur.execute(query)
            cn.commit()
            print("\n-- RECORD DELETED  --")
    def clear():
        for i in range(1,50):
            print()
    while True:
        print("1. SHOW SPARE PARTS RECORD ")
        print("2. ADD NEW SPARE PART RECORD ")
        print("3. SEARCH PARTS RECORD ")
        print("4. EDIT SPARE PARTS RECORD ")
        print("5. DELETE SPARE PART RECORD ")
        print("0. EXIT")
        ans = int(input("Enter your choice :"))
        if ans==1:
            showAll()
        elif ans==2:
            addpart()
        elif ans==3:
            searchpart()
        elif ans==4:
            editpart()
        elif ans==5:
            delpart()
        elif ans==0:
            print("lIVE THE SPEED!!!!!")
            cn.close()
            break


elif choice == 3:
    def showAll():
               
               
    
        global cn
        global cur
    
        try:
            query="select * from Customer_Details"
            cur.execute(query)
            results = cur.fetchall()
            print("-----------------------------------------------------------------------")
            print('%5s'%"S_No",'%13s'%'Name','%18s'%'Purchase','%25s'%'Total_Cost(In K)')
            print("-----------------------------------------------------------------------")
            count=0
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3])

                count+=1
            print("---------------------------TOTAL RECORD : ",count,"-------------------------")
        except:
            print("Error!!!!!")

        
    def addCd():
              
        global cn,cur
        print("-----------------------------------ADD NEW CUSTOMER RECORD----------------------------")
        sno = int(input("Enter serial number: "))
        mc = input("Enter name of the customer: ")
        purchase=input("Enter purchase details: ")
        tc=int(input("Enter Total cost of the purchase:"))
        query="insert into Customer_Details values("+str(sno)+",'"+mc+"','"+purchase+"',"+str(tc)+")"
        cur.execute(query)
        cn.commit()
        print("\n -- RECORD ADDED SUCCESSFULLY!!!!! --")

    
    def searchCd():
        global cn,cur
        print("-----------------------------------SEARCH CUSTOMER RECORD-----------------------")
        sno = int(input("Enter customer number to search :"))
        query="select * from Customer_Details where S_No="+str(sno)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- SORRY! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("-------------------------------------------------------------------")
            print('%5s'%"S_No",'%13s'%'Name','%18s'%'Purchase','%25s'%'Total_Cost(In K)')
            print("-------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3])
        print("-"*92)



    def editCd():
        global cn,cur
        print("-----------------------------------EDIT CUSTOMER DETAILS-----------------------------------")
        sno = int(input("Enter customer record no. to edit :"))
        query="select * from Customer_Details where S_No="+str(sno)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- CHECK THE INPUTTED SERIAL NUMBER!!!!!! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("--------------------------------------------------------------------")
            print('%5s'%"S_No",'%13s'%'Name','%18s'%'Purchase','%25s'%'Total_Cost(In K)')
            print("--------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3],)
        print("-"*92)
        ans = input("Are you sure to update ? (y/n)")
        if ans=="y" or ans=="Y":
            d = input("Enter new customer name to update (enter old value if not to update) :")
            s = int(input("Enter total cost to update (enter old value if not to update) :"))
            query="update Customer_Details set Name ='"+d+"',Total_Cost="+str(s) + " where S_No="+str(sno)
            cur.execute(query)
            cn.commit()
            print("\n-- RECORD UPDATED  --")
                
    def delCd():
        global cn,cur
        print("-------------------------DELETE CUSTOMER RECORD------------------------")
        en = int(input("Enter Customer Record number to delete :"))
        query="select * from Customer_Details where S_No="+str(en)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\-- SORRY! NO MATCHING DETAILS AVAILABLE --")
        else:
       
            print("---------------------------------------------------------------------")
            print('%5s'%"S_No",'%13s'%'Name','%18s'%'Purchase','%25s'%'Total_Cost(In K)')
            print("---------------------------------------------------------------------")
            for row in results:
                print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3])
        print("-"*92)
        ans = input("Are you sure to delete ? (y/n)")
        if ans=="y" or ans=="Y":
            query="delete from Customer_Details where S_No="+str(en)
            cur.execute(query)
            cn.commit()
            print("\n-- RECORD DELETED  --")
    def clear():
        for i in range(1,50):
            print()
    while True:
        print("1. SHOW CUSTOMER RECORD ")
        print("2. ADD NEW CUSTOMER RECORD ")
        print("3. SEARCH CUSTOMER RECORD ")
        print("4. EDIT CUSTOMER RECORD ")
        print("5. DELETE CUSTOMER RECORD ")
        print("0. EXIT")
        ans = int(input("Enter your choice :"))
        if ans==1:
            showAll()
        elif ans==2:
            addCd()
        elif ans==3:
            searchCd()
        elif ans==4:
            editCd()
        elif ans==5:
            delCd()
        elif ans==0:
            print("lIVE THE SPEED!!!!!")
            cn.close()
            break









    
    

