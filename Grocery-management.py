import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='manager', database='grocery_shop')
if conn.is_connected():
    print('successfully connected')
c = conn.cursor()

print('grocery shop management system')
print('1.login')
print('2.exit')
choice = int(input('enter your choice:'))
if choice == 1:
    user_name = input('enter your user name=')
    password = input('enter your password=')
    while user_name == 'rudra' and password == 'rudra123':
        print('connected successfully')

        print('grocery shop')
        print('1.customer details')
        print('2.product details')
        print('3.worker details')
        print('4.see all customer details')
        print('5.see all product details')
        print('6.see all worker details')
        print('7.see one customer details')
        print('8.see one product details')
        print('9.see one worker details')
        print('10.stocks')
        print('11.pie chart for avalibility of stock')
        print('12.exit')
        choice = int(input('enter the choice'))
        if choice == 1:
            cust_name = input('enter your name=')
            phone_no = int(input('enter your  phone number='))
            cost = float(input('enter your cost='))
            sql_insert = "insert into customer_details values(" + str(phone_no) + ",'" + (cust_name) + "'," + str(
                cost) + ")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')


        elif choice == 2:
            product_name = input('enter  product name=')
            product_cost = float(input('enter the cost='))
            sql_insert = "insert into product_details values(""'" + (product_name) + "'," + str(product_cost) + ")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')


        elif choice == 3:
            worker_name = input('enter your name=')
            worker_work = input('enter your work=')
            worker_age = int(input('enter your  age='))
            worker_salary = float(input('enter your salary='))
            phone_no = int(input('enter your  phone number='))
            sql_insert = "insert into worker_details values(" "'" + (worker_name) + "'," "'" + (
                worker_work) + "'," + str(worker_age) + "," + str(worker_salary) + "," + str(phone_no) + ")"
            c.execute(sql_insert)
            conn.commit()
            print('data is updated')


        elif choice == 4:
            t = conn.cursor()
            t.execute('select*from customer_details')
            record = t.fetchall()
            for i in record:
                print(i)

        elif choice == 5:
            t = conn.cursor()
            t.execute('select*from product_details')
            record = t.fetchall()
            for i in record:
                print(i)

        elif choice == 6:
            t = conn.cursor()
            t.execute('select*from worker_details')
            record = t.fetchall()
            for i in record:
                print(i)


        elif choice == 7:
            a = input('enter your name')
            t = 'select*from customer_details where cust_name=("{}")'.format(a)
            c.execute(t)
            v = c.fetchall()
            for i in v:
                print(v)


        elif choice == 8:
            a = input('enter your product_name')
            t = 'select*from product_details where product_name=("{}")'.format(a)
            c.execute(t)
            v = c.fetchall()
            for i in v:
                print(v)

        elif choice == 9:
            a = input('enter your name')
            t = 'select*from worker_details where worker_name=("{}")'.format(a)
            c.execute(t)
            v = c.fetchall()
            for i in v:
                print(v)


        elif choice == 10:
            print('******************************************')
            f = open('test.txt', 'r')
            data = f.read()
            print(data)
            f.close()
            print('******************************************')

        elif choice == 11:
            import matplotlib.pyplot as plt

            items = ('shoes', 'stationary', 'watch', 'house use', 'food items')
            avalibility = [156, 200, 103, 206, 196]
            colors = ['red', 'yellowgreen', 'blue', 'gold', 'green']
            plt.pie(avalibility, labels=items, colors=colors)
            plt.title('avalibility of items in shop')
            plt.show()

        elif choice == 12:
            exit()



    else:
        print('wrong password, try again ')

if choice == 2:
    exit()

