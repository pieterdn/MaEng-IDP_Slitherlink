import drawsvg as draw
import sys
output_str = sys.argv[1]
input_str = sys.argv[2]

coords_str = input_str.replace('(', '').replace(')', '')
coords_list = coords_str.split(', ')

d = draw.Drawing(600, 600, origin='top-left')

arrow = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=5, orient='auto')
arrow.append(draw.Lines(-0.4, -0.5, -0.1, 0.3, 0.5, 0, fill='black', close=True))

for i in range(0, len(coords_list), 4):
    x1, y1, x2, y2 = map(int, coords_list[i:i+4])
    d.append(draw.Line(x1*10, y1*10, x2*10, y2*10, stroke_width=2, stroke='black', fill='none', marker_end=arrow))

d.set_pixel_scale(2)

d.save_svg(output_str)





