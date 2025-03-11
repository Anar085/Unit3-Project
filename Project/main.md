# Unit 3: Point of Sale (POS) application for Turkish Restaurant

## Criteria A: Planning

![Figure-1](https://github.com/user-attachments/assets/5dd5a3b2-ae3c-43ac-9833-f5a5fc9c4cb8)
**Fig 1** *Represents example of big-medium sized Turkish Restaurant*

## Problem definition
  My client, Ritsu Okazaki, operates a big-sized Turkish restaurant focused on delivering high-quality dining experience. However, the restaurant currently faces several challenges related to order management and payments. Waiters in his resturant manually take orders and deliver them to the kitchen, which sometimes causes mistakes and miscommunication. And additionally, there are more problems caused by manual order management such as losing bills, miscommuncation over the orders need to be canceled, and etc. That is why, he thinks they need digital system for their order management, but he has some concerns. Firstly, he is concerned about unauthorized access for the relevan roles in this digital platform which can lead to misusage. Secondly, they have a really big restaurant consisting two different halls (inside and terrace), which makes it hard for waiters and admins if they only see the number of the tables in the platform. Thirdly, he is concerned about the data storage in the system as he does want sensitive data to be easily accessed, but at the same time he wants to keep the track of orders, users' account and etc. Lastly, he is concerned about dismanagement and confusion caused by taking orders and he wishes this system to be user-friendly.

*See the evidence of the discussion with customer here:* [Evidence_customer.pdf](https://github.com/user-attachments/files/19174110/Evidence_customer.pdf)


## Proposed Solution
  I will be creating the POS program in Python. Python is an interpreted language that is supported by all the major operating systems and architectures, unlike compiled languages like Java. If Python is installed, the program will be compatible with basically any computer, which will make it ideal for Ritsu's restaurant if they ever need to change the hardware or migrate with different computer systems at any point in the future. The language is also open-source, which means there are no licensing costs, which can be allocated to other parts of the business [^1]. Because the program will be running on computers, as opposed to mobile phones, it is logical to utilize a language aimed at desktop applications, which eliminates mobile languages like Swift and Kotlin [^2].
  In the user interface, I will be using the Kivy framework. Kivy was designed with use for Python in mind, so it is among the most compatible application frameworks with my choice of language. Like its native language, Kivy is cross-platform, maintaining the advantage of easy portability between different devices [^3]. KivyMD will be incorporated as an extension, which includes Material Design features. This gives the application a stylish appearance fitting for the professional image of Ritsu's high-end Turkish restaurant, while also incorporating touch-based interface features suitable for restaurant workers to use the system in an efficient manner[^4].
  SQLite will be used for data storage. CSV and JSON files were also considered, but data relationship complexity between orders, menu items, tables, and user accounts requires a more solid database setup[^5]. SQLite offers great advantages in the sense that it is serverless, it requires no standalone server process. This is cost-effective for the restaurant in the sense that no server hardware and its upkeep will be paid for[^6]. SQLite, along with Python, is cross-platform, which ensures portability of the application[^7]. Compared to MySQL, which is also a very popular database program, SQLite is the most suited for this application in the sense that it is suited for local, single-app usage with many workers reading off of and writing to the same database file in a shared system—precisely the setup in Ritsu's restaurant business[^8]. SQLite's strong security features will also be beneficial in protecting confidential data such as encrypted user credentials and order history.
  This combination of technologies—Python, Kivy/KivyMD, and SQLite—provides the ideal answer to Ritsu's problems: secure role-based access, graphical depiction of the restaurant layout in a easily understood manner, secure data storage with permanent history, and user-friendly interface for easing the order management process eliminating ambiguity.

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

2. **Waiter Specific**: Waiters can select a table, create new orders with specific quantities and the app calculates the total cost, including service charges and taxes, and allows waiters to print bills. Waiters can add to their ongoing orders anytime they come back to their table screen.
  **[ISSUE TACKLED]**: `Confusion caused by taking orders is gone as all operations for waiters are in one screen for certain table`

3. **Admin-Specific**: Admins can view all ongoing orders through tables, cancel or finish orders, which automatically update table statuses. They can access detailed order information: items, quantities, and total costs.
  **[ISSUE TACKLED]**:  `Dismanagement is prevented, now Admins have full control over the table`

4. User passwords are encrypted as hashes, and all data (orders, users, tables) is stored permanently in an SQLite database.  
   **[ISSUE TACKLED]**: `Explotiation of sensitive data is prevented as they are securely stored, and order history can be used when app restarts.`

5. The User interface provides "touchable" map of restaurant and there is a clear navigation between screens (for ex, Login to Waiter/Admin Inside/Terrace to Table Screens).  
   **[ISSUE TACKLED]**: `Confusion caused by the largeness of restaurant for both waiters and admins is now minimized`



# Criteria B: Design

## System Diagram
![image](https://github.com/user-attachments/assets/0bf2d13b-c348-4cac-adbc-668b745cb426)

**Fig 2** *System diagram of proposed solution*


## UML diagram
![UML_diagram](https://github.com/user-attachments/assets/a8a50182-0e1b-4cfe-a2c1-1c98522ee23e)
**Fig 3** *UML Diagram of the classes*

## ER diagram
![ER_diagram'](https://github.com/user-attachments/assets/cdc9052d-ff27-43ae-a7e9-fc00b042e05a)

**Fig 4** *ER Diagram of the database*

## Flow diagrams for algorithms
![flow1](https://github.com/user-attachments/assets/6299626b-271f-4c92-b38a-57d05c7865ab)

**Fig 5** This flowchart represents the login process from **LoginScreen** class. (Easy)
![flow2](https://github.com/user-attachments/assets/ffff4b0e-df87-4bc2-8472-fae75a4214d8)

**Fig 6** This flowchart represents the batch update process from the **Table_Waiter** class, where multiple items are updated in the database. (Medium)

![flow3r](https://github.com/user-attachments/assets/6bb26b1d-c313-41d8-8e50-67d5e415358d)

**Fig 7** This flowchart represents the entire lifecycle of an order, from creation to completion or cancellation. (Hard)




## Test Plan

## Record of Tasks| Task No | Planned Action                                                                                         | Planned Outcome                                                                                                | Time Estimate | Target Completion Date | Criterion |
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
# Criteria C: Development

## List of techniques used




# Criteria D: Functionality



