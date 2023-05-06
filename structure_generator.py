import sys
def main():
    if(len(sys.argv) != 3):
        print("Please specify the 2 required arguments: <amount_of_columns> <amount_of_rows>")
        exit()

    amount_of_columns = int(sys.argv[1])
    amount_of_rows = int(sys.argv[2])
    output = f"\n//===========================\n// idp structure for a {amount_of_columns} x {amount_of_rows}\n//===========================\n\t"
    
    #     cell_column := {1, 2, 3}.
    output += "cell_column := {"
    for i in range(1,amount_of_columns+1):
        output += f"{i}, "
    output = output[:-2]
    output += "}.\n\t"

    #     cell_row := {1, 2, 3}.
    output += "cell_row := {"
    for i in range(1,amount_of_rows+1):
        output += f"{i}, "
    output = output[:-2]
    output += "}.\n\t"

    #     point_column := {1, 2, 3, 4}.
    output += "point_column := {"
    for i in range(1,amount_of_columns+2):
        output += f"{i}, "
    output = output[:-2]
    output += "}.\n\t"

    #     point_row := {1, 2, 3, 4}.
    output += "point_row := {"
    for i in range(1,amount_of_rows+2):
        output += f"{i}, "
    output = output[:-2]
    output += "}.\n\t"

    #     cell_value := {-1, 0, 1, 2, 3}.
    output += "cell_value := {-1, 0, 1, 2, 3}.\n\t"



    #     // cell relations, how one cell lies in relation to another
    output += "// cell relations, how one cell lies in relation to another\n\t"
    #     n_cell := {(1, 2, 1, 1), (1, 3, 1, 2), (2, 2, 2, 1), (2, 3, 2, 2), (3, 2, 3, 1), (3, 3, 3, 2)}.
    output += "n_cell := {"
    for x in range(1, amount_of_columns+1):
        for y in range(2, amount_of_rows+1):
            output += f"({x}, {y}, {x}, {y-1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     e_cell := {(1, 1, 2, 1), (1, 2, 2, 2), (1, 3, 2, 3), (2, 1, 3, 1), (2, 2, 3, 2), (2, 3, 3, 3)}.
    output += "e_cell := {"
    for x in range(1, amount_of_columns):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x+1}, {y}), "
    output = output[:-2]
    output += "}.\n\t"
    
    #     s_cell := {(1, 1, 1, 2), (1, 2, 1, 3), (2, 1, 2, 2), (2, 2, 2, 3), (3, 1, 3, 2), (3, 2, 3, 3)}.
    output += "s_cell := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows):
            output += f"({x}, {y}, {x}, {y+1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     w_cell := {(2, 1, 1, 1), (2, 2, 1, 2), (2, 3, 1, 3), (3, 1, 2, 1), (3, 2, 2, 2), (3, 3, 2, 3)}.
    output += "w_cell := {"
    for x in range(2, amount_of_columns+1):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x-1}, {y}), "
    output = output[:-2]
    output += "}.\n\t"



    #     // Point relations, how one point lies in relation to another
    output += "// Point relations, how one point lies in relation to another\n\t"
    #     n_point := {(1, 2, 1, 1), (2, 2, 2, 1), (3, 2, 3, 1), (4, 2, 4, 1), (1, 3, 1, 2), (2, 3, 2, 2), (3, 3, 3, 2), (4, 3, 4, 2), (1, 4, 1, 3), (2, 4, 2, 3), (3, 4, 3, 3), (4, 4, 4, 3)}.
    output += "n_point := {"
    for x in range(1, amount_of_columns+2):
        for y in range(2, amount_of_rows+2):
            output += f"({x}, {y}, {x}, {y-1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     e_point := {(1, 1, 2, 1), (2, 1, 3, 1), (3, 1, 4, 1), (1, 2, 2, 2), (2, 2, 3, 2), (3, 2, 4, 2), (1, 3, 2, 3), (2, 3, 3, 3), (3, 3, 4, 3), (1, 4, 2, 4), (2, 4, 3, 4), (3, 4, 4, 4)}.
    output += "e_point := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows+2):
            output += f"({x}, {y}, {x+1}, {y}), "
    output = output[:-2]
    output += "}.\n\t"

    #     s_point := {(1, 1, 1, 2), (2, 1, 2, 2), (3, 1, 3, 2), (4, 1, 4, 2), (1, 2, 1, 3), (2, 2, 2, 3), (3, 2, 3, 3), (4, 2, 4, 3), (1, 3, 1, 4), (2, 3, 2, 4), (3, 3, 3, 4), (4, 3, 4, 4)}.
    output += "s_point := {"
    for x in range(1, amount_of_columns+2):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x}, {y+1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     w_point := {(2, 1, 1, 1), (3, 1, 2, 1), (4, 1, 3, 1), (2, 2, 1, 2), (3, 2, 2, 2), (4, 2, 3, 2), (2, 3, 1, 3), (3, 3, 2, 3), (4, 3, 3, 3), (2, 4, 1, 4), (3, 4, 2, 4), (4, 4, 3, 4)}.
    output += "w_point := {"
    for x in range(2, amount_of_columns+2):
        for y in range(1, amount_of_rows+2):
            output += f"({x}, {y}, {x-1}, {y}), "
    output = output[:-2]
    output += "}.\n\t"



    #     // Point to cell relations, how a point lies in relation to a cell
    output += "// Point to cell relations, how a point lies in relation to a cell\n\t"

    #     nw_cp := {(1, 1, 1, 1), (2, 1, 2, 1), (3, 1, 3, 1), (1, 2, 1, 2), (2, 2, 2, 2), (3, 2, 3, 2), (1, 3, 1, 3), (2, 3, 2, 3), (3, 3, 3, 3)}.
    output += "nw_cp := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x}, {y}), "
    output = output[:-2]
    output += "}.\n\t"

    #     ne_cp := {(1, 1, 2, 1), (2, 1, 3, 1), (3, 1, 4, 1), (1, 2, 2, 2), (2, 2, 3, 2), (3, 2, 4, 2), (1, 3, 2, 3), (2, 3, 3, 3), (3, 3, 4, 3)}.
    output += "ne_cp := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x+1}, {y}), "
    output = output[:-2]
    output += "}.\n\t"

    #     sw_cp := {(1, 1, 1, 2), (2, 1, 2, 2), (3, 1, 3, 2), (1, 2, 1, 3), (2, 2, 2, 3), (3, 2, 3, 3), (1, 3, 1, 4), (2, 3, 2, 4), (3, 3, 3, 4)}.
    output += "sw_cp := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x}, {y+1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     se_cp := {(1, 1, 2, 2), (2, 1, 3, 2), (3, 1, 4, 2), (1, 2, 2, 3), (2, 2, 3, 3), (3, 2, 4, 3), (1, 3, 2, 4), (2, 3, 3, 4), (3, 3, 4, 4)}.
    output += "se_cp := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x+1}, {y+1}), "
    output = output[:-2]
    output += "}.\n\t"



    #     // cell to point relations, how a cell lies in relation to a point
    output += "// cell to point relations, how a cell lies in relation to a point\n\t"

    #     nw_pc := {(2, 2, 1, 1), (3, 2, 2, 1), (4, 2, 3, 1), (2, 3, 1, 2), (3, 3, 2, 2), (4, 3, 3, 2), (2, 4, 1, 3), (3, 4, 2, 3), (4, 4, 3, 3)}.
    output += "nw_pc := {"
    for x in range(2, amount_of_columns+2):
        for y in range(2, amount_of_rows+2):
            output += f"({x}, {y}, {x-1}, {y-1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     ne_pc := {(1, 2, 1, 1), (2, 2, 2, 1), (3, 2, 3, 1), (1, 3, 1, 2), (2, 3, 2, 2), (3, 3, 3, 2), (1, 4, 1, 3), (2, 4, 2, 3), (3, 4, 3, 3)}.
    output += "ne_pc := {"
    for x in range(1, amount_of_columns+1):
        for y in range(2, amount_of_rows+2):
            output += f"({x}, {y}, {x}, {y-1}), "
    output = output[:-2]
    output += "}.\n\t"

    #     sw_pc := {(2, 1, 1, 1), (3, 1, 2, 1), (4, 1, 3, 1), (2, 2, 1, 2), (3, 2, 2, 2), (4, 2, 3, 2), (2, 3, 1, 3), (3, 3, 2, 3), (4, 3, 3, 3)}.
    output += "sw_pc := {"
    for x in range(2, amount_of_columns+2):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x-1}, {y}), "
    output = output[:-2]
    output += "}.\n\t"
    
    #     se_pc := {(1, 1, 1, 1), (2, 1, 2, 1), (3, 1, 3, 1), (1, 2, 1, 2), (2, 2, 2, 2), (3, 2, 3, 2), (1, 3, 1, 3), (2, 3, 2, 3), (3, 3, 3, 3)}.
    output += "se_pc := {"
    for x in range(1, amount_of_columns+1):
        for y in range(1, amount_of_rows+1):
            output += f"({x}, {y}, {x}, {y}), "
    output = output[:-2]
    output += "}.\n\t"
    
    
    
    output += "\n//===========================\n"
    print(output)





if __name__ == "__main__":
    
    main()