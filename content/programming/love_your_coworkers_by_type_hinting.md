Title: Love Your Coworkers By Type Hinting
Date: 2023-08-18
Modified: 2023-08-18
Category: Programming
Tags: python, programming, type-hints
Slug: love-your-coworkers-by-type-hinting
Authors: Austin Witherspoon

# You should be using type hints in your python code!

I'm not going to force you, I won't reject your pull request - but if you care about your codebase and your coworkers, you should type hint your code.

Now I want to first get the obvious out of the way-

- I'm **not** saying you need to type hint every single variable
- I'm **not** saying you need to type hint every single utility script

## Your editor should do the work for you 90% of the time

I'm a python developer, writing most of my python in VS Code. I've installed the Python extension, and all of my code gets run through Pylance. Pylance is going to attempt to *✨magically✨* deduce the types of everything it possibly can!

So this is not necessary:

```python
clearly_a_string: str = "this is a string."
```

Even without the `: str`, if I hover over `clearly_a_string` in vs_code, it will tell me it's type!

![Screenshot of VS Code inferring the type of a variable](/static/clearly_a_string.jpg)

## When you actually need types

Image this- you just started a new job at the *frombulator factory*. What's a frombulator? No idea! You've been hired to code, not to ask questions!

Your first task is to debug some code crashing from the following exception: `TypeError: 'NoneType' object is not iterable`

```python
def fromble_all_sklunks(sklunks, querker, schlamp_connection):
	logger.debug("Prefromble cleanup")
	frombulator_core.prep(sklunks, schlamp_connection)

	logger.debug("kleenching all pips")
	pips = schlamp_connection.get_all()
	for pip in pips:
		pip.kleench(sklunks[-1])

	logger.debug("main frombulation")
	return frombulator_core.process(sklunks)
```

Imposter syndrome kicks in, sweat pooling in your socks. You're afraid to ask your manager or coworkers too many questions on your first day, and everybody is acting like kleenching is normal.

What is a sklunk?

Why are we pipping things?

Is there a god?

Normally, you'd need to take a fifteen minute break and then hop onto the development wiki to read all about shlamp connections. Half your afternoon will be spent trying to search for every industry keyword you can think of.

## Code can be documentation, if you let it

Let's take that example and type hint it:
<!-- PELICAN_END_SUMMARY -->

```python
def fromble_all_sklunks(sklunks:List[Sklunk], querker:str, schlamp_connection:Schlampper) -> FrombleResult:
	logger.debug("Prefromble cleanup")
	frombulator_core.prep(sklunks, schlamp_connection)

	logger.debug("kleenching all pips")
	pips: Optional[List[Pip]] = schlamp_connection.get_all() # in the real world, this would be automatically inferred!
	for pip in pips:
		pip.kleench(sklunks[-1])

	logger.debug("main frombulation")
	return frombulator_core.process(sklunks)
```

It's hard to convey the benefit entirely in a blog post, because the actual benefit is *interactive*.
You can hover over `schlamp_connection` and read the docstring about the Schlampper!

Right click on `Pip` and read about what a pip is.

You don't even need to leave your editor. Screw the wiki. Everything is right here in front of you.

That's the beauty of type hints that every Java programmer already knows - reading code should be *easy*. Questions can be answered by hovering, maybe quickly jumping to another file.

And of course, not to mention that adequate type hints will also allow your editor to *highlight errors* for you!

With type hints, VS Code might immediately highlight `for pip in pips:` red, since pips might equal `None`!

## Functions are the most important place to type hint

I'll say it again - types are automatically inferred whenever possible by your editor!

Take this:
```python

def repeat_five_times(obj):
    return [obj for _ in range(5)]

test = repeat_five_times("hello") # type: ???
```

This mysterious function does.. something. Obviously as a human we can read it, but our editor might not!
> Note: Pylance is actually smart enough to figure this one out, but I needed a simple example.

Now `test` remains a mystery for the rest of our script! This can actually infect other code, because the moment you let this `Any` type, it can impact Pylance's ability to infer *other* things too. Eventually you end up with the same thing you see the moment a system gets complicated enough - Pylance has no idea what anything is anymore.

```python
from typing import TypeVar

T = TypeVar('T')
def repeat_five_times(obj:T) -> list[T]:
    return [obj for _ in range(5)]

test = repeat_five_times("hello") # type: List[str]
```


### But pylance can never infer the types handed to a function!

A function is a sort of mystery box to the type checker - There's no logic it can use to deduce anything, since technically our code can throw anything at a function!

Just because our code looks like this:
```python
clearly_a_string = "test"

def process_a_string(value):
	# do string stuff

process_a_string(clearly_a_string) # ???
```

It's not safe for Pylance to assume anything! For all we know, we could have another file somewhere that calls `process_a_string(5)`

## So always type hint function arguments (and if you're in a good mood, return types)!
We want to be lazy, and Pylance will let us be lazy most of the time.

If you type hint your function arguments, that information can be carried through the function body, and with any luck beyond that function!

If every (major) function in your code base is type hinted, you'll start seeing type hints appear in places you never expected.

... And the moment you see those type hints, you're communicating to other developers, and to your editor!

Your editor will start showing you errors in your code before they happen!

Your new coworker will be able to hover over stuff to see what they are!

Life will be slightly better for everybody.