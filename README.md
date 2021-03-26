# Python Exercises

## Calculate year of birth

### Tasks

- define the variables `age` and `name`
- make a calculation for the year in which the person was born
- print out "OMG person, you are age years old, so you were born in year" with the correct values

### Second Part

- prompt the user for input and re-assessing the variable `age` and `name`
- figure out a way to account for if the person's birthday has already happened this year or not

### Extra

- go look into the library time
- print out the amount of hours this person has lived

### Acceptance Criteria

- program defines the variable `age` and `name`
- program prints the string "OMG person, you are age years old, so you were born in year"

## Lists - Restaurant Waiter Helper Program
### Summary

- Now that we've created had some time to use our lists, time to make something more useful.
- You are going to make a program that helps a waiter with his menu and his orders.
- See tasks for the user stories.

### Tasks

User stories:

- As a User I want to be able to see the menu in a formatted way, so that I can order my meal.

- As a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

- As a user, I want to have my order read back to me in formatted way so I know what I ordered.

### Acceptance Criteria

- its own project on your laptop and Github
- be git tracked
- have 5 commits minimum
- has documentation
- follows best practices

### Documentation
- The menu is created as a list containing each menu item
- To display the menu, I printed a heading, and then iterated over each menu item and printed it
- I created an `ordering` variable, which was set to `True`
- While `ordering` remains `True`, the user is asked to input a menu item to order
- If the input matches a menu item, it is added to an `order_items` list, and a confirmation message is printed
- If the input does not match, the user is prompted to try again
- If the letter "x" is input, `ordering` is set to `False` and the loop ends
- To read back the order, I used a `print()` statement for the heading, and then iterated over each item in the order with `print()`

## Xmas Holiday list that never ends
- Use a while loop to keep things going!
- Your task is to create a list of xmas gifts using cool control flow now!
- hint: While loops and break conditions, use lists and append, iterate to print

### User stories:

- As a user, i want to be able to add items to the list, so I can read it later.
- As a user, I want to be able to keep adding things to the list until I use exit
- As a user, I should be able to use the word exit in a sentence and still have the program terminate, so that anyone can use it
- As a user, when the program exits, I want to see the complete list in caps lock and numbered, so that I know what to buy. example:
   - 1 - RC car
   - 2 - PS2
   - 3 - GTA Vice City
    
## DRY Code and Functions
### Tasks
- Make a loop with a range that says hello 10 times
- Create another loop with a range that asks for names and appends to list names
- Make a loop that iterates over each name in lit_name and formats it into lowercase in a new variable called list names lower
- Iterate over a list of values to find if they are even

## Fizzbuzz
### The problem
- Write a program that prints the numbers from 1 to 100
- But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”
- For numbers which are multiples of both three and five print “FizzBuzz”
- Must be in class and method format

### Documentation
- Defined `Fizzbuzz` as a class
- Defined `fizz_nums`, `buzz_nums`, and `fizzbuzz_nums` as attributes referring to the divisors of the numbers that should be replaced by them
- Defined a method `fizzbuzz_individual(num)` which returns "Fizz", "Buzz", "Fizzbuzz", or the number according to the rules above when given a single number
- Defined a method `fizzbuzz_one_to_hundred()`, which uses the `fizzbuzz_individual` method to return the numbers 1-100 according to the Fizzbuzz rules
- To call `fizzbuzz_individual` in the new method, it must be written as a method on the class, i.e. `Fizzbuzz().fizzbuzz_individual(num)`

## Scrabble score calculator
### Task
- Given standard Scrabble scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided

### Documentation
- A `letter_score` attribute on the `Scrabble` class contains the score of each letter within a dictionary
- A method `calculate_score()` sets a `score` variable to 0, and then iterates over each letter in the argument
- It references the `letter_score` dictionary and adds the score of each letter to `score`
- `score` is then returned

## Control flow age and permission

## Dictionary basics