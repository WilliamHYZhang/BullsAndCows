'''
Bulls and Cows

Searches through all https://scrabble.merriam.com/3-letter-words and makes the best possible guess every turn.

Usage:
add => adds a guess from another player's turn
play => output best guess at current turn
print => output current search space
'''
from collections import Counter

word_list = set(
    filter(lambda x: len(Counter(x)) == len(x),
           [word.strip() for word in open('words.txt', 'r').readlines()]))
search_space = word_list


def search(bulls, cows, guess):
    cur_search = set(search_space)
    for bull in bulls:
        cur_search = set(
            filter(lambda x: x.find(guess[bull]) == bull, cur_search))
    for cow in cows:
        cur_search = set(
            filter(lambda x: x.find(guess[cow]) not in [-1, cow], cur_search))
    exclude = guess
    for i in bulls + cows:
        exclude = exclude.replace(guess[i], '')
    cur_search = set(
        filter(lambda x: not any([c in x for c in exclude]), cur_search))
    return cur_search


while True:
    print('Current search space:', len(search_space), 'words')
    cmd = input('Input <command>: ')
    if cmd == 'add':
        guess, bulls, cows = input('Input <word, bulls, cows>: ').split()
        bulls, cows = [int(bulls), int(cows)]
        if bulls == 0:
            if cows == 0:
                search_space = search([], [], guess)
            elif cows == 1:
                cur_search = set()
                for i in range(3):
                    cur_search.update(search([], [i], guess))
                search_space = cur_search
            elif cows == 2:
                cur_search = set()
                for i in range(3):
                    cur_search.update(
                        search([], [x for x in list(range(3)) if x != i],
                               guess))
                search_space = cur_search
        elif bulls == 1:
            if cows == 0:
                cur_search = set()
                for i in range(3):
                    cur_search.update(search([i], [], guess))
                search_space = cur_search
            elif cows == 1:
                cur_search = set()
                for i in range(3):
                    for j in range(3):
                        if i == j:
                            continue
                        cur_search.update(search([i], [j], guess))
                search_space = cur_search
            elif cows == 2:
                cur_search = set()
                for i in range(3):
                    cur_search.update(
                        search([i], [x for x in list(range(3)) if x != i],
                               guess))
                search_space = cur_search
        elif bulls == 2:
            cur_search = set()
            for i in range(3):
                cur_search.update(
                    search([x for x in list(range(3)) if x != i], [], guess))
            search_space = cur_search
    elif cmd == 'play':
        print('Best guess:', list(search_space)[0])
    elif cmd == 'print':
        print(search_space)
    else:
        print('Invalid command, try again')
