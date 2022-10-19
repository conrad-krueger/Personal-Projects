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
    
    
    int x1 = rand()%(dimension-5 + 1);

    int y1 = rand()%(dimension-5 + 1);


    int x2 = rand()%(dimension-5 + 1);
    int y2 = rand()%(dimension-5 + 1);
    if (x1 == x2){
        if (x1 == 0)
            x1+=4;
        else if (x1 == dimension-1)
            x1-=4;

    }
    if (y1 == y2){
        if (y1 == 0)
            y1+=4;
        else if (y1 == dimension-1)
            y1-=4;
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

    int x1 = rand()%(dimension-5);
    int y1 = rand()%(dimension-5);

     int remain = std::min(dimension-x1,dimension-y1);

     int randRemain;
    if (remain == 6)
        randRemain = rand() % (remain - 7) + 5;
    else
        randRemain = rand() % (remain - 6) + 5;
    
   

     for (int more = 0; more <= randRemain; more++){
         grid[x1+more][y1+more] = 1;
         grid[x1+randRemain - more][y1+ more] = 1;

     }

     return grid;
    
}


/**
 * Generates a randomly sized Right Triangle on a grid
 * @param dimension dimension of grid
 * @return vector of a vector of doubles that contains the coordinates of a square
 */
vector<vector<double>> generateTriangle(int dimension){
    vector<vector<double>> grid(dimension);
    for (int i = 0; i < dimension; i++){
        vector<double> row(dimension,0);
        grid.at(i) = row;
    }

    int x1 = rand()%(dimension-5);
    int y1 = rand()%(dimension-5);

    int remain = std::min(dimension-x1,dimension-y1);

    int randRemain;
    if (remain == 6)
        randRemain = rand() % (remain - 7) + 5;
    else
        randRemain = rand() % (remain - 6) + 5;

     for (int more = 0; more <= randRemain; more++){
         grid[x1+more][y1+more] = 1;
         grid[x1+more][y1] = 1;
         grid[x1+randRemain][y1+more] = 1;
         
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

    size_t numOfShapes = 2500; //number of shapes
    size_t numOfTest = 1000; //number of shapes in testing vector

    for (size_t i = 0; i < numOfShapes; i++){
        
        int choose = rand()%2;
        vector<double> label = {1};
        if (choose == 1){ //Square
            vector<vector<double>> sq = generateSquare(DIM);
            training_data.push_back(flatten(sq));
        }else if (choose == 0){ // X
            vector<vector<double>> xs = generateX(DIM);
            training_data.push_back(flatten(xs));
            label = {0};
        }else{
            vector<vector<double>> tri = generateTriangle(DIM);
            training_data.push_back(flatten(tri));
            label = {0,0,1};
        }
        training_label.push_back(label);

    }

    for (size_t i = 0; i < numOfTest; i++){
        
        int choose = rand()%2;

        vector<double> label = {1};
        if (choose == 1){ //Square
            vector<vector<double>> sq = generateSquare(DIM);
            testing_data.push_back(flatten(sq));
        }else if (choose == 0){ // X
            vector<vector<double>> xs = generateX(DIM);
            testing_data.push_back(flatten(xs));
            label = {0};
        }else{
            vector<vector<double>> tri = generateTriangle(DIM);
            testing_data.push_back(flatten(tri));
            label = {0,0,1};
        }
        
        testing_label.push_back(label);

    }

    //number of nodes in each DNN layer
    vector<size_t> layers4 = {DIM*DIM,DIM*DIM/4,100,1};
    vector<string> active = {"logistic","logistic","logistic"};

    

    try{
        DenseNeuralNetwork dnn("cross_entropy",layers4, active);
        
        dnn.train(training_data, training_label, 50 , 0.01, 32, dnn.zeroOrOne, true, true); //training data with learning rate of 0.01 on 35 epochs
        cout << endl;

        dnn.save("model5.txt");
        

        //visually see some of the predictions
        /*for (int i = 0; i < 5; i++){
            vector<vector<double>> shape = generateSquare(DIM);
            cout << "SQUARE [1 0 0]: " << endl;
            print(shape);
            vector<double> res = dnn.predict(flatten(shape));
            cout << "PREDICTS: " << res.at(0) << " " << res.at(1) << " " << res.at(2) << endl;
            
            shape = generateX(DIM);
            cout << "X [0 1 0]: " << endl;
            print(shape);
            res = dnn.predict(flatten(shape));
            cout << "PREDICTS: " << res.at(0) << " " << res.at(1) << " " << res.at(2) << endl;

            shape = generateTriangle(DIM);
            cout << "Triangle [0 0 1]: " << endl;
            print(shape);
            res = dnn.predict(flatten(shape));
            cout << "PREDICTS: " << res.at(0) << " " << res.at(1) << " " << res.at(2) << endl;
        }*/

        dnn.test(testing_data, testing_label, dnn.zeroOrOne);
        cout << endl;
        

    }catch(const char*& err){ //Most errors in the DNN are thrown as array of chars 
        cout << err << endl;
    }catch(const std::exception& excpt){ 
        cout << excpt.what() << endl;
    }catch(const string& excpt){ 
        cout << excpt << endl;
    }

    return 0;
}


