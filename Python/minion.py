# The Minion Game in Python
def minion_game(string):
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i

    if player1 > player2:
        print("Kevin N Score:", player1)
    elif player1 < player2:
        print("Stuart WIN Score:",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")

if __name__ == '__main__':
    print("PLEASE INPUT WORDS :")
    s = input()
    minion_game(s)
