all: build/vUS3.pdf

# hier Python-Skripte:
build/plota.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/plotb.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/plotc.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/plot2.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py

build/plot3.pdf: plot.py ../matplotlibrc ../header-matplotlib.tex | build
	TEXINPUTS=$$(pwd)/..: MATPLOTLIBRC=../matplotlibrc python plot.py



# hier weitere Abhängigkeiten für build/vXXX.pdf deklarieren:
build/vUS3.pdf: build/plota.pdf
build/vUS3.pdf: build/plotb.pdf
build/vUS3.pdf: build/plotc.pdf
build/vUS3.pdf: build/plot2.pdf
build/vUS3.pdf: build/plot3.pdf

build/vUS3.pdf: FORCE | build
	# to find header and bib files in the main directory
	TEXINPUTS=..: \
	BIBINPUTS=..: \
	max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	vUS3.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
