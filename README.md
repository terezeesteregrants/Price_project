# Cenu salīdzināšanas uzdevums

### Uzdevuma apraksts

Uzdevums ir izveidot programmu, kas salīdzina Apple iPad 10.9" Wi-Fi 64GB - Blue 10th gen (2022) cenas tet.lv, euronics.lv un rdveikals.lv vietnēs, attiecīgi izsūta uz savu e-pastu par izdevīgāko piedāvājumu un saglabā datus par cenām excel failā. 
Šeit ir, norādījumi kā jāizstrādā uzdevums:

1. Izveidojiet e-pasta nosūtīšanu (`send_email`) funkciju. Norādiet savu izvēlētu tēmu, ziņojumu, kas paziņotu par zemāko cenu norādītajos internetveikalos. Šim izmanto Gmail SMTP serveri, parole jāiegūst no sava google konta.

2. Izgūstiet datus par cenu no attiecīgi norādītajām mājaslapām 

3. Salīdziniet cenas ar `check_price` funkciju.

4. Paziņojiet norādītajam e-pasta adresātam par zemāko pieejamo cenu produktam attiecīgajā mājaslapā. 

5. Piefiksējiet datus un cenu izmaiņas (ja tādas ir), excel datnē, izveidojot failu `price_tracker.xslx`, norādt vietnes nosaukumu, cenu un laiku, kurā tas tiek apskatīts. 

Mērķis ir uzzināt, kurā vietnē ir visizdevīgākais piedāvājums izvēlētajam produktam, kā arī pārskatāmi to aplūkot Excel faila datnē.

**Programmu jāiesniedz kā result.py failu.**

### Izmantotās bibliotēkas

1. `pandas` 
Izmantots, lai analizētu un saglabātu datus. Šajā uzdevumā tiek izmantots, lai apstrādātu datus, izveidotu DataFrame, saglabājot to Excel failā.

2. `selenium`
Izmantots, lai iegūtu mājaslapu datus izvēlētajiem internetveikaliem. Galvenokārt, bibliotēka ļauj automatizēt pārlūku darbības, piemēram, mūsu uzdevumā, lai iegūt datus no tīmekļa ar 'find_element' funkciju, kā arī izpilda 'time_sleep' funkciju, kas nodrošina ielādes gaidīšanu.

3. `smtplib`
Nodrošina e-pastu nosūtīšanas funkciju, izmantojot Gmail SMTP serveri.


### Programmas izmantošanas metodes

1. Pārliecināties vai ir instalēt nepieciešamās bibliotēkas, ja nav, tad ar funkciju var instalēt `pip install` + (bibliotēkas nosaukums)

2. Izveidojiet savu gmail e-pastu (ja tāda nav). Iegūstiet no Google App Passwords kodēta forma parolei, lai izmantotu `smtplib` bibliotēku (norādījumus var apsatīt norādītajā linkā kā to panākt: https://youtu.be/ueqZ7RL8zxM?si=PEVj_CAWWrwCrULX)

3.Salīdziniet cenas, attiecīgi izsūtiet epastu, kur norāda mājaslapas, kur cenas viszemākās vai visas ja cenas vienādas.

4.Saglabājiet datus Excel failā `price_tracker.xlsx`, kur būs norādīta informācija par izpildes laiku, veikalu un cenu.

