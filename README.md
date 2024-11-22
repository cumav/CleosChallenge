# Gedanken vor Implementierung

Da die Sprache frei wählbar ist, habe ich mich für die Sprache entschieden, die ich am meisten verwende: Python. Beim Überlegen der Challenge ist aufgefallen, dass sich besonders auf folgende Themen fokussiert wird:

* Die Implementierung von API-Endpunkten, inklusive Speichern und Ändern der Daten
* Die Authentifizierung und Autorisierung von Anfragen

Nach Recherche wurden drei potentielle Frameworks identifiziert:

* Flask
* FastAPI 
* Django

### Flask

Mit Flask lassen sich theoretisch super schnell APIs erstellen. Es ist aber meines Wissens eher "Bare Bones" und würde später Mehraufwand bei unter anderem Datenvalidierung und Authentifizierung verursachen.

### FastAPI

Ähnlich wie Django, der Implementierungsaufwand scheint ähnlich zu sein (durch Hinzuziehen von ChatGPT bestätigt).

### Django

Django ist das bekannteste Framework, und Funktionen wie Token-Authentifizierung habe ich in Django in meiner Vergangenheit schon umgesetzt. Viele geforderte Funktionen werden schon vom Django Framework selbst geliefert. Sowohl der Aufwand als auch die Qualität sollten hier am optimalsten sein.

Warum Qualität? Ein weit verbreitetes Framework macht im Vergleich zu Eigenimplementierungen Sinn, da besonders bei sicherheitsrelevanten Themen wie Login etc. eine Eigenimplementierung häufig risikoreicher ist.

## Entscheidung

Django

# Umsetzung

### Aufgabe 1

Anforderungen:

* Implementiere ein GET -Endpoint /customers/:id/contracts, der alle Verträge eines
Kunden liefert.
* Implementiere ein GET -Endpoint /customers/:id/contracts/:contract_id , der die
    * Einfaches Datenmodel für beide erstellt. Serializer zum einfachen Umwandeln hin und rück konvertieren in JSON und View um API Endpunkt schlussendlich zu implementieren
* Details eines spezifischen Vertrags liefert.
  * Detail "premium" hinzugefügt
* Erstelle eine einfache Datenstruktur (z. B. in JSON), die die Stammdaten eines Kunden
und die Verträge repräsentiert.
  * Automatisch durch die models erstellt. Hierzu muss 
```
python manage.py makemigrations
python manage.py migrate
```
ausgeführt werden.

Ich habe zusätzlich Fixtures angelegt, um Daten wie folgt einzuspielen:

```
python manage.py loaddata initial_data.json
```
