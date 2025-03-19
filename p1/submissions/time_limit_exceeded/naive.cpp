#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<string> players(n);
    unordered_map<string, int> player_index;

    // Reading players and creating a map from player name to their index
    for (int i = 0; i < n; ++i) {
        cin >> players[i];
        player_index[players[i]] = i;
    }

    // Processing the operations
    for (int i = 0; i < k; ++i) {
        string player_x, player_y, operation;
        cin >> player_x >> operation >> player_y;

        int x_idx = player_index[player_x];
        int y_idx = player_index[player_y];

        if (operation == ">") {
            // player X > player Y -> place X immediately before Y
            string temp = players[x_idx];
            players.erase(players.begin() + x_idx);
            int insert_pos = (x_idx < y_idx) ? y_idx - 1 : y_idx;
            players.insert(players.begin() + insert_pos, temp);
            // Update the player index map after the change
            for (int j = 0; j < n; ++j) {
                player_index[players[j]] = j;
            }
        } else if (operation == "<") {
            // player X < player Y -> place X immediately after Y
            string temp = players[x_idx];
            players.erase(players.begin() + x_idx);
            int insert_pos = (x_idx < y_idx) ? y_idx : y_idx + 1;
            players.insert(players.begin() + insert_pos, temp);
            // Update the player index map after the change
            for (int j = 0; j < n; ++j) {
                player_index[players[j]] = j;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << i + 1 << " " << players[i] << endl;
    }

    return 0;
}
