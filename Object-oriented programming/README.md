# Object-oriented programming

## Classes and objects
*Notebook* : classes_objects.ipynb
*Related Files in assets folder* : accounts.json, log_transaction.json
Quite a classic though. I remember this exercise from my training on the way to be a Data Engineer. The bonus part of transferring funds to another account and to log each transaction. It's really an enrichment. I added some enhancements as it was not asked for this exercise : add an account file to save the current status of each account (the related functions create_account and update_account). You will see in log_transaction.json, all the failed attempts before I make all of it work.

## Constructor and methods
*Notebook* : constructors_methods.ipynb
*Related Files in assets folder* : library_books.json, library_transaction.json
A step forward OOP. The project was quite simple a library with basic operations : add, borrow (without time limit) and return a book, view all the books in the catalog. The bonus part was truly exciting : save the books in a file for persistence (I added functions to save books in a JSON file, then convert the JSON into list of Book objects), I added a transaction log to track all the operations made in the Library, set a time limit for borrowing a book and add a search module. Above all, very enriching

## Inheritance
*Notebook* : inheritance.ipynb
*Related Files in assets folder* : employees.json
I discovered multiple inheritance and multi-level inheritance that I did not know before. Overall, the experience while learning is quite thrilling. I noticed that I'm now able to forecast whether a project needs a persistence file or not, before the trainer even announces the bonus part (add an Intern class with a fixed stipend, save employees in a file, implement search by ID). I went a bit further as the search I implemented is based on either name or ID, and I began a module to update an employee. This part will be a focus for another commit.

## Polymorphism
*Notebook* : polymorphism.ipynb
*Related Files in assets folder* :
Quite new to me as I can't remember when I ever used this concept. Interesting though! I learned that one of its application is GUI, which is one of the core concepts of this 100 projects challenge. I look forward to work on it.

## Encapsulation
*Notebook* : encapsulation.ipynb
*Related Files in assets folder* : user_profiles.json
One of these lessons that I particularly enjoy as it explains step by step what is what. I already used public, protected and private attributes without assessing to what they actually refers to. I created my own bonus challenge as I created a class for UserProfileApp which was not required in the bonus challenge of the lesson. Of course, persistence in an app is the key factor : Sooooo load in JSON file!

## Static and class methods
*Notebook* : static_class_methods.ipynb
*Related Files in assets folder* : inventory.json
A good way to remind what is static method and to discover the power of class method that I can't remember if whether I ever used it. The project was thrilling to work on especially as I changed the paradigm of the exercise which was to create Main loop function resetting at each time the list of products. I still used JSON file for data persistence but I may consider loading data in CSV files in upcoming projects.