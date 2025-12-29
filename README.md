# Latviešu vārdadienu projekts

Projekts latviešu vārdadienu datu apstrādei un interaktīvai vērtēšanas lietotnei.

## Struktūra

```
.
├── scripts/          # Python skripti datu apstrādei
├── data/             # CSV datu faili (lejupielādēti ar scripts/download_data.py)
├── docs/             # Tīmekļa lietotne (GitHub Pages)
└── README.md         # Šis fails
```

## Sākšana

### 1. Datu lejupielāde

Lejupielādējiet nepieciešamos CSV failus (no projekta saknes direktorijas):

```bash
python3 scripts/download_data.py
```

Tas lejupielādēs:
- `data/name_days.csv` - paplašinātais kalendārs
- `data/traditional_name_days.csv` - tradicionālais kalendārs
- `data/gender_data.csv` - dzimuma dati

**Piezīme**: Popularitātes datu faili (`0_0_1920_2020_all_data.csv` un `1_0_1920_2020_all_data.csv`) nav iekļauti lejupielādē, jo to URL nav pieejams. Ja jums ir šie faili, novietojiet tos `data/` mapē.

### 2. Datu apstrāde

Apstrādājiet datus un izveidojiet JSON failu (no projekta saknes direktorijas):

```bash
python3 scripts/process_name_days.py
```

Tas izveidos `docs/name_days_processed.json` ar visiem vārdiem, dzimumiem, skaitiem, kalendāra tipiem un popularitātes datiem.

### 3. Tīmekļa lietotne

Atveriet `docs/name_rating_app.html` pārlūkprogrammā vai izmantojiet GitHub Pages.

## GitHub Pages iestatīšana

### Automātiskā izvietošana (ieteicams)

Projekts ietver GitHub Actions darbplūsmu, kas automātiski izvieto lietotni GitHub Pages, kad tiek veiktas izmaiņas `main` branch.

1. Dodieties uz repository Settings
2. Skatiet sadaļu "Pages"
3. Izvēlieties "Source": "GitHub Actions"
4. Saglabājiet

### Manuālā izvietošana

1. Dodieties uz repository Settings
2. Skatiet sadaļu "Pages"
3. Izvēlieties "Source": "Deploy from a branch"
4. Izvēlieties branch: `main` (vai `master`)
5. Izvēlieties folder: `/docs`
6. Saglabājiet

Lietotne būs pieejama: `https://[username].github.io/[repository-name]/name_rating_app.html`

## Atkarības

- Python 3.6+
- `requests` (instalē ar `pip install -r scripts/requirements.txt`)

## Detalizēta informācija

- Skatiet `docs/README.md` par tīmekļa lietotnes lietošanu
- Skatiet `scripts/README.md` par datu apstrādes procesu
