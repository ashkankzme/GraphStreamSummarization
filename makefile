SRC= exp1-a.py
AUXILIARY= makefile
ALL= $(SRC) $(AUXILIARY)

demo:
   python3.6 exp1-a.py

all.zip: $(ALL)
zip all.zip $(ALL)

clean:
\rm data/exp1-a*