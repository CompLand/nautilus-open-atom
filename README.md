# nautilus-open-atom
Nautilus extension to open Atom in the current directory  
Written by [CompLand Team](compland.ir)  
Mahdi Fooladgar (@professormahi)


# Requirements
This extension needs `python2.7` and all other packages that are mentioned in `requirements.txt` file, to install them on Debian based Linux systems:  
```bash
$ apt-get update && apt-get install python2.7 \
                    python-nautilus \
                    python-gconf \
                    gir1.2-gconf-2.0 -y
```

# Install
There are two way of installing :
#### Source Code
To install using source code first you must `clone` this repository and then you need to put the [python file](nautilus-open-atom.py) in one of the paths bellow:  
1. `$XDG_DATA_DIR/share/nautilus-pyhton/extentions` to add extension for all users  
2. `~/.local/share/nautilus-python/extensions/` to add extension to your own nautilus file manager

Then after restarting the `nautilus` using `nautilus -q` you have extension in you nautilus

#### Debian package
To install `nautilus-open-atom` extension in Debian based system just download the [deb file](nautilus-open-atom_0.9.deb) and the use `dpkg` to install it:  
```bash
$ dpkg -i nautilus-open-atom.deb
```
