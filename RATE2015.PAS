PROGRAM CALCOLO_INTERESSI_E_RATE_(input,output);
uses crt,printer;
  VAR  tipo_calcolo,tipo_rata,tipo_stampa:CHAR;
       v,k,J,h,conta,conta2,conta3,operazioni,nro_rate:INTEGER;
       m,l,MINIMO,MASSIMO,valore_rata,percentuale,e,x,prestito,inter:REAL;

  PROCEDURE Do_Loop1(zz:integer);
    BEGIN
      (* clrscr; *)
      conta:=1;
      inter:=x*percentuale/v;
      x:=(x+inter-e);
      writeln('  ',conta:7,'  ',e:19:2,'  ',x:20:2,'  ',inter:19:2);
      REPEAT
        conta:=conta+1;
        inter:=x*percentuale/v;
        x:=(x+inter-e);
        IF zz=1 THEN
          BEGIN
            writeln('  ',conta:7,'  ',e:19:2,'  ',x:20:2,'  ',inter:19:2);
            IF (conta=24) or (conta=48) or (conta=72) THEN
              BEGIN
                readln;clrscr;
              END;
            IF conta=nro_rate THEN
              BEGIN
                writeln;
                IF tipo_rata='m'
                  THEN writeln('   numero rate    rata mensile       capitale residuo          interesse')
                  ELSE writeln('   numero rate   rata semestrale     capitale residuo          interesse');
              END
          END (* if zz=1 *)
      UNTIL conta=nro_rate;
      IF zz=1 THEN BEGIN
           gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
         END;
    END;

  PROCEDURE  Do_Loop2(zz:integer);
    BEGIN
      clrscr;
      x:=prestito;conta:=1;
      x:=x+(x*e/v)-valore_rata;clrscr;
      writeln('  ',conta:10,'  ',e:28:9,'  ',x:26:2);
      REPEAT
        conta:=conta+1;x:=x+(x*e/v)-valore_rata;
        IF zz=1 THEN BEGIN
             writeln('  ',conta:10,'  ',e:28:9,'  ',x:26:2);
             IF (conta=24) or (conta=48) or (conta=72) THEN BEGIN
                  readln;clrscr;
                END;
             IF conta=nro_rate THEN BEGIN
                  writeln;
                  writeln('      numero rate         percentuale interesse       capitale residuo');
                END
           END
      UNTIL conta=nro_rate;
      IF zz=1 THEN BEGIN
           gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
         END;
  END;

  PROCEDURE Calcolo_Interessi;FORWARD;
  PROCEDURE Calcolo_Rate;FORWARD;

  PROCEDURE Scelta_Tipo_Rate;
    BEGIN
      REPEAT
        clrscr;
        gotoxy(25,04);writeln('SCELTA RATE MENSILI O SEMESTRALI');
        gotoxy(30,09);writeln('M    PER RATA MENSILE');
        gotoxy(30,13);writeln('S    PER RATA SEMESTRALE');
        gotoxy(30,17);writeln('X    PER FINE LAVORO');
        gotoxy(36,22);writeln('SCELTA:');
        gotoxy(45,22);readln(tipo_rata);
        CASE tipo_rata OF
                    'm': BEGIN v:=1200; k:=9000; END;
                    's': BEGIN v:=200;  k:=1500; END;
                    END;
      UNTIL (tipo_rata='m') or (tipo_rata='s') or (tipo_rata='x');
    END;

  PROCEDURE Main_Menu;
    BEGIN
      clrscr;
      gotoxy(29,04);write('R    PER CALCOLO RATE');
      gotoxy(29,08);write('I    PER CALCOLO INTERESSI');
      gotoxy(29,12);write('S    PER SCELTA TIPO RATE');
      gotoxy(29,16);write('X    PER FINE LAVORO');
      gotoxy(27,22);write('PREMERE      R   I   S   X ');
    END;

  PROCEDURE Principale;
    BEGIN
      gotoxy(55,22);readln(tipo_calcolo);
      CASE tipo_calcolo OF
                    'r': Calcolo_Rate;
                    'i': Calcolo_Interessi;
                    's': Scelta_Tipo_Rate;
                    'x': BEGIN END
      END; (* fine CASE OF *)
    END;

  PROCEDURE Stampa_Loop1(zz:integer); FORWARD;

  PROCEDURE Calcolo_Rate;
    BEGIN
      clrscr;
      gotoxy(26,05);write('PRESTITO LIRE: ');
      gotoxy(26,10);write('PERCENTUALE: ');
      gotoxy(26,15);write('NUMERO RATE: ');
      gotoxy(21,22);write('STAMPA A VIDEO O SU CARTA (v/c): ');
      gotoxy(41,05);readln(prestito);
      gotoxy(39,10);readln(percentuale);
      gotoxy(39,15);readln(nro_rate);
      gotoxy(54,22);readln(tipo_stampa);

      IF (prestito>=MINIMO) AND (prestito<=MASSIMO) THEN
        IF percentuale*nro_rate<k  THEN
          IF (nro_rate>=2) AND (nro_rate<=32000) THEN BEGIN
            (* tutte le condizioni soddisfate *)
            e:=prestito/nro_rate;
            operazioni:=0;
            conta3:=0;
            m:=10000000000.0;
            REPEAT
              operazioni:=operazioni+1;
              x:=prestito;
              Do_Loop1(0);
              writeln(x);
              IF x>0 THEN e:=e+m;
              IF x<0 THEN BEGIN
                            e:=e-m;
                            conta3:=conta3+1;
                            CASE conta3 OF
                              1: m:=10000000000.0;
                              2: m:=1000000000;
                              3: m:=100000000;
                              4: m:=10000000;
                              5: m:=1000000;
                              6: m:=100000;
                              7: m:=10000;
                              8: m:=1000;
                              9: m:=100;
                              10: m:=10;
                              11: m:=1;
                              12: m:=0.1;
                              13: m:=0.01;
                            END;
                          END;
            UNTIL (conta3=14) OR (operazioni=250);
            writeln(conta3);
            writeln(operazioni);
            readln;
            e:=e+0.001;
            x:=prestito;
            writeln(e:19:2);
            writeln(x);
            readln;
            IF tipo_stampa='c' THEN Stampa_Loop1(1) (* stampa su carta *)
                               ELSE Do_Loop1(1); (* stampa a video *)
          END (* end main loop *)
          (* gestione valori inseriti errati! *)
          ELSE BEGIN (* numero rate errato *)
            gotoxy(13,24);write('IMMETTERE ALMENO 2 RATE O MENO DI 32000:  PREMI INVIO ');
            readln;
          END
        ELSE BEGIN (* percentuale*nro_rate>=k *)
          gotoxy(16,24);write('PERCENTUALE O RATE TROPPO GRANDI:  PREMI INVIO ');
          readln;
        END
      ELSE BEGIN (* valore del prestito errato *)
        gotoxy(10,24);write('A PRESTITO METTERE UN NUMERO DA  4  A  12  CIFRE:  PREMI INVIO ');
        readln;
      END
    END;

  PROCEDURE Stampa_Loop2; FORWARD;

  PROCEDURE Calcolo_Interessi;
    BEGIN
      operazioni:=0; J:=8;
      clrscr;
      gotoxy(26,05);writeln('PRESTITO LIRE: ');
      gotoxy(26,10);IF tipo_rata='m' THEN writeln('RATA MENSILE:')
                                     ELSE writeln('RATA SEMESTRALE:');
      gotoxy(26,15);writeln('NUMERO RATE:');
      gotoxy(21,22);writeln('STAMPA A VIDEO O SU CARTA (v/c): ');
      gotoxy(41,05);readln(prestito);
      IF tipo_rata='m' THEN gotoxy(40,10)
                       ELSE gotoxy(43,10);
      readln(valore_rata);
      gotoxy(39,15);readln(nro_rate);
      gotoxy(54,22);readln(tipo_stampa);
      IF valore_rata*nro_rate<prestito*J THEN
        IF nro_rate*valore_rata>=prestito THEN
          IF (prestito>=MINIMO) AND (prestito<=MASSIMO) THEN BEGIN
            conta2:=0;e:=1;l:=10;
              REPEAT
                operazioni:=operazioni+1;
                Do_Loop2(0);
                IF x<0 THEN e:=e+l;
                IF x>0 THEN BEGIN
                           e:=e-l;conta2:=conta2+1;
                                     CASE conta2 OF
                                       1: l:=1;
                                       2: l:=0.1;
                                       3: l:=0.01;
                                       4: l:=0.001;
                                       5: l:=0.0001;
                                       6: l:=0.00001;
                                       7: l:=0.000001;
                                       8: l:=0.0000001;
                                       9: l:=0.00000001;
                                      10: l:=0.000000001;
                                     END;
                         END;
              UNTIL (conta2=11) OR (operazioni=470);
              e:=e+0.0000000001;
              IF tipo_stampa='v' THEN Do_Loop2(1)
                                 ELSE Stampa_Loop2;
          END
            ELSE BEGIN
              gotoxy(10,24);write('A PRESTITO METTERE UN NUMERO DA  4  A  12  CIFRE:  PREMI INVIO ');
              readln;
            END
          ELSE BEGIN
            gotoxy(20,24);write('OPERAZIONE IMPOSSIBILE:  PREMI INVIO ');
            readln;
          END
        ELSE BEGIN
          gotoxy(15,24);write('PERCENTUALE O RATE TROPPO GRANDI:  PREMI INVIO ');
          readln;
        END
    END;

  PROCEDURE Stampa_Loop1;
    BEGIN
      writeln(lst); writeln(lst);
      writeln(lst,'        PRESTITO LIRE: ',prestito:18:0);
      writeln(lst,'        INTERESSE: ',percentuale:22:9);
      writeln(lst,'        NUMERO RATE: ',nro_rate:20);
      writeln(lst); writeln(lst);
      conta:=1;clrscr;inter:=x*percentuale/v;x:=(x+inter-e);
      writeln(lst,'  ',conta:7,'  ',e:19:2,'  ',x:19:2,'  ',inter:18:2);
      REPEAT
        conta:=conta+1;inter:=x*percentuale/v;x:=(x+inter-e);
        writeln(lst,'  ',conta:7,'  ',e:19:2,'  ',x:19:2,'  ',inter:18:2);
        IF conta=nro_rate
        THEN BEGIN
            writeln(lst);
            IF tipo_rata='m' THEN
                               writeln(lst,'   numero rate   rata mensile        capitale residuo         interesse')
                             ELSE
                               writeln(lst,'   numero rate  rata semestrale      capitale residuo         interesse');
        END;
      UNTIL conta=nro_rate;
      gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
    END;

  PROCEDURE Stampa_Loop2;
    BEGIN
      writeln(lst); writeln(lst);
      writeln(lst,'        PRESTITO LIRE: ',prestito:18:0);
      IF tipo_rata='m'
             THEN writeln(lst,'        RATA MENSILE: ',valore_rata:19:0)
             ELSE writeln(lst,'        RATA SEMESTRALE: ',valore_rata:16:0);
      writeln(lst,'        NUMERO RATE: ',nro_rate:20);
      writeln(lst); writeln(lst);
      x:=prestito; conta:=1;
      x:=x+(x*e/v)-valore_rata;
      writeln(lst,'  ',conta:7,'  ',e:26:9,'  ',x:26:2);
      REPEAT
        conta:=conta+1; x:=x+(x*e/v)-valore_rata; 
        writeln(lst,'  ',conta:7,'  ',e:26:9,'  ',x:26:2);
        IF conta=nro_rate THEN BEGIN
                          writeln(lst);
                          writeln(lst,'   numero rate      percentuale interesse          capitale residuo');
                        END
      UNTIL conta=nro_rate;
      gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
    END;

BEGIN
  (* imposto valore costanti *)
  MINIMO:=1000; MASSIMO:=1000000000000.0;

  tipo_calcolo:='0'; (* valore iniziale diverso da 'x' *)
  textbackground(blue);textcolor(yellow);
  (* imposto il tipo di rata (mensile o semestrale) *)
  Scelta_Tipo_Rate;
  (* inizio il ciclo principale *)
  WHILE (tipo_rata <> 'x') AND (tipo_calcolo <> 'x') DO
    BEGIN
      Main_Menu;
      Principale;
    END;
END.
