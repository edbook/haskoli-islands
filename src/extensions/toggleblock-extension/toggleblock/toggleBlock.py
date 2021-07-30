#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import directives

try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive

TB_COUNTER = 0

js_showhide = """\
<script type="text/javascript">
    function showhide(element){
        if (!document.getElementById)
            return

        if (element.style.display == "block")
            element.style.display = "none"
        else
            element.style.display = "block"
    };
</script>
"""


def nice_bool(arg):
    tvalues = ("true", "t", "yes", "y")
    fvalues = ("false", "f", "no", "n")
    arg = directives.choice(arg, tvalues + fvalues)
    return arg in tvalues


class beginToggle(nodes.General, nodes.Element):
    pass


class endToggle(nodes.General, nodes.Element):
    pass


def beginToggle_visit(self, node):
    """Visit toggleable text block"""
    global TB_COUNTER
    TB_COUNTER += 1

    fill_header = {
        "divname": "toggleblock{0}".format(TB_COUNTER),
        "startdisplay": "none" if node["starthidden"] else "block",
        "label": node.get("label"),
    }

    divheader = (
        """<div class="admonition note"><p class="first admonition-title"><a href="javascript:showhide(document.getElementById('{divname}'))">"""
        """{label}</a></p>"""
        """<div id="{divname}" style="display: {startdisplay}"><br/>"""
    ).format(**fill_header)

    header = js_showhide + divheader
    self.body.append(header)


def beginToggle_depart(self, node):
    pass


def tex_beginToggle_visit(self, node):
    pass


def tex_beginToggle_depart(self, node):
    pass


def endToggle_visit(self, node):
    self.body.append("</div></div>")


def endToggle_depart(self, node):
    pass


def tex_endToggle_visit(self, node):
    pass


def tex_endToggle_depart(self, node):
    pass


class BeginToggleDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = dict(starthidden=nice_bool, label=str)

    def run(self):
        bt = beginToggle()
        bt["starthidden"] = self.options.get("starthidden", True)
        bt["label"] = self.options.get("label", "|>")

        return [bt]


class EndToggleDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        et = endToggle()

        return [et]


def setup(app):
    app.add_node(
        beginToggle,
        html=(beginToggle_visit, beginToggle_depart),
        latex=(tex_beginToggle_visit, tex_beginToggle_depart),
    )
    app.add_node(
        endToggle,
        html=(endToggle_visit, endToggle_depart),
        latex=(tex_endToggle_visit, tex_endToggle_depart),
    )
    app.add_directive("begin-toggle", BeginToggleDirective)
    app.add_directive("end-toggle", EndToggleDirective)

    return {"version": "0.3"}
