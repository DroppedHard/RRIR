# Projekt z przedmiotu Rachunek Różniczkowy i Różnicowy

Autorzy:
<ul>
  <li>Kacper Jurek</li>
  <li>Marcin Żurawel</li>
  <li>Szymon Wójcik</li>
</ul>

Aby skorzystać ze spisu treści, proszę nacisnąć menu w lewym górnym rogu tego okna.

# Wstęp

Projekt polega na zaimplementowaniu metody numerycznej strzałów, która na podstawie różniczki drugiego rzędu i warunków brzegowych wylicza funkcję zbliżoną do funkcji wyliczonej algebraicznie. Program został napisany w Pythonie, graficzny interfejs został stworzony przy pomocy biblioteki `matplotlib.pyplot`.

## Wymagania sprzętowe

Procesor: Intel Core i7-5820K
Karta graficzna: Nvidia GeForce GTX 1080
Pamięć RAM: 16GB
Miejsce na dysku: 1GB
System operacyjny: Windows 10

## Korzystanie z programu

Po uruchomieniu programu powinno wyświelić się okno, gdzie możemy wyróżnić następujące sekcje:
- __Step size__, gdzie możemy ustawić dokładność naszych argumentów funkcji.
- __Equations__, gdzie możemy z listy rozsuwalnej wybrać odpowiednie zagadnienia brzegowe.
- __Przycisk `plot`__, gdzie po naciśnięciu jego otrzymamy wykresy strzałów i wykres funkcji reprezentującej odpowiedź wyznaczoną algebraicznie.
- __Siatkę__, gdzie będą przedstawione graficznie wykresy kolejnych strzałów, oraz funkcji wyznaczonej algebraicznie.

Każde naciśnięcie przycisku `plot` spowoduje ponowne uruchomienie algorytmu, co skutkuje różnymi wykresami strzałów.
Rozmiar siatki automatycznie dopasowuje się do wartości otrzymanych funkcji.

# Opis metody

## Algorytm

# Literatura

- [Numeryczne rozwiązywanie równań różniczkowych - 6.5. Meoda strzałów](https://mst.mimuw.edu.pl/lecture.php?lecture=nrr&part=Ch6&fbclid=IwAR1p5peMRisEqJiwsH8QCsOHMHEBsbFqin3WmF1HWAToaFC5UGvYP6Hbmac#S5)
- [Wikipedia - metoda strzałów](https://pl.wikipedia.org/wiki/Metoda_strzałów)
- [Inżynierskie metody numeryczne 2010/2011 - Wykład 8: Metoda Numerowa, różnic skończonych 1D, metoda strzałów](https://home.agh.edu.pl/~bszafran/imn10/szpi2.pdf)
- [Metody Numeryczne Równania różniczkowe zwyczajne](http://wygasz.edu.pl/ludzie/szewczuk/mn_data/wyklad7.pdf)
