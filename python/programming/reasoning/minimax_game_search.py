"""
A complete minimax game solver with alpha-beta pruning and depth limiting.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Any, Union
import copy


class GameState(ABC):
    """Abstract base class for game states."""
    
    @abstractmethod
    def get_legal_moves(self) -> List[Any]:
        """Return a list of legal moves from this state."""
        pass
    
    @abstractmethod
    def make_move(self, move: Any) -> 'GameState':
        """Return a new game state after applying the given move."""
        pass
    
    @abstractmethod
    def is_terminal(self) -> bool:
        """Return True if this is a terminal state (win/loss/draw)."""
        pass
    
    @abstractmethod
    def get_result(self) -> Optional[int]:
        """Return the game result if terminal: 1 (win), -1 (loss), 0 (draw), None (not terminal)."""
        pass


class Evaluator(ABC):
    """Abstract base class for position evaluation."""
    
    @abstractmethod
    def evaluate(self, state: GameState) -> float:
        """Evaluate the given non-terminal state. Higher values favor the maximizing player."""
        pass


class TicTacToeState(GameState):
    """Tic-TacToe game state implementation."""
    
    def __init__(self, board: Optional[List[List[Optional[str]]]] = None, player: str = 'X'):
        """Initialize with optional board and current player."""
        self.board = board or [[None for _ in range(3)] for _ in range(3)]
        self.player = player
    
    def get_legal_moves(self) -> List[Tuple[int, int]]:
        """Return list of empty positions as (row, col) tuples."""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    moves.append((i, j))
        return moves
    
    def make_move(self, move: Tuple[int, int]) -> 'TicTacToeState':
        """Return new state with move applied."""
        if self.board[move[0]][move[1]] is not None:
            raise ValueError("Invalid move")
        
        new_board = copy.deepcopy(self.board)
        new_board[move[0]][move[1]] = self.player
        next_player = 'O' if self.player == 'X' else 'X'
        return TicTacToeState(new_board, next_player)
    
    def is_terminal(self) -> bool:
        """Check if game is over."""
        return self.get_result() is not None
    
    def get_result(self) -> Optional[int]:
        """Return 1 if X wins, -1 if O wins, 0 for draw, None for ongoing."""
        # Check rows, columns, diagonals for wins
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return 1 if self.board[i][0] == 'X' else -1
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return 1 if self.board[0][i] == 'X' else -1
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return 1 if self.board[0][0] == 'X' else -1
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return 1 if self.board[0][2] == 'X' else -1
        
        # Check for draw
        if all(self.board[i][j] is not None for i in range(3) for j in range(3)):
            return 0
        
        # Game not over
        return None
    
    def __str__(self) -> str:
        """String representation of the board."""
        result = ""
        for i in range(3):
            row = "|".join([self.board[i][j] if self.board[i][j] else " " for j in range(3)])
            result += row + "\n"
            if i < 2:
                result += "-----\n"
        return result


class TicTacToeEvaluator(Evaluator):
    """Simple evaluator for Tic-TacToe."""
    
    def evaluate(self, state: TicTacToeState) -> float:
        """Evaluate non-terminal state based on potential winning lines."""
        if state.is_terminal():
            result = state.get_result()
            return float('inf') if result == 1 else float('-inf') if result == -1 else 0.0
        
        score = 0
        # Check rows
        for i in range(3):
            x_count = sum(1 for j in range(3) if state.board[i][j] == 'X')
            o_count = sum(1 for j in range(3) if state.board[i][j] == 'O')
            if x_count > 0 and o_count == 0:
                score += 10 ** x_count
            elif o_count > 0 and x_count == 0:
                score -= 10 ** o_count
        
        # Check columns
        for j in range(3):
            x_count = sum(1 for i in range(3) if state.board[i][j] == 'X')
            o_count = sum(1 for i in range(3) if state.board[i][j] == 'O')
            if x_count > 0 and o_count == 0:
                score += 10 ** x_count
            elif o_count > 0 and x_count == 0:
                score -= 10 ** o_count
        
        # Check diagonals
        diagonals = [
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]
        ]
        
        for diag in diagonals:
            x_count = sum(1 for i, j in diag if state.board[i][j] == 'X')
            o_count = sum(1 for i, j in diag if state.board[i][j] == 'O')
            if x_count > 0 and o_count == 0:
                score += 10 ** x_count
            elif o_count > 0 and x_count == 0:
                score -= 10 ** o_count
                
        return float(score)


class MinimaxSolver:
    """Minimax solver with alpha-beta pruning and depth limiting."""
    
    def __init__(self, evaluator: Evaluator):
        """Initialize with an evaluator."""
        self.evaluator = evaluator
        self.nodes_explored = 0
    
    def solve(self, state: GameState, depth_limit: int = 10) -> Tuple[Optional[Any], float]:
        """
        Solve the game from the given state.
        
        Args:
            state: Current game state
            depth_limit: Maximum search depth
            
        Returns:
            Tuple of (best_move, best_score)
        """
        self.nodes_explored = 0
        best_move, best_score = self._minimax(state, depth_limit, True, float('-inf'), float('inf'))
        return best_move, best_score
    
    def _minimax(self, state: GameState, depth: int, maximizing: bool, 
                 alpha: float, beta: float) -> Tuple[Optional[Any], float]:
        """Internal minimax implementation with alpha-beta pruning."""
        self.nodes_explored += 1
        
        # Terminal state or depth limit reached
        if state.is_terminal() or depth == 0:
            if state.is_terminal():
                result = state.get_result()
                return None, float(result) if result is not None else self.evaluator.evaluate(state)
            else:
                return None, self.evaluator.evaluate(state)
        
        best_move = None
        if maximizing:
            max_eval = float('-inf')
            for move in state.get_legal_moves():
                child_state = state.make_move(move)
                _, eval_score = self._minimax(child_state, depth - 1, False, alpha, beta)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cutoff
            return best_move, max_eval
        else:
            min_eval = float('inf')
            for move in state.get_legal_moves():
                child_state = state.make_move(move)
                _, eval_score = self._minimax(child_state, depth - 1, True, alpha, beta)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            return best_move, min_eval


def main():
    """Demo: Play Tic-TacToe with minimax AI."""
    print("Tic-TacToe Minimax Demo")
    print("=======================")
    
    # Create game components
    evaluator = TicTacToeEvaluator()
    solver = MinimaxSolver(evaluator)
    
    # Create initial state
    state = TicTacToeState()
    print("Initial board:")
    print(state)
    
    # Play a few moves
    moves_played = 0
    while not state.is_terminal() and moves_played < 9:
        if state.player == 'X':
            # Human player (or could be another AI)
            legal_moves = state.get_legal_moves()
            move = legal_moves[0]  # Just pick first available move for demo
            print(f"Player {state.player} moves: {move}")
        else:
            # AI player using minimax
            print(f"AI ({state.player}) thinking...")
            move, score = solver.solve(state, depth_limit=9)  # Full depth for small game
            print(f"AI chooses move {move} with score {score} (explored {solver.nodes_explored} nodes)")
        
        if move is None:
            break
            
        state = state.make_move(move)
        print(f"Board after move {moves_played + 1}:")
        print(state)
        
        moves_played += 1
    
    # Show final result
    result = state.get_result()
    if result == 1:
        print("X wins!")
    elif result == -1:
        print("O wins!")
    elif result == 0:
        print("It's a draw!")
    else:
        print("Game not finished")


if __name__ == "__main__":
    main()