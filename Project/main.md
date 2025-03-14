# Unit 3: Point of Sale (POS) application for Turkish Restaurant

## Criteria A: Planning

![Figure-1](https://github.com/user-attachments/assets/5dd5a3b2-ae3c-43ac-9833-f5a5fc9c4cb8)
**Fig 1** *Represents example of big-medium sized Turkish Restaurant*

## Problem definition
  My client, R.O, operates a big-sized Turkish restaurant focused on delivering high-quality dining experience. However, the restaurant currently faces several challenges related to order management and payments. Waiters in his resturant manually take orders and deliver them to the kitchen, which sometimes causes mistakes and miscommunication. And additionally, there are more problems caused by manual order management such as losing bills, miscommuncation over the orders need to be canceled, and etc. That is why, he thinks they need digital system for their order management, but he has some concerns. Firstly, he is concerned about unauthorized access for the relevan roles in this digital platform which can lead to misusage. Secondly, they have a really big restaurant consisting two different halls (inside and terrace), which makes it hard for waiters and admins if they only see the number of the tables in the platform. Thirdly, he is concerned about the data storage in the system as he does want sensitive data to be easily accessed, but at the same time he wants to keep the track of orders, users' account and etc. Lastly, he is concerned about dismanagement and confusion caused by taking orders and he wishes this system to be user-friendly.

**See the evidence of the consultation in the Appendix**.


## Proposed Solution
  I proposed to my client to develop a POS program in Python. Python is an interpreted language that is supported by all the major operating systems and architectures, unlike compiled languages like Java. If Python is installed, the program will be compatible with basically any computer, which will make it ideal for R.O.'s restaurant if they ever need to change the hardware or migrate with different computer systems at any point in the future. The language is also open-source, which means there are no licensing costs, which can be allocated to other parts of the business [^1]. Because the program will be running on computers, as opposed to mobile phones, it is logical to utilize a language aimed at desktop applications, which eliminates mobile languages like Swift and Kotlin [^2].
  In the user interface, I proposed to use the Kivy framework. Kivy was designed with use for Python in mind, so it is among the most compatible application frameworks with my choice of language. Like its native language, Kivy is cross-platform, maintaining the advantage of easy portability between different devices [^3]. KivyMD will be incorporated as an extension, which includes Material Design features. This gives the application a stylish appearance fitting for the professional image of R.O.'s high-end Turkish restaurant, while also incorporating touch-based interface features suitable for restaurant workers to use the system in an efficient manner[^4].
  For storing the data, a database system is important rather than flat files like text or CSV. The restaurant POS must be accessed by multiple staff members at once, needed to have advanced data relations between orders, items, tables, and users, and transaction integrity for financials. A database provides built-in protection for data integrity, efficient querying for real-time use, and security features that would necessitate huge amounts of code with less advanced storage alternatives. These requirements necessitate an actual database system that is mandatory for secure POS operation.
  I proposed to use SQLite for data storage. CSV and JSON files were also considered, but data relationship complexity between orders, menu items, tables, and user accounts requires a more solid database setup[^5]. SQLite offers great advantages in the sense that it is serverless, it requires no standalone server process. This is cost-effective for the restaurant in the sense that no server hardware and its upkeep will be paid for[^6]. SQLite, along with Python, is cross-platform, which ensures portability of the application[^7]. Compared to MySQL, which is also a very popular database program, SQLite is the most suited for this application in the sense that it is suited for local, single-app usage with many workers reading off of and writing to the same database file in a shared system—precisely the setup in R.O.'s restaurant business[^8]. SQLite's strong security features will also be beneficial in protecting confidential data such as encrypted user credentials and order history.
  This combination of technologies—Python, Kivy/KivyMD, and SQLite—provides the ideal answer to R.O's problems: secure role-based access, graphical depiction of the restaurant layout in a easily understood manner, secure data storage with permanent history, and user-friendly interface for easing the order management process eliminating ambiguity.

## Success Criterions

[^1]: Merrill, Cache. "7 Important Reasons Why You Should Use Python." Zibtek, 1 September 2019, https://www.zibtek.com/blog/7-important-reasons-why-you-should-use-python
[^2]:Yakymiv, Volodymyr. "Choosing the Best Language for App Development: 7 Options to Consider." Forbytes, 3 November 2023, https://forbytes.com/blog/best-language-for-app-development
[^3]:"Kivy Tutorial." Free Learning Platform For Better Future, https://www.javatpoint.com/kivy#AdvantagesDisadvantages/
[^4]:"Building a Simple Application using KivyMD in Python." GeeksforGeeks, https://www.geeksforgeeks.org/building-a-simple-application-using-kivymd-in-python/
[^5]:"Should you use CSV, JSON, or SQL?." PythonHow, https://pythonhow.com/python-tutorial/miscellaneous/csv-json-or-sql/
[^6]:"AQLite Is Serverless." SQLite, https://www.sqlite.org/serverless.html
[^7]:"SqLite Advantages." Free Learning Platform For Better Future, https://www.javatpoint.com/sqlite-advantages-and-disadvantages
[^8]:Yugulalp, Serdar. "Why you should use SQLite." Infoworld, 13 February 2019, https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html 




1. The pos app allows users to log in with valid credentials and directs them to appropriate interfaces based on their roles (Waiter or Administrator).  
   **[ISSUE TACKLED]**: `Unauthorized access is prevented, and users only see functionality based on their role.`

2. **Waiter Specific**: The app displays an interactive table selection screen, processes order creation with automatic price calculations (including taxes and service charges), and generates printable bills.
  **[ISSUE TACKLED]**: `Confusion caused by taking orders is gone through a unified, table-specific interface.`

3. **Admin-Specific**: The system provides comprehensive order monitoring across all tables, processes order status changes with automatic table status updates, and displays detailed order.
  **[ISSUE TACKLED]**:  `Management inefficiency is now solved by centralized control and real-time monitoring.`

4. The application enables real-time order modification, which allows waiters to add items to existing orders and admins to track changes in real-time across the restaurant's operations.
   **[ISSUE TACKLED]**: `Discrepancies in communication between service staff and kitchen are now eliminated through synchronized order updates.`

5. The User interface provides "touchable" map of restaurant and the app provides clear navigation between screens (for ex, Login to Waiter/Admin Inside/Terrace to Table Screens).  
   **[ISSUE TACKLED]**: `Confusion caused by the largeness of restaurant for both waiters and admins is now minimized`



# Criteria B: Design

## System Diagram
![image](https://github.com/user-attachments/assets/0bf2d13b-c348-4cac-adbc-668b745cb426)

**Fig 2** *System diagram of proposed solution*


## UML diagram
![UML_diagram](https://github.com/user-attachments/assets/a8a50182-0e1b-4cfe-a2c1-1c98522ee23e)
**Fig 3** *UML Diagram of the classes*

## ER diagram
![ER_diagram_1](https://github.com/user-attachments/assets/3f73557a-0f26-48e7-a815-86c3a701cc53)

**Fig 4** *ER Diagram of the database*

## Flow diagrams for algorithms
![flow1](https://github.com/user-attachments/assets/6299626b-271f-4c92-b38a-57d05c7865ab)

**Fig 5** *This flowchart represents the login process from **`LoginScreen`** class. (Easy)*
![flow2](https://github.com/user-attachments/assets/ffff4b0e-df87-4bc2-8472-fae75a4214d8)

**Fig 6** *This flowchart represents the batch update process from the **`Table_Waiter`** class, where multiple items are updated in the database. (Medium)*

![flow3r](https://github.com/user-attachments/assets/6bb26b1d-c313-41d8-8e50-67d5e415358d)

**Fig 7** *This flowchart represents the entire lifecycle of an order, from creation to completion or cancellation. (Hard)*




## Test Plan
| Test No | Test Goal                                                                                                                                       | Test Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Supposed Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Pass/Error |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| 1       | To ensure that users can log in with valid credentials and are directed  to the correct interface based on their role (Waiter or Administrator) | 1. Run the pos_system.py and enter "Alex_waiter_5" as username and "55" password 2. Press "Login" button 3. Press "Logout" button in waiter interface and enter "Bob_admin_5" as username and "55" as password 4. Press "Login" button 5. Press "Logout" button in admin interface and enter "admin" as username and "1234" as password which are invalid. 6. Press "Login" button                                                                                                                     | 1. Verify that the user is redirected to  the Waiter interface after step 2 2. Verify that the user is redirected to  the Admin interface after step 4 3. Verify that the system gives error  message-"Invalid Credentials" after step 6                                                                                                                                                                                                                                                                                                                        |            |
| 2       | To ensure waiters can create orders, add items with quantities,  calculate totals (including taxes and service charges), and print bills        | 1. Run the pos_system.py and enter "Alex_waiter_5" as username and "55" as password. 2. Press "Login" button. 3. Press table number "14". 4. Press "Adana Kebab" from the menu section. 5. Enter "2" as quantity. 6. Press "Print the bill". 7. Press "Out" icon and press table number "14" again.                                                                                                                                                                                                    | 1. Verify that Table Waiter screen is opened  for that table "14" after step 3 2. Verify that "Adana Kebab" is visible in  Ordered items section with price "1500 Yen" and quantity "2" after  step 5 3. Verify the total of the bill printed is "3150 Yen" after step 6 4. Ensure that "Adana Kebab x 2 = 3000 Yen" is still shown in  Ordered items section after step 7                                                                                                                                                                                      |            |
| 3       | To ensure that admins can monitor all tables,  cancel/finish orders, and update table statuses automatically                                    | 1. Run the pos_system.py and enter "Bob_admin_5" as username and "55" as password 2. Press "Login" button 3. Press the table "14", view its details (items, quantities, and total  costs), and press "finish" or "cancel" button. 4. Press the table "14" 5. Press the "out" icon, and then press the "Cash register/Ongoing Orders" button 6. Press the check button for the table "3" and then press "finish" or "cancel" button 7. Press "Back" button and press the table "3"                      | 1. Verify that it is possible to see the ongoing order and  its details during step 3 2. Verify that screen is directed to Admin Inside after  step 3 3. Verify table status of table 14 is now "Available" after step 4 4. Verify that data table screen is out after step 5 5. Verify that order in table 3 is now finished/canceled after step 7                                                                                                                                                                                                             |            |
| 4       | To ensure real-time order modification  and synchronization between waiters and admins                                                          | 1. Run the pos_system.py and enter "Alex_waiter_5" as username and "55" password 2. Press "Login" button 3. Press table number "12" 4. Press "Pide" from menu section 5. Enter "2" as quantity 6. Press "out" button 7. Press "Logout" button 8. Enter "Bob_admin_5" as username and "55" as password 9. Press "Login" button 10. Press table number "12" 11. Press "finish" or "cancel" button 12. Press "Logout" 13. Enter "Alex_waiter_5" as username and "55" password 14. Press table number "12" | 1. Verify that the admin can see the ongoing order (Pide x 2) in real-time after step 10. 2. Verify that the admin's updates also reflects on the waiter screen after step 13.                                                                                                                                                                                                                                                                                                                                                                                  |            |
| 5       | Verify that the app provides a touchable map of the restaurant  and clear navigation between screens.                                           | 1. Run the pos_system.py and enter "Alex_waiter_5" as username and "55" password 2. Press the "Login" button  3. Use the touchable map to select a table "23". 4. Press the "Back" button. 5. Press "Logout" button6. Enter "Bob_admin_5" as username and "55" as password 6. Press "Login" button 7. Use the touchable map to select a table "23". 8. Press the "Back" button.                                                                                                                        | 1. Verify that the Waiter Inside/Terrace screen is displayed after step 2. 2. Verify that the table screen "23" is displayed after selecting a table during step 3. 3. Verify that the Waiter Inside/Terrace screen is displayed after  pressing the "Back" button after step 4. 4. Verify that the Admin Inside/Terrace screen is displayed after step 6. 5. Verify that the Admin table screen is displayed after selecting a table after step 7. 6. Verify that the Admin Inside/Terrace screen is displayed after  pressing the "Back" button after step 8. |            |
## Record of Tasks

| Task No | Planned Action                                                                                         | Planned Outcome                                                                                                | Time Estimate | Target Completion Date | Criterion |
|---------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write problem definition                                                                               | Meet with client and finalize a description of the problem.                                                    | 30 min        | February 24            | A         |
| 2       | Suggest and finalize success criteria                                                                  | Meet with client and agree on success criteria for the POS solution.                                           | 30 min        | February 25            | A         |
| 3       | Write proposed solution                                                                                | Finalize the success criteria and propose a solution for the POS system.                                       | 30 min        | February 25            | A         |
| 4       | Create a system diagram and share it with client                                                       | To have a clear idea of the hardware and software  requirements for the proposal solution                      | 1 hour        | February 26            | B         |
| 5       | Create UML and ER diagrams                                                                             | Plan the backend structure of the POS app.                                                                     | 2 hours       | February 27            | B         |
| 6       | Create 3 flow diagrams: easy, medium, and hard in terms of development complexity                      | To have clear idea of development in non-coding language                                                       | 3 hours       | February 27            | B         |
| 7       | Create basic screens and navigation                                                                    | Creating blank screens for all planned screens and linking them using ScreenManager.                           | 1 hour        | February 28            | C         |
| 8       | Create login and registration screen                                                                   | Making login and registration screens fully functional that they get user data from the database               | 2 hours       | February 28            | C         |
| 9       | Create the layout of Inside and Terrace map of restaurant in Kivy                                      | Getting accurate digital map of restaurant                                                                     | 2 hours       | March 1                | C         |
| 10      | Customize the circular and rectangular table buttons for better visuality and more complex development | Getting rectangular and circular table buttons that can be touched, put some text on, and color can be changed | 4 hours       | March 2                | C         |
| 11      | Design Waiter Table screen in kivy file                                                                | Getting waiter-friendly interface for better order taking                                                      | 2 hours       | March 3                | C         |
| 12      | Code the Waiter Table class in python                                                                  | Getting fully functional waiter section: correct order management and table status update                      | 5 hours       | March 4                | C         |
| 13      | Apply the same layout for the Admin Inside and Terrace except some admin special functionalities       | Get the same restaurant map for admins for real time and admin friendly table management                       | 30 min        | March 5                | C         |
| 14      | Design Admin Available Table screen in kivy file                                                       | Getting admin-friendly interface for available tables                                                          | 2 hours       | March 5                | C         |
| 15      | Code the Admin Available Table class in python                                                         | Getting appropriate available table screen based on the table touched                                          | 1 hour        | March 5                | C         |
| 16      | Follow the task no 13 and no 14 for also Admin Occupied class and screen                               | Get a screen where admin can finish/cancel order of the table touched                                          | 3 hours       | March 6                | C         |
| 17      | Create a data table for Ongoing Orders that can be only accessed by admins                             | Make tracking ongoing orders easier for admins                                                                 | 2 hours       | March 7                | C         |
| 18      | Create a test plan and fix the errors                                                                  | Make sure that there will be no challenge for my customer                                                      | 2 hours       | March 7                | B         |
| 19      | Document the list of techniques used for coding part and explain my code by picking the special parts  | To make documentation of the coding part more understandable                                                   | 2 hours       | March 8                | C         |
| 20      | Give information about my data storing method- SQL Databases                                           | To give description of the data format used                                                                    | 1 hour        | March 9                | B         |
| 21      | Take 4 min video demonstrating the application and its functionalities                                 | To achieve clear and concise explanation of the project, its results, and its implementation                   | 2 hours       | March 10               | D         |

## Data storing method

![image](https://github.com/user-attachments/assets/c9c5a570-bb1c-4e8b-b7a0-45902964fd75)

**Fig 8** *This extract is an example how the data is stored -**SQL Database***
(Inconsistencies in ids are due to ***Canceled*** orders)

![image](https://github.com/user-attachments/assets/69ee158b-fdc3-485a-85fa-9ad500a21b25)

**Fig 9** *This extract is an example how the sensitive data such as passwords of users are stored as a **hash** for improved security*

# Criteria C: Development

## List of techniques used

1. *OOP Paradigm* - **#SC1, #SC2, #SC3, #SC4, #SC5** 
2. *Use of Properties instead of regular variables* - **#SC2, #SC3, #SC4, #SC5**
3. *Threading method, batch update, and fixing pragma modes* - **#SC2, #SC4** 
4. *Customization of Buttons* - **#SC5**

[^9]: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
[^10]: https://kivy.org/doc/stable/api-kivy.properties.html
[^11]: https://docs.python.org/3/library/threading.html


### 1.  *OOP Paradigm *-** #SC1, #SC2, #SC3, #SC4, #SC5** 
OOP paradigm is one of the focuses of this project and `OrderedItem` class was the best example of how I applied OOP priniciples to this project. The use of OOP paradigm allowed me to make my code more reusable and optimized and if there will be any extension in the project, just editing the `OrderedItem ` class, which *encapsulates* all details of item , including everything, will allow developers to save time. This is how it was defined:
```.py
class OrderedItem:
    def __init__(self,name,price,quantity,item_id=None):
        self.name=name
        if isinstance(price,str) and "¥" in price:
            self.price=int(price.split("¥")[0].strip())
        else:
            self.price=int(price)
        self.quantity=quantity
        self.total=self.price*self.quantity
        self.item_id=item_id
```
Here we can see that all details of item is initialized. When a new OrderedItem object is created, this method is automatically called to set up the object. There is also a conditional statement `isinstance(price, str)` that checks if `price` parameter is string AND if it contains Japanese Yen `¥` symbol. If both condtions are true it splits the string at the `¥` by using `price.split("¥")` and takes the fisrt part of the result by using `[0]`. Then it gets rid of any spaces with `strip()` and converts it to integer by using `int()`. And this integer then is assigned to the `self.price` for future usage. Overall,  for example, if the price passed from menu is "100¥", this technique will extract numeric value part `100` and assign it to the `self.price` for billing calculations. This *encapsulation* makes it reusable and inheretable throughout the project as my project is mainly about item order management. Through the use of this class in `Table_Waiter` screen, I made sure that this development is optimized and repetitions are minimized. This class also includes the `_str_` method:
```.py
    def __str__(self):
        return f"{self.name} x{self.quantity} - {self.price}¥ = {self.total}¥"
```
This `__str__` method provides a formatted string representation of the item, where it combiness its name, quantity, price, and total cost into a single string. This is used to display item details in the UI and generate summaries for database storage. For example, in the `Table_Waiter` screen, the `update_ordered_items_display` method uses `__str__` to populate the ordered items list: 
```.py
def update_ordered_items_display(self):  
    for item in self.order_items:  
        self.ids.ordered_items_list.add_widget(OneLineListItem(text=str(item)))  
```
This where the update to display takes place: first `self.ids.ordered_items_list` represents `id` of `MDList` widget in the Kivy UI, then here `add_widget()` is a Kivy method that adds a child widget to a parent widget, in this case, it is adding a new item to the `MDList` display. And then `OneLineListItem(text=str(item))` creates a new instance of the OneLineListItem class, which is typically from the KivyMD library for a simple list item that displays a single line of text. Then `str(item)` converts the `item` object to a string representation. This also shows that the items in `self.order_items` are objects of the `OrderedItem` class that I showed above. For this to work properly, the `OrderedItem` class need to have a `__str__` method to convert objects to strings. In the flow of my application this method is called whenever the ordered items chage, for example when items are added to a ongoing order, to make the UI stay synchronized with the raw data model.

### 2. *Use of Properties instead of regular variables* - **#SC2, #SC3, #SC5**
I used `Kivy`'s `Properties` (for example `StringProperty`, `ListProperty`, `ObjectProperty` and etc) in especially table screens where I mostly need to deal with the components of the ui for fully functionality. For example:
```.py
class Table_Waiter(MDScreen):
    selected_table=StringProperty("")
    order_items=ListProperty([])
    quantity_dialog=ObjectProperty(None)
    current_food=StringProperty("")
    current_price=StringProperty("")
    order_id=NumericProperty(0)
```
I came up with this technique after research in web kivy documentation [^10]. Without `Properties`, I would have needed to write repetitive code to manually refresh the UI every time a variable changed, such as when a new item is added to the order or the selected table was updated, which would lead to a poor extensivibilty. They are the most efficient way to work with ui back end logic, and they eliminate the need for manual UI refresh all the time, which is very important factor for screens like `Table_Waiter` as they need more maintainable variables.   


### 3. *Threading method, batch update, and fixing pragma modes* - **#SC2** 
Back then, in the `Table_Waiter` screen, as test user, when I was doing multiple transactions, such as adding a new order, printing the bill, or inputting the quantity in the dialog and etc., I was facing a major challenge where screen was freezing after pressing the button to the relevant transaction and I was getting the error- "database is locked". And when I was deeply looking for the reason, I found out that database operations can be enough time-consuming that can be get locked for other operation, which reduces the user experience. I researched for the solution and found about Threading [^11] method which was the best solution to my problem as it offloads database updates to a thread working in the background and makes the UI stay responsive during updates. I implemented it in `process_order `function in the `Table_Waiter` class, where most of database updates and validations are happening. The most important part of this function is to use `threading` for the function `batch_update_db`:
```.py
threading.Thread(target=self.batch_update_db).start()  
```
`batch_update_db` function updates the items list in `order_items`. By uploading this to a background thread, ui remains responsive and does not get freeze. One of the most important aspects of the `batch_update_db` function is its use of the `executemany` method for batch database operations. Instead of executing individual `INSERT` or `UPDATE` statements for each item, `executemany` processes multiple rows in a single database call which reduces the time database needs multiople transactions:
```.py
items_to_insert=[(order_id,item.name,item.price,item.quantity) for item in new_items]  # here use of [ ] reduces the number of code lines and is more way faster
cursor.executemany('''  
    INSERT INTO order_items (order_id,food_name,price,quantity)  
    VALUES (?,?,?,?)  
''',items_to_insert)  
```
But initially, I used `PRAGMA` modes like:
```.py
journal_mode=WAL # Write-Ahead Logging 
```
This was for to enable concurrent database access, which would prevent the `"database is locked"` error. But I did not get the result I wanted that is why I continued with `Threading`.
### 4. *Customization of Buttons* - **#SC5** 
To address **#SC5** I had to find the best way to mimic the restaurant's actual map in my pos system. For this I decided to customize the table buttons based on the shape they have in reality: rectangular and circular. To match app with real ones I created the classes `CustomRectButton` and `CustomCircleButton`. They are inheriting from Kivy's `ButtonBehavior` and `Widget` classes to customly draw the tables using Kivy's `canvas` instructions. For example, the CustomCircleButton class draws a circle and tabs using `Ellipse` and `Rectangle` to represent the round table with 4 chairs:
```.py
class CustomCircleButton(ButtonBehavior,Widget):  
    def __init__(self,**kwargs):  
        super().__init__(**kwargs)  
        with self.canvas.before:  
            self.bg_color=Color(0.8,0.8,0.8,1)
            self.bg_ellipse=Ellipse(pos=self.pos,size=self.size)  
            self.tab_top=Rectangle(pos=(self.x+40,self.y+80),size=(20,20))  

```
The function `update_graphics` is making sure that if user changes button's size and position, shapes are drawn again based on new position and size:
```.py
def update_graphics(self,*args):  
    self.bg_ellipse.pos=(self.x,self.y)  
    self.bg_ellipse.size=(self.width,self.height)  
```



# Criteria D: Functionality

https://github.com/user-attachments/assets/2e201ba1-7571-4eb8-85ee-5d90ac2e8270



