# Google-Analytics extension
A Sphinx Extension implementing Google Analytics and a custom Scroll Depth extension.

Upon calling this extension it produces a gtag tracking code for each site except index.html which is of no interest to us.

This extension can furthermore add a HTML code snippet under each subsection in your Sphinx document. These code snippets define html elements which are then tracked using the Scroll Depth extension for Google Analytics. In `conf.py` set `enable_custom_scrolldepth = True` to enable. If disabled i.e. `enable_custom_scrolldepth = False` it will result in scroll events being fired in 25%, 50%, 75% and 100% intervals.

More info on Scroll Depth: scrolldepth.parsnip.io


# Set up
1. Copy the google-analytics folder to you Sphinx Project.
2. Navigate to google-analytics and run the following commands for Mac/Linux:

```bash
$ python setup.py build
$ sudo python setup.py install
```

If you're using windows run:

```bash
$ python setup.py build
$ python setup.py install
```

3. Copy `jquery.scrolldepth.js` to your `_static` directory.
4. Add `analytics.analytics` to your list of extensions in `conf.py`.
5. Note that `jquery.scrolldepth.js` requires jQuery, make sure that jQuery is available.
