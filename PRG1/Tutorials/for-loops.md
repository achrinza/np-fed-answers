# For loops

At the end of this tutorial, you'll learn:

* For-loops vs while-loops
* * When to use for-loops
* * How are for-loops simplier than their while-loop counterpart
* For-loops to iterate over each item in a list
* For-loops with range()
* * Using range() to create an auto-incrementing `i` variable
* Combining iteration over each item and range() using enumerate()
* For-loops with zip()
* * Use cases where zip() is useful
* * Using zip() to iterate multiple lists simultaneously
* Combining enumerate() and zip()

## For-loops vs while-loops

Let's say we have a list of users.

```python
users = [
    "Adam Levi",
    "Tony Tank",
    "Richard Lee",
    "Atmos Wee",
    "Pula Utin"
]
```

If we wanted to print all of the users, we could use a while-loop.

```python
i = 0
while i < len(users):
    print(users[i])
    i += 1
```

Noticed how we had to:

1. Manually declare `i` outside the while-loop
2. Manually increment `i` at the end of the while-loop

These are error-prone as they add unecesssary complexity:

1. `i` is acccessible outside the while-loop
2. `i` may be accidentally not incremented

So what if we re-wrote this using a for-loop?

```python
for user in users:
    print(user)
```

Wow, wasn't that much easier? We didn't even need to worry about an `i` variable!

That's the magic of for-loops.

---

What if we wanted to print a number next to the name? Something like this...

```plaintext
1. Adam Levi
2. Tony Tank
3. Richard Lee
4. Atmos Wee
5. Pula Utin
```

Well, we could use range() to loop through the length of the list...

```python
for i in range(len(users)):
    print(str(i) + ".", users[i])
```

But now we have to manually pull up the current user using the `[]` index notation. Furthermore, we now have clunky `range(len(users))` nesting!

What if we could have the for-loop give us both the current index and the current user's name?

That's enumerate() to the rescue! If we incorporated it, we would now have...

```python
for i, user in enumerate(users):
    print(str(i) + ".", user)
```

Ain't that simple? That prints exactly the same as the previous code (without `enumerate()`), but now it's much simpler! No longer do we have to deal with `users[i]` or `range(len(users))`.

---

Now we've decided to allow our program to output the users' name *and* their account balance.

In this case, the users' account balance is given as a separate list for some weird reason...

```python
users_balance = [
    101,
    3024,
    540,
    1235,
    52
]
```

But we're in luck! The first balance in `users_balance` belongs to the first user in `users`, the 2nd user balance belongs to the 2nd user, and so on.

We can take advantage of this.

We could use `range()` to leverage the current index to recall the current user and their balance with the `[]` index notation.

```python
for i in range(len(users)):
    print(str(i) + ".", users[i], "-", users_balance[i])
```

That'll give us...

```plaintext
1. Adam Levi - 101
2. Tony Tank - 3024
3. Richard Lee - 540
4. Atmos Wee - 1235
5. Pula Utin - 52
```

But now the same problems has re-appeared! the weird `range(len(users))` nesting and the need to use `[]`.

That's where `zip()` comes in handy! Let's try it...

```python
for user, balance in zip(users, users_balance):
    print(users, "-", users_balance)
```

Wait a minute, we've lost our numbering! Not to worry, we can combine `zip()` with `enumerate()`!

```python
for i, (user, balance) in enumerate(zip(users, users_balance)):
    print(str(i) + ".", user, "-", balance)
```

Ok, hold up. Why are `user` and `balance` in parenthesis `()`?

Well, we've just nested `zip()` inside `enumerate()`.

If we didn't use `()`, we'd need to change our code to as follows:

```python
for i, user in enumerate(zip(users, users_balance)):
    print(str(i) + ".", user[i], "-", balance[i])
```

Notice how `user` became a list? By using `()` we're telling the for-loop to deconstruct the list into separate variables.

In layman terms, take the first and second items of the list and store them into `user` and `balance` respectively.

How nifty is that?