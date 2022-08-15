# Anfaengerpraktikum-20-21
Protokolle und Dateien aus dem Anfängerpraktikum aus dem Winter- und Sommersemester 2021/2022
---
## Git nutzen
https://guides.github.com/introduction/flow/.

1. Neuen Branch erstellen: `git branch <name>`.
2. Auf den Branch wechseln: `git checkout <name>`.
3. Änderungen vornehmen und commiten.
4. Den Branch pushen: `git push -u <name>`.
5. Pull Request oauf github erstellen.

- Falls eine zu große Datei hochgeladen wurde und somit ein Fehler ausgegeben wird, oder wenn einfach der letzte 
    lokale commit gelöscht werden soll: `# git reset --soft HEAD^`

---

## Makefile nutzen

Wenn mehrere Plots oder andere Grafiken von einer Python Datei erstellt werden, dann muss das dementsprechend in der Makefile vermerkt werden, Beispiel:

build/orange.pdf build/gruen.pdf build/blau.pdf: plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
  
--- 

### Klausur

Ich habe mit dem folgende Notion Dokument gelernt. Ich bin die ganzen Protokolle durchgegangen und habe dabei das wichtigste rausgeschrieben.

https://joelkoch.notion.site/Praktikum-77b5f862999f42f3859922f2ed441d72