# MAE 281A Lectures

| Service | Status |
| ------- | ------ |
| Linters | [![Travis-CI](https://api.travis-ci.org/tdenewiler/mae281a-lectures.svg?branch=master)](https://travis-ci.org/tdenewiler/mae281a-lectures/branches) |

This repository contains lecture notes completed for [MAE 281A](http://flyingv.ucsd.edu/krstic/teaching/281a/281a.html)
at UC San Diego during Fall quarter 2009 and taught by Prof Krstic.

You can compile using

```
pdflatex mae281a_lectures.tex
bibtex mae281a_lectures.aux
pdflatex mae281a_lectures.tex
pdflatex mae281a_lectures.tex
```

After running those commands initially, further changes can be compiled just running a single `pdflatex` command.
