class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        # Check lowercase, uppercase and digit
        lower = False
        upper = False
        digit = False

        for ch in password:
            if ch.islower():
                lower = True
            elif ch.isupper():
                upper = True
            elif ch.isdigit():
                digit = True

        missing = 0
        if not lower:
            missing += 1

        if not upper:
            missing += 1

        if not digit:
            missing += 1

        # Find groups of 3 or more consecutive characters
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1

            length = j - i
            if length >= 3:
                repeats.append(length)
            i = j

        # Case 1: password is too short
        if n < 6:
            return max(missing, 6 - n)

        # Case 2: password length is valid
        elif n <= 20:
            replace = 0
            for length in repeats:
                replace += length // 3
            return max(missing, replace)

        # Case 3: password is too long
        else:
            delete = n - 20

            # First use deletions on groups where they reduce replacements
            for i in range(len(repeats)):
                if delete == 0:
                    break

                length = repeats[i]
                # For length % 3 == 0,
                # one deletion reduces one replacement
                if length % 3 == 0:
                    remove = min(delete, 1)
                    repeats[i] -= remove
                    delete -= remove

            # Next handle groups where 2 deletions reduce 1 replacement
            for i in range(len(repeats)):
                if delete == 0:
                    break

                length = repeats[i]
                if length % 3 == 1:
                    remove = min(delete, 2)
                    repeats[i] -= remove
                    delete -= remove

            # Remaining deletions
            # Every 3 deletions reduce one replacement
            for i in range(len(repeats)):

                if delete == 0:
                    break
                remove = min(delete, 3 * (repeats[i] // 3))
                repeats[i] -= remove
                delete -= remove

            # Calculate remaining replacements
            replace = 0
            for length in repeats:
                replace += length // 3
            return (n - 20) + max(missing, replace)