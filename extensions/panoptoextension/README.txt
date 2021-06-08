This module defines a directive, `ggb`.  It takes a single, required
argument, a geogebra tube ID::

    .. ggb:: 1264951

The referenced geogebra applet will be embedded into HTML output.  
Installation
============
   1. Install this extension: 

    python setup.py build
    sudo python setup.py install  OR  python setup.py install --user

   2. Move 'layout.html' and 'resizegg.js' to your '_templates' directory 
    (if there is already a custom layout file then copy lines 2-7 of 
    'layout.html' and paste to that file).    

    3. Add 'ggbextension.ggb' to your extensions in 'conf.py'

Options
=======

There are 5 optional parameters.
"width" and "height" are the applet width and height, the defaults are 700 px width and 400 px height. 

"img" is the location of an image file to be put in place of the applet into latex output, relative to the _build/latex folder (or wherever the generated latex output ends up). If the img parameter is not listed no image is included in the output. 

"imgwidth" is the width of that image, default value is 8cm.

 
"zoom_drag" (default setting: false) to control whether the user can drag the applet image around and zoom in and out.

.. ggb:: 1264951
    :width: 846
    :height: 664
    :img: ../../_static/hi_logo.jpg
    :imgwidth: 4cm
    :zoom_drag: true 

