
:: A LaTeX toolchain : PDFLaTeX -> BibTeX -> MakeIndex (Glossary) -> MakeIndex (Acronyms) -> PDFLaTeX -> PDFLaTeX

@echo off
echo Building %1 ...
pdflatex -synctex=1 -interaction=batchmode %1.tex 
bibtex %1
makeindex -s %1.ist -t %1.glg -o %1.gls %1.glo
makeindex -s %1.ist -t %1.alg -o %1.acr %1.acn
pdflatex -synctex=1 -interaction=batchmode %1.tex
pdflatex -synctex=1 -interaction=batchmode %1.tex
echo Cleaning up ...
del %1.acn %1.acr %1.alg %1.aux %1.bbl %1.blg %1.glg %1.glo %1.gls %1.synctex.gz %1.ist %1.lof %1.log %1.lot %1.out %1.toc
echo Done.