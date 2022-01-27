# banking-system
 
<b>Inledning</b>

Arbetet går ut på att skapa en applikation som ska kunna hantera kunder och deras konton i en fiktiv bank. Applikationen körs i terminalen och all data gällande kunder, konton och transaktioner sparas i och hämtas från textfiler (ex. “customer_data.txt”).

Arbetet ska utföras under två veckors tid och avslutas med en inlämning samt redovisning av koden. Arbetet ska även innehålla user stories, klassdiagram samt milestones och tasks.

Målet med arbetet är att genom terminalen få input från användaren för att sedan visa eller skapa data som är kopplad till banken och dess kunder.

<b>User Stories</b>

- Som användare vill jag kunna se alla kunder i banken, den information som är intressant är fullständigt namn samt personnummer.
- Som användare vill jag kunna se övergripande information om en specifik kund i banken, den information som är intressant är namn, personnummer, kontonummer, kontotyp samt saldo.
- Som användare vill jag kunna lägga till nya kunder i banken.
- Som användare vill jag kunna ändra namn på befintliga kunder i banken.
- Som användare vill jag kunna radera befintliga kunder (och deras konton) i banken.
- Som användare vill jag kunna skapa nytt konto åt befintliga kunder i banken.
- Som användare vill jag kunna stänga valt konto åt befintliga kunder i banken.
- Som användare vill jag kunna sätta in och ta ut pengar från valt konto i banken.
- Som användare vill jag kunna se alla utförda transaktioner från valt konto i banken, den information som är intressant är kontonummer, insättning eller uttag med summa samt datum.

<b>Teknologier</b>

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

<b>Klassdiagram</b>

![bank_class_diagram](https://user-images.githubusercontent.com/89841651/151386656-e395631c-ed43-493b-a249-fd6bfdfc5984.JPG)

<b>Milestones & Tasks</b>

Kravinsamling:
- Sammanställ de krav som framgår i uppgiftens specifikation.
- Rangordna kraven efter prioritet.

Implementation:
- Skapa en datasource-klass som hanterar var datan kommer ifrån.
- Skapa en bank-klass som hanterar kunder och dess konton.
- Skapa en customer-klass som endast skapar objekt av kunder.
- Skapa en account-klass som endast skapar objekt av konton.
- Skapa en transaction-klass som endast skapar objekt av transaktioner.
- Skapa main-scriptet som hanterar UI genom terminalen.
