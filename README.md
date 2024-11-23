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
### Aufgabe 2

Anforderungen:
* Implementiere ein PUT -Endpoint /customers/:id/contracts/:contract_id , das die Vertragsdaten aktualisiert.
  * Umstellung durch das Ersetzen von "RetrieveAPIView" mit "RetrieveUpdateAPIView"
* Die Eingabedaten werden als JSON im Request-Body übergeben.
  * Wird von Django Rest so erwartet
* Validiere die Eingabedaten und stelle sicher, dass ungültige Änderungen zurückgewiesen werden.
  * Durch Validierungsmethoden im Serializer

Verifizierung: 
`http://127.0.0.1:8000/api/customers/1/contracts/2/` aufrufen, mit body:
```json
{
    "contract_number": "654321",
    "customer": 1,
    "premium": "-1.00"
}
```
Fehlermeldung: "Premium must be positive".
Weitere Fehlermeldungen werden automatisch generiert (auch siehe models.py).

### Aufgabe 3


Anforderungen:

* Lade die Vertragsdaten über die API und zeige sie in einer Tabelle an.
  * Serializer "ContractListSerializer" angepasst, damit über den Endpunkt `/api/customers/:id/contracts/` nun alle werte übergeben werden. Hier mit sollen rekursive anfragen vermieden werden.
* Binde ein Formular ein, das es ermöglicht, die Vertragsdaten zu ändern.
  * Implementierung fetch anfragen auf die API, Überlegung bei mehr anfragen einen fetch handler zu bauen. 
  * Beim form-submit wurde direkt die Seite neu geladen. Beim simplen neu laden geht jedoch die customer ID verloren daher, `e.preventDefault()` um Refresh zu unterbinden und nur die Tabelle neu zu laden.
* Nach dem Abschicken des Formulars sollen die Änderungen in der API gespeichert und eine Bestätigung der geänderten Daten angezeigt werden.

### Aufgabe 4

Anforderungen:

* Im Web-Frontend wird nach der Aktualisierung eine Liste der geänderten Felder mit alten und neuen Werten angezeigt.
  * Abgleich der History im Frontend und einfügen der Historischen werte falls eine Änderung vorliegt. 
  * Zusätzlich Fehlerbehebung von verwechslung von ContractID und ContractName und folgende falsche Abspeicherung. `Patch` wäre optimaler da hier nicht alle Felder geupdated werden müssen.
* Speichere die alten Werte in einer Datenstruktur, um sie für den Vergleich anzuzeigen.
  * Um die Änderungshistorie im Django model zu Tracken, gibt es das Modul `django-simple-history`. Nach Implementierung müssen nun noch die Datenbankmigrationen durchgeführt werden,
  so wie der ``ContractListSerializer`` um `last_hisotry` erweitert werden.
```
python manage.py makemigrations
python manage.py migrate 
```

### Aufgabe 5

Anforderungen:

* Implementiere einen POST-Endpoint /login, der Benutzername und Passwort akzeptiert und bei erfolgreicher Authentifizierung einen Token zurückgibt.
  * Implementierung der `Login` view unter Verwendung der Django eigenen Authentifizierung und Benutzerverwaltung.
  * Hierfür kann ein Benutzer mit `python manage.py createsuperuser` angelegt werde (zur schnellen Demo). Hier username: admin und PW: admin. SQLLite Datei lade ich daher mit ins repo
* Überprüfe bei jedem API-Aufruf, ob ein gültiger Token im Header enthalten ist.
  * Durch Django eigene `permission_classes`
  * Im frontend nach login über SessionStore aufrufbar
* Tokens werden serverseitig in einer einfachen Datenstruktur gespeichert.
  * Übernommen von Django
