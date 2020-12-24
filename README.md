# 163Lu Symmetry Partner Bands within Triaxial Rotor Model and the Wobbling Structure

A short article to be considered as a _Rapid Communication*_ for PRC (Main author).

ℹ Last paper to be submitted under the current PhD. program @ UNIBUC (by the end of Summer '21).

## Generating draft in preprint mode

The python script `copy-file.py` is creating a copy of the original `.tex` file and it changes the template mode as a `preprint`. The script compiles (using `subprocess` package) both `.tex` files with `pdflatex` (which is locally installed on the machine via the [MacTex](https://www.tug.org/mactex/mactex-download.html) package). After compilation, the script also takes care of cleaning up the remaining files (i.e. `.aux`, `.log` ). 

The script requires permission for execution within the shell.