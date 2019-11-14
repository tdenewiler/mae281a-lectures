# MAE 281A Lectures

| Service | Status |
| ------- | ------ |
| Linters | [![Travis-CI](https://api.travis-ci.org/tdenewiler/mae281a-lectures.svg?branch=master)](https://travis-ci.org/tdenewiler/mae281a-lectures/branches) |

This repository contains lecture notes completed for [MAE 281A](http://flyingv.ucsd.edu/krstic/teaching/281a/281a.html)
at UC San Diego during Fall quarter 2009 and taught by Prof Krstic.

You can compile using

```shell
pdflatex mae281a_lectures.tex
bibtex mae281a_lectures.aux
pdflatex mae281a_lectures.tex
pdflatex mae281a_lectures.tex
```

After running those commands initially, further changes can be compiled just running a single `pdflatex` command.

## Static Analysis

[Statick](https://github.com/sscpac/statick) is used to ensure consistent style and that certain classes of errors
do not exist in this repository.
To run Statick locally, do the following:

```shell
apt install chktex lacheck
pip install -r requirements.txt
mkdir statick_output
statick . statick_output --user-paths statick_config --profile tex-profile.yaml --config tex-config.yaml
```
