# hfs_fit

**A python fitting program for atomic emission lines with hyperfine structure (HFS).**

Performs parameter optimization in the analysis of emission line hyperfine structure (HFS). The code uses a simulated annealing algorithm to optimize the magnetic dipole interaction constants, electric quadrupole interaction constants, Voigt profile widths and the center of gravity wavenumber for a given emission line profile. The fit can be changed visually with sliders for parameters, which is useful when the HFS constants are unknown.

<img src="fits/z3P2---a3D3 (spectrum.txt).png">

## Quickstart

* requires python 3.6 or higher
* run `pip install .` to install package
* run `example.py` in an interactive python environment to see an example

## Testing

To run the package tests, first install tox (`pip install tox`) then:

* `tox -e pytest` to run test suite in a virtual environment (may take a few mins)
* `tox -e pylint` to lint code

## Files and Explanations

```code
📦hfs_fit
 ┣ 📂data (holds )
 ┃ ┣ 📜fitLog.xlsx (parameters saved here when desired)
 ┃ ┣ 📜z3P2---a3D3 (spectrum.txt).png (example output plot)
 ┃ ┗ 📜spectrum.txt (UV sample of Co II spectrum with 4 Co II lines)
 ┣ 📂hfs_fit
 ┃ ┣ 📜interpolation.py (cubic spline interpolation in hfs_fit.py.)
 ┃ ┣ 📜relInt.py (calculate relative intensities of HFS components)
 ┃ ┣ 📜hfs_fit.py (main class)
 ┃ ┣ 📜LU.py (LU decomposition for interpolation.py)
 ┃ ┗ 📜__init__.py
 ┣ 📂tests (test suite)
 ┣ 📜README.md
 ┣ 📜example.py (demonstraints basic usage)
 ┣ 📜setup.cfg (package settings)
 ┣ 📜setup.py
 ┗ 📜tox.ini (test config)
```

## Useful Functions and Notes

* Can plot transition diagram with components using the LineFig() method in the hfs class. nInterp argument for this is the number of points to artificially add to make lines smooth, 1 for no interpolation (default). The spacing between texts may not be perfect, most of the time the level label will touch a level line, can change this by changing the location of the texts from lines 678-681.

* Can plot spectrum using the PlotSpec() method in the hfs class, put a wavenumber in the bracket and it will plot around that wavenumber.

* Use hjw() of hfs class to half all jumpwidths before Optimise(), this is convenient when performing the final optimisation of parameters, or if the initial guess is very good.

* Can always re-open the sliders plot with PlotGuess() method of the hfs class. If the sliders don't work, try closing and opening it up again (this happens sometimes in iPython).

* Can also add points for smoothing during fitting, to do this change the nInterp value in the WNRange() method of hfs and re-import hfs.

* HFS components are plotted by default, can turn this off using PlotGuess(components = False)

* The reset button of PlotGuess() doesn't seem to work in iPython.

* If the instrumental profile (Fourier transform spectroscopy only) is negligible, put icut at the maximum value.
