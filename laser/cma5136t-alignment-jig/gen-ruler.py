#!/usr/bin/env python3

import os
import subprocess
import svgwrite

color_black = '#000000'
color_red = '#ff0000'
color_green = '#00ff00'
inch = 25.4
font_size = 5
y_font_offset = 1

def path_abs(d, parent, coords, **kwargs):
    path = parent.add(d.path(d='M', **kwargs))
    path.push(coords[0])
    path.push('L')
    path.push(coords[1:])
    path.push('Z')

def line_abs(d, parent, x, y, w, h, **kwargs):
    coords = [
        (x, y),
        (w, h)
    ]
    if 'stroke' not in kwargs:
        kwargs['stroke'] = color_black
    path_abs(d, parent, coords, stroke_width='0.01mm', fill='none', **kwargs)

def text_abs(d, parent, x, y, s, **kwargs):
    text = parent.add(d.text(s, x=[x], y=[y], font_size=str(font_size) + 'px', **kwargs))

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

    g_corner = d.add(d.g())
    line_abs(d, g_corner, w_mm - (0), 0, w_mm - (10), 0,  stroke=color_green)
    line_abs(d, g_corner, w_mm - (0), 0, w_mm - (0),  10, stroke=color_green)

    g_ruler_lines_x = d.add(d.g())
    g_ruler_numbers_x = d.add(d.g(fill=color_red))
    for x in range(0, int(w_mm - offset)):
        line_end = line_end_of(x)
        xp = w_mm - (offset + x)
        yps = line_start
        ype = line_end
        line_abs(d, g_ruler_lines_x, xp, yps, xp, ype)
        if x % 10 == 0:
            fx = xp
            fy = line_end + (font_size / 2) - y_font_offset
            tf = f'rotate(-90, {fx}, {line_end})'
            text_abs(d, g_ruler_numbers_x, fx, fy, str(x), transform=tf)

    g_ruler_lines_y = d.add(d.g())
    g_ruler_numbers_y = d.add(d.g(fill=color_red))
    for y in range(0, int(h_mm - offset)):
        line_end = line_end_of(y)
        xps = w_mm - (line_start)
        xpe = w_mm - (line_end)
        yp = offset + y
        line_abs(d, g_ruler_lines_y, xps, yp, xpe, yp)
        if y % 10 == 0:
            fx = xpe
            fy = yp + (font_size / 2) - y_font_offset
            text_abs(d, g_ruler_numbers_y, fx, fy, str(y))

    d.save()

if __name__ == '__main__':
    w_mm = int(48 * inch);
    h_mm = int(24 * inch);
    gen_ruler('ruler-48x24.svg', w_mm, h_mm)
