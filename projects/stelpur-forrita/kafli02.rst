Day 1 - Git and GitHub
======================

Given access to an online repository on GitHub such as `this example repository <https://github.com/mitaerika/example-repo>`_, 
developers can clone the project to their machine and work with them locally.

Say that we have this file directory ``C:\Users\username\Documents`` and we want to put the project under Documents like so: ::

    C:/
    |- Users 
        |- username
            |- Documents
                |- <new location for the project folder>

Then we do the following:

1. Open the Command Line Interface (CLI).
On Windows, it is called the Command Prompt (shortcut: `Windows+r` key then type `cmd`).
On Mac or Linux systems, it is called the Terminal (shortcut: `Command+r` key).

2. Navigate to the correct directory ``C:\Users\username\Documents``.
We can go further down the directory with ``cd``.

3. Get the repository web url, this is usually the url of the repository ending with ``.git``.

.. image:: myndir/weburl.png
   :width: 600

4. Run the following code

.. code-block::

    git clone <weburl>

5. Success metric: The project folder for ``example-repo`` exists at ``C:\Users\username\Documents\example-repo``.
