# FDS Assignment 1
Hi guys, this is the README, please simply follow along with the instructions
below to get started. I don't know you guys' background, but trust me, this 
is how you properly set up nearly any production project in the real world. So 
please don't be mad at me for going in this specific direction and drag you all 
into this. I think this is genuinely good for real-world preperation.

First of all, you will need either Python 3.12.x or 3.13.x to be able to 
work within this environment. That is due to the fact that earlier versions 
of Python are simply more reliable (see why [here](https://www.python.org/downloads/), you can also 
install Python from that URL).

Once you have Python installed, I personally prefer to use 
[Poetry](https://python-poetry.org/docs/) as my package manager. Please, 
read the docs for further understanding, but the following steps should be 
sufficient to get you started. If something doesn't work, either send me a 
message or just spam an LLM until it work :)

## Setting up the Enviornment
The first step is to install Poetry globally:
```
pip install poetry
```

Move to the project directory:

```
cd ~/path/to/fds_assignment_1 # NOTE: NOT the one in /src !!!
```

Create the virtual environment:

```
poetry install
```

Activate it:

```
$(poetry env activate) # for macOS or Linux
poetry env activate # for Windows
```

Or use `poetry shell` as an alternative.

From here on, you should be good to go. I'd recommend either everyone 
creates their own branch, and we'll come together later, or we actually 
do merges with pull requests and stuff (which is often a pain in the ass).
