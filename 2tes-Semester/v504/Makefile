all: build/v504.pdf

# hier Python-Skripte:
build/plot1.pdf build/plot2.pdf build/plot3.pdf build/plot4.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/v504.pdf: build/plot1.pdf build/plot2.pdf build/plot3.pdf build/plot4.pdf

build/v504.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	v504.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
