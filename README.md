# banking-system
 
## **Inledning**

Arbetet går ut på att skapa en applikation som ska kunna hantera kunder och deras konton i en fiktiv bank. Applikationen körs i terminalen och all data gällande kunder, konton och transaktioner sparas i och hämtas från textfiler (ex. “customer_data.txt”).

Arbetet ska utföras under två veckors tid och avslutas med en inlämning samt redovisning av koden. Arbetet ska även innehålla user stories, klassdiagram samt milestones och tasks.

Målet med arbetet är att genom terminalen få input från användaren för att sedan visa eller skapa data som är kopplad till banken och dess kunder.

**User Stories**

- Som användare vill jag kunna se alla kunder i banken, den information som är intressant är fullständigt namn samt personnummer.
- Som användare vill jag kunna se övergripande information om en specifik kund i banken, den information som är intressant är namn, personnummer, kontonummer, kontotyp samt saldo.
- Som användare vill jag kunna lägga till nya kunder i banken.
- Som användare vill jag kunna ändra namn på befintliga kunder i banken.
- Som användare vill jag kunna radera befintliga kunder (och deras konton) i banken.
- Som användare vill jag kunna skapa nytt konto åt befintliga kunder i banken.
- Som användare vill jag kunna stänga valt konto åt befintliga kunder i banken.
- Som användare vill jag kunna sätta in och ta ut pengar från valt konto i banken.
- Som användare vill jag kunna se alla utförda transaktioner från valt konto i banken, den information som är intressant är kontonummer, insättning eller uttag med summa samt datum.

**Teknologier**

Programmeringsspråk:
Python

Moduler:
datasource.py,
bank.py,
customer.py,
account.py,
transaction.py

IDE:
Visual Studio Code

Data storage:
.txt

## **Klassdiagram**

![bank_class_diagram](https://user-images.githubusercontent.com/89841651/151386656-e395631c-ed43-493b-a249-fd6bfdfc5984.JPG)

## **Milestones & Tasks**

Kravinsamling:
- Sammanställ de krav som framgår i uppgiftens specifikation.
- Rangordna kraven efter prioritet.

Förberedelser:
- Skapa nytt projekt på Github.
- Sätt upp arbetsschema.

Implementation:
- Skapa en datasource-klass som hanterar var datan kommer ifrån.
   - Skapa en .txt-fil för kundinformation och populera den med mockdata efter mallen i inlämningsuppgiften.
   - Skapa en .txt-fil för transaktioner.
   - Implementera alla funktioner som ingår i kraven för inlämningsuppgiften.
   - Se över funktionalitet med befintliga funktioner och lägg till funktioner om det behövs.
- Skapa en bank-klass som hanterar kunder och dess konton.
   - Implementera alla funktioner som ingår i kraven för inlämningsuppgiften.
   - Se över funktionalitet med befintliga funktioner och lägg till funktioner om det behövs.
- Skapa en customer-klass som endast skapar objekt av kunder.
- Skapa en account-klass som endast skapar objekt av konton.
- Skapa en transaction-klass som endast skapar objekt av transaktioner.
- Skapa main-scriptet som hanterar UI genom terminalen.
   - Skapa en funktion som kör en prompt över valen som användaren har (se user stories).
   - Skapa funktioner för upprepande kod.
   - Säkerställ att all input kontrolleras.

Kvalitetskontroll:
- Se över all kod och korta ner där det finns utrymme.
- Kommentera alla funktioner för smidigare navigering.
- Leta efter buggar
- Leta efter buggar
- Leta efter buggar
