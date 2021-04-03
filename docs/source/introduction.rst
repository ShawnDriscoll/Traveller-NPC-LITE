**Introduction**
================

Preface
-------

I am an old-school computer programmer from the 1970s.

That sounded redundant after reading it. Oh well. Hardly anyone still
uses that term these days. Everyone is an app developer now. Or a coder. Most write for phones instead of computers. And their
code is pretty much connected at the hip to the web.

I'll face it, everything is web-based now. Years would go by and I'd think about figuring a way to make my computer programs
work on the Internet. Or at least run in a web browser. But after reading the books and seeing the complications involved, I'd
go back to programming computers the way I knew how.

Like I said before, I've been programming computers for a long time. I've tried so many languages over the years. And when I gave
Python a try, I ceased using anything else. Python was the language I had been waiting for. I have books on C/C++, MS Visual Studio,
BASIC, Lisp, Pascal, FORTRAN, ASM, and so many others that I won't look at again.

One thing nice about Python is that something cool comes out for it every day. Some of the things that have come out are web page
servers, which run in the background on your computer and listen for requests from web browsers. Some have been around for years,
like `Django
<https://en.wikipedia.org/wiki/Django_(web_framework)>`__ and `Flask
<https://en.wikipedia.org/wiki/Flask_(web_framework)>`__.

One doesn't often think "Python" when developing a web site. But it can do the job, surprisingly. Of course, knowing HTML is still
a requirement. The trick is also getting Python to output HTML "code." For that, I recently chose to use `Bottle
<https://en.wikipedia.org/wiki/Bottle_(web_framework)>`__ because it's more minimal compared to Django and Flask.

I spent a day learning Bottle. That's how easy it was to set up and start using. I just wish I had thought of doing it sooner.

-Shawn


Requirements
------------

* **Microsoft Windows**
   
   **TravLITE** has been tested on Windows 10 only.
   It has not been tested on MacOS or Linux.
   
* **Classic Python 2.5**
   
   **TravLITE** was written using the C implementation of Classic Python
   version 2.5.4. Also known as CPython.
   
* **bottle 0.12.13**

   bottle is the web framework used for serving the web page requests.

* **colorama 0.2.7**

   Because CMD may have some colored text messages for debugging.
   
* **py2exe 0.6.9**

   Used by setup_TL.py for making EXEs of the Python code for you. Optional.
   
.. Warning::
   **TravLITE** will not work with **Python 2.6+**.
