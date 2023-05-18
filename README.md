---
title: Concordia CS 331 Software Engineering Web Development Project
author: Ian Kollipara
date: Wednesday May 17, 2023
---


# Introduction
Welcome to your first foray into Web Development!
My name is Ian, and I am a former student of Concordia tasked with developing this part of the curriculum.
Web Development is a huge beast, and this is only a small taste of what is included.
If you are more interested, please feel free to contact me at [ian.kollipara@gmail.com](mailto:ian.kollipara@gmail.com).

This project is divided by commits, with each commit adding in more details to the project.
This is for the first real commit.

# Tools of the Trade
In web development there are two key concepts to understand:
1. Backend
2. Frontend

## Backend
Let's start with the first one: Backend.
Backend is the term used for what runs on the server, or rather not in the browser.
This is where languages you might've heard of run, these include:
- Python
- Scala
- Java
- C#
- PHP
- F#

In our case, we will be working with Python.
Most of you should have some familiarity with Python, which should aid you on your journey.
However, there will be features used in Python you may not be familiar with, which we will cover
when we get there.

The backend is where we do actions such as:
- Interacting with the database
- Authenticating with a third party^[A third party is anything that isn't your application]
- Secretive Business Logic

Now our application won't have too much secret knowledge, but we will need to work with a database, and 
authenticate with a third party.

## Frontend
Now, on the frontend.
This is really just anything that runs in the browser.
Basically, this is the "website" part of the application.
This is what the person visiting your site will see.

There are a few technologies in this space.
The 3 most important are:
- HTML: The Content
- CSS: The Style
- Javascript: The Interaction

Nowadays there are a lot of ways to provide these three pieces, we will look at 3 of them in this application.
1. Templated HTML using the [Jinja Templating Language](https://jinja.palletsprojects.com/en/3.1.x/)
2. Using a Javascript Frontend Framework (In our case Vue)
3. Using a compile-to-js language (Elm)

These 3 were chosen to show both the differences and similaries of each approach to better understand how we can use
each.

# Task 1: Installing the Dependencies
Alright, enough talk!
Let's write some code, or rather set up our development environment.

We will be using a tool called [Poetry](https://python-poetry.org/).
Poetry is a tool for managing a Python development environment^[We use tools like these to help automate our environment. We want something to declare what libraries and other things we are using. Tools like Poetry exist in other languages too, think `package.json` in the JS world.]
First, you want to install poetry, which myself or Prof. Gubanyi should have done.
Now open a terminal and run 
```bash
poetry --version
```
This should give some output, which means its installed correctly.
Now run
```bash
poetry init
```
Follow through the prompts, naming your project **holidays**.
Then just press enter through the rest of the settings.
Now keep that terminal open, and run the following commands
```bash
mkdir holidays tests
touch holidays/__init__.py tests/__init__.py
poetry add -G dev black pytest
poetry install
```

What we've done here is initialize our project structure, and add two development dependencies.
Development dependencies are things you need only when developing the code, not when you're running it.
In our case, we added a formatter and a testing library to our development dependencies.

Now, we created two weird python files, both of which have the name `__init__.py`.
Think back to classes, we know that `__init__` is the constructor, and in this case `__init__.py` is our
package constructor.
A package is one unit bigger than a module, which is one unit bigger than a class.
We will organize around packages and modules over classes, as classes are not always needed and Python can be
written without one.

Now open that `holidays/__init__.py` and add the following:
```python
"""
Holidays
--------
"""

print("Hello World")
```

Now run 
```bash
python holidays/__init__.py
# => Hello World
```
Congrats on starting this project!
