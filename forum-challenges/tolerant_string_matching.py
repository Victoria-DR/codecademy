def basicMatch(message, snippet):
    # Check without regard to case if snippet is a substring of message
    return snippet.upper() in message.upper()

# print(basicMatch("Codecademy taught me to code", "code"))
# print(basicMatch("A really long string", "on"))
# print(basicMatch("Welcome to the internet", "hello"))
# print(basicMatch("CaseInsEnSiTiVE", "caseinsensitive"))

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
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded, 1)
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

# print(intermediateMatch("Codecademy is great", "codecademy", []))
# print(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
# print(intermediateMatch("Codec%65demy is great", "codec%65demy", [["%65", "A"]]))
# print(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"], ["%67", "D"]]))
# print(intermediateMatch("Co%67ec%65demy is great", "codec%65demy", [["%65", "A"], ["%67", "D"]]))
# print(intermediateMatch("Co%67eca%68emy is great", "codecademy", [["%67", "D"], ["%68", "D"]]))
# print(intermediateMatch("Co%67eca%67emy is great", "co%67ecademy", [ ["%67", "D"]]))
# print(intermediateMatch("Codecademy is great", "codec%65demy", [["%65", "A"]]))
# print(intermediateMatch("abc%6efg", "abcdefg", [["e", "d"], ["%6", "e"]]))

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
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded, 1)
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

# print(hardMatch("Codecademy is great", "codecademy", []))
# print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
# print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "A"]]))
# print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]))
