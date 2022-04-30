all: build/v500.pdf

# hier Python-Skripte:
build/orange.pdf: plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotA.py

build/gruen.pdf:plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotA.py

build/blau.pdf:plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotA.py

build/violett.pdf:plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotA.py

build/rot.pdf:plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotA.py

build/gegenspannung.pdf:plotA.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotA.py


build/aufgb.pdf: plotB.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plotB.py

# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/v500.pdf: build/orange.pdf
build/v500.pdf: build/gruen.pdf 
build/v500.pdf: build/blau.pdf
build/v500.pdf: build/violett.pdf
build/v500.pdf: build/rot.pdf
build/v500.pdf: build/gegenspannung.pdf
build/v500.pdf: build/aufgb.pdf

build/v500.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v500.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
