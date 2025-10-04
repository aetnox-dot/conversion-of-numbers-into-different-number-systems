def error_detection(text : str, notation1 : int, notation2 : int):
    all = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    if not isinstance(notation1, int) or not isinstance(notation2, int):
        return "number system error: Bases must be integers (INT)."
    if notation2 <2 or notation1 <2 or notation2 > 36 or notation1 > 36:
        return "number system error: Bases must be between 2 and 36."
    if text not in all[:notation1]:
        return f"number system error: The character {text} is not valid in base {notation1} numbers."


def translation_letters (number : str, typ : bool):
    mapping = {
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16,
        "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23,
        "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30,
        "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35}
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if typ == False:
        if str(number) in numbers:
            return str(number)
        else:
            for key, value in mapping.items():
                if value == number:
                    return key    
    elif typ:
        if number in numbers:
            return int(number)
        else:
            for key, value in mapping.items():
                if key == number:
                    return value


def notation_ (number, notation1 : int, notation2 : int):

    number = str(number)
    number = number.upper()
    for chois in number:
        search = error_detection(chois, notation1, notation2)
        if search != None:
            return search

    if notation1 == 10:

        new_number = []
        number = int(number)

        while number >= notation2:

            remainder = number % notation2
            number = number // notation2
            new_number.insert(0, translation_letters(remainder, False))

        new_number.insert(0, translation_letters(number, False))

        return "".join(new_number)

    elif notation2 == 10:
        number_int = []
        for chois in number:
            number_int.append(translation_letters(chois, True))

        new_number = 0
        copy_number = number_int[:]

        for chois in number_int:
            new_number = new_number + chois*notation1**(len(copy_number)-1)
            copy_number.pop(0)
        return str(new_number)
    
    else:
        number_int = []
        for chois in number:
            number_int.append(translation_letters(chois, True))

        number = 0
        copy_number = number_int[:]

        for chois in number_int:
            number = number + chois*notation1**(len(copy_number)-1)
            copy_number.pop(0)

        new_number = []

        while number >= notation2:

            remainder = number % notation2
            number = number // notation2
            new_number.insert(0, translation_letters(remainder, False))

        new_number.insert(0, translation_letters(number, False))

        return "".join(new_number)