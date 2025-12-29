# Datu apstrādes skripti

Šajā mapē atrodas Python skripti latviešu vārdadienu datu lejupielādei un apstrādei.

## Prasības

```bash
pip install -r requirements.txt
```

## Izmantošana

### 1. Lejupielādēt datus

No projekta saknes direktorijas:

```bash
python3 scripts/download_data.py
```

Tas lejupielādēs:
- `data/name_days.csv` - paplašinātais kalendārs
- `data/traditional_name_days.csv` - tradicionālais kalendārs  
- `data/gender_data.csv` - dzimuma dati

### 2. Apstrādāt datus

No projekta saknes direktorijas:

```bash
python3 scripts/process_name_days.py
```

Tas izveidos `docs/name_days_processed.json` ar visiem apstrādātajiem datiem.

## Failu struktūra

- `download_data.py` - Lejupielādē CSV failus no Latvijas valdības datu portāla
- `process_name_days.py` - Apstrādā CSV failus un izveido JSON ar vārdiem, dzimumiem, skaitiem, kalendāra tipiem un popularitātes datiem
- `requirements.txt` - Python atkarības

