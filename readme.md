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

## Lekce 3 (18. 12. 2024)

## Lekce 4 (19. 12. 2024)