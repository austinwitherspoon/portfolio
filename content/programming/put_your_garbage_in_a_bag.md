Title: Put your garbage in a bag! (Python type hints)
Date: 2023-08-18
Modified: 2023-09-06
Category: Programming
Tags: python, programming, type-hints
Slug: put-your-garbage-in-a-bag-python
Authors: Austin Witherspoon

I love type hints. I learned how to code in PHP and Javascript in the 2000's, with no types, no IDE auto-completion - it worked, but it was messy.

Eventually I moved to Java, learning how to make Minecraft mods. There was _some_ documentation, but not much. This is when I learned how magical "strong typing" can be. When you're a kid learning to program you can feel pretty helpless, but Java's strong typing along with help from the IDE meant that I could _discover how these libraries worked on my own_. No documentation needed. I realized that my IDE could tell me what things were, how they worked, and how I could interact with them.

Eventually after graduating film school, I got a job at a VFX company and started learning Python as a way of automating my work tasks. _I was thrown back into my earlier childhood years of PHP and Javascript - no typing, no auto-complete, sometimes writing code in Notepad._ I had come full circle from weak typing to strong typing and back again, and realized it _sucks_ to not have your tools help you.

Now, I want to clarify - I love Python. It makes me happy.

But we can use it better!

If you're reading this, you likely already know python type hints. (_Even if you're working in the film industry, where for some reason we're still stuck on python 2 years after it reached end of life!_) My goal isn't to teach you how they work - there's plenty of tutorials out there. My goal is to make you _care_ about type hints, at least in the most critical places in your code.

# Put your garbage in a bag

Look, I know you may not want to use type hints. It's annoying, it's extra work, I get it.

But my philosophy has become this - at the very minimum, you should by putting extra effort into the borders between your code and somebody else's code.
You gotta bag your shit.

<!-- PELICAN_END_SUMMARY -->

Everybody writes bad code sometimes. Our world is built on terrible, horrible, no good, very bad code. Frankly it's terrifying.

But the system functions because we can interface with it, and it works!

At the end of the day, I don't care how `submit_to_other_department()` works, I just care *that* it works. I use hundreds of apps and tools every day and have no idea what they're doing on the inside. As a developer, I do the same thing with a lot of code! I don't have time to understand the inner workings of every single module we have at a large company. Code that other teams are responsible for (It's good to learn, but you can only do so much in a day!) There's a certain point where you have to trust that it will work, and make a ticket if it doesn't.

Let's take a look at that simple `submit_to_other_department()` example-
Let's assume I'm new to the company and this code, but my boss pointed me in the right direction that we have some library code to submit some forms to another department.

Now there could be a internal wiki page about this module and it's functions, maybe some readthedocs pages, and that would be great! But frequently, there isn't.

If I import that function and hover over it in VS Code, it might look like this:

```python
def submit_to_other_department(package: Any) -> Any:
	...
```

Oh no.
What's a package? Do I get a confirmation number back? Is there a god?

But if somebody had added type hints and a docstring to this, it would be way better!

```python
def submit_to_other_department(package: PackageDict) -> None:
	"""Submits a package dictionary to the database.
	Raises DuplicatePackage or DatabaseError.
	"""
```

Wow! Even in this bad example, I understand the code immediately a lot better. Let me right click on PackageDict and Jump to Definition-

```python
class PackageDict(TypedDict):
	name:str
	message:Optional[str]
	sender_id:int
	...
```

By adding type hints to this function, I can now return to the magic I once experience in Java! I can right click on things and see what they are. I can start typing and have PackageDict auto-complete key names!

And anything that the type hints didn't cover (exceptions? important gotchas?) can be in the docstring!

This is putting your garbage in a bag - I don't care if you type hint your code. It doesn't matter to me _how_ `submit_to_other_department()` works. By adding type hints to the function, I don't need documentation. I can explore and learn about your module without ever leaving my editor. Go ahead! Ignore all type hints inside the body of the function. Just, for the love of god, be kind and document what your function expects and returns.

As a programmer, I'm wildly more efficient when I work with code like this. And now, I try to write code that does this too, as a courtesy to all of my coworkers and all who will work here after I'm gone one day.

Utility scripts? Don't even worry about type hints (unless you really want to!)
Private methods? Who cares (maybe it's still a good habit to make though!)
Dataclasses? Pydantic? Who cares! (They're great though if you're interested!)
Inside of your function? Fuck it! (Pylance will probably do this automagically if your arguments are hinted anyway!)


You can write garbage code, but please give it to me in a nice, labeled, type hinted bag.