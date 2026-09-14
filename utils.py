class utils:
    def reversed(self, number):
        """Return the integer with its digits reversed."""
        if not isinstance(number, int):
            raise TypeError("reversed expects an int")

        sign = -1 if number < 0 else 1
        return sign * int(str(abs(number))[::-1])

    def formatter(self, number):
        """Return the number in binary (base 2) and octal (base 8) format."""
        if not isinstance(number, int):
            raise TypeError("formatter expects an int")

        return bin(number), oct(number)
