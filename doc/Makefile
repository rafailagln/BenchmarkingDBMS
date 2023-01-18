.SUFFIXES:.eps .pdf .gz .data .dot

main.pdf: main.tex 
	pdflatex -shell-escape main
	bibtex main
	pdflatex -shell-escape main
	pdflatex -shell-escape main

clean:
	rm -f main.aux main.pdf main.blg main.tdo main.thm main-blx.bib main.bbl main.dvi main.toc main.run.xml  *.log *.out *pyg