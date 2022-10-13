# # youtuber = "love me "
# # print('subscribe to' + youtuber)
# # print('subscribe to {}'.format(youtuber) )
# # print(f'subscribe to {youtuber}')
# adj = input('adjective: ')
# verb1 = input('verb: ')
# verb2 = input('verb: ')
# famous_person = input('famous person: ')
# madlib = f'computer programing is so {adj}! it make me so excited all the time because \
#     i love to {verb1}.Stay hydrated and {verb2} like you are {famous_person}!'
# print(madlib)
# import random

# def guess (x):
#     random_number = random.randint(1,x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'guess a number between 1 and {x} :'))
#         if guess < random_number:
#             print('almost close to ans :')
#         elif guess > random_number:
#             prnit ('too far from ans :')
#     print("bingooo{}".format(random_number))

# def computer_guess(x):
#     low = 1 
#     high = x 
#     feedback = ''
#     while feedback != 'c':
#         if low != high :
#          guess = random.randint(low,high)
#         else :
#             guess = low 
#         feedback = input(f"is {guess}too high (h), too low(l) , or correct(c)???.")
#         if feedback == "h":
#             high = guess -1
#         elif feedback == "l":
#             low = guess + 1
#     print (f"bingo {guess}")
# # guess(10)

# rock paper scissor 


# import random

# def play():
#     user =input("'r' for rock 'p' for paper 's' for scissors")

#     computer = random.choice(['r','p','s'])

#     if user == computer:
#         return 'tie'
#     if is_win(user,computer):
#         return 'you won!'

#     return 'you lost'

# def is_win(player,oppsite):
#     if (player =='r' and oppsite == 's') or (player == 's'and oppsite == 'p') or (player == 'p'and oppsite == 'r'):
#         return 
import random
class Board:
    def __init__(self, dim_size , num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        self.board = self.make_new_board(self)
        self,assign_values_to_board()

        set.dug = set()
    def make_new_board(self):

        def assign_values_to_board(self):








         for r in range (self.dim_size): 
            for c in range (self.dim_size):
                if self.board[r][c] == '*':
                    continue

                self.board[r][c] = self.get_num_neigboring_bomb(r,c)

        def get_num_neigboring_bomb(r,c):

        bomb_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dum_size 

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bomb_planted += 1
        return board


def play(dim_size = 10 , num_bombs = 10):
    pass

    