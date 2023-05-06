import drawsvg as draw

input_str = "(1, 1, 1, 2), (1, 2, 2, 2), (1, 4, 1, 5), (1, 5, 1, 6), (1, 6, 2, 6), (2, 1, 1, 1), (2, 2, 2, 3), (2, 3, 3, 3), (2, 4, 1, 4), (2, 5, 3, 5), (2, 6, 2, 5), (3, 1, 2, 1), (3, 2, 3, 1), (3, 3, 3, 4), (3, 4, 2, 4), (3, 5, 4, 5), (4, 1, 4, 2), (4, 2, 3, 2), (4, 3, 5, 3), (4, 4, 4, 3), (4, 5, 4, 6), (4, 6, 5, 6), (5, 1, 4, 1), (5, 2, 6, 2), (5, 3, 5, 2), (5, 4, 4, 4), (5, 5, 5, 4), (5, 6, 6, 6), (6, 1, 5, 1), (6, 2, 6, 1), (6, 5, 5, 5), (6, 6, 6, 5)"

coords_str = input_str.replace('(', '').replace(')', '')
coords_list = coords_str.split(', ')

d = draw.Drawing(600, 600, origin='top-left')

arrow = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=5, orient='auto')
arrow.append(draw.Lines(-0.4, -0.5, -0.1, 0.3, 0.5, 0, fill='black', close=True))

for i in range(0, len(coords_list), 4):
    x1, y1, x2, y2 = map(int, coords_list[i:i+4])
    d.append(draw.Line(x1*10, y1*10, x2*10, y2*10, stroke_width=2, stroke='black', fill='none', marker_end=arrow))

d.set_pixel_scale(2)

d.save_svg('arrows2.svg')





