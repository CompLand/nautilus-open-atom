import os
import urllib

from gi.repository import Nautilus, GObject, GConf

ATOM_KEY = '/apps/nautilus-open-atom/exec'

class OpenAtomExtention(Nautilus.MenuProvider, GObject.GObject):
    """OpenAtomExtention class"""
    def __init__(self):
        print "Initializing nautilus-open-atom extension"
        self.client = GConf.Client.get_default()

    def _open_atom(self, file):
        filename = urllib.unquote(file.get_uri()[7:])
        atom = self.client.get_string(ATOM_KEY)

        if not atom:
            atom='/usr/bin/atom'

        if file.is_directory():
            os.chdir(filename)
            os.system('%s &' % atom)
        else:
            print '%s %s &'.format(atom, file)
            os.system('%s %s &'.format(atom, file))

    def menu_activate_cb(self, menu, file):
        self._open_atom(file)

    def menu_background_activate_cb(self, menu, file):
        self._open_atom(file)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return  # TODO Change

        file = files[0]

        print file.get_name()
        item = Nautilus.MenuItem(name="NautilusPython::openatom_item",
                                label='Open in Atom',
                                tip='Open %s in Atom' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return item,


    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(name='NautilusPython::openatom_item',
        label='Open in Atom',
        tip='Open Atom in this directory')

        item.connect('activate', self.menu_background_activate_cb, file)
        return item,
