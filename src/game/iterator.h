#pragma once

#include "game/game_state.h"

#include <vector>

// The history boards generated by SGF parser may have some error.
// The GameStateIterator promises that the outputs training data is
// correct.
class GameStateIterator {
public:
    GameStateIterator(GameState &state);

    // Reset current game state. It will fill the moves from game state
    // history to the itself move history buffer. So becare that it will
    // cut off future history boards in the move history buffer. 
    void Reset();

    // Return true the current board in the history has 
    // next move.
    bool Next();

    // Return current game state.
    GameState &GetState();

    // Return current side to move.
    int GetToMove() const;

    // Return current move.
    int GetVertex() const;

    // Return next move. Will return pass if there is no
    // next move.
    int GetNextVertex() const;

    // Return number of move.
    int MaxMoveNumber() const;

private:
    struct ColorVertex {
        int to_move;
        int vertex;
    };

    // the current game state
    GameState curr_state_;

    // the move history buffer
    std::vector<ColorVertex> move_history_;

    int curr_idx_;
};
