### Pontomenos App
---
Pontomenos is an application for tracking time points worked. It was made for a presentation at my current company, @Mercos, which consists of teaching and demonstrating concepts about the rabbitMQ tool and messaging queues.

### Installation

You may be able to use any version, but i strong recommend `python==3.10`. <br>
After that, run `pip install -r requirements.txt` to install dependencies.

> 💭 Don't forget to already have rabbitMQ installed in your computer

Almost done! Now create an python file as `constants.py`, copy/past the code below and change with your credentials.

```py
# default credentials for rabbitMQ
HOST = 'localhost'
PORT = 5672
USERNAME = 'guest'
PASSWORD = 'guest'
```

### Running

Start the consumer agent

```py
python3 main.py consume
```

And now publish messages in queue:

```py
python3 main.py publish [description] [device] [count_to_publish]
```

example:

```py
python3 main.py publish "going out for lunch" "desktop" 1
```

You will be able to see this message in about 1 to 5 seconds on your consumer

example:

```
 I get the message!
 Let's start digging, it might take a while! expected time: 5s
=== Your clock in ========= 
 time: 27/09/2023 - 21:56:47
 description: going out for lunch
 device: desktop
 hash: 7d8d8199-7f7c-4d9d-94de-9e68699f31c0
===========================
```

#### Feel free to contribute :)
