.PHONY: all
all: floorplan-overview.png floorplan-large.png

## Remove colons in 'qs:layer' tags, remove carriage returns...
## then get block reference names from comments and add them as
## class declarations.  Also, remove any style specs in the svg..
floorplan-clean.svg: floorplan.svg
	sed -e's/qs:layer/qslayer/g' -e's/\r//' $< | \
	sed -e'/<!-- Block Reference: /{n;d;}' | \
	sed -e's/<!-- Block Reference: \([^ ]*\).*$$/&\n\t<g class="\1">/g' | \
	sed -e's/style="[^"]*"//g' > $@

floorplan-overview.svg: floorplan-clean.svg
	sed -e'4i <style> @import url(floorplan-overview.css); </style>' $< | \
	sed -e'3 c\<svg width="1024px" viewBox="-648.0049 -534.0049 1293.0098 1033.0098" version="1.1" xmlns="http://www.w3.org/2000/svg" style="stroke-linecap:round;stroke-linejoin:round;fill:none" xmlns:qs="http://qcad.org/namespaces/svg">' > $@

floorplan-large.svg: floorplan-clean.svg
	sed -e'4i <style> @import url(floorplan-large.css); </style>' $< | \
	sed -e'3 c\<svg width="2400px" viewBox="-848.0049 -534.0049 1493.0098 1033.0098" version="1.1" xmlns="http://www.w3.org/2000/svg" style="stroke-linecap:round;stroke-linejoin:round;fill:none" xmlns:qs="http://qcad.org/namespaces/svg">' > $@

## Render png's using some type of browser..
BROWSER=/cygdrive/c/Program\ Files/Mozilla\ Firefox/firefox.exe
BROWSER_OPTIONS=--new-instance --screenshot

%.png: %.svg
	$(BROWSER) $(BROWSER_OPTIONS) \
	"$(subst /,\,C:/cygwin64$(PWD)/$@)" "file:///C:/cygwin64$(PWD)/$<"

clean:
	rm *.png floorplan-overview.svg floorplan-large.svg floorplan-clean.svg
