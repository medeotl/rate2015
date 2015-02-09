PROGRAM CALCOLO_INTERESSI_E_RATE_(input,output);
uses crt,printer;
  VAR  scelta,sc_rate,tipo_stampa:CHAR;
       v,k,j,h,conta3,conta2,operazioni,conta,rate:INTEGER;
       m,l,minimo,massimo,rata_semestrale,percentuale,e,x,prestito,inter:REAL;

  PROCEDURE do_loop1(zz:integer);
    BEGIN
      conta:=1;clrscr;inter:=x*percentuale/v;x:=(x+inter-e);
      writeln('  ',conta:7,'  ',e:19:2,'  ',x:20:2,'  ',inter:19:2);
      REPEAT
        conta:=conta+1;inter:=x*percentuale/v;x:=(x+inter-e);
        IF zz=1 THEN BEGIN
             writeln('  ',conta:7,'  ',e:19:2,'  ',x:20:2,'  ',inter:19:2);
             IF (conta=24) or (conta=48) or (conta=72) THEN BEGIN
                 readln;clrscr;
               END;
             IF conta=rate THEN BEGIN
                  writeln;
                  IF sc_rate='m' THEN writeln('   numero rate    rata mensile       capitale residuo          interesse')
                                 ELSE writeln('   numero rate   rata semestrale     capitale residuo          interesse');
                END
           END
      UNTIL conta=rate;
      IF zz=1 THEN BEGIN
           gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
         END;
    END;

  PROCEDURE  do_loop2(zz:integer);
    BEGIN
      x:=prestito;conta:=1;clrscr;
      x:=x+(x*e/v)-rata_semestrale;clrscr;
      writeln('  ',conta:10,'  ',e:28:9,'  ',x:26:2);
      REPEAT
        conta:=conta+1;x:=x+(x*e/v)-rata_semestrale;
        IF zz=1 THEN BEGIN
             writeln('  ',conta:10,'  ',e:28:9,'  ',x:26:2);
             IF (conta=24) or (conta=48) or (conta=72) THEN BEGIN
                  readln;clrscr;
                END;
             IF conta=rate THEN BEGIN
                  writeln;
                  writeln('      numero rate         percentuale interesse       capitale residuo');
                END
           END
      UNTIL conta=rate;
      IF zz=1 THEN BEGIN
           gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
         END;
  END;

  PROCEDURE calcolo_interessi;FORWARD;
  PROCEDURE calcolo_rate;FORWARD;

  PROCEDURE SCELTA_RATE;
    BEGIN
      REPEAT
        clrscr;
        gotoxy(25,4);writeln('SCELTA RATE MENSILI O SEMESTRALI');
        gotoxy(30,9);writeln('M    PER RATA MENSILE');
        gotoxy(30,13);writeln('S    PER RATA SEMESTRALE');
        gotoxy(30,17);writeln('X    PER FINE LAVORO');
        gotoxy(36,22);writeln('SCELTA:');
        gotoxy(45,22);readln(sc_rate);
        CASE sc_rate OF
                    'm': BEGIN v:=1200; k:=9000; j:=8; END;
                    's': BEGIN v:=200; k:=1500; j:=8; END;
                    END;
      UNTIL (sc_rate='m') or (sc_rate='s') or (sc_rate='x');
    END;

  PROCEDURE MENU1;
    BEGIN
      operazioni:=0; minimo:=1000; massimo:=1000000000000.0;
      clrscr;
      gotoxy(29,4);write('R    PER CALCOLO RATE');
      gotoxy(29,8);write('I    PER CALCOLO INTERESSI');
      gotoxy(29,12);write('S    PER SCELTA RATE');
      gotoxy(29,16);write('X    PER FINE LAVORO');
      gotoxy(27,22);write('PREMERE      R   I   S   X ');
    END;

  PROCEDURE principale;
    BEGIN
      gotoxy(55,22);readln(scelta);
      CASE scelta OF
                  'r': calcolo_rate;
                  'i': calcolo_interessi;
                  's': scelta_rate;
                  'x': BEGIN END
                  ELSE
                  menu1;
                  END;
    END;

  PROCEDURE stampa_loop1(zz:integer); FORWARD;

  PROCEDURE calcolo_rate;
    BEGIN
      clrscr;gotoxy(26,5);write('PRESTITO LIRE: ');
      gotoxy(26,10);write('PERCENTUALE: ');
      gotoxy(26,15);write('NUMERO RATE: ');
      gotoxy(21,22);write('STAMPA A VIDEO O SU CARTA (v/c): ');
      gotoxy(41,5);readln(prestito);
      gotoxy(39,10);readln(percentuale);
      gotoxy(39,15);readln(rate);
      gotoxy(54,22);readln(tipo_stampa);
      IF (rate>=2) AND (rate<=32000) THEN
        IF percentuale*rate<k  THEN
          IF (prestito>=minimo) AND (prestito<=massimo) THEN BEGIN
            e:=prestito/rate;conta3:=0;m:=10000000000.0;
            REPEAT
              operazioni:=operazioni+1;x:=prestito;
                   DO_LOOP1(0);
              IF x>0 THEN e:=e+m;
                IF x<0 THEN BEGIN
                           e:=e-m;conta3:=conta3+1;
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
            e:=e+0.001;x:=prestito;
            IF tipo_stampa='c' THEN STAMPA_LOOP1(1)
                               ELSE DO_LOOP1(1);
          END
          ELSE BEGIN
            gotoxy(10,24);write('A PRESTITO METTERE UN NUMERO DA  4  A  12  CIFRE:  PREMI INVIO ');
            readln;
          END
        ELSE BEGIN
          gotoxy(16,24);write('PERCENTUALE O RATE TROPPO GRANDI:  PREMI INVIO ');
          readln;
        END
      ELSE BEGIN
        gotoxy(13,24);write('IMMETTERE ALMENO 2 RATE O MENO DI 32000:  PREMI INVIO ');
        readln;
      END
    END;

  PROCEDURE stampa_loop2; FORWARD;

  PROCEDURE calcolo_interessi;
    BEGIN
      clrscr;gotoxy(26,5);writeln('PRESTITO LIRE: ');
      gotoxy(26,10);IF sc_rate='m' THEN writeln('RATA MENSILE:')
                                  ELSE writeln('RATA SEMESTRALE:');
      gotoxy(26,15);writeln('NUMERO RATE:');
      gotoxy(21,22);writeln('STAMPA A VIDEO O SU CARTA (v/c): ');
      gotoxy(41,5);readln(prestito);
      IF sc_rate='m' THEN gotoxy(40,10)
                     ELSE gotoxy(43,10);
                     readln(rata_semestrale);
      gotoxy(39,15);readln(rate);
      gotoxy(54,22);readln(tipo_stampa);
      IF rata_semestrale*rate<prestito*j THEN
        IF rate*rata_semestrale>=prestito THEN
          IF (prestito>=minimo) AND (prestito<=massimo) THEN BEGIN
            conta2:=0;e:=1;l:=10;
              REPEAT
                operazioni:=operazioni+1;
                do_loop2(0);
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
              UNTIL (conta2=11) OR (operazioni=470);e:=e+0.0000000001;
              IF tipo_stampa='v' THEN do_loop2(1)
                                 ELSE stampa_loop2;
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

  PROCEDURE stampa_loop1;
    BEGIN
      writeln(lst); writeln(lst);
      writeln(lst,'        PRESTITO LIRE: ',prestito:18:0);
      writeln(lst,'        INTERESSE: ',percentuale:22:9);
      writeln(lst,'        NUMERO RATE: ',rate:20);
      writeln(lst); writeln(lst);
      conta:=1;clrscr;inter:=x*percentuale/v;x:=(x+inter-e);
      writeln(lst,'  ',conta:7,'  ',e:19:2,'  ',x:19:2,'  ',inter:18:2);
      REPEAT
        conta:=conta+1;inter:=x*percentuale/v;x:=(x+inter-e);
        writeln(lst,'  ',conta:7,'  ',e:19:2,'  ',x:19:2,'  ',inter:18:2);
        IF conta=rate
        THEN BEGIN
            writeln(lst);
            IF sc_rate='m' THEN writeln(lst,'   numero rate   rata mensile        capitale residuo         interesse')
            ELSE writeln(lst,'   numero rate  rata semestrale      capitale residuo         interesse');
        END;
      UNTIL conta=rate;
      gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
    END;

  PROCEDURE stampa_loop2;
    BEGIN
      writeln(lst); writeln(lst);
      writeln(lst,'        PRESTITO LIRE: ',prestito:18:0);
      IF sc_rate='m'
             THEN writeln(lst,'        RATA MENSILE: ',rata_semestrale:19:0)
             ELSE writeln(lst,'        RATA SEMESTRALE: ',rata_semestrale:16:0);
      writeln(lst,'        NUMERO RATE: ',rate:20);
      writeln(lst); writeln(lst);
      x:=prestito; conta:=1;
      x:=x+(x*e/v)-rata_semestrale;
      writeln(lst,'  ',conta:7,'  ',e:26:9,'  ',x:26:2);
      REPEAT
        conta:=conta+1; x:=x+(x*e/v)-rata_semestrale;
        writeln(lst,'  ',conta:7,'  ',e:26:9,'  ',x:26:2);
        IF conta=rate THEN BEGIN
                          writeln(lst);
                          writeln(lst,'   numero rate      percentuale interesse          capitale residuo');
                        END
      UNTIL conta=rate;
      gotoxy(35,25);write('premi invio ');gotoxy(30,35);readln;
    END;

BEGIN
  scelta:='0';
  textbackground(blue);textcolor(yellow);scelta_rate;
  REPEAT
    IF scelta<>'x' THEN
                     BEGIN
                       menu1;
                       IF sc_rate<>'x' THEN principale;
                     END;
  UNTIL (scelta='x') or (sc_rate='x');
END.
