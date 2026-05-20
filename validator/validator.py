def main():
    IBAN = input("type a IBAN: ").strip()
    IBAN = IBAN.replace(" ", "")
    if verify(IBAN):
        print("valid")
    else:
        print("invalid")


def verify(iban):
    if not iban.isalnum():
        print("invalid caracters")
    elif len(iban) > 30 or len(iban) < 15:
        print("invalid lenght")
    else:
        final = ""
        iban = iban[4:] + iban[0:4]
        for ch in iban:
            if ch.isalpha():
                ch = ch.upper()
                ch = lettonum(ch)
            final = final + str(ch)
        if int(final) % 97 == 1:
            return True
        else:
            return False


def lettonum(ch):
    n = ord(f"{ch}") - 55
    print(ord("A"))
    return n


if __name__ == "__main__":
    main()
