import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        
    def create_widgets(self):
        # Estilo para botões
        button_style = {'font': ('Arial', 40), 'width': 5, 'height': 2, 'bg': 'black', 'fg': 'white'}
        
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", **button_style,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
                
    def on_button_click(self, row, col):
        button = self.buttons[row][col]
        if button['text'] == " ":
            button['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Jogo da Velha", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            elif self.check_full():
                messagebox.showinfo("Jogo da Velha", "Empate!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                
    def check_winner(self):
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            if all([self.buttons[i][j]['text'] == self.current_player for j in range(3)]):
                return True
            if all([self.buttons[j][i]['text'] == self.current_player for j in range(3)]):
                return True
        
        if all([self.buttons[i][i]['text'] == self.current_player for i in range(3)]):
            return True
        if all([self.buttons[i][2-i]['text'] == self.current_player for i in range(3)]):
            return True
        
        return False
    
    def check_full(self):
        return all([self.buttons[row][col]['text'] != " " for row in range(3) for col in range(3)])
    
    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = " "
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
