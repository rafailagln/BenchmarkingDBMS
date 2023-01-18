PAPER = main
TEX = $(wildcard *.tex)
BIB = bib.bib

.PHONY: all clean
.FORCE: 

$(PAPER).pdf: clean $(TEX) $(BIB) 
	pdflatex -shell-escape  $(PAPER)
	bibtex  $(PAPER)
	pdflatex -shell-escape  $(PAPER)
	pdflatex -shell-escape  $(PAPER)

clean:
	rm -f *.aux *.bbl *.blg *.log *.out $(PAPER).pdf *.fdb_latexmk *.tdo *.dvi *.toc *.run.xml *.fls *.thm *-blx.bib
