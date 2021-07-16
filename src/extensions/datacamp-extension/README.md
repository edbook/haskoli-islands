## Installation

Windows:

```bash
$ python setup.py build
$ python setup.py install
```

Mac/Linux:

```bash
$ python setup.py build
$ sudo python setup.py install
```
Move `datacamp-custom.css` to `_static/css` in the root of your project. 
Add `datacamp-extension.datacamp.datacamp` `datacamp.datacamp` to your extensions in `conf.py`. 
## How to use it
* **Python**
To install packages/libraries behind the scene use 
```
:library: datetime, numpy as np
```
This will result in:
```python
import datetime
import numpy as np
```
Without the user knowing. It's also possible to import libraries with the rest of your code.
[List of supported python packages](http://documents.datacamp.com/default_python_packages.txt)
**Examples**
```
.. datacamp::
    :lang: python
    :libary: numpy as np, matplotlib.pyplot as plt
    
    import matplotlib.animation as animation
    
    fig = plt.figure()
    def f(x, y):
        return np.sin(x) + np.cos(y)
    x = np.linspace(0, 2 * np.pi, 120)
    y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
    im = plt.imshow(f(x, y), animated=True)
    def updatefig(*args):
        global x, y
        x += np.pi / 15.
        y += np.pi / 20.
        im.set_array(f(x, y))
        return im,
    ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
    plt.show()
```
* **R**
To install packages/libraries behind the scene use 
```
:library: datetime, numpy as np
```
This will result in:
```r
import datetime
import numpy as np
```
Without the user knowing. It's also possible to import libraries with the rest of your code.
[List of supported R packages](http://documents.datacamp.com/default_r_packages.txt)
**Examples**
```
.. datacamp::
    :lang: r
    :library: ggplot2

    options(scipen=999)  # turn-off scientific notation like 1e+48
    theme_set(theme_bw())  # pre-set the bw theme.
    data("midwest", package = "ggplot2")
    gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
        geom_point(aes(col=state, size=popdensity)) + 
        geom_smooth(method="loess", se=F) + 
        xlim(c(0, 0.1)) + 
        ylim(c(0, 500000)) + 
        labs(subtitle="Area Vs Population", 
        y="Population", 
        x="Area", 
        title="Scatterplot", 
        caption = "Source: midwest")
    gg
```
R is the default language if :lang: option is not set.
If you want to use a package that is not available, create an issue on [datacamps github](https://github.com/datacamp/datacamp-light/issues) and they can install it (it's not possible to install packages at runtime).