class Tictactoe:
    def __init__(self,player_1,player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.scoreBoard = {self.player_1: 0, self.player_2: 0}  
        self.playerChoice = {'X' : "", 'O' : ""}
        self.PlayerPosition = {'X' : [], 'O' : []}
        self.option = ['X', 'O'] 
        self.CurrentPlayer = None
        self.GameStatus = None

    def boardGrid(self,arr):
        print("\n")  
        print("\t|     |      |     |")  
        print("\t|  {}  |  {}   |  {}  |".format(arr[0], arr[1], arr[2]))  
        print('\t|_____|______|_____|')    
        print("\t|     |      |     |")
        print("\t|  {}  |  {}   |  {}  |".format(arr[3], arr[4], arr[5]))  
        print('\t|_____|______|_____|')  
        print("\t|     |      |     |")
        print("\t|   {} |  {}   |  {}  |".format(arr[6], arr[7], arr[8]))  
        print('\t|_____|______|_____|') 
        print("\n")

    def gameScoreBoard(self):
        print("\t--------------------------------")  
        print("\t         SCORE BOARD       ")  
        print("\t--------------------------------")  
        list_of_the_two_players = list(self.scoreBoard.keys())  
        print("\t   ", list_of_the_two_players[0], "\t    ", self.scoreBoard[list_of_the_two_players[0]])  
        print("\t   ", list_of_the_two_players[1], "\t    ", self.scoreBoard[list_of_the_two_players[1]])  
    
        print("\t--------------------------------\n")

    def gameValidation(self,CurrentPlayerMark):  
        PlayerWinCombination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]   
        
        for ele in PlayerWinCombination:  
            if all(j in self.PlayerPosition[CurrentPlayerMark] for j in ele):  
                self.GameStatus = 'Win'
                return CurrentPlayerMark 
        
        if len(self.PlayerPosition['X']) + len(self.PlayerPosition['O']) == 9:
            self.GameStatus = 'Tie'
            return True
        return False 

    def gamePlay(self):
        board = [' ' for _ in range(9)]

        self.boardGrid(board)
        while True:

            print("player ", self.CurrentPlayer, " .choose your block : ", end="")  
            CurrentPlayerMark = [k for k,v in self.playerChoice.items() if v == self.CurrentPlayer][0]
            blockIndex = int(input())
            
            ## Block Index Validation
            if blockIndex < 1 or blockIndex > 9:  
                print("This is an Invalid Input!!!")  
                continue  
    
            ## To check if the block in the grid is not filled up already
            if board[blockIndex - 1] != ' ':  
                print("The position is already filled. Please try again!")  
                continue  

            board[blockIndex - 1] = CurrentPlayerMark
            self.PlayerPosition[CurrentPlayerMark].append(blockIndex)

            GameResult = self.gameValidation(CurrentPlayerMark)

            if self.GameStatus == 'Win':
                self.boardGrid(board)
                print(self.CurrentPlayer, " has won the tic tac toe game!")       
                print("\n")  
                player_won = self.playerChoice[GameResult]  
                self.scoreBoard[player_won] = self.scoreBoard[player_won] + 1 
    
                self.gameScoreBoard()
                return True 
            
            if self.GameStatus == 'Tie':
                self.boardGrid(board)
                print("It was close! Game is Tied")  
                print("\n")  
                return True

            if self.CurrentPlayer == self.player_1:  
                self.CurrentPlayer = self.player_2  
            else:   
                self.CurrentPlayer = self.player_1


    def playerChoiceMethod(self):
        self.CurrentPlayer = self.player_1
        while True:  
            print(self.CurrentPlayer, ",Make the choice for the series of the Tic tac toe game:")  
            print("Please press X or O or S for Exit")  
            try:
                PlayerSelection  = str(input().upper())
            except ValueError:
                print("Enter valid Input!!! Please Try Again\n")  
                continue  

            if PlayerSelection == 'X':
                self.playerChoice['X'] = self.CurrentPlayer
                if  self.CurrentPlayer == self.player_1:
                    self.playerChoice['O'] = self.player_2
                else:
                    self.playerChoice['O'] = self.player_1
            elif PlayerSelection == 'O':
                self.playerChoice['O'] = self.CurrentPlayer
                if  self.CurrentPlayer == self.player_1:
                    self.playerChoice['X'] = self.player_2
                else:
                    self.playerChoice['X'] = self.player_1
            elif PlayerSelection == 'S':
                print("Thanks for playing the game!!!")
                print("The final scores are")  
                #self.gameScoreBoard()  
                break    
            else:  
                print("Invalid choice!!\n") 
            
            self.gamePlay()
            
                

if __name__ == '__main__':

    ### Enter Player Names
    print("player 1 Enter Your Name")  
    player_1 = input("player 1: ")  
    print("\n")
    print("player 2 Enter Your Name")  
    player_2 = input("player 2: ")  
    print("\n")

    gameObj = Tictactoe(player_1,player_2)
    gameObj.playerChoiceMethod()