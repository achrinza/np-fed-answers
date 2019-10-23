# Functions

At the end of this tutorial, you'll learn:

* What are functions
* Function arguments
* Function that returns a value
* Use-cases of functions

---

Functions are a way to create a block of code that can be re-used. For example:

```python
def print_hi():
    print("Hi!")

print_hi()
print_hi()
print_hi()
```

This would give us:

```plaintext
Hi!
Hi!
Hi!
```

If we wanted to change it to print out `Hello!` instead, we could do it easily:

```python
def print_hi():
    print("Hello!")

print_hi()
print_hi()
print_hi()
```

Notice how we only needed to change the logic once, and that applied to every instance of `print_hi()`? That's the beauty of functions; It allows consolidation of program logic into one block to be re-used and allows for easy modification.

---

What if we wanted the program to greet a person by their name, say like: `Hello, [name]`?

That's where `function arguments` come in. All we have to do is:

```python
def print_hi(name):
    print("Hello,", name)

print_hi("Steve")
print_hi("Harvey")
print_hi("Bumblebee")
```

That'll give us:

```plaintext
Hello, Steve
Hello, Harvey
Hello, Bumblebee
```

---

But what if we wanted our function to return a value for our code to use later (Not output directly)?

Well, we can throw in a `return` statement.

```python
def return_hi(name):
    return "Hello, " + name

greeting = return_hi("Steve") + "!"
print(greeting)
```

Noticed how we used `return` instead of `print()`?

And that we took the output of `return_hi()` and stored it into `greeting`?

And also how we appended `!` into `greeting`?

Before finally printing the final result!

Very cool, eh?

Welp, that's all to it!