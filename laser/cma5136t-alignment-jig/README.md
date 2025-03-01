= CMA5136T alignment jig & ruler

== Manufacturing a jig

* Place 48" w x 24" h 1/4" thick wood sheet into the large LASER without any
jig present. Push the sheet into the very far back/right corner.

* Load and run `cma5136t-alignment-jig-cut-jig.lbrn2`. This will leave you with
a large L-shaped piece that is the jig itself, and a narrow L-shaped strip that
will be used during the process of engraving the ruler onto the jig.

* Remove the waste piece from the LASER (large rectangle).

* Swap the jig and thin strip, so that 1" strip is in the corner of the LASER,
and the jig is pushed into the corner of the strip.

* Load and run `cma5136t-alignment-jig-engrave-ruler.lbrn2`.

* Load a previously made jig into the corner of the LASER cutter, then place
the new jig at the origin.

* Load and run `cma5136t-alignment-jig-engrave-main-labels.lbrn2`.

== Updating the ruler image

* Execute `gen-ruler.py`.

* Open `cma5136t-alignment-jig-engrave-ruler.lbrn2` in LightBurn.

* Delete all existing content.

* Import `ruler-48x24.svg`.

* Set the position of the imported objects to x=0, y=0.
