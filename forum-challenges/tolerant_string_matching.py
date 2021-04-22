def basicMatch(message, snippet):
    # Check without regard to case if snippet is a substring of message
    return snippet.upper() in message.upper()

print("Basic\n***************")
print(basicMatch("Codecademy taught me to code", "code"))
print(basicMatch("A really long string", "on"))
print(basicMatch("Welcome to the internet", "hello"))
print(basicMatch("CaseInsEnSiTiVE", "caseinsensitive"))


def intermediateMatch(message, snippet, decodings):
    # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message_alter:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    matches = False
    start = 0
    index = 0
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded.upper(), 1)
                    # Allow for decoding to occur only once
                    index += 1
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return intermediateMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    return matches

print("\n\nIntermediate\n***************")
print(intermediateMatch("Codecademy is great", "codecademy", []))
print(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
print(intermediateMatch("Codec%65demy is great", "codec%65demy", [["%65", "A"]]))
print(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"], ["%67", "D"]]))
print(intermediateMatch("Co%67ec%65demy is great", "codec%65demy", [["%65", "A"], ["%67", "D"]]))
print(intermediateMatch("Co%67eca%68emy is great", "codecademy", [["%67", "D"], ["%68", "D"]]))
print(intermediateMatch("Co%67eca%67emy is great", "co%67ecademy", [ ["%67", "D"]]))
print(intermediateMatch("Codecademy is great", "codec%65demy", [["%65", "A"]]))
print(intermediateMatch("abc%6efg", "abcdefg", [["e", "d"], ["%6", "e"]]))


def hardMatch(message, snippet, decodings):
    # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message_alter:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    matches = False
    start = 0
    index = 0
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded.upper(), 1)
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return hardMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    return matches

print("\n\nHard\n***************")
print(hardMatch("Codecademy is great", "codecademy", []))
print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "A"]]))
print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]))


def extremeMatch(message, snippet, decodings):
    # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message_alter:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    matches = False
    start = 0
    index = 0
    times_decoded = 0
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check for cycles in decodings
        if times_decoded > len(decodings):
            return False

        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
            times_decoded = 0
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded.upper(), 1)
                    times_decoded += 1
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return extremeMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    return matches

print("\n\nExtreme\n***************")
print(extremeMatch("$1cademy is great", "codecademy", [["$2", "co"], ["$1", "code"]]))
print(extremeMatch("$2decademy is great", "codecademy", [["$1", "code"], ["$2", "co"]]))
print(extremeMatch("%1 is great", "codecademy", [["%1", "codecademy"], ["%68", "D"]]))
print(extremeMatch("%1 is great", "codecademy", [["%1", "codecademy"], ["codecademy", "%2"], ["%2", "%1"]]))
print(extremeMatch("%1 is great", "code", [["%1", "codecademy"], ["%68", "D"]]))
print(extremeMatch("%1 is great", "code", [["%1", "co"], ["%68", "D"]]))
print(extremeMatch("%1 is great", "code", [["%1", "co"], ["co", "d"], ["d", "%1"]]))


def bonusMatch(message, snippet, decodings):
        # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    matches = False
    start = 0
    index = 0
    times_decoded = 0
    length_difference = 0
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check for cycles in decodings
        if times_decoded > len(decodings):
            return False, 0, 0

        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
            times_decoded = 0
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded.upper(), 1)
                    times_decoded += 1
                    length_difference -= len(decoded) - len(coded)
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                start += 1
                return bonusMatch(message[start], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    if matches:
        return True, start, start + index + length_difference
    else:
        return False, 0, 0

print("\n\nBonus\n***************")
print(bonusMatch("Codecademy is great", "codecademy", []))
print(bonusMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
print(bonusMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "A"]]))
print(bonusMatch("Co%67ecademy teaches me to code", "code", [["%67", "d"], ["d", "a"]]))
print(bonusMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]))
