# imports
import os
import urllib

from gi.repository import Nautilus, GObject, GConf

ATOM_KEY = '/apps/nautilus-open-atom/exec'  # ATOM_KEY in GConf
ATOM_Default = '/usr/bin/atom'

class OpenAtomExtention(Nautilus.MenuProvider, GObject.GObject):
    """
    OpenAtomExtention class
    Derives from Nautilus.MenuProvider
    """
    def __init__(self):
        print "Initializing nautilus-open-atom extension"
        self.client = GConf.Client.get_default()  # Find GConf Settings

    def _open_atom(self, file):
        filename = urllib.unquote(file.get_uri()[7:])
        atom = self.client.get_string(ATOM_KEY)  # Find Atom from GConf to exec

        # Check if GConf key was exist
        if not atom:
            atom=ATOM_Default

        # Check if the request is for a directory
        if file.is_directory():
            os.chdir(filename)
            os.system('%s &' % atom)
        else:  # Atom must open a file
            print '%s %s &'.format(atom, file)
            os.system('%s %s &'.format(atom, file))

    def menu_activate_cb(self, menu, file):
        self._open_atom(file)

    def menu_background_activate_cb(self, menu, file):
        self._open_atom(file)

    def get_file_items(self, window, files):
        """
        Triggers if right clicking on a file/directory
        :file file/directory that clicked open
        """
        if len(files) != 1:  # Just open a file/directory
            return

        file = files[0]
        # Creating the menu item
        item = Nautilus.MenuItem(name="NautilusPython::openatom_item",
                                label='Open in Atom',
                                tip='Open %s in Atom' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return item,


    def get_background_items(self, window, file):
        """
        Triggers if right clicking on background
        :file the directory that are in
        """
        # Creating the menu item
        item = Nautilus.MenuItem(name='NautilusPython::openatom_item',
        label='Open in Atom',
        tip='Open Atom in this directory')

        item.connect('activate', self.menu_background_activate_cb, file)
        return item,
