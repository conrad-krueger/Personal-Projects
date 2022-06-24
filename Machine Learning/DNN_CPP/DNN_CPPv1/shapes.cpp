#include "DenseNeuralNetwork.h"
#include <time.h>
#include <iostream>
#include <string>
using std::cout, std::endl, std::string;

/**
 * Prints a shape
 * @param vect a shape to be printed out
 * @return None
 */
void print(vector<vector<double>> vect){
    cout << "====================="<<endl;
    for (vector<double> row : vect){
         for (double entry : row){
             if (entry == 1)
                cout << 'O';
            else
                cout << ' ';
        }
        cout << endl;
    }
    cout << "====================="<<endl;
}

/**
 * Generates a randomly sized square on a grid
 * @param dimension dimension of grid
 * @return vector of a vector of doubles that contains the coordinates of a square
 */
vector<vector<double>> generateSquare(int dimension){
    vector<vector<double>> grid(dimension);
    for (int i = 0; i < dimension; i++){
        vector<double> row(dimension,0);
        grid.at(i) = row;
    }
    
    
    int x1 = rand() % dimension;

    int y1 = rand()%dimension;


    int x2 = rand()%dimension;
    int y2 = rand()%dimension;
    if (x1 == x2){
        if (x1 == 0)
            x1++;
        else if (x1 == dimension-1)
            x1--;

    }
    if (y1 == y2){
        if (y1 == 0)
            y1++;
        else if (y1 == dimension-1)
            y1--;
    }

    if (x2 < x1){
        for (int i = x2; i <= x1; i++){
            grid[i][y1] = 1;
            grid[i][y2] = 1;
        }
    }else{
        for (int i = x1; i <= x2; i++){
            grid[i][y1] = 1;
            grid[i][y2] = 1;
        }

    }

    if (y2 < y1){
        for (int i = y2; i <= y1; i++){
            grid[x1][i] = 1;
            grid[x2][i] = 1;
        }
    }else{
        for (int i = y1; i <= y2; i++){
            grid[x1][i] = 1;
            grid[x2][i] = 1;
        }

    }
    return grid;



    
}

/**
 * Generates a randomly sized X on a grid
 * @param dimension dimension of grid
 * @return vector of a vector of doubles that contains the coordinates of a square
 */
vector<vector<double>> generateX(int dimension){
    vector<vector<double>> grid(dimension);
    for (int i = 0; i < dimension; i++){
        vector<double> row(dimension,0);
        grid.at(i) = row;
    }

     int x1 = rand() % dimension;
     int y1 = rand()%dimension;

     int remain = std::min(dimension-x1,dimension-y1);

     int randRemain = rand()%remain;

     for (int more = 0; more <= randRemain; more++){
         grid[x1+more][y1+more] = 1;
         grid[x1+randRemain - more][y1+ more] = 1;

     }

     return grid;
    
}

/**
 * Flattens a vector of a vector of doubles to a vector of doubles (useful for passing it as the input node for the DNN)
 * @param vect a shape
 * @return vector of doubles that represent the shape as 1 dimensional
 */
vector<double> flatten(vector<vector<double>> vect){
    vector<double> flat(vect.size() * vect.size());
    int i = 0;
    for (vector<double> row : vect){
         for (double entry : row){
             flat.at(i) = entry;
             i++;
        }
    }
    return flat;
}


int main(){
    
    const int DIM = 50;
    srand(time(NULL)); //generate different random shapes every execution

    //vectors of training and testing data
    vector<vector<double>> training_data = {};
    vector<vector<double>> training_label = {};
    vector<vector<double>> testing_data = {};
    vector<vector<double>> testing_label = {};

    size_t numOfShapes = 2000; //number of shapes
    size_t numOfTest = 500; //number of shapes in testing vector

    for (size_t i = 0; i < numOfShapes; i++){
        
        int choose = rand()%2;
        vector<double> label = {1};
        if (choose == 1){ //Square
            vector<vector<double>> sq = generateSquare(DIM);
            training_data.push_back(flatten(sq));
        }else{ // X
            vector<vector<double>> xs = generateX(DIM);
            training_data.push_back(flatten(xs));
            label = {0};
        }
        training_label.push_back(label);

    }

    for (size_t i = 0; i < numOfTest; i++){
        
        int choose = rand()%2;

        vector<double> label = {1};
        if (choose == 1){ //Square
            vector<vector<double>> sq = generateSquare(DIM);
            testing_data.push_back(flatten(sq));
        }else{ // X
            vector<vector<double>> xs = generateX(DIM);
            testing_data.push_back(flatten(xs));
            label = {0};
        }
        
        testing_label.push_back(label);

    }

    //number of nodes in each DNN layer
    vector<size_t> layers4 = {DIM*DIM, DIM*DIM/4, 100, 10, 1};

    

    try{
        DenseNeuralNetwork dnn(layers4);
        
        dnn.train(training_data, training_label, 12, 0.01, true); //training data with learning rate of 0.01 on 12 epochs
        cout << endl;

        dnn.test(testing_data, testing_label);
        cout << endl;

        //visually see some of the predictions
        for (int i = 0; i < 5; i++){
            vector<vector<double>> shape = generateSquare(DIM);
            cout << "SQUARE: " << endl;
            print(shape);
            cout << "PREDICTS: " << dnn.predict(flatten(shape)).at(0) << "   (closer to 1 = square, closer to 0 = X)" << endl;
            
            shape = generateX(DIM);
            cout << "X: " << endl;
            print(shape);
            cout << "PREDICTS: " << dnn.predict(flatten(shape)).at(0) << "   (closer to 1 = square, closer to 0 = X)" << endl;

        }
        

    }catch(const char*& err){ //Most errors in the DNN are thrown as array of chars 
        cout << err << endl;
    }catch(const std::exception& excpt){ 
        cout << excpt.what() << endl;
    }

    return 0;
}


