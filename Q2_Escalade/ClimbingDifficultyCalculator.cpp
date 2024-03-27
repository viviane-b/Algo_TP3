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
int dijkstraClimbing(const vector<vector<int>>& wall);

struct Node { // Node for djikstra
    int row, col, difficulty;
    Node(int x, int y, int d) {
        row = x;
        col = y;
        difficulty = d;
    }
};

//https://www.geeksforgeeks.org/custom-comparator-in-priority_queue-in-cpp-stl/
struct CompareNodes { // min heap on difficulty (least diff 1st)
    bool operator()(const Node& a, const Node& b) { // overload >
        return a.difficulty > b.difficulty;
    }
};


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
        minPathSum = dijkstraClimbing(wall);
    }else{
        cout<< "Error, file is empty" << endl;
    }
    
    return minPathSum;
}

// Simplified Dijkstra
int dijkstraClimbing(const std::vector<std::vector<int>>& wall) {
    int rows = wall.size(), cols = wall[0].size(); // get rows + col sizes
    vector<vector<int>> minDiff(rows, vector<int>(cols, 1e9)); //min difficulty vector init w/ big number
    priority_queue<Node, vector<Node>, CompareNodes> pq; //priority queue (min difficulty)

    // Init pq w/ 1st row
    for (int j = 0; j < cols; ++j) {
        minDiff[rows - 1][j] = wall[rows - 1][j];
        pq.emplace(rows - 1, j, wall[rows - 1][j]); //emplace directly constructs :https://en.cppreference.com/w/cpp/container/priority_queue/emplace
    }

    // Dijkstra's algorithm
    while (!pq.empty()) {
        Node node = pq.top(); //Set node as ref top
        pq.pop(); //pop top off

        if (node.row == 0) { // Reached the top of the wall!
            return node.difficulty;
        }

        // Check up, left, and right
        vector<pair<int, int>> directions{{-1, 0}, {0, -1}, {0, 1}};// up, left, right use pair to seperate into row, col mapping
        for (pair<int, int> dir : directions) {
            int newRow = node.row + dir.first;
            int newCol = node.col + dir.second;
            if (newRow >= 0 && newCol >= 0 && newRow < rows && newCol < cols) {
                int newDiff = node.difficulty + wall[newRow][newCol];
                if (newDiff < minDiff[newRow][newCol]) { //new diff less than past? set
                    minDiff[newRow][newCol] = newDiff;
                    pq.emplace(newRow, newCol, newDiff);
                }
            }
        }
    }

    // Error
    return -1;
}
