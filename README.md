# Moniton

A simple python curses screen dashboard. Used as a monitoring tool by
brodokk for his self-hosted services at home and on some ranted server over the
internet. Can be easly customised for other usages, see Modularity section.

## Usage

For installation it's recommended to setup a virtual env, then install the
package:

```
python -m venv .venv
source .venv/bin/activate
python setup.py install
```

Finally for launch the dashboard, just use the commande `moniton`.

## Modularity

The code has been designed for keep the posibility to easily add or remove
widgets on the screen. The `jobs` folder contains the class who are used to
define those widgets. There is already some widgets configured as example.

When needed a widget can use some customisable variables. The default
configuration file at `~/.config/moniton/config.toml` can be used for that.
For each class inheriting the `Job` class in the `jobs` folder you can put
variables in the section of the same name as the class.

It's a good practice to put some documentation at the top of the file who
contains the job and have only one widget by job file.
