def basicMatch(message, snippet):
    # Check without regard to case if snippet is a substring of message
    return snippet.upper() in message.upper()

# print(basicMatch("Codecademy taught me to code", "code"))
# print(basicMatch("A really long string", "on"))
# print(basicMatch("Welcome to the internet", "hello"))
# print(basicMatch("CaseInsEnSiTiVE", "caseinsensitive"))

def intermediateMatch(message, snippet, decodings):
    # Render case insensitive
    message = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    # Find first occurence of first character in snippet
    start = message.find(snippet[0])
    if start == -1:
        # Determine if the first character of snippet is encoded in message
        if snippet[0] not in decoding_dict.values():
            return False
        else:
            # Decode the first character of snippet in message
            for coded, decoded in decoding_dict.items():
                if decoded == snippet[0]:
                    message = message.replace(coded, decoded, 1)
                    # Find new first occurence of first character in snippet
                    start = message.find(snippet[0])

    matches = False
    index = 1
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message) - len(snippet)):
        # Check if letter is the same in message and snippet
        if message[start + index] == snippet[index]:
            index += 1
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message[start + index: start + index + len(coded)]:
                    message = message[:start + index] + message[start + index:].replace(coded, decoded, 1)
                    index += 1
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return intermediateMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            print(message, snippet)
            matches = True if (snippet.upper() in message.upper()) else False
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
    