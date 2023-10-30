# RSA-notes
Notes from experimenting on rsa...

## Quick Start
```python
python3 rsa-test.py [Poruka]
```
***Poruka*** je string koji će se enkriptirati i dekriptirati.

## Argumenti
```python
python3 rsa-test.py [arg1] [arg2]
```
***arg1*** je string poruka koja će se enkriptirati i dekriptirati. <br>
***arg2*** je broj 1, 6, 100 ili 250 koji određuje alternativne p i q te d i e tako da program ne mora generirati.

## Opcije u kodu
### _doDecript 
  Ne koristi se jer je zakomentiran
### _generate_key
  **True**: Tražiti će unos broja bitova i onda generirati *keypair* (p i q)[^1] <br>
  **False**: Koristi zadane vrijednosti zadane CLI argumentima

> [^1]: Ovo dugo traje pa je default False

## Izlaz
Za ulaz:
```python
python3 rsa-test.py Poruka 6
```
Izlaz će izgledati:
```python
de mod ln =  1
 n  =  780800588233
 ln =  780798819220
 e  =  65537
 d  =  493412623373

[754572165661, 233818160843, 367288071411, 313094748251, 656836297297, 583802863494]
Poruka
```
Gdje su e i d, javni i privatni ključ, a polje brojeva iznad izlaza su enkriptirana ASCII slova poruke.

> [!IMPORTANT]
> *!OVO NIJE PRODUKCIJSKA APLIKACIJA! - već samo za igranje s RSA enkripcijskim protokolom*
