# Poziom 1: Pełna Lista 180 Zadań Podstawowych Pythona
### Kompletny Program dla Myślących Przestrzennie i Wizualnie

> [!NOTE]
> 12 Modułów × 15 Zadań = 180 konkretnych, praktycznych ćwiczeń.
> Każde zadanie posiada gotowe rozwiązanie w standardzie PEP 8 (<= 88 znaków).

[🇬🇧 English version (ALL_180_TASKS.md)](ALL_180_TASKS.md)

---

## Moduł 1: Zmienne i Przypisywanie Wartości

1. **Variable Assignment**: Stwórz zmienną `imie` i przypisz do niej swoje imię. Wyświetl ją.  
   [Rozwiązanie](Module_01_Variables/solutions/task_01.py)
2. **Variable Reassignment**: Stwórz zmienną `wiek` z wartością 25, a następnie zmień jej wartość na 26. Wyświetl obie wartości.  
   [Rozwiązanie](Module_01_Variables/solutions/task_02.py)
3. **Arithmetic Sum**: Utwórz zmienne `a = 7` i `b = 3`. Oblicz ich sumę i zapisz w zmiennej `suma`. Wyświetl `suma`.  
   [Rozwiązanie](Module_01_Variables/solutions/task_03.py)
4. **Overwriting Variables**: Nadpisz zmienną `suma` wynikiem mnożenia `a` i `b`. Wyświetl nową wartość.  
   [Rozwiązanie](Module_01_Variables/solutions/task_04.py)
5. **Rectangle Area**: Utwórz zmienne `szerokosc = 5` i `wysokosc = 10`. Oblicz pole prostokąta i zapisz w zmiennej `pole`.  
   [Rozwiązanie](Module_01_Variables/solutions/task_05.py)
6. **Gross Price and VAT Calculation**: Utwórz zmienną `cena_netto = 100` i `vat = 0.23`. Oblicz `cena_brutto` i wyświetl. Zawiera interaktywność i ochronę przed ujemnym VAT.  
   [Rozwiązanie](Module_01_Variables/solutions/task_06.py)
7. **Renaming Variables**: Zmień nazwę zmiennej `stara` na `nowa` (przypisz wartość z `stara` do `nowa`, a `stara` usuń).  
   [Rozwiązanie](Module_01_Variables/solutions/task_07.py)
8. **Dynamic Typing**: Utwórz zmienną `liczba = 42`, a następnie przypisz do niej napis 'czterdzieści dwa'. Wyświetl zmienną.  
   [Rozwiązanie](Module_01_Variables/solutions/task_08.py)
9. **Multiple Assignment**: W jednej linii utwórz zmienne `x`, `y`, `z` i przypisz im wartości 1, 2, 3.  
   [Rozwiązanie](Module_01_Variables/solutions/task_09.py)
10. **Internal Variable Naming**: Utwórz zmienną `_prywatna` z wartością 'tajne' i wyświetl ją.  
   [Rozwiązanie](Module_01_Variables/solutions/task_10.py)
11. **Long String Variable**: Utwórz zmienną `dlugi_opis` zawierającą tekst: 'Python to język programowania wysokiego poziomu.'  
   [Rozwiązanie](Module_01_Variables/solutions/task_11.py)
12. **Case Sensitivity**: Utwórz zmienne `wiekOsoby` i `wiek_osoby` z różnymi wartościami. Sprawdź, czy Python traktuje je jako różne.  
   [Rozwiązanie](Module_01_Variables/solutions/task_12.py)
13. **Self-referential Arithmetic**: Utwórz zmienną `temp = 15`, a następnie nadpisz ją wynikiem działania `temp * 2 + 5`.  
   [Rozwiązanie](Module_01_Variables/solutions/task_13.py)
14. **Floating-Point Division**: Utwórz zmienną `wynik_dzielenia = 15 / 4` i wyświetl jej wartość.  
   [Rozwiązanie](Module_01_Variables/solutions/task_14.py)
15. **NoneType Evaluation**: Utwórz zmienną `pusty` z wartością `None`, a następnie sprawdź jej typ za pomocą `type()`.  
   [Rozwiązanie](Module_01_Variables/solutions/task_15.py)

## Moduł 2: Podstawowe Typy Danych

1. **Four Primitive Types**: Utwórz zmienne: `liczba_calkowita = 10`, `ulamek = 3.14`, `tekst = 'Python'`, `czy_prawda = True`. Wyświetl typ każdej z nich.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_01.py)
2. **Float Inspection**: Sprawdź typ wartości `3.1415` za pomocą funkcji `type()`.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_02.py)
3. **Boolean Flag**: Utwórz zmienną `czy_slonecznie = False` i wyświetl jej typ.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_03.py)
4. **String Concatenation Fix**: Połącz napis 'Mam ' z liczbą 30 i napisem ' lat' – napraw błąd używając konwersji na tekst.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_04.py)
5. **String to Integer Conversion**: Utwórz zmienną `wiek = '18'`. Przekonwertuj ją na liczbę całkowitą, dodaj 2 i wyświetl wynik.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_05.py)
6. **Type of Booleans**: Sprawdź, co zwróci `type(True)` oraz `type(False)`.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_06.py)
7. **Float Truncation**: Utwórz zmienną `temperatura = 36.6`. Przekonwertuj ją na `int` i wyświetl. Co się stało?  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_07.py)
8. **Division Result Type**: Oblicz `10 / 3` i sprawdź typ wyniku.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_08.py)
9. **Chained Conversions**: Utwórz zmienną `napis = '456'`. Przekonwertuj ją najpierw na `int`, a potem na `float`.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_09.py)
10. **String vs Boolean Trap**: Utwórz zmienną `czy_deszcz = 'False'`. Sprawdź jej typ – czy to wartość logiczna?  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_10.py)
11. **The None Object**: Utwórz zmienną `nic = None` i sprawdź jej typ.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_11.py)
12. **Formatting Number with String**: Połącz liczbę `75` z napisem ' punktów' za pomocą konwersji.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_12.py)
13. **Numeric Literals with Underscores**: Utwórz zmienną `milion = 1_000_000`. Wyświetl jej wartość i typ.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_13.py)
14. **Truthiness Evaluation**: Sprawdź, co zwróci `bool(0)`, `bool(42)`, `bool('')`, `bool('Hello')`.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_14.py)
15. **Implicit Type Coercion**: Utwórz zmienną `wynik = 7 + 2.5`. Sprawdź, jakiego typu jest wynik.  
   [Rozwiązanie](Module_02_Data_Types/solutions/task_15.py)

## Moduł 3: Operatory i Wyrażenia

1. **Four Basic Arithmetic Operations**: Poproś użytkownika o dwie liczby, a następnie wyświetl ich sumę, różnicę, iloczyn i iloraz.  
   [Rozwiązanie](Module_03_Operators/solutions/task_01.py)
2. **Modulo Remainder**: Oblicz resztę z dzielenia 29 przez 6.  
   [Rozwiązanie](Module_03_Operators/solutions/task_02.py)
3. **Exponentiation**: Oblicz 2 do potęgi 8.  
   [Rozwiązanie](Module_03_Operators/solutions/task_03.py)
4. **Floor Division**: Użyj operatora dzielenia całkowitego `//` dla liczb 17 i 4. Wyświetl wynik.  
   [Rozwiązanie](Module_03_Operators/solutions/task_04.py)
5. **Augmented Assignment Operators**: Utwórz zmienną `x = 10`. Użyj operatorów `+=`, `-=`, `*=`, `/=` i po każdej operacji wyświetl `x`.  
   [Rozwiązanie](Module_03_Operators/solutions/task_05.py)
6. **Comparison Operators**: Porównaj liczby 15 i 20 za pomocą operatorów: `==`, `!=`, `>`, `<`, `>=`, `<=`. Wyświetl każdy wynik.  
   [Rozwiązanie](Module_03_Operators/solutions/task_06.py)
7. **Logical AND**: Sprawdź, czy liczba 8 jest większa od 5 i jednocześnie mniejsza od 12.  
   [Rozwiązanie](Module_03_Operators/solutions/task_07.py)
8. **Logical OR**: Sprawdź, czy liczba 3 jest większa od 10 lub mniejsza od 5.  
   [Rozwiązanie](Module_03_Operators/solutions/task_08.py)
9. **Logical NOT**: Użyj operatora `not` na wartości `True` i wyświetl wynik.  
   [Rozwiązanie](Module_03_Operators/solutions/task_09.py)
10. **Arithmetic Mean**: Oblicz średnią arytmetyczną trzech liczb: 12, 15, 20.  
   [Rozwiązanie](Module_03_Operators/solutions/task_10.py)
11. **Circle Area Formula**: Oblicz pole koła o promieniu 5 (przyjmij π = 3.14).  
   [Rozwiązanie](Module_03_Operators/solutions/task_11.py)
12. **Even / Odd Number Check**: Zapytaj użytkownika o liczbę i sprawdź, czy jest parzysta (użyj `%`).  
   [Rozwiązanie](Module_03_Operators/solutions/task_12.py)
13. **Quadratic Discriminant**: Oblicz deltę dla równania: a=1, b=4, c=4 (wzór: b² - 4ac).  
   [Rozwiązanie](Module_03_Operators/solutions/task_13.py)
14. **Square Root via Exponent**: Oblicz pierwiastek kwadratowy z 64 używając operatora `**`.  
   [Rozwiązanie](Module_03_Operators/solutions/task_14.py)
15. **Case Sensitive String Equality**: Porównaj napisy 'Python' i 'python' – czy są równe? Wyświetl wynik.  
   [Rozwiązanie](Module_03_Operators/solutions/task_15.py)

## Moduł 4: Konwersje Typów Danych

1. **String to Int and Addition**: Zamień napis '250' na liczbę całkowitą i dodaj 75.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_01.py)
2. **String to Float and Multiplication**: Zamień napis '6.28' na liczbę zmiennoprzecinkową i pomnóż przez 3.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_02.py)
3. **Number to String Concatenation**: Zamień liczbę 99 na napis i połącz z napisem ' problemów'.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_03.py)
4. **Boolean Casting**: Użyj `bool()` na wartościach: 0, 1, '', 'Python'. Wyświetl wyniki.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_04.py)
5. **User Float Input Sum**: Poproś użytkownika o dwie liczby (jako tekst), przekonwertuj je na `float` i wyświetl ich sumę.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_05.py)
6. **Float String to Integer Pitfall**: Spróbuj zamienić napis '12.7' na `int`. Co się dzieje? Zapisz kod i zobacz efekt.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_06.py)
7. **List to String Representation**: Użyj `str()` do połączenia listy `[1, 2, 3]` z napisem ' elementy'.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_07.py)
8. **String 'True' to Boolean Verification**: Przekonwertuj napis 'True' na `bool` i wyświetl wynik.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_08.py)
9. **Whitespace Stripping Before Conversion**: Zamień napis '   99   ' na `int` (użyj `strip()` przed konwersją).  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_09.py)
10. **Chained Float and Int Conversion**: Utwórz zmienną `cena = '49.99'`. Zamień ją najpierw na `float`, a potem na `int`. Wyświetl oba wyniki.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_10.py)
11. **String '0' Truthiness**: Zamień napis '0' na `bool` – co otrzymasz?  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_11.py)
12. **Exception Handling on Invalid Conversion**: Spróbuj zamienić napis 'abc' na `int`. Użyj `try/except`, aby przechwycić błąd.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_12.py)
13. **Float to Int Truncation Analysis**: Zamień liczbę 7.99 na `int` i wyświetl. Co się stało z częścią ułamkową?  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_13.py)
14. **Defensive safe_int Function**: Napisz funkcję `bezpieczna_int(napis)`, która zwraca `None`, jeśli konwersja się nie uda.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_14.py)
15. **None to String**: Zamień wartość `None` na napis i wyświetl.  
   [Rozwiązanie](Module_04_Type_Casting/solutions/task_15.py)

## Moduł 5: Wejście i Wyjście

1. **User Greeting**: Zapytaj użytkownika o imię i przywitaj się komunikatem: 'Cześć, [imię]!'.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_01.py)
2. **Age Confirmation**: Zapytaj o wiek i wyświetl: 'Masz [wiek] lat.'.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_02.py)
3. **Two Numbers Sum**: Poproś o dwie liczby, a następnie wyświetl ich sumę.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_03.py)
4. **Number Squared**: Poproś o liczbę i wyświetl jej kwadrat.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_04.py)
5. **Favorite Color**: Zapytaj o ulubiony kolor i wyświetl: 'Twój ulubiony kolor to [kolor].'.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_05.py)
6. **Three Numbers Mean**: Poproś o trzy liczby i oblicz ich średnią.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_06.py)
7. **Location Formatter**: Zapytaj o miasto i kraj, a następnie wyświetl: 'Mieszkasz w [miasto], [kraj].'.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_07.py)
8. **Float Precision Formatter**: Poproś o liczbę rzeczywistą i wyświetl ją z dokładnością do 2 miejsc po przecinku.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_08.py)
9. **Integer Division and Remainder**: Poproś o dwie liczby całkowite, a następnie wyświetl wynik dzielenia całkowitego i resztę.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_09.py)
10. **Uppercase Transformation**: Zapytaj o tekst i wyświetl go wielkimi literami.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_10.py)
11. **Birth Year to Age Calculator**: Zapytaj o rok urodzenia i oblicz wiek (przyjmij bieżący rok = 2026).  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_11.py)
12. **Rectangle Geometry**: Poproś o długość i szerokość prostokąta, wyświetl pole i obwód.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_12.py)
13. **Name and Lucky Number**: Zapytaj o imię i liczbę, a następnie wyświetl: 'Cześć [imię]! Twoja liczba to [liczba].'.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_13.py)
14. **Sum Check on Three Inputs**: Poproś o trzy liczby i sprawdź, czy pierwsza jest sumą dwóch kolejnych.  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_14.py)
15. **Product Invoice Summary**: Zapytaj o nazwę produktu i cenę netto, wyświetl cenę brutto (23% VAT).  
   [Rozwiązanie](Module_05_Input_Output/solutions/task_15.py)

## Moduł 6: Myślenie Programistyczne (Wzorzec IPO)

1. **IPO Pattern: Rectangle Area**: Napisz program obliczający pole prostokąta. Podziel kod na trzy sekcje: wejście, przetwarzanie, wyjście.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_01.py)
2. **IPO Pattern: User Profile Bio**: Napisz program, który pobiera imię, wiek i miasto, a następnie wyświetla zdanie z tymi danymi.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_02.py)
3. **IPO Pattern: BMI Calculator**: Napisz program obliczający BMI (waga w kg, wzrost w m) – wzór: `waga / wzrost²`.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_03.py)
4. **IPO Pattern: Distance Unit Converter**: Napisz program przeliczający kilometry na mile (1 mila = 1.609344 km).  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_04.py)
5. **IPO Pattern: Academic Grade Average**: Napisz program, który pobiera trzy oceny (1–6) i oblicza średnią arytmetyczną.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_05.py)
6. **IPO Pattern: Time Conversion**: Napisz program zamieniający podaną liczbę godzin na minuty i sekundy.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_06.py)
7. **IPO Pattern: Year to Day Counter**: Napisz program obliczający liczbę dni w podanej liczbie lat (bez lat przestępnych).  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_07.py)
8. **IPO Pattern: Currency Converter**: Napisz program przeliczający kwotę w PLN na EUR (kurs: 1 EUR = 4.30 PLN).  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_08.py)
9. **IPO Pattern: Trapezoid Area**: Napisz program obliczający pole trapezu według wzoru: `P = ((a + b) * h) / 2`.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_09.py)
10. **IPO Pattern: Speed and Distance**: Napisz program, który pobiera prędkość (km/h) i czas (h), a następnie oblicza dystans.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_10.py)
11. **IPO Pattern: Discount Calculator**: Napisz program obliczający cenę po rabacie 20% od podanej ceny.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_11.py)
12. **IPO Pattern: Reverse Three Numbers**: Napisz program, który pobiera trzy liczby i wyświetla je w odwrotnej kolejności.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_12.py)
13. **IPO Pattern: Text Multiplier**: Napisz program, który pobiera tekst i liczbę `n`, a następnie wyświetla tekst `n` razy.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_13.py)
14. **IPO Pattern: CLI Calculator**: Napisz prosty kalkulator – pobiera dwie liczby i znak działania (+, -, *, /), wyświetla wynik.  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_14.py)
15. **IPO Pattern: Triangle Area**: Napisz program obliczający pole trójkąta ((podstawa * wysokość) / 2).  
   [Rozwiązanie](Module_06_Algorithmic_Thinking/solutions/task_15.py)

## Moduł 7: Ćwiczenia Rozszerzone

1. **Basic User Profile Interaction**: Podstawowa wersja: poproś o imię, wiek, ulubioną liczbę. Wyświetl: 'Cześć [imię]! Za 10 lat będziesz mieć [wiek+10] lat, a Twoja liczba razy 3 to [liczba*3].'  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_01.py)
2. **Explicit Type Conversions**: Dodaj konwersję wieku i liczby na `int` (użyj `int()`).  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_02.py)
3. **F-String Formatting Integration**: Sformatuj wynik za pomocą f-stringa.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_03.py)
4. **Digit String Validation**: Dodaj walidację: jeśli użytkownik poda wiek niebędący liczbą, wyświetl komunikat błędu.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_04.py)
5. **Decimal Precision Display**: Oblicz wiek za 10 lat i wyświetl go z dwoma miejscami po przecinku (np. 30.00).  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_05.py)
6. **Exception Handling for Input Parsing**: Dodaj obsługę `ValueError` przy konwersji wieku i liczby.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_06.py)
7. **String Sanitization with strip**: Użyj `strip()` przed konwersją, aby usunąć przypadkowe spacje.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_07.py)
8. **Favorite Color Integration**: Dodaj pytanie o ulubiony kolor i wpleć go w zdanie.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_08.py)
9. **Square Root on Secondary Number**: Zapytaj o dodatkową liczbę i wyświetl jej pierwiastek kwadratowy.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_09.py)
10. **Dual Favorite Numbers Math**: Zapytaj o dwie ulubione liczby, wyświetl ich sumę, różnicę i iloczyn.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_10.py)
11. **Unified Multi-line F-String**: Wyświetl wszystkie dane w jednym zdaniu z użyciem jednego f-stringa.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_11.py)
12. **Retry Loop on Parsing Errors**: Dodaj pętlę, aby program pytał ponownie w przypadku błędu.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_12.py)
13. **Date of Birth Age Resolution**: Zapytaj o datę urodzenia (dzień, miesiąc, rok) i oblicz dokładny wiek.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_13.py)
14. **Color to HEX Code Lookup**: Zapytaj o ulubiony kolor i wyświetl jego kod HEX (np. #FF0000 dla czerwonego – użyj słownika).  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_14.py)
15. **Comprehensive Registration Engine**: Połącz wszystko: walidacja, f-stringi, konwersje, obliczenia i czytelne komunikaty.  
   [Rozwiązanie](Module_07_Extended_Practice/solutions/task_15.py)

## Moduł 8: Standard PEP 8 i Czysty Kod

1. **PEP 8 snake_case Convention**: Zmień nazwę zmiennej `mojaZmienna` na zgodną z PEP 8 (`snake_case`).  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_01.py)
2. **Four Spaces Indentation**: Popraw wcięcia w kodzie: zastąp tabulatory 4 spacjami.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_02.py)
3. **Whitespace Around Binary Operators**: Dodaj spacje wokół operatorów w wyrażeniu: `a+b*c`.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_03.py)
4. **88-Character Visual Line Limit**: Skróć długą linię dzieląc ją na kilka linii.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_04.py)
5. **Function snake_case Naming**: Napisz funkcję `pole_prostokata` używając `snake_case`.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_05.py)
6. **Docstring Documentation**: Dodaj docstring do funkcji opisujący jej działanie.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_06.py)
7. **Return Values Over Side Effects**: W funkcji użyj `return` zamiast `print` – zwróć wynik, a nie wyświetlaj.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_07.py)
8. **Blank Line Section Separation**: Oddziel w kodzie sekcje: wejście, przetwarzanie, wyjście – użyj pustych linii.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_08.py)
9. **Descriptive Identifier Names**: Zmień nazwy zmiennych `a` i `b` na bardziej opisowe (np. `szerokosc`, `wysokosc`).  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_09.py)
10. **Digit Grouping with Underscores**: Użyj podkreśleń do oddzielenia tysięcy w liczbie `1000000`.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_10.py)
11. **Avoid Ambiguous Single-Letter Identifiers**: Unikaj używania `l` (małe L) jako nazwy zmiennej – zmień na `dlugosc`.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_11.py)
12. **Identity Check Against None**: Zamień `if x == None` na `if x is None`.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_12.py)
13. **Consistent String Quotes**: Ujednolic cudzysłowy – użyj `"` dla wszystkich napisów w kodzie.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_13.py)
14. **Top-Level Imports Ordering**: Umieść wszystkie importy na górze pliku.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_14.py)
15. **Main Entry Point Guard**: Dodaj konstrukcję `if __name__ == '__main__':` i umieść w niej wywołanie głównej funkcji.  
   [Rozwiązanie](Module_08_PEP8_Standard/solutions/task_15.py)

## Moduł 9: F-Stringi i Formatowanie Napisów

1. **Basic F-String Interpolation**: Używając f-stringa, wyświetl: 'Mam na imię Anna i mam 30 lat.' (zmienne `imie`, `wiek`).  
   [Rozwiązanie](Module_09_FStrings/solutions/task_01.py)
2. **Pi Precision Formatting**: Wyświetl liczbę π = 3.1415926535 z dokładnością do 2 miejsc po przecinku.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_02.py)
3. **Fraction Division Precision**: Wyświetl wynik dzielenia 22/7 z dokładnością do 3 miejsc po przecinku.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_03.py)
4. **In-line Arithmetic in F-Strings**: W f-stringu wykonaj obliczenie: 'Suma 5 i 7 to {5+7}'.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_04.py)
5. **Quotes Handling in F-Strings**: Wyświetl tekst: To jest 'cytat' w tekście używając f-stringa bez ucieczki.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_05.py)
6. **Column Alignment and Padding**: Wyświetl tabelkę: `| imię: Kacper | wiek: 25 |` z wyrównaniem do 10 znaków.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_06.py)
7. **Leading Zeros Date Formatting**: Wyświetl datę w formacie `DD-MM-RRRR` z zerami wiodącymi (np. `05-03-2026`).  
   [Rozwiązanie](Module_09_FStrings/solutions/task_07.py)
8. **Percentage Formatting**: Wyświetl procent 0.8567 jako `85.67%`.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_08.py)
9. **Thousands Separators**: Wyświetl liczbę 1234567 z separatorami tysięcy: `1,234,567`.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_09.py)
10. **Function Invocation in Expressions**: W f-stringu wywołaj funkcję `len('Python')` wewnątrz `{}`.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_10.py)
11. **Binary Number Representation**: Wyświetl liczbę 255 w systemie binarnym.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_11.py)
12. **Explicit Positive/Negative Sign**: Wyświetl liczbę 3.14 ze znakiem: `+3.14`.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_12.py)
13. **Dictionary Field Interpolation**: Utwórz słownik `osoba = {'imie': 'Ewa', 'wiek': 28}` i wyświetl jego zawartość za pomocą f-stringa.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_13.py)
14. **Scientific Notation**: Wyświetl liczbę 0.0001234 w notacji naukowej.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_14.py)
15. **Direct Prompt Greeting F-String**: Połącz f-stringa z `input()` w jednej linii: zapytaj o imię i od razu wyświetl powitanie.  
   [Rozwiązanie](Module_09_FStrings/solutions/task_15.py)

## Moduł 10: Walidacja Danych i Obsługa Błędów

1. **Integer Parsing with try/except**: Poproś użytkownika o liczbę całkowitą. Użyj `try/except` do obsługi `ValueError`.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_01.py)
2. **Whitespace Sanitization Before Parse**: Poproś o liczbę, użyj `strip()` przed konwersją, aby usunąć spacje.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_02.py)
3. **Empty String Guard**: Poproś o tekst. Jeśli użytkownik nic nie wpisze, wyświetl: 'Nie podano tekstu.'  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_03.py)
4. **Float Parsing Guard**: Poproś o liczbę zmiennoprzecinkową. Obsłuż błąd, jeśli użytkownik poda coś innego.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_04.py)
5. **Looping Integer Validator**: Napisz funkcję `pobierz_int()`, która pyta aż do podania poprawnej liczby całkowitej.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_05.py)
6. **Age Range Assertion**: Poproś o wiek. Jeśli wiek nie mieści się w zakresie 0–120, wyświetl błąd.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_06.py)
7. **Strictly Positive Number Guard**: Poproś o liczbę dodatnią. Jeśli użytkownik poda 0 lub ujemną, wyświetl komunikat.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_07.py)
8. **Alphabetic Only Name Check**: Poproś o tekst i sprawdź, czy nie zawiera cyfr.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_08.py)
9. **ZeroDivisionError Exception Handler**: Poproś o dwie liczby i wykonaj dzielenie. Obsłuż błąd dzielenia przez zero.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_09.py)
10. **LBYL Defensive Division Guard**: Poproś o dwie liczby. Sprawdź, czy druga liczba nie jest zerem przed dzieleniem.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_10.py)
11. **Year Range Validation**: Poproś o rok. Sprawdź, czy rok jest z zakresu 1900–2026.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_11.py)
12. **Full try-except-else-finally Flow**: Użyj bloku `try/except/else/finally` – w `else` wyświetl wynik, w `finally` napisz 'Koniec operacji'.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_12.py)
13. **Allowed Options Whitelist**: Poproś o kolor z listy: czerwony, zielony, niebieski. Jeśli nie ma na liście, wyświetl błąd.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_13.py)
14. **Divisibility Prime Check**: Poproś o liczbę i sprawdź, czy jest liczbą pierwszą (dla uproszczenia sprawdź podzielność przez 2 i 3).  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_14.py)
15. **Multi-field Validation Pipeline**: Połącz walidację imienia (niepusty tekst), wieku (liczba 0–120) i ulubionej liczby w jednym programie.  
   [Rozwiązanie](Module_10_Data_Validation/solutions/task_15.py)

## Moduł 11: REPL i Szybkie Testowanie

1. **REPL Math Evaluation**: Oblicz `25 * 4 - 10`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_01.py)
2. **Type Introspection**: Sprawdź typ wartości 'Python' i 3.1415.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_02.py)
3. **Power Calculation**: Utwórz zmienną `x = 6` i oblicz `x ** 3`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_03.py)
4. **Lexicographical Comparison**: Sprawdź, czy 'banan' jest większe od 'jabłko'.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_04.py)
5. **Function Rapid Testing**: Zdefiniuj funkcję `kwadrat(n)` zwracającą `n * n` i przetestuj dla 7.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_05.py)
6. **REPL Interactive Echo**: Użyj `input()` w REPL, wpisz swoje imię i wyświetl je.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_06.py)
7. **Padded Integer Parse**: Sprawdź działanie `int('   50   ')`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_07.py)
8. **Float Rounding**: Sprawdź, co robi `round(2.71828, 2)`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_08.py)
9. **Truthiness of Non-Empty String**: Sprawdź, co zwróci `bool('False')`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_09.py)
10. **Exception Inspection**: Spróbuj wykonać `10 / 0` i odczytaj typ błędu.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_10.py)
11. **List Length Inspection**: Utwórz listę `[5, 10, 15]` i sprawdź `len(lista)`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_11.py)
12. **Substring Search**: Sprawdź, czy napis 'programowanie' zawiera podnapis 'gram'.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_12.py)
13. **String Multiplication**: Oblicz `'Ha' * 5`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_13.py)
14. **Type of None**: Sprawdź, co zwróci `type(None)`.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_14.py)
15. **Built-in Docstring Help**: Wpisz `help(print)` i przeczytaj dokumentację.  
   [Rozwiązanie](Module_11_REPL_Testing/solutions/task_15.py)

## Moduł 12: Zadania Integracyjne

1. **Four Primitive Types Showcase**: Napisz program, który używa wszystkich typów danych: `int`, `float`, `str`, `bool` – wyświetl je z opisem.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_01.py)
2. **Defensive CLI Calculator**: Stwórz kalkulator z walidacją wejścia i obsługą błędów (dzielenie przez zero, złe dane).  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_02.py)
3. **Circle Geometry Engine**: Napisz program obliczający pole i obwód koła. Użyj f-stringa do wyświetlenia wyniku z 2 miejscami po przecinku.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_03.py)
4. **User Registration System**: Stwórz program rejestracyjny: pobierz imię, email, wiek. Sprawdź, czy email zawiera `@`, a wiek jest liczbą.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_04.py)
5. **Bidirectional Temperature Converter**: Napisz program konwertujący temperaturę: z °C na °F i z °F na °C. Użytkownik wybiera kierunek.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_05.py)
6. **Interactive 3-Question Quiz**: Stwórz prosty quiz: 3 pytania. Punkty po każdej odpowiedzi.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_06.py)
7. **Number Guessing Game**: Napisz program, który losuje liczbę z zakresu 1–10, a użytkownik zgaduje. Podpowiedzi: za dużo/za mało.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_07.py)
8. **Log Export Payload Simulator**: Stwórz program, który zapisuje wprowadzone dane do pliku (symulacja – wyświetl, co by zapisał).  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_08.py)
9. **ASCII Data Table Formatter**: Napisz program, który wyświetla wszystkie wprowadzone dane w formie prostej tabeli.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_09.py)
10. **Interactive Multi-Menu System**: Stwórz program z menu: 1 – kalkulator, 2 – konwerter temperatury, 3 – wyjście. Użytkownik wybiera opcję.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_10.py)
11. **Dictionary Profile Record**: Napisz program przechowujący dane w słowniku: `{'imie': '...', 'wiek': ..., 'miasto': '...'}`. Wyświetl zawartość.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_11.py)
12. **Student Grade Report Generator**: Stwórz program generujący raport: pobierz imię, trzy oceny, oblicz średnią i wyświetl w ładnym formacie.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_12.py)
13. **Continuous Loop Until Exit**: Napisz program, który działa w pętli aż użytkownik wpisze 'exit'. W każdej iteracji pyta o liczbę i wyświetla jej kwadrat.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_13.py)
14. **Structured Three-Function Architecture**: Stwórz program podzielony na funkcje: `pobierz_dane()`, `przetworz_dane()`, `wyswietl_wynik()`.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_14.py)
15. **Production Grade Student Assessment Engine**: Napisz kompletny program zgodny z PEP 8, z f-stringami, walidacją, obsługą błędów i komentarzami – np. system ocen ucznia.  
   [Rozwiązanie](Module_12_Capstone_Projects/solutions/task_15.py)
