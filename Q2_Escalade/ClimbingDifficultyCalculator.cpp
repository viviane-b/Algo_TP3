// Cassandre Hamel, 20210863
// Viviane Binet, 20244728
#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm> 
#include <queue>
using namespace std;

vector<vector<int>> getTheNorthFace(const string filePath);
int ClimbingDP(const vector<vector<int>>& wall);

vector<vector<int>> getTheNorthFace(const string filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Error with file: " << filePath << std::endl;
        return {};
    }

    vector<vector<int>> crag;
    string difficultyIndex;
    //https://stackoverflow.com/questions/37957080/can-i-use-2-or-more-delimiters-in-c-function-getline
    while (getline(file, difficultyIndex)) {
        vector<int> row;
        stringstream ss(difficultyIndex);
        while (getline(ss, difficultyIndex, ',')) {
            row.push_back(stoi(difficultyIndex));
        }
        crag.push_back(row);
    }

    file.close();
    return crag;
}

ClimbingDifficultyCalculator::ClimbingDifficultyCalculator() {}

int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(const std::string filename) {
   
    vector<vector<int>> wall = getTheNorthFace(filename);
    int minPathSum = -1;
    if(wall.size() != 0){
        minPathSum = ClimbingDP(wall);
    }else{
        cout<< "Error, file is empty" << endl;
    }
    
    return minPathSum;
}

int ClimbingDP(const std::vector<std::vector<int>>& wall) {
    int rows = wall.size(), cols = wall[0].size();
    vector<vector<int>> dp(rows, vector<int>(cols, 1e9));

    // Init bottom row 
    for (int j = 0; j < cols; ++j) {
        dp[rows - 1][j] = wall[rows - 1][j];
    }

    // Fill the DP table from bottom to top
    for (int i = rows - 2; i >= 0; --i) {
        for (int j = 0; j < cols; ++j) {
            // Difficulty of going up
            dp[i][j] = wall[i][j] + dp[i + 1][j];
            // Left (if within bounds) get min between current and left
            if (j > 0){
                dp[i][j] = min(dp[i][j], wall[i][j] + dp[i][j - 1]); //check if less than up
            }
            // Right (if within bounds) get min between current and right
            if (j < cols - 1){
                dp[i][j] = min(dp[i][j], wall[i][j] + dp[i][j + 1]); //check if less than up
            }
        }
        // Check the min difficulty continuing left ->
        for (int j = 1; j < cols; ++j) {
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + wall[i][j]);
        }
        // Check the min difficulty continuing right <-
        for (int j = cols - 2; j >= 0; --j) {
            dp[i][j] = min(dp[i][j], dp[i][j + 1] + wall[i][j]);
        }
    }

    // Find the minimum difficulty from the top row
    int minDifficulty = dp[0][0];
    for (int j = 1; j < cols; ++j) {
        minDifficulty = min(minDifficulty, dp[0][j]);
    }

    return minDifficulty;
}