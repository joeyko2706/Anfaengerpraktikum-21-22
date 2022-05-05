# Anfaengerpraktikum-20-21
Protokolle und Dateien aus dem Anfängerpraktikum aus dem Winter- und Sommersemester 2021/2022
---

## Makefile nutzen

Wenn mehrere Plots oder andere Grafiken von einer Python Datei erstellt werden, dann muss das dementsprechend in der Makefile vermerkt werden, Beispiel:

build/orange.pdf build/gruen.pdf build/blau.pdf: plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py
  
