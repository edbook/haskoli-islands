# SphinxScrolldepth
A Sphinx Extension implementing the Scroll Depth extension for Google Analytics.

This extension adds a HTML code snippet under each subsection in your Sphinx document. These code snippets define html elements which are then tracked using the Scroll Depth extension for Google Analytics.

More info on Scroll Depth: scrolldepth.parsnip.io

How to find and analyze info from Scroll Depth: https://medium.com/google-analytics/hacking-google-analytics-24762924fbf8#.v5okjcm6o

# Set up
1. Copy the SphinxScrolldepth folder to you Sphinx Project.
2. Navigate to SphinxScrollDepth and run the following commands:

	>>python setup.py build

	>>sudo python setup.py install

3. Copy 'jquery.scrolldepth.js' to your '_static' directory.
4. Add 'scrolldepth.scrolldepth' to your list of extensions in 'conf.py'.
5. Copy 'layout.html' to your '_templates' directory. If there already exists a custom layout file then copy the contents of 'layout.html' to that file (be careful to copy each bit of code to the correct place in the file). Note that SphinxScrolldepth requires jQuery, make sure that jQuery is available.
6. Add to 'layout.html' your Google Analytics tracking code to the indicated line. The Google Analytics tracking code can be found at analytics.google.com under ADMIN > Tracking Info > Tracking Code and should look similar to this:

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-123455678-1', 'auto');
  ga('send', 'pageview');


Note: By default only subsections are tracked. Scroll Depth supports tracking of other events of interest, e.g. Percentage-based tracking, User interaction and tracking of other website elements. These can be enabled in the 'layout.html' file. See scrolldepth.parsnip.io for more info.