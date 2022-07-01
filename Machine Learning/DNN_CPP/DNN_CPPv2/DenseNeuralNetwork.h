#ifndef DENSE_NEURAL_NETWORK_H
#define DENSE_NEURAL_NETWORK_H
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>
using std::vector, std::string;


class DenseNeuralNetwork{
    
    double** delta; //for updating //NEED TO COPY IN copy() and DEALLOCATE IN clear()

    string loss;
    
    double*** weights; 
    double** nodes;
    double* biases;

    

    size_t layerTotal;
    size_t nodeTotal;
    size_t weightTotal;
    vector<size_t> nodePerLayer;

    vector<string> activationPerLayer;

    

    void computeLayer(size_t layer, string activation);

    void copy(const DenseNeuralNetwork& dnn);

    void clear();


    public:


    //Constructor
    DenseNeuralNetwork(string loss, vector<size_t> numOfNodes, vector<string> activationPerLayer);

    //Copy Constructor
    DenseNeuralNetwork(const DenseNeuralNetwork& dnn):delta(),loss(), weights(), nodes(), biases(),layerTotal(), nodeTotal(), weightTotal(), nodePerLayer(), activationPerLayer(){
        copy(dnn);
    }

    //Destructor
    ~DenseNeuralNetwork(){
        clear();
    }

    //Copy Assignment Operator
    DenseNeuralNetwork& operator=(const DenseNeuralNetwork& rhs){
        if (&rhs != this)
            copy(rhs);
        return *this;
    }


    //Load weights and Biases
    void loadModel(vector<double> weights, vector<double> biases);

    //Update weights
    void update(double learning_rate, vector<double> expected);

    //Train model
    void train(vector<vector<double>> data, vector<vector<double>> expected, size_t epochs, double learning_rate, bool (*isAccurate)(vector<double>, vector<double>), bool verbose);

    //Test multiple inputs (not training data and will not perform back prop)
    void test(vector<vector<double>> data, vector<vector<double>> expected, bool (*isAccurate)(vector<double>, vector<double>));

    //Predict value based on current weights
    vector<double> predict(vector<double> input);



    //Activation functions
    long double static relu(double val){
        if (val == 0) throw "ERROR: ReLU(0) is undefined";
        return (val < 0)? 0 : val;
    }
    long double static logistic(double val){
        return 1.0 / (1.0+exp(-1*val));
    }

    long double static tanh(double val){
        return (1-exp(-2*val))/(1+exp(-2*val));
    }

    long double static linear(double val){
        return val;
    }

    void static softmax(double* layer, size_t size){
        double denom = 0;

        for (size_t i = 0; i < size; i++){
            denom += exp(layer[i]);
        }

        for(size_t i = 0; i < size; i++){
            layer[i] = exp(layer[i])/denom; 
        }
        
    }

    //isAccurate Functions to use

    //for softmax
    bool static maxIndx(vector<double> predicted, vector<double> actual){
        size_t indxPred = 0;
        double valPred = predicted.at(0);
        for (size_t i = 0; i < predicted.size(); i++){
            if (predicted.at(i) > valPred){
                indxPred = i;
                valPred = predicted.at(i);
            }

        }

        size_t indxAct = 0;
        double valAct = actual.at(0);
        for (size_t i = 0; i < actual.size(); i++){
            if (actual.at(i) > valAct){
                indxAct = i;
                valAct = actual.at(i);
            }

        }
        return (indxPred == indxAct);
    }
    
    //closer to 1 or 0 (for logisitic and one output node)
    bool static zeroOrOne(vector<double> predicted, vector<double> actual){
        if (actual.at(0) == 1 && predicted.at(0) >= 0.5) return true;
        if (actual.at(0) == 0 && predicted.at(0) < 0.5) return true;
        return false;
    }




    //prints weights and biases and other general info
    void info(bool explain);

    void printNodes();

    //getters
    size_t getLayerTotal() const{ return layerTotal;}
    size_t  getNodeTotal() const { return nodeTotal;}
    size_t  getWeightTotal() const{ return weightTotal;}
    string getLossFunction() const { return loss;} 

    double getWeight(size_t i, size_t j, size_t k) const{
        if (i >= getNodePerLayer().size()-1 || j >= getNodePerLayer().at(i+1) || k >= getNodePerLayer().at(i))
            throw std::out_of_range("ERROR: Weight does not exist at this index.");
        return weights[i][j][k];
    }
    double getBias(size_t i) const{
        if (i >= getNodePerLayer().size()-1)
            throw std::out_of_range("ERROR: Bias does not exist at this index.");
        return biases[i];
    }
    vector<size_t> getNodePerLayer() const {return nodePerLayer;}

    vector<string> getActivations() const {return activationPerLayer;}





};

#endif
