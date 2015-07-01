#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import sys # per controllo versione python

class Handler:
    k = 9000 ; v = 1200 # valori iniziali per rata mensile
    J = 8 # valore COSTANTE per calcolo interessi
    
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def rataMensile(self, radiobutton):
        if radiobutton.get_active():
            self.k = 9000
            self.v = 1200
            builder.get_object( "lbl_valore_rata" ).set_text("Valore rata mensile")

    def rataSemestrale(self, radiobutton):
        if radiobutton.get_active():
            self.k = 1500
            self.v = 200
            builder.get_object( "lbl_valore_rata" ).set_text("Valore rata semestrale")

    def calcolaRate(self, button):
        
        def Do_Loop1(zz):
            x = prestito
            conta = 1
            inter = x * percentuale / self.v
            x = x + inter - e
            if zz == 1: # stampa calcoli relativi a rata 1
                print("\t%d\t \t%0.2f\t \t\t%0.2f\t \t\t%0.2f " % (conta, e, x, inter) )
            while True:
                conta += 1
                inter = x * percentuale / self.v
                x = x + inter - e
                if zz == 1: # stampa calcoli relativi a rate 2..n
                    print("\t%d\t \t%0.2f\t \t\t%0.2f\t \t\t%0.2f " % (conta, e, x, inter) )
                if conta == nro_rate :
                    break
            if zz == 1: # stampa piè di pagina
                print("\n")
                if builder.get_object( "rata mensile" ).get_active():
                    print("   numero rate        rata mensile         capitale residuo          interesse")
                else:
                    print("   numero rate       rata semestrale       capitale residuo          interesse")
            return x

        percentuale = builder.get_object( "percentuale" ).get_value()
        nro_rate = builder.get_object( "nro_rate" ).get_value_as_int()

        # controllo correttezza valori inseriti
        if percentuale * nro_rate > self.k :
            # errore!
            dialog = builder.get_object( "error_percentuale_dialog" )
            dialog.run()

            dialog.hide()
            return    

        # tutte le condizioni verificate, effettuo il calcolo
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
        while True:
            # ricerchiamo il corretto valore di "e"
            operazioni += 1
            x = Do_Loop1(0)
            if x > 0 :
                e = e + m
            elif x < 0 :
                e = e - m
                conta3 += 1
                m = lista_m[conta3]
            if (conta3 == 14) or (operazioni == 250) :
                break
        e += 0.001
        x = prestito
        # ora che conosciamo il valore di "e" rifacciamo il calcolo
        # e stampiamolo
        Do_Loop1(1)

    def calcolaInteressi(self, button):

        def Do_Loop2(zz):
            x = prestito
            conta = 1
            x = x + (x*e/v) - valore_rata
            if zz == 1: # stampa calcoli relativi a rata 1
                print( "\t%d\t \t%0.2f\t \t\t%0.2f" % (conta, e, x) )
            while True:
                conta += 1
                x = x + (x*e/v) - valore_rata
                if zz = 1 : # stampa calcoli relativi a rate 2..n
                    print( "\t%d\t \t%0.2f\t \t\t%0.2f" % (conta, e, x) )
                if conta == nro_rate :
                    break
            if zz == 1: # stampa piè di pagina
                print("\n      numero rate         percentuale interesse       capitale residuo")

        prestito = builder.get_object( "prestito" ).get_value()
        valore_rata = builder.get_object( "valore_rata" ).get_value()
        nro_rate = builder.get_object( "nro_rate" ).get_value()

        # controllo correttezza valori inseriti:
        if (valore_rata * nro_rate >= prestito * self.J) or (valore_rata * nro_rate <  prestito) :
            # errore!
            dialog = builder.get_object( "error_percentuale_dialog" )
            dialog.run()
    
            dialog.hide()
            return
        # tutte le condizioni verificate, effettuo il calcolo
        operazioni = 0
        conta2 = 0
        e = 1
        l = 10
        lista_l = (         None,   # 0   non verrà mai usato
                               1,   # 1
                             0.1,   # 2
                            0.01,   # 3
                           0.001,   # 4
                          0.0001,   # 5
                         0.00001,   # 6
                        0.000001,   # 7
                       0.0000001,   # 8
                      0.00000001,   # 9
                     0.000000001,   # 10
                     0.000000001)   # 11  mantengo valore del 10
        while True:
            operazioni += 1
            Do_Loop2(0)
            if x < 0:
                e = e+l
            elif x >0:
                e = e-l
                conta2 += 1
                l = lista_l[conta2]
            if conta2 = 11 or operazioni = 470:
                break
        e = e + 0.0000000001
        
             
        

# controllo che versione python sia la 3.x
if sys.version[0] == "2":
    # errore! eseguito programma con python 2.x
    print("\a") # ding!
    print("ERRORE!")
    print("Eseguire il programma con la versione 3.x di Python")
    print("")
    raise SystemExit
    
GUI = './guimockup.ui'

builder = Gtk.Builder()
builder.add_from_file( GUI )
builder.connect_signals( Handler() )

window = builder.get_object( "window1" )
window.show_all()

Gtk.main()
