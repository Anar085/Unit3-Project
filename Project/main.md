# Unit 3: Point of Sale (POS) application for Turkish Restaurant

## Criteria A: Planning

![Figure-1](https://github.com/user-attachments/assets/5dd5a3b2-ae3c-43ac-9833-f5a5fc9c4cb8)
**Fig 1** Represents example of big-medium sized Turkish Restaurant

## Problem definition
My client Ritsu operates a big-sized Turkish restaurant focused on delivering high-quality dining experience. To improve efficiency and minimize order-processing errors, they need a digital POS restaurant order management system with two separate interfaces—one for waiters and another for administrators. The system features a monitor placed near the kitchen, where waiters can log in and take customer orders. Once the meal is prepared and served to the customer, the waiter should print the bill for payment, get the payment from customer, and bring the money (or the receipt if paid by the bank card) and the bill to the cash register. Once administrator seating in the cash register figures out that everything was fine about serving, he/she can finalize the order, which automatically sets the table's status to be "Available" in the pos system. But in the case waiter made a mistake on his/her order, it is not possible for them to cancel the order as it prevents first corruption, in case where waiter can get the payment and cancel order, which makes the order "disappear" from the track of orders, and second the possible chaos in the kitchen caused by the preparation of "canceled" order. If a user logs in as an administrator, they gain additional privileges, such as the ability to cancel orders, view and edit ongoing orders. 


My client, Ritsu Okazaki, operates a big-sized Turkish restaurant focused on delivering high-quality dining experience. At the same time he wants to minimize order-processing errors and increase efficiency. However, the restaurant currently faces several challenges related to order management and payments:

1. Order Errors: Waiters manually take orders and deliver them to the kitchen, which increases the chances of mistakes and miscommunication.
2. Order Cancellation Issues: There is a risk of corruption if waiters can cancel orders after receiving payments, as it could make orders disappear from the records, leading to accountability issues and potential financial losses.
3. Kitchen Confusion: Canceling orders after they have been sent to the kitchen can cause disruption and wasted resources, creating chaos and inefficiency.
Table Availability Tracking: There is no streamlined way to update the table status after a customer has completed their meal and paid, making it challenging to manage seating effectively.
Limited Control for Administrators: Administrators lack the ability to efficiently track ongoing orders, cancel incorrect ones, or make adjustments when necessary.

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



