#for https://www.hackerrank.com/challenges/merge-the-tools/
def merge_the_tools(string, k):
    # your code goes here

    substrings = [string[i:i+k] for i in range(0, len(string), k)]

    for substring in substrings:
        unique_chars = ''
        for char in substring:
            if char not in unique_chars:
                unique_chars += char
        print(unique_chars)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)