test: face.mdl myscript.mdl lex.py main.py matrix.py mdl.py display.py draw.py gmath.py yacc.py
	python main.py face.mdl
	python main.py myscript.mdl

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
