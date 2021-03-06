from tempfile import NamedTemporaryFile
import os

import NimLime
from sublime_plugin import TextCommand
from sublime import Region
from utils.misc import NimLimeMixin
from utils.idetools import Idetools

import sublime

# Resources
# http://sublimetext.info/docs/en/extensibility/plugins.html
# http://www.sublimetext.com/docs/2/api_reference.html#sublime.View
# http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/
# http://www.sublimetext.com/docs/plugin-examples

NimLime.add_module(__name__)

class LookupCommand(TextCommand, NimLimeMixin):

    def run(self, edit):
        filename = self.view.file_name()
        sels = self.view.sel()

        if filename is None or not filename.endswith(".nim"):
            return

        for sel in sels:
            pos = self.view.rowcol(sel.begin())
            line = pos[0] + 1
            col = pos[1]

            Idetools.lookup(self, False, filename, line, col)