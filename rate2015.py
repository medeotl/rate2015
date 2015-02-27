#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class Handler:
    k = 9000 ; v = 1200 # valori iniziali per rata mensile
    J = 8 # valore costante per calcolo interessi

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def rataMensile(self, radiobutton):
        if radiobutton.get_active():
            self.k = 9000
            self.v = 1200

    def rataSemestrale(self, radiobutton):
        if radiobutton.get_active():
            self.k = 1500
            self.v = 200

    def calcolaRate(self, button):
        print (self.k, self.v, self.J)

GUI = '/home/medeo/coding/abandoned/rate/rate2015/guimockup.ui'

builder = Gtk.Builder()
builder.add_from_file(GUI)
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
