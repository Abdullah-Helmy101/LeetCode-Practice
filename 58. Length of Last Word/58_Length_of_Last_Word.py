def lengthOfLastWord(s: str) -> int:
    string = s.split()

    return len(string[-1])


lengthOfLastWord('Hello World')