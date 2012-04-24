Introduction
############

In 2006 Gina Trapani first published the first CLI script for a todo.txt-file
on the blog `Lifehacker`_.
The format is a nice and easy way of keeping track of a busy life. The cli,
the format and concept is described at the `todotxt`_-web site.

A problem with the simple todo list as e text file, is that there is a fair 
deal manual work needs to be performed to keep the list manageable:

1. New items must be added
2. Items must be marked as done
3. Done items must be removed
4. The list must be sorted

An advantage with the text file format is however the great deal of automation 
that is possible. This software deals with the points 3 and 4 from the list
above. The thought is to have the software running automatically every night,
or other time not using the list, so that every morning yesterdays messy old
list is cleaned up and ready to be used to get things done.

Comparison to the todotxt-CLI
*****************************

The main purpose of the CLI is to ease the manual manupilation of a todo.txt
file. Autotodotxt has a different scope. It is specifically designed to be
called by Cron or other operating system schedulers.

.. _todotxt: http://todotxt.com/
.. _lifehacker: http://lifehacker.com/
