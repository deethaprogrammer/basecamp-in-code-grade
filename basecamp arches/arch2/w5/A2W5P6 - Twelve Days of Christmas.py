def next_verse(vers_number: int) -> str:
    verse = ""
    present = {
    1: "On the 1st day of Christmas, my true love sent to me a partridge in a pear tree",
    2: "On the 2nd day of Christmas, my true love sent to me two turtle doves",
    3: "On the 3rd day of Christmas, my true love sent to me three French hens",
    4: "On the 4th day of Christmas, my true love sent to me four calling birds",
    5: "On the 5th day of Christmas, my true love sent to me five gold rings(fivegolden rings)",
    6: "On the 6th day of Christmas, my true love sent to me six geese a-laying",
    7: "On the 7th day of Christmas, my true love sent to me seven swans a-swimming",
    8: "On the 8th day of Christmas, my true love sent to me eight maids a-milking",
    9: "On the 9th day of Christmas, my true love sent to me nine ladies dancing",
    10: "On the 10th day of Christmas, my true love sent to me ten lords a-leaping",
    11: "On the 11th day of Christmas, my true love sent to me eleven pipers piping",
    12: "On the 12th day of Christmas, my true love sent to me twelve drummers drumming"
    }
    presents = {
    1: "a partridge in a pear tree",
    2: "two turtle doves",
    3: "three French hens",
    4: "four calling birds",
    5: "five gold rings(fivegolden rings)",
    6: "six geese a-laying",
    7: "seven swans a-swimming",
    8: "eight maids a-milking",
    9: "nine ladies dancing",
    10: "ten lords a-leaping",
    11: "eleven pipers piping",
    12: "twelve drummers drumming"
}
    for i in range(vers_number, 0, -1):
        if i == vers_number:
            verse +=(present[i])
        elif i == 1 and not i == vers_number:
            verse += (" and " + presents[i])
        else:
            verse += (", " + presents[i])
    return verse

if __name__ == "__main__":
    for j in range (1, 13):
        print(next_verse(j))