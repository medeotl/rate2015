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
        percentuale = builder.get_object( "percentuale" ).get_value_as_int()
        nro_rate = builder.get_object( "nro_rate" ).get_value_as_int()
        if percentuale * nro_rate < self.k :
            # errore!
            dialog = builder.get_object( "error_percentuale_dialog" )
            dialog.run()
            print("ERROR dialog closed")

            dialog.hide()
        print (percentuale, nro_rate)

GUI = '/home/medeo/coding/abandoned/rate/rate2015/guimockup.ui'

builder = Gtk.Builder()
builder.add_from_file( GUI )
builder.connect_signals( Handler() )

window = builder.get_object( "window1" )
window.show_all()

Gtk.main()
