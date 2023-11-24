#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Gtk, Gio, GLib, Pango, PangoCairo
import sys # per controllo versione python
import math

class Handler:
    k = 9000 ; v = 1200 # valori iniziali per rata mensile
    J = 8 # valore COSTANTE per calcolo interessi

    def onDeleteMainWindow(self, *args):
        Gtk.main_quit(*args)

    def onDeleteOutputWindow (self, outputWin, event):
        print ( outputWin.get_size() )
        outputWin.hide()
        return True

    def rataMensile(self, radiobutton):
        if radiobutton.get_active():
            self.k = 9000
            self.v = 1200
            builder.get_object( "lbl_valore_rata" ).set_text( "Valore rata mensile" )

    def rataSemestrale(self, radiobutton):
        if radiobutton.get_active():
            self.k = 1500
            self.v = 200
            builder.get_object( "lbl_valore_rata" ).set_text( "Valore rata semestrale" )

    def calcolaRate(self, button):

        def Do_Loop1(zz):
            x = prestito
            conta = 1
            inter = x * percentuale / self.v
            x = x + inter - e
            if zz == 1: # memorizzo il calcolo della prima rata
                output = "\n"
                output += "  {0:7}   {1:19.2f}   {2:20.2f}   {3:19.2f}" \
                    .format(conta, e, x, inter)
                output += "\n"
            while True:
                conta += 1
                inter = x * percentuale / self.v
                x = x + inter - e
                if zz == 1: # memorizzo i calcoli relativi a rate 2..n
                    output += "  {0:7}   {1:19.2f}   {2:20.2f}   {3:19.2f}" \
                        .format(conta, e, x, inter)
                    output += "\n"
                if conta == nro_rate :
                    break
            if zz == 1: # visualizzo risultati in finestra modale
                output += "\n"
                if builder.get_object( "rata mensile" ).get_active():
                    output += ("    numero rate        rata mensile         capitale residuo          interesse    ")
                else:
                    output += ("    numero rate       rata semestrale       capitale residuo          interesse    ")
                output += "\n"

                txt_buffer = builder.get_object( "output_buffer" )
                txt_buffer.set_text(output)

                outputWin.resize(1050,510)
                outputWin.show_all()
            return x

        print( "Calcolo Rate in corso..." )

        percentuale = builder.get_object( "percentuale" ).get_value()
        nro_rate = builder.get_object( "nro_rate" ).get_value_as_int()

        # controllo correttezza valori inseriti
        if percentuale * nro_rate > self.k :
            # errore!
            dialog = builder.get_object( "error_percentuale_dialog" )
            dialog.run()

            dialog.hide()
            return

        # effettuo il calcolo
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
        # ora conosciamo il valore di "e", rifacciamo il calcolo e stampiamolo
        Do_Loop1(1)
        print( "Fine Calcolo Rate" )

    def calcolaInteressi(self, button):

        def Do_Loop2(zz):
            x = prestito
            conta = 1
            x = x + (x*e/self.v) - valore_rata
            if zz == 1: # stampa calcoli relativi a rata 1
                output = "\n"
                output += "   {0:7}  {1:19.2f}    {2:20.2f}".format(conta, e, x)
                output += "\n"

            while True:
                conta += 1
                x = x + (x*e/self.v) - valore_rata
                if zz == 1 : # stampa calcoli relativi a rate 2..n
                    output += "   {0:7}  {1:19.2f}    {2:20.2f}".format(conta, e, x)
                    output += "\n"
                if conta == nro_rate :
                    break
            if zz == 1: # stampa piè di pagina
                output += "\n"
                output += ("    numero rate    percentuale interesse    capitale residuo    ")
                output += "\n"

                txt_buffer = builder.get_object( "output_buffer" )
                txt_buffer.set_text(output)

                outputWin.resize(815,510)
                outputWin.show_all()
            return x

        print( "Calcolo Interessi in corso...\n" )

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
        # effettuo il calcolo
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
                     0.000000001    # 11  mantengo valore del 10
                  )

        while True:
            # ricerchiamo il corretto valore di "e"
            operazioni += 1
            x = Do_Loop2(0)
            if x < 0:
                e = e+l
            elif x >0:
                e = e-l
                conta2 += 1
                l = lista_l[conta2]
            if conta2 == 11 or operazioni == 470:
                break
        e = e + 0.0000000001
        # ora conosciamo il valore di "e" rifacciamo il calcolo e stampiamolo
        Do_Loop2(1)
        print( "Fine Calcolo Interessi" )

    def pageChanged (self, stack, event):
        if stack.get_visible_child_name() == "pagina rate":
            btn_calcola.set_label( "Calcola Rate" )
            btn_calcola.disconnect_by_func(self.calcolaInteressi)
            btn_calcola.connect( "clicked", self.calcolaRate )
        else:
            btn_calcola.set_label( "Calcola Interessi" )
            btn_calcola.disconnect_by_func(self.calcolaRate)
            btn_calcola.connect( "clicked", self.calcolaInteressi)

    ######----------               STAMPA               ----------######

    def stampa (self, button):
        HEADER_HEIGHT = 10 * 72 / 25.4
        HEADER_GAP = 3 * 72 / 25.4

        o_buffer = builder.get_object( "output_buffer" )
        start, end = o_buffer.get_bounds()
        output = o_buffer.get_text(start, end, True)
        parent = builder.get_object( "outputWindow" )
        tipo_calcolo = btn_calcola.get_label()
        print ("stampo")

        def prepara_stampa():
            self.operation = Gtk.PrintOperation()
            print_data = {
                          'filename': output,
                          'font_size': 12.0,
                          'lines_per_page': 0,
                          'lines': None,
                          'num_lines': 0,
                          'num_pages': 0
                         }

            self.operation.connect('begin-print', begin_print, print_data)
            self.operation.connect('draw-page', draw_page, print_data)
            self.operation.connect('end-print', end_print, print_data)

            self.operation.set_use_full_page(False)
            self.operation.set_unit(Gtk.Unit.POINTS)
            self.operation.set_embed_page_setup(True)

            settings = Gtk.PrintSettings()

            dir = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_DOCUMENTS)
            if dir is None:
                dir = GLib.get_home_dir()
            if settings.get(Gtk.PRINT_SETTINGS_OUTPUT_FILE_FORMAT) == 'ps':
                ext = '.ps'
            elif settings.get(Gtk.PRINT_SETTINGS_OUTPUT_FILE_FORMAT) == 'svg':
                ext = '.svg'
            else:
                ext = '.pdf'

            uri = "file://%s/gtk-demo%s" % (dir, ext)
            settings.set(Gtk.PRINT_SETTINGS_OUTPUT_URI, uri)
            self.operation.set_print_settings(settings)

        def begin_print(operation, print_ctx, print_data):
            height = print_ctx.get_height() - HEADER_HEIGHT - HEADER_GAP
            print_data['lines_per_page'] = \
                math.floor(height / print_data['font_size'])

            s = output

            print_data['lines'] = s.split('\n')
            print_data['num_lines'] = len(print_data['lines'])

            print_data['num_pages'] = \
                (print_data['num_lines'] - 1) / print_data['lines_per_page'] + 1

            operation.set_n_pages(print_data['num_pages'])

        def draw_page(operation, print_ctx, page_num, print_data):
            cr = print_ctx.get_cairo_context()
            width = print_ctx.get_width()

            cr.rectangle(0, 0, width, HEADER_HEIGHT)
            cr.set_source_rgb(0.8, 0.8, 0.8)
            cr.fill_preserve()

            cr.set_source_rgb(0, 0, 0)
            cr.set_line_width(1)
            cr.stroke()

            layout = print_ctx.create_pango_layout()
            desc = Pango.FontDescription('sans 14')
            layout.set_font_description(desc)

            layout.set_text(tipo_calcolo, -1)
            (text_width, text_height) = layout.get_pixel_size()

            if text_width > width:
                layout.set_width(width)
                layout.set_ellipsize(Pango.EllipsizeMode.START)
                (text_width, text_height) = layout.get_pixel_size()

            cr.move_to((width - text_width) / 2,
                       (HEADER_HEIGHT - text_height) / 2)
            PangoCairo.show_layout(cr, layout)

            page_str = "%d/%d" % (page_num + 1, print_data['num_pages'])
            layout.set_text(page_str, -1)

            layout.set_width(-1)
            (text_width, text_height) = layout.get_pixel_size()
            cr.move_to(width - text_width - 4,
                       (HEADER_HEIGHT - text_height) / 2)
            PangoCairo.show_layout(cr, layout)

            layout = print_ctx.create_pango_layout()

            desc = Pango.FontDescription('monospace')
            desc.set_size(print_data['font_size'] * Pango.SCALE)
            layout.set_font_description(desc)

            cr.move_to(0, HEADER_HEIGHT + HEADER_GAP)
            lines_pp = int(print_data['lines_per_page'])
            num_lines = print_data['num_lines']
            data_lines = print_data['lines']
            font_size = print_data['font_size']
            line = page_num * lines_pp

            for i in range(lines_pp):
                if line >= num_lines:
                    break

                layout.set_text(data_lines[line], -1)
                PangoCairo.show_layout(cr, layout)
                cr.rel_move_to(0, font_size)
                line += 1

        def end_print(operation, print_ctx, print_data):
            pass

        prepara_stampa()
        a = Gtk.PrintOperationAction.PRINT_DIALOG
        result = self.operation.run(a, parent)

        if result == Gtk.PrintOperationResult.ERROR:
            print("Errore")
            message = self.operation.get_error()

            dialog = Gtk.MessageDialog(parent,
                                       0,
                                       Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CLOSE,
                                       message)

            dialog.run()
            dialog.destroy()

        output = builder.get_object( "output_buffer" )



######----------                MAIN                ----------######


# controllo che versione python sia la 3.x
if sys.version[0] == "2":
    # errore! eseguito programma con python 2.x
    print( "\a" ) # ding!
    print( "ERRORE! rilevato python 2" )
    print( "Eseguire il programma con la versione 3.x di Python" )
    print( "" )
    raise SystemExit

GUI = './finestraPrincipale.ui'

builder = Gtk.Builder()
builder.add_from_file( GUI )
btn_calcola = builder.get_object( "calcola" )
builder.connect_signals( Handler() )


window = builder.get_object( "mainWindow" )
outputWin = builder.get_object( "outputWindow" )
window.show_all()

Gtk.main()
