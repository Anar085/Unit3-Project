# Unit 3: Point of Sale (POS) application for Turkish Restaurant

## Criteria A: Planning

![Figure-1](https://github.com/user-attachments/assets/5dd5a3b2-ae3c-43ac-9833-f5a5fc9c4cb8)
**Fig 1** Represents example of big-medium sized Turkish Restaurant

## Problem definition
My client, Ritsu Okazaki, operates a big-sized Turkish restaurant focused on delivering high-quality dining experience. However, the restaurant currently faces several challenges related to order management and payments. Waiters in his resturant manually take orders and deliver them to the kitchen, which sometimes causes mistakes and miscommunication. And additionally, there are more problems caused by manual order management such as losing bills, miscommuncation over the orders need to be canceled, and etc. That is why, he thinks they need digital system for their order management, but he has some concerns. Firstly, he is concerned about unauthorized access for the relevan roles in this digital platform which can lead to misusage. Secondly, they have a really big restaurant consisting two different halls (inside and terrace), which makes it hard for waiters and admins if they only see the number of the tables in the platform. Thirdly, he is concerned about the data storage in the system as he does want sensitive data to be easily accessed, but at the same time he wants to keep the track of orders, users' account and etc. Lastly, he is concerned about dismanagement and confusion caused by taking orders and he wishes this system to be user-friendly.


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

**Fig 2** System diagram of proposed solution


## UML diagram
![UML_diagram](https://github.com/user-attachments/assets/a8a50182-0e1b-4cfe-a2c1-1c98522ee23e)
**Fig 3** UML Diagram of the classes

## ER diagram
![ER_diagram'](https://github.com/user-attachments/assets/cdc9052d-ff27-43ae-a7e9-fc00b042e05a)

**Fig 4** ER Diagram of the database

## Flow diagrams for algorithms

## Test Plan

## Record of Tasks


# Criteria C: Development

## List of techniques used




# Criteria D: Functionality



