#include <iostream>
#include <vector>
#include <string>
#include "DenseNeuralNetwork.h"

using std::vector, std::cout, std::endl;

//Returns true if predicted data is within 0.1 units of expected data  (NOT TRULY INDICATIVE OF ACCURACY)
bool withinMargin(vector<double> data, vector<double> expect){
    return ((data.at(0) - expect.at(0) <= 0.1 && data.at(0) - expect.at(0) >= -0.1) || (expect.at(0) -  data.at(0) <= 0.1 && expect.at(0) -  data.at(0) >= -0.1));
}


int main(){
    const size_t SIZE = 1000;
    const size_t decimalsplace = 2000000;


    vector<vector<double>> train_feature = {};
    vector<vector<double>> train_label = {};

    vector<vector<double>> test_feature = {};
    vector<vector<double>> test_label = {};


    for(size_t i = 0; i < SIZE; i++){
        double noise = (rand()%100)/50 -1; //-1 to +1 noise
        //generate number btwn -10 and 10
        double num1 = (double) (rand()%(decimalsplace))/(100000) - 10; 
        double num2 = (double) (rand()%(decimalsplace))/(100000) - 10;
        vector<double> feat = {num1, num2}; 
        double result = 2*num1 - 3*num2 + noise; //linear relationship should be close to y = 2a - 3b
        vector<double> label = {result}; 


        train_feature.push_back(feat);

        train_label.push_back(label);            
    }

    //smae thing but for testing data
    for(size_t i = 0; i < SIZE/10; i++){
        double noise = (rand()%100)/100;
        double num1 = (double) (rand()%(decimalsplace))/(100000) - 10;
        double num2 = (double) (rand()%(decimalsplace))/(100000) - 10;
        vector<double> feat = {num1, num2}; 
        double result = 2*num1 - 3*num2 + noise;
        vector<double> label = {result}; 


        test_feature.push_back(feat);

        test_label.push_back(label);            
    }

    //architecture 
    vector<string> activation = {"linear"};
    vector<size_t> layer = {2,1};
    DenseNeuralNetwork dnn("mean squared error", layer, activation);


    dnn.info(false); //print weights before training
    dnn.train(train_feature, train_label, 10, 0.01, withinMargin,true);
    dnn.info(false); //print weights after training (should be close to 2 and -3)

    dnn.test(test_feature, test_label, withinMargin);

    //Within .1 is not an appropriate metric of accuracy
    //Develop coefficent of determination
    double sst = 0; //sum of squares total
    double sse = 0; //sum of squares error
    double avg = 0;
    for (size_t i = 0; i < test_feature.size(); i++){
        double val = dnn.predict(test_feature.at(i)).at(0);
        sse += (val - test_label.at(i).at(0))*(val - test_label.at(i).at(0));
        avg += val;
    }
    avg*=avg;
    avg /= test_feature.size();


    for (size_t i = 0; i < test_feature.size(); i++){
        double val = dnn.predict(test_feature.at(i)).at(0);
        sst += (val*val);
    }
    sst -= avg;

    cout << "\n\n A \"within x margin\" is not the best metric of accuracy. A Coefficent of Determination will show the proportion of the variation of the output explained by the linear relationship with the input. \n";
    cout << "SSE: " << sse << "\t SST: " << sst << "\n";
    cout << "Coefficent of Determination (r^2): " << 1-(sse/sst) << endl;



    
        





}