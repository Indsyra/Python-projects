# Object-oriented programming

## Classes and objects
*Notebook* : classes_objects.ipynb
*Related Files in assets folder* : accounts.json, log_transaction.json
Quite a classic though. I remember this exercise from my training on the way to be a Data Engineer. The bonus part of transferring funds to another account and to log each transaction. It's really an enrichment. I added some enhancements as it was not asked for this exercise : add an account file to save the current status of each account (the related functions create_account and update_account). You will see in log_transaction.json, all the failed attempts before I make all of it work.

## Constructor and methods
*Notebook* : constructors_methods.ipynb
*Related Files in assets folder* : library_books.json, library_transaction.json
A step forward OOP. The project was quite simple a library with basic operations : add, borrow (without time limit) and return a book, view all the books in the catalog. The bonus part was truly exciting : save the books in a file for persistence (I added functions to save books in a JSON file, then convert the JSON into list of Book objects), I added a transaction log to track all the operations made in the Library, set a time limit for borrowing a book and add a search module. Above all, very enriching