#!/usr/bin/python3
# -*- coding: utf-8 -*-

# impostare delete-event di GtkWidget a onDeleteWindow in GLADE per la finestra
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

gui2betested = './finestraPrincipale.ui'
builder = Gtk.Builder()
builder.add_from_file(gui2betested)
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.set_default_size(350,170)
window.show_all()

Gtk.main()
