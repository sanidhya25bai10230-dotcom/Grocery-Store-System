total_amount = 0

print("Welcome To Grocery Store")
print("Press 1 to start shopping ")
print("Press 0 to exit from store")
choice = input("enter the choice ")


if choice == '1':
   print("You may start shopping")
   
   while True:
   
       print("What you would like to buy") 
       print("Press 3 to buy dairy products ")
       print("Press 4 to buy fruits ")
       print("Press 5 to buy cookies")
       print("Press 6 to buy chocolates")
       print("Press 0 to exit and get total amount")
       Your_preference = input("enter your shopping preference ")
       if Your_preference =='0':
          break

       elif Your_preference == '3':
            print("you have selected dairy product as your preference")
            Dairy_products = ['Milk' , 'Chesse' , 'Cream' , 'Cottage Cheese']
            print("The dairy products available are", Dairy_products)
            print("Press A for milk")
            print("Press B for Cheese")
            print("Press C for Cream")
            print("Press D for Cottage Cheese")
            Dairy_choice = input("Enter the your choice for the dairy product")

            price = 0

            if Dairy_choice == 'A':
               price = 24
               item = "Milk"
            elif Dairy_choice== 'B':
              price = 100
              item = "Cheese"
            elif Dairy_choice== 'C':
              price = 68
              item = "Cream"
            elif Dairy_choice == 'D':
              price = 120
              item = "Cottage Cheese"
            else :
              print("wrong option is selected ")
              continue

            total_amount += price
            print("The selected item and price is=", item , price)

       elif Your_preference == '4':
            print("You have selected fruits as your preference")
            Fruits = ['Mango' , 'Apple' , 'Orange' , 'Kiwi' ]
            print("The fruits available are " , Fruits) 
            print("Press E for Mango")
            print("Press F for Apple")
            print("Press G for Orange")
            print("Press H for Kiwi")
            Fruit_choice = input("Enter your choice for fruits")

            price = 0
            if Fruit_choice == 'E':
               price = 45
               item = "Mango"
            elif Fruit_choice == 'F':
               price = 56
               item = "Apple"
            elif Fruit_choice == 'G':
               price = 55
               item = "Orange"
            elif Fruit_choice == 'H':
               price = 67
               item = "Kiwi"
            else:
               print("Wrong option is selected ")
               continue
   
            total_amount += price
            print("The selected item and price is=", item , price)



       elif Your_preference == '5':
            price = 75
            item = "cookies"
            total_amount += price
            print("The selected item and price is=", item , price)
            continue

       elif Your_preference == '6':
            price = 100
            item = "chocolates"
            total_amount += price
            print("The selected item and price is=", item , price)
            continue

       else:
           print("Wrong option is choosen")
           continue
if choice == '0':  
  print("Thank you for your visit")

elif choice == '1':
  print("Your total amount is ", total_amount)
  print("Pay at the counter")

else:
  print("Invalid choice entered")
