# Latviešu vārdadienu vērtēšanas lietotne

Interaktīva tīmekļa lietotne latviešu vārdu vērtēšanai un izpētei.

## Funkcijas

1. **Filtrēšana**:
   - Filtrēšana pēc kalendāra (Tradicionālais vai Paplašinātais)
   - Filtrēšana pēc dzimuma (Visi, Vīrietis, Sieviete, Nedefinēts)
   - Filtrēšana pēc datuma diapazona (no/līdz datums DD.MM formātā)
   - Filtrus var saglabāt un atjaunot pēc lapas pārlādēšanas

2. **Vērtēšanas sistēma**:
   - 5 zvaigžņu vērtēšanas sistēma katram vārdam:
     - 1 zvaigzne = Mazāk patīk
     - 2 zvaigznes = Nedaudz patīk
     - 3 zvaigznes = Neitrāli/Patīk
     - 4 zvaigznes = Ļoti patīk
     - 5 zvaigznes = Ļoti ļoti patīk
   - Vērtētie vārdi tiek organizēti atsevišķās cilnēs
   - Nevērtētie vārdi tiek rādīti sākumlapā

3. **Automātiskā saglabāšana**:
   - Vērtējumi tiek automātiski saglabāti pārlūkprogrammas localStorage pēc katras mijiedarbības
   - Dati tiek saglabāti starp sesijām
   - Filtrus un aktīvo cilni arī saglabā

4. **Eksportēšana un importēšana**:
   - Poga "Saglabāt" - eksportē vērtējumus kā JSON failu
   - Poga "Ielādēt" - importē vērtējumus no JSON faila
   - Ērti koplietot vai dublēt vērtējumus

5. **Statistika**:
   - Kopējais vārdu skaits
   - Filtrēto vārdu skaits
   - Vērtēto vārdu skaits
   - Vārdu skaits katrā vērtējuma līmenī

6. **Popularitātes grafiks**:
   - Vārdiem ar pieejamiem datiem par popularitāti tiek rādīts grafiks
   - Grafiks parādās, kad uzvedat peles kursoru uz vārda kartītes
   - Grafiks rāda vārda popularitāti no 1920. līdz 2020. gadam
   - Kartītē ir indikators (📊), kas norāda, ka vārdam ir pieejami popularitātes dati

7. **Organizācija**:
   - Vārdi tiek grupēti pēc datuma
   - Datumi tiek sakārtoti hronoloģiski
   - Kad visi vārdi noteiktā datumā ir novērtēti, datums tiek noņemts no "Nevērtētie vārdi" cilnes

8. **Responsīvs dizains**:
   - Lietotne aizpilda visu ekrānu
   - Pielāgojas dažādiem ekrāna izmēriem
   - Optimizēts darbam uz datora, planšetes un mobilā tālruņa

## Kā izmantot

1. **Atvērt lietotni**:
   - Vienkārši atveriet `name_rating_app.html` pārlūkprogrammā
   - Pārliecinieties, ka `name_days_processed.json` atrodas tajā pašā mapē

2. **Filtrēt vārdus**:
   - Izmantojiet pogu "Paplašinātais kalendārs", lai rādītu arī paplašinātā kalendāra vārdus (pēc noklusējuma rāda tikai tradicionālos)
   - Izmantojiet dzimuma izvēlni, lai filtrētu pēc dzimuma
   - Ievadiet datuma diapazonu DD.MM formātā (piemēram, "01.01" līdz "31.12")
   - Datuma diapazons var aptvert gadu (piemēram, "15.06" līdz "15.02")

3. **Vērtēt vārdus**:
   - Noklikšķiniet uz zvaigznes (1-5), lai novērtētu katru vārdu
   - 1 zvaigzne = mazāk patīk, 5 zvaigznes = ļoti patīk
   - Vērtējumi tiek saglabāti automātiski
   - Novērtētie vārdi tiek izcelti zaļā krāsā
   - Novērtētie vārdi pazūd no "Nevērtētie vārdi" cilnes un parādās atbilstošajā vērtējuma cilnē

4. **Skatīt vērtējumus**:
   - Izmantojiet cilnes, lai skatītu vārdus pēc vērtējuma līmeņa
   - "Nevērtētie vārdi" - rāda tikai vārdus, kas vēl nav novērtēti
   - Cilnes ar zvaigznēm (★ līdz ★★★★★) - rāda vārdus ar atbilstošu vērtējumu

5. **Saglabāt un ielādēt vērtējumus**:
   - Noklikšķiniet uz pogas "Saglabāt", lai eksportētu vērtējumus kā JSON failu
   - Noklikšķiniet uz pogas "Ielādēt", lai importētu vērtējumus no JSON faila
   - Ielādētie vērtējumi tiek apvienoti ar esošajiem

6. **Notīrīt datus**:
   - Noklikšķiniet uz pogas "Notīrīt visu" (augšējā labajā stūrī)
   - Apstipriniet darbību dialoga logā
   - Tas dzēsīs visus vērtējumus un atiestatīs filtrus

7. **Skatīt popularitātes grafiku**:
   - Uzvediet peles kursoru uz vārda kartītes ar indikatoru 📊
   - Grafiks parādīs vārda popularitāti laika gaitā
   - Grafiks tiks novietots pa labi no kartītes, ja ir vietas, pretējā gadījumā pa kreisi

## Tehniskās detaļas

- **Glabāšana**: Vērtējumi tiek saglabāti pārlūkprogrammas localStorage
- **Datu formāts**: Izmanto `name_days_processed.json` kā datu avotu
- **Nav nepieciešams serveris**: Darbojas pilnībā bezsaistē pārlūkprogrammā
- **Valoda**: Visi teksti ir latviešu valodā

## Pārlūkprogrammu saderība

Darbojas visās mūsdienīgās pārlūkprogrammās:
- Chrome/Edge
- Firefox
- Safari
- Opera

## Piezīmes

- Lietotnei nepieciešams `name_days_processed.json` tajā pašā mapē
- Ja redzat CORS kļūdas, var būt nepieciešams palaist lokālu tīmekļa serveri:
  ```bash
  # Python 3
  python -m http.server 8000
  
  # Pēc tam atveriet: http://localhost:8000/name_rating_app.html
  ```

## Datu struktūra

Lietotne sagaida JSON failu ar šādu struktūru:
```json
[
  {
    "name": "Vārds",
    "date": "DD.MM",
    "gender": "Vīrietis|Sieviete|Nedefinēts",
    "count": 0,
    "kalendārs": "tradicionālais|paplašinātais",
    "popularity": {
      "1920": 0,
      "1925": 0,
      ...
    }
  }
]
```

## Saglabāšanas formāts

Vērtējumi tiek saglabāti kā JSON objekts, kur:
- Atslēga: `"Vārds_Datums"` (piemēram, `"Jānis_01.01"`)
- Vērtība: vērtējums no 1 līdz 5 (0 nozīmē nav novērtēts)
