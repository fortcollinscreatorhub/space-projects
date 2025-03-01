#!/usr/bin/env python3

import os
import subprocess
import svgwrite

color_black = '#000000'
color_tool1 = '#f36926'
inch = 25.4

def path_abs(d, parent, coords, **kwargs):
    p = d.path(d='M', **kwargs)
    p.push(coords[0])
    p.push('L')
    p.push(coords[1:])
    p.push('Z')
    parent.add(p)

def line_abs(d, parent, x, y, w, h, **kwargs):
    coords = [
        (x, y),
        (w, h)
    ]
    if 'stroke' not in kwargs:
        kwargs['stroke'] = color_black
    path_abs(d, parent, coords,
        stroke_width='0.1mm', fill='none', **kwargs,
        style='vector-effect:non-scaling-stroke;-inkscape-stroke:hairline;stroke-width:0.26458333;stroke-dasharray:none'
    )

def gen_ruler(filename, w_mm, h_mm):
    d = svgwrite.Drawing(filename, profile='full', size=('%dmm' % w_mm, '%dmm' % h_mm))
    d.viewbox(0, 0, w_mm, h_mm)

    offset = 1 * inch
    line_start = offset + 2
    line_end_long = offset - 10
    line_end_mid = offset - 7.5
    line_end_short = offset - 5

    def line_end_of(d):
        if d % 10 == 0:
            return line_end_long
        if d % 5 == 0:
            return line_end_mid
        return line_end_short

    g_corner = d.g()
    d.add(g_corner)
    line_abs(d, g_corner, w_mm - (0), 0, w_mm - (10), 0,  stroke=color_tool1)
    line_abs(d, g_corner, w_mm - (0), 0, w_mm - (0),  10, stroke=color_tool1)

    g_ruler_x = d.g()
    d.add(g_ruler_x)
    for x in range(0, int(w_mm - offset)):
        line_end = line_end_of(x)
        line_abs(d, g_ruler_x, w_mm - (offset + x), line_start, w_mm - (offset + x), line_end)

    g_ruler_y = d.g()
    d.add(g_ruler_y)
    for y in range(0, int(h_mm - offset)):
        line_end = line_end_of(y)
        line_abs(d, g_ruler_y, w_mm - (line_start), offset + y, w_mm - (line_end), offset + y)

    d.save()

if __name__ == '__main__':
    w_mm = int(48 * inch);
    h_mm = int(24 * inch);
    gen_ruler('ruler-48x24.svg', w_mm, h_mm)
