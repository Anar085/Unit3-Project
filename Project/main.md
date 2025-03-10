# Unit 3: Point of Sale (POS) application for Turkish Restaurant

## Criteria A: Planning

![Figure-1](https://github.com/user-attachments/assets/5dd5a3b2-ae3c-43ac-9833-f5a5fc9c4cb8)
**Fig 1** Represents example of big-medium sized Turkish Restaurant

## Problem definition
My client, Ritsu Okazaki, operates a big-sized Turkish restaurant focused on delivering high-quality dining experience. However, the restaurant currently faces several challenges related to order management and payments. Waiters in his resturant manually take orders and deliver them to the kitchen, which sometimes causes mistakes and miscommunication. And additionally, there are more problems caused by manual order management such as losing bills, miscommuncation over the orders need to be canceled, and etc. That is why, he thinks they need digital system for their order management, but he has some concerns. Firstly, he is concerned about unauthorized access for the relevan roles in this digital platform which can lead to misusage. Secondly, they have a really big restaurant consisting two different halls (inside and terrace), which makes it hard for waiters and admins if they only see the number of the tables in the platform. Thirdly, he is concerned about the data storage in the system as he does want sensitive data to be easily accessed, but at the same time he wants to keep the track of orders, users' account and etc. Lastly, he is concerned about dismanagement and confusion caused by taking orders and he wishes this system to be user-friendly.


## Proposed Solution


## Success Criterions

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 


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

## Flow diagrams for algorithms



## Data storing method





**Fig.5** Shows a section of the online API server http://192.168.4.137/readings where the data is being stored in real time every 1 minute

## Test Plan
                                                        |                 |            |

## Record of Tasks


# Criteria C: Development

## List of techniques used




# Criteria D: Functionality



