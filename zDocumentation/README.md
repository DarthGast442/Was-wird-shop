# Was-wird-shop
Alina und Christian versuchen einen Shop mit DB, Front- und Backend zu bauen. Schauen wir mal was wird. Was wird!

Inhaltsverzeichnis:
1. Installieren der notwendigen Software
2. Starten der Website 
3. DB-User

Installieren der notwendigen Software:
1.1 SQL Server Management Studio
    Das Programm SQL Server Management Studio von Microsoft muss installiert werden.
    Zusätzlich muss das Programm ODBC Driver for SQL Server installiert werden (ebenfalls von Microsoft)
    Kofiguration: Im SSMS muss ein rechtsklick auf den Server durchgeführt werden (oberstes Item in der linken Auswahlleiste).
    Dort Rechtsklick und "Properties" auswählen. Dann Security aufrufen und sowohl SQL Server als auch Windows Authentification Mode erlauben.

Aufrufen der Website:
1. ein neues cmd-Fenster aufrufen
2. Den Pfad, an dem die Datei "shop.py" liegt kopieren. Beispiel: C:\Users\A1D5A54\OneDrive - REWE digital\Dokumente\sonstiges\IT-Projekte\Was-wird-shop\Backend\Python
3. Eingabe in cmd: cd C:\Users\A1D5A54\OneDrive - REWE digital\Dokumente\sonstiges\IT-Projekte\Was-wird-shop\Backend\Python\shop.py
4. Eingabe in cmd: py shop.py 
5. Die Website ist unter der Adresse 127.0.0.1:5000 erreichbar

DB-User:
1. DB_ALL
Password: WasWirdShop123
authorizations: ALL
Use: currently for every DB-operation; Future: disabled/special admin tasks