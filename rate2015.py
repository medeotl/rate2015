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
        
        def Do_Loop1(zz):
            x = prestito
            conta = 1
            inter = x * percentuale / self.v
            x = x + inter - e
            print("%d\t %0.2f\t %0.2f\t %0.2f " % (conta, e, x, inter) )
            while True:
                conta += 1
                inter = x * percentuale / self.v
                x = x + inter - e
                if zz == 1: # stampa i risultati
                    print("\t%d\t \t%0.2f\t \t\t%0.2f\t \t\t%0.2f " % (conta, e, x, inter) )
                if conta == nro_rate :
                    break
            if zz == 1:
                print("\n")
                if builder.get_object( "rata mensile" ).get_active():
                    print("   numero rate        rata mensile         capitale residuo          interesse")
                else:
                    print("   numero rate       rata semestrale       capitale residuo          interesse")
            return x

        percentuale = builder.get_object( "percentuale" ).get_value_as_int()
        nro_rate = builder.get_object( "nro_rate" ).get_value_as_int()
        if percentuale * nro_rate > self.k :
            # errore!
            dialog = builder.get_object( "error_percentuale_dialog" )
            dialog.run()

            dialog.hide()
            return    

        # tutte le condizioni verificate, posso effettuare il calcolo
        prestito = builder.get_object( "prestito" ).get_value_as_int()
        e = prestito/nro_rate
        operazioni = 0
        conta3 = 0
        m = 10000000000.0
        lista_m = (         None,       # 0   non verrà mai usato
                   10000000000.0,       # 1
                      1000000000,       # 2
                       100000000,       # 3
                        10000000,       # 4
                         1000000,       # 5
                          100000,       # 6
                           10000,       # 7
                            1000,       # 8
                             100,       # 9
                              10,       # 10
                               1,       # 11
                               0.1,     # 12
                               0.01,    # 13
                               0.01)    # 14  mantengo valore del 13
        percentuale = builder.get_object( "percentuale" ).get_value_as_int()
        while True:
            # ricerchiamo il corretto valore di "e"
            operazioni += 1
            x = Do_Loop1(0)
            print(x)
            if x > 0 :
                e = e + m
            elif x < 0 :
                e = e - m
                conta3 += 1
                m = lista_m[conta3]
                #~ print m
            if (conta3 == 14) or (operazioni == 250) :
                break
        e += 0.001
        x = prestito
        # ora che conosciamo il valore di "e" rifacciamo il calcolo
        # e stampiamolo
        Do_Loop1(1)
        print ("finito!")
        

GUI = '/home/medeo/coding/abandoned/rate/rate2015/guimockup.ui'

builder = Gtk.Builder()
builder.add_from_file( GUI )
builder.connect_signals( Handler() )

window = builder.get_object( "window1" )
window.show_all()

Gtk.main()
