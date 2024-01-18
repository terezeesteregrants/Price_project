# Cenu salīdzināšanas uzdevums

### Uzdevuma apraksts

Uzdevums ir izveidot programmu, kas salīdzina Apple iPad 10.9" Wi-Fi 64GB - Blue 10th gen (2022) cenas tet.lv, euronics.lv un rdveikals.lv vietnēs, attiecīgi izsūta uz savu e-pastu par izdevīgāko piedāvājumu un saglabā datus par cenām excel failā. 
Šeit ir, norādījumi kā jāizstrādā uzdevums:

1. Izveido e-pasta nosūtīšanu ('send_email') funkciju. Norāda savu izvēlētu tēmu, ziņojumu, kas paziņotu par zemāko cenu norādītajos internetveikalos. Šim izmanto Gmail SMTP serveri, parole jāiegūst no sava google konta.

2. Izgūst datus par cenu no attiecīgi norādītajām mājaslapām 

3. Salīdzina cenas ar 'check_price' funkciju.

4. Paziņo norādītajam e-pasta adresātam par zemāko pieejamo cenu produktam attiecīgajā mājaslapā. 

5. Piefiksē datus un cenu izmaiņas (ja tādas ir), excel datnē, izveidojot failu 'price_tracker.xslx', norādt vietnes nosaukumu, cenu un laiku, kurā tas tiek apskatīts.

Mērķis ir uzzināt, kurā vietnē ir visizdevīgākais piedāvājums izvēlētajam produktam.

**Programmu jāiesniedz kā result.py failu.**

### Izmantotās bibliotēkas

1. 'pandas' 
Izmantots, lai analizētu un saglabātu datus. Šajā uzdevumā tiek izmantots, lai apstrādātu datus, izveidotu DataFrame, saglabājot to Excel failā.

2. 'selenium'
Izmantots, lai iegūtu mājaslapu datus izvēlētajiem internetveikaliem. Galvenokārt, bibliotēka ļauj automatizēt pārlūku darbības, piemēram, mūsu uzdevumā, lai iegūt datus no tīmekļa ar 'find_element' funkciju, kā arī izpilda 'time_sleep' funkciju, kas nodrošina ielādes gaidīšanu.

3. 'smtplib'
Nodrošina e-pastu nosūtīšanas funkciju, izmantojot Gmail SMTP serveri.


### Programmas izmantošanas metodes

1. Pārliecināties vai ir instalēt nepieciešamās bibliotēkas, ja nav, tad ar funkciju var instalēt 'pip install' + (bibliotēkas nosaukums)

2. Izveido savu gmail e-pastu (ja tāda nav), iegūt no Google App Passwords kodēta forma parolei
