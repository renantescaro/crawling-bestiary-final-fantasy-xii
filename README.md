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
```
