#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def rataMensile(self, radiobutton):
        if radiobutton.get_active():
            print("rataMensile")

    def rataSemestrale(self, radiobutton):
        if radiobutton.get_active():
            print("rataSemestrale")

    def calcolaRate(self, button):
        print ("a Morris piace il pinnacchio")

GUI = '/home/medeo/coding/abandoned/rate/rate2015/guimockup.ui'
builder = Gtk.Builder()
builder.add_from_file(GUI)
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
