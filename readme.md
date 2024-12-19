# Testování softwaru a TDD

## Lekce 1 (16. 12. 2024)
Prošli jsme prezentaci slajdy 1-34:
- Motivace - proč testovat
- TDD (Test-Driven Development)
- Druhy testů
  - Unit testy
  - Integrační testy
  - End-to-end testy
  - Akceptační testy
- PyTest
  - [Dokumentace](https://docs.pytest.org/en/latest/contents.html)
  - Instalace:
    - ```bash
      pip install pytest
      ```
  - Testování
    - assert
    - testování vyvolané vyjímky
    - testování pomocí třídy

### Domácí úkol
Definujte třídu `ComplexNumber` reprezentující [komplexní číslo](https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo)
a definujte následující metody:
- [x] `__init__` (konstruktor)
- [x] `__eq__` (rovnost)
- [ ] `__lt__` (<)
- [ ] `__gt__` (>)
- [x] `__repr__`
- [ ] `__str__`
- [x] `properties` (gettery a settery)
- [ ] `add` (sčítání)
- [ ] `subtract` (odečítání)
- [ ] `multiply` (násobení)
- [ ] `divide` (dělení)
- [ ] `conjugate` (číslo komplexně sdružené)
- [ ] `absolute_value` (absolutní hodnota)

**A vše řádně otestujte.**

## Lekce 2 (17. 12. 2024)
Prošli jsme prezentaci slajdy 35-47:
- fixtures
- parametrické testy
- mockování
- coverage
  - `pip install coverage`

Prošli jsme úkoly z Journey:
- [x] Cvičení 2
- [x] Cvičení 3
- [x] Cvičení 4

## Lekce 3 (18. 12. 2024)
Prošli jsme úkol z Journey:
- [x] Cvičení 5

A další cvičné příklady:
- [x] is_prime a factorial
- [x] word_count
- [x] fibonacci

## Lekce 4 (19. 12. 2024)
Procvičili jsme další úkoly:
- [x] library
- [x] matrix (transpozice)
- [ ] Task manager

### Domácí úkoly
#### Správa uživatelských účtů a volání externího API
Vytvořte třídu `User`, která má atributy `username` (uživatelské jméno) a `email`.
Vytvořte třídu `UserManager`, která umožňuje přidávat uživatele a odesílat ověřovací e-mail prostřednictvím externí služby.
Metoda `send_verification_email(user)` ve třídě `UserManager` by měla volat metodu `send_email(to, subject, body)`, 
která simuluje volání externího API pro odesílání e-mailu.
Použijte **mock** objekty, abyste otestovali, zda metoda `send_verification_email` volá `send_email` s odpovídajícími parametry.

#### Validace rodného čísla
Napište funkci validující rodné číslo. 
Funkce `is_valid()` bere jako parameter string s rodným číslem, 
a vráti `True` nebo `False` v závislosti na výsledku validace.

- K funkci přidejte pozitivní i negativní testy.
- Zkuste použít programování s cyklem. 
- Zkuste parametrizování testu. 
- Zkuste testování výjimek.

[Odkaz na paragraf 2 zákona stanovující validní rodné číslo](https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1995/301/)