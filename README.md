# Library Management System
 A local library is in dire need of a web application to ease their work. The library management system must allow a librarian to track books and their quantity, books issued to members, book fees.
 For the sake of simplicity, you don't have to implement sessions and roles, you can assume that the app will be used by the librarian only.

The following functionalities are there in  application:

# Base Library System
### Librarians must be able to maintain:<br>
*  Books with stock maintained<br>
*  Members<br>
*  Transactions<br>
* The use cases included here are to:<br>

### Perform general CRUD operations on Books and Members<br>
* Issue a book to a member<br>
* Issue a book return from a member<br>
* Search for a book by name and author<br>
* Charge a rent fee on book returns<br>
* Make sure a member’s outstanding debt is not more than Rs.500<br>


# Overview
### Home page
 * The Home page covers all the books that are currently in the inventory, if the Librarian wishes to add more books, 
they can go to the add books page and search using the keywords of the book. 

* The home page also provides the option to rent out a book, it redirects to the rent-out page from where the Librarian can select from the list of available members, if the user wants to add new members, they can move to the members page where they can add the member's name and their initial balance. 

##### Home Page
 ![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Home.png)


##### Add Books Page
 ![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Add_books.png) 


#####  Rent Out Page
 ![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/rent_out.png)

#####  Add Members Page
 ![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Members.png)
* Disabled Delete buttons implies that the member has taken a book and the member cannot be deleted until they have returned the book.



### Return Book Page

* If the member wants to return the book the librarian can head to the return book page and click on return, after return a summary page is displayed which shows the current balance of the user and the total amount paid to the library, the fees for renting a book is calculated by the formula => 500₹ (initial charges) + 10₹ X (The number of days for which the book was issued) 

#####  Return Page
 ![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Return_book.png)


#####  Summary Page
 ![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Summary.png)

### Transactions Page

* To see the transaction history the Librarian can head to the transactions page which shows the transactions arranged from most recent to least recent, A transaction in which the book was rented is shown by red color and a transaction in which the book was returned is shown by green color. 

#####  Transactions Page
![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Transactions.png)


### Analytics Page
![alt text](https://github.com/MonuKumar1/LibraryManagementSystem/blob/master/images/Analytics.png)
* The Analytics Page shows the top 5 books which were issued the greatest number of times and the top 5 spenders who have spent the most amount of money in the library. 



