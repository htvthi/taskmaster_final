# taskmaster_final 

---

> Aufgaben und Projekt für die Lehrveranstaltung "Betriebliche Anwendungen" an der HTW Berlin SoSe 2020 von [Hai Trang Vu Thi](https://github.com/htvthi) und [Anne Gliesche](https://github.com/spielogabi)

---
--- 

### Aufgabenstellung 

Die Aufgabe bestand darin ein Django- Projekt im Team von zwei Leuten, zu entwickeln.
Folgende Punkte sind für ein erfolgreiches Projekt notwendig

#### Konzept

Im Vorfeld wurde ein Konzept ausgearbeitet, welches die Vision klar darstellt und zudem mindestens 4 User Cases mit funktionellen Anforderungen zeigt

#### Umfang und Funktionalität

+ Die Anwendung stürzt nicht ab bei lokaler Ausführung
+ Implementieren aller CRUD Operationen
+ Verwenden von HTML und CSS
+ Die Anwendung darf kein Blog sein
+ Implementieren eines Login-Systems, alternativ Einbinden einer Datenbank

#### Versionskontrolle 

Das Projekt ist in ein GitHub Repository zu pushen, an welchem kontoinuierlich gearbeitet werden sollte.

#### Deployment 

Das Projekt ist auf einem Sever zu deployen. Auch hier ist ein kontinuierliches Deployen erstrebenswert. 

---

### Idee

Unser Projekt ist eine To-Do-Liste. Um Tasks anzulegen, benötigt man vorher einen Account. Diesen kann man über die Registrierung anlegen.
Tasks können angelegt, bearbeitet und gelöscht werden.

---

### Handhabung 

#### Login Seite 

Das Projekt startet auf der Login Seite. Dort kann man seine Credentials eintragen. Sollte man zum aktuellen Zeitpunkt noch kein Konto haben, so besteht die Möglichkeit über einen Link zur Registrierung gehen. 
Ist der Login falsch, wird eine Fehlermeldung ausgegeben. Ist der Login erfolgreich, kommt man auf die Seite mit den angelegten Tasks. 

#### Registrierung

Auf der Register Seiter legt man mit einem Usernamen, Emailadresse und dem Passwort, einen Account an. Ist das Passwort nicht sicher genug, bekommt man eine Fehlermeldung.
Ist die Registrierung erfolgreich, kommt man auf die Homepage

#### Homepage 

Task können hier über ein Formular angelegt werden. Sind sie gespeichert, besteht die Möglichkeit über Buttons,  sie zu bearbeiten oder zu löschen. 
Die Tasks sind in einer Datenbank gespeichert. 
Zu dem können Tasks als abgearbeitet angekreuzt werden, worauf hin sie durchgestrichen sind.
Außerdem besteht die Möglichkeit, sich über die Taskseite auch wieder auszuloggen.

#### Löschen 

Auf der Löschen Seite können die Tasks gelöscht werden, aber man kann auch zurück auf die Tasks Liste, sollte man versehentlich drauf geklickt haben.

#### Bearbeiten

Auf der Bearbeiten Seite können Tasks über das Formular nur bearbeitet werden.

---


