# Firebase iestatīšana - Mākoņa sinhronizācija

Šis ceļvedis palīdzēs jums iestatīt Firebase autentifikāciju un datu sinhronizāciju, lai jūsu vērtējumi tiktu saglabāti mākonī un būtu pieejami no jebkura ierīces vai pārlūkprogrammas.

## ✅ GitHub Pages saderība

**Jā, Firebase darbojas ar GitHub Pages!** Firebase ir pilnībā klienta puses (client-side) risinājums, kas nozīmē:
- ✅ Nav nepieciešams serveris vai backend
- ✅ Darbojas ar statiskiem failiem (HTML, CSS, JavaScript)
- ✅ Perfekti saderīgs ar GitHub Pages
- ✅ Nav nepieciešamas papildu konfigurācijas GitHub pusē

Vienīgais, kas jādara, ir pievienot jūsu GitHub Pages domēnu Firebase autentifikācijas autorizēto domēnu sarakstā (skatīt 7. soli).

## Kāpēc Firebase?

- **Mākoņa sinhronizācija**: Jūsu dati tiek saglabāti mākonī un ir pieejami no jebkuras ierīces
- **Bezmaksas**: Firebase piedāvā bezmaksas plānu ar pietiekami daudz resursiem mazām lietotnēm
- **Vienkārša iestatīšana**: Tikai daži soļi, lai sāktu darbu

## Soļi

### 1. Izveidot Firebase projektu

1. Dodieties uz [Firebase Console](https://console.firebase.google.com/)
2. Noklikšķiniet uz "Add project" (Pievienot projektu)
3. Ievadiet projekta nosaukumu (piemēram, "latvian-names")
4. Izvēlieties vai ieslēgt Google Analytics (nav obligāti)
5. Noklikšķiniet "Create project" (Izveidot projektu)

### 2. Iespējot Authentication

1. Firebase Console kreisajā izvēlnē izvēlieties "Authentication"
2. Noklikšķiniet "Get started" (Sākt)
3. Dodieties uz cilni "Sign-in method"
4. Noklikšķiniet uz "Email/Password"
5. Ieslēdziet "Enable" un saglabājiet

### 3. Izveidot Firestore datu bāzi

1. Firebase Console kreisajā izvēlnē izvēlieties "Firestore Database"
2. Noklikšķiniet "Create database"
3. Izvēlieties "Start in test mode" (Sākt testa režīmā)
4. Izvēlieties reģionu (piemēram, "europe-west1" vai tuvāko)
5. Noklikšķiniet "Enable"

**Svarīgi**: Pēc tam iestatiet drošības noteikumus (skatīt zemāk).

### 4. Iegūt Firebase konfigurāciju

1. Firebase Console kreisajā izvēlnē izvēlieties "Project settings" (⚙️ ikona)
2. Ritiniet uz leju līdz sadaļai "Your apps"
3. Noklikšķiniet uz ikonu "</>" (Web)
4. Ievadiet app nosaukumu (piemēram, "Latvian Names App")
5. Noklikšķiniet "Register app"
6. Kopējiet konfigurācijas objektu

### 5. Pievienot konfigurāciju lietotnei

1. Atveriet `docs/name_rating_app.html`
2. Atrodiet rindu ar `const firebaseConfig = {`
3. Aizstājiet visas `YOUR_*` vērtības ar jūsu Firebase konfigurācijas vērtībām:

```javascript
const firebaseConfig = {
    apiKey: "AIzaSy...",  // Jūsu API atslēga
    authDomain: "your-project.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project.appspot.com",
    messagingSenderId: "123456789",
    appId: "1:123456789:web:abc123"
};
```

### 6. Iestatīt Firestore drošības noteikumus

1. Firebase Console → Firestore Database → "Rules" cilne
2. Aizstājiet esošos noteikumus ar šiem:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users can only read/write their own ratings
    match /userRatings/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

3. Noklikšķiniet "Publish" (Publicēt)

### 7. Pievienot autentifikācijas domēnu (GitHub Pages) ⚠️ SVARĪGI

**Firebase darbojas ar GitHub Pages!** Firebase ir pilnībā klienta puses risinājums, tāpēc tas darbojas ar jebkuru statisko hosting pakalpojumu, ieskaitot GitHub Pages.

Tomēr jums **obligāti** jāpievieno jūsu GitHub Pages domēns Firebase autentifikācijai:

1. Firebase Console → Authentication → Settings
2. Ritiniet uz leju līdz "Authorized domains"
3. Noklikšķiniet "Add domain"
4. Ievadiet jūsu GitHub Pages domēnu:
   - Ja izmantojat `username.github.io/repository-name`: `username.github.io`
   - Ja izmantojat custom domēnu: ievadiet to domēnu
5. Saglabājiet

**Piezīme**: Firebase pēc noklusējuma ietver `localhost`, tāpēc lokālā testēšana darbojas bez papildu iestatījumiem.

## Pārbaude

1. Atveriet lietotni pārlūkprogrammā
2. Jums vajadzētu redzēt pieteikšanās logu
3. Noklikšķiniet uz "Reģistrēties" un izveidojiet kontu
4. Pēc reģistrācijas jūs būsiet ielogoti
5. Novērtējiet dažus vārdus
6. Atveriet lietotni citā pārlūkprogrammā vai ierīcē
7. Ielogojieties ar to pašu kontu
8. Jūsu vērtējumi vajadzētu būt redzami!

## Funkcijas

- **Automatiskā sinhronizācija**: Katru reizi, kad novērtējat vārdu, dati tiek saglabāti gan localStorage, gan Firebase
- **Mākoņa rezerves kopija**: Jūsu dati ir droši saglabāti mākonī
- **Pieejamība no jebkuras ierīces**: Ielogojieties no jebkuras ierīces, lai redzētu savus vērtējumus
- **LocalStorage kā rezerves kopija**: Ja Firebase nav pieejams, dati tiek saglabāti localStorage

## Izmaksas

Firebase bezmaksas plāns (Spark) ietver:
- 50,000 lasīšanas operācijas dienā
- 20,000 rakstīšanas operācijas dienā
- 20,000 dzēšanas operācijas dienā
- 1 GB glabāšanas vietas

Mazām lietotnēm tas ir vairāk nekā pietiekami!

## Atbalsts

Ja rodas problēmas:
1. Pārbaudiet, vai Firebase konfigurācija ir pareiza
2. Pārbaudiet, vai Authentication ir ieslēgta
3. Pārbaudiet, vai Firestore drošības noteikumi ir pareizi iestatīti
4. Atveriet pārlūkprogrammas konsole (F12), lai redzētu kļūdu ziņojumus

## Bez Firebase

Ja nevēlaties izmantot Firebase, lietotne turpinās darboties ar localStorage. Vienkārši neaizstājiet Firebase konfigurāciju, un lietotne izmantos tikai localStorage (dati būs pieejami tikai tajā pašā pārlūkprogrammā).

