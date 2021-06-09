If you want to use this folder as a clone of the repository and update with
new versions of the macros, you need to perform a **sparse checkout** with git.
`The steps to do a sparse clone are as follows::

   git clone <reauthoring repo URL> Reauthoring
   cd Reauthoring

This creates the repository with a clone of the remote files. Then do::

   git config core.sparsecheckout true

Now define which files/folders you want to check out by listing them in 
``.git/info/sparse-checkout``::

   echo "/Sphinx_ext" >> .git/info/sparse-checkout

Update the repository with the directories just selected:: 

   git read-tree -m -u HEAD
