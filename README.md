## Crwaling Bestiary Final Fantasy XII
https://finalfantasy.fandom.com/wiki/Bestiary_(Final_Fantasy_XII)

<br>

## Instalação das Dependências

### No Windows
Instalar todas as dependências
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
<br>

### No Linux
Instalar todas as dependências
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


Executar
```bash
scrapy runspider listing.py -o listing.json
scrapy runspider items.py -o items.json
```

## items.json
```
[{
    "name": "Cactoid ",
    "image": "https://static.wikia.nocookie.net/finalfantasy/images/e/e9/XIICactoid.jpg/revision/latest?cb=20080510235535",
    "url": "https://finalfantasy.fandom.com/wiki/Cactoid_(Final_Fantasy_XII)",
    "location": "Dalmasca Estersand (Yardang Labyrinth, Banks of the Nebra); Dalmasca Westersand (The Yoma, Galtea Downs); Trial Mode Stage 3 (Zodiac versions)",
    "type": "Normal enemy",
    "data": "StatsAI"
}]
```

<br>

## listing.json

```
[{
    "name": "Nightwalker",
    "link": "https://finalfantasy.fandom.com/wiki/Nightwalker_(Final_Fantasy_XII)",
    "sups": [
        {
            "link_0": "https://finalfantasy.fandom.com/wiki/Reaper_Claw"
        }, {
            "link_1": "https://finalfantasy.fandom.com/wiki/Reaper_Mage"
        }
    ]
}]
```
