def check_triangle(side_a, side_b, side_c) -> bool:
    if (side_a >= side_b + side_c) or (side_b >= side_a + side_c) or (side_c >= side_b + side_a):
        return False
    else:
        return True

if __name__ == "__main__":
    while True:
        try:
            side_1 = float(input("length of the 1st side: "))
            side_2 = float(input("length of the 2nd side: "))
            side_3 = float(input("length of the 3rd side: "))
            break
        except ValueError:
            print("input is incorrect")
            
    if check_triangle(side_1, side_2, side_3):
        print("Possible triangle")
    else:
        print("Impossible triangle")