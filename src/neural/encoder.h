#pragma once

#include <vector>
#include <array>
#include "game/symmetry.h"
#include "game/game_state.h"
#include "neural/network_basic.h"

class Encoder {
public:
    static constexpr int kPlaneChannels = kInputChannels;
    static constexpr int kHistoryMove = 8;
    static constexpr int kNumFeatures = 12;

    static Encoder& Get();

    InputData GetInputs(const GameState &state, int symmetry = Symmetry::kIdentitySymmetry) const;

    std::vector<float> GetPlanes(const GameState &state, int symmetry = Symmetry::kIdentitySymmetry) const;

    std::string GetPlanesString(const GameState &state, int symmetry = Symmetry::kIdentitySymmetry) const;

private:
    void SymmetryPlanes(const GameState &state, std::vector<float> &planes, int symmetry) const;

    void FillColorStones(std::shared_ptr<const Board> board,
                         std::vector<float>::iterator black_it,
                         std::vector<float>::iterator white_it) const;

    void FillMove(std::shared_ptr<const Board> board,
                  std::vector<float>::iterator move_it) const;

    void EncoderHistoryMove(const GameState &state,
                            int counter,
                            std::vector<float>::iterator it) const;

    void FillKoMove(std::shared_ptr<const Board> board,
                    std::vector<float>::iterator ko_it) const;

    void FillCaptureMove(std::shared_ptr<const Board> board,
                         std::vector<float>::iterator capture_it) const;

    void FillLiberties(std::shared_ptr<const Board> board,
                       std::vector<float>::iterator liberties_it) const;

    void FillLadder(std::shared_ptr<const Board> board,
                    std::vector<float>::iterator ladder_it) const;

    void FillSideToMove(std::shared_ptr<const Board> board,
                        float komi,
                        std::vector<float>::iterator color_it) const;

    void EncoderFeatures(const GameState &state,
                         std::vector<float>::iterator it) const;

};
