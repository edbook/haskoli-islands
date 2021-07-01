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

Add the following lines to the conf.py file in the root directory

```python
katex_path = 'https://cdn.jsdelivr.net/npm/katex@0.10.0-rc/dist/katex.min.js'
katex_render = 'https://cdn.jsdelivr.net/npm/katex@0.10.0-rc/dist/contrib/auto-render.min.js'
render_math = 'rendermath.js'
katex_css = 'https://cdn.jsdelivr.net/npm/katex@0.10.0-rc/dist/katex.min.css'
```

Add `katex.katex` to your extensions in `conf.py`. NOTE, in the list of extension, katex must come before sagecell.
Finally move rendermath.js to the /_static directory in the root of your project. </br>
Note that you can follow the when they issue the latest version at:
https://github.com/Khan/KaTeX/releases

## How to use it

Has the same functionality as MathJax

## Latex/katex - known problems
### List of commands
- `\mbox`
- `\label`
- `\nonumber`
- `{\cal (*)}`
- `\` - single backslash spacing - note that version 0.10.0 eliminates this problem but is still in alpha testing
- `\begin{align} - \end{align}`
- `\root (*) \of (*)`

### Substitution suggestions
List of substitutions which work but are open for modification
- (*) is used to represent inputs, when multiple they are to be interpreted respectively in the New column
- "-" means it can be left empty without affecting the html endproduct
- clean_rst.py is a script with regular expressions which finds and replaces with the following solutions.
- To run just navigate to /katex-extension and run 'python(3) clean_rst.py'

<center>

| Old        | New           |
| ------------- |:--------------|
| `\mbox`      | `\text` |
| `\label`      | -      |
| `\nonumber` | -      |
| `{\cal (*)}` | `\mathcal{(*)}`      |
| `\begin{align} - \end{align}` | `\begin{aligned} - \end{aligned}`      |
| `\root (*) \of (*)` | `\sqrt[(*)]{(*)}`      |

</center>

