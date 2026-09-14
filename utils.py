class utils:
    def reversed(self, number):
        "Return the integer with its digits reversed."

        "save sign in variable"
        sign = -1 if number < 0 else 1
        
        return sign * int(str(abs(number))[::-1])
        "[start:stop:step], -1 steps once backwards, requires a sequence of digits hence convert to string first"

    def formatter(self, number):
        "Return the number in binary (base 2) and octal (base 8) format."

        return bin(number), oct(number)
