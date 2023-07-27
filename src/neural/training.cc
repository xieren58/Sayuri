#include "game/types.h"
#include "neural/training.h"
#include "neural/network_basic.h"

void ArrayStreamOut(std::ostream &out, const std::vector<float> &arr) {
    const auto size = arr.size();
    for (size_t i = 0; i < size; ++i) {
        out << arr[i];
        if (i != size-1) out << ' ';
    }
    out << std::endl;
}

void OwnershipStreamOut(std::ostream &out, const std::vector<int> &arr) {
    const auto size = arr.size();
    for (size_t i = 0; i < size; ++i) {
        const auto v = arr[i];
        if (v == 0) {
            out << 0;
        } else if (v == 1) {
            out << 1;
        } else if (v == -1) {
            out << (1 + 2);
        }
    }
    out << std::endl;
}

void PlanesStreamOut(std::ostream &out, const std::vector<float> &arr, size_t planes) {
    const auto size = arr.size();
    const auto spatial = size / planes;
    const bool remaining = (spatial % 4 != 0);
    const auto saved_planes = planes-4; // Last four channels are not binary features.

    for (size_t p = 0; p < saved_planes; ++p) {
        for (size_t idx = 0; idx+4 <= spatial; idx+=4) {
            int hex = 0;

            auto bit_1 = (int)arr[idx + spatial * p+0];
            auto bit_2 = (int)arr[idx + spatial * p+1];
            auto bit_3 = (int)arr[idx + spatial * p+2];
            auto bit_4 = (int)arr[idx + spatial * p+3];

            hex += bit_1;
            hex += bit_2 << 1;
            hex += bit_3 << 2;
            hex += bit_4 << 3;

            out << std::hex << hex;
        }
        if (remaining) {
            out << (bool)arr[spatial * (p+1) - 1];
        }

        out << std::dec << std::endl;
    }
}

void Training::StreamOut(std::ostream &out) const {
    if (discard) {
        return;
    }

    out << version << std::endl;
    out << mode << std::endl;
    out << board_size << std::endl;
    out << komi << std::endl;

    PlanesStreamOut(out, planes, kInputChannels);
    out << (side_to_move == kBlack ? 1 : 0) << std::endl;

    ArrayStreamOut(out, probabilities);
    ArrayStreamOut(out, auxiliary_probabilities);
    OwnershipStreamOut(out, ownership);

    out << result << std::endl;
    out << q_value << std::endl;
    out << final_score << std::endl;
}

int GetTrainingVersion() {
    return 1;
}

int GetTrainingMode() {
    return 0;
}
