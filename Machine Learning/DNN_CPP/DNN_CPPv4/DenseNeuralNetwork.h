#ifndef DENSE_NEURAL_NETWORK_H
#define DENSE_NEURAL_NETWORK_H
#include <string>
#include <vector>
#include <stdexcept>
#include <cmath>
using std::vector, std::string;


class DenseNeuralNetwork{
    
    double** delta; 

    string loss;

    

    
    double*** weights; 
    double** nodes;
    double* biases;

    
    size_t layerTotal;
    size_t nodeTotal;
    size_t weightTotal;
    vector<size_t> nodePerLayer;

    vector<string> activationPerLayer;

    long double (*L)(double,double);
    long double (*D_L)(double,double);

    vector<long double(*)(double)> activation;
    vector<long double(*)(double)> activationDerivatives;

    void copy(const DenseNeuralNetwork& dnn);

    void clear();

    void computeLayer(double** nodes, size_t layer);

    void calcNode(double** nodes, size_t j, size_t layer);
    void calcDelta(double** delta, size_t i, size_t j, double*** weightsDelta, double* biasesDelta, double** nodes);


    void updateAcc(double** nodes, double*** weightsDelta, double* biasesDelta, vector<double> expected);

    void changeWB(double*** weightsDelta, double* biasesDelta, double lr, size_t batch_size);

    void trainOne(const vector<double>& data, const vector<double>& expected, double** nodes, double** delta, double*** weightsDelta, double* biasesDelta, bool (*isAccurate)(vector<double>, vector<double>), double* lossNum, int* acc);
    void trainMore(const vector<double>& data1, const vector<double>& data2, const vector<double>& expected1, const vector<double>& expected2, int indx, double*** nodes, double*** delta, double*** weightsDelta, double* biasesDelta, bool (*isAccurate)(vector<double>, vector<double>), double* lossNum, int* acc){
        trainOne(data1, expected1, nodes[indx], delta[indx], weightsDelta, biasesDelta, isAccurate, lossNum, acc);
        trainOne(data2, expected2, nodes[indx], delta[indx], weightsDelta, biasesDelta, isAccurate, lossNum, acc);
        //trainOne(data3, expected3, nodes[indx], delta[indx], weightsDelta, biasesDelta, isAccurate, lossNum, acc);
        //trainOne(data4, expected4, nodes[indx], delta[indx], weightsDelta, biasesDelta, isAccurate, lossNum, acc);
    }

    public:

    


    //Constructor
    DenseNeuralNetwork(string loss, vector<size_t> numOfNodes, vector<string> activationPerLayer);

    DenseNeuralNetwork(string filename): delta(), loss(), weights(), nodes(), biases(),layerTotal(), nodeTotal(), weightTotal(), nodePerLayer(), activationPerLayer(), L(), D_L(), activation(), activationDerivatives(){
        load(filename);
    }


    //Copy Constructor
    DenseNeuralNetwork(const DenseNeuralNetwork& dnn):delta(), loss(), weights(), nodes(), biases(),layerTotal(), nodeTotal(), weightTotal(), nodePerLayer(), activationPerLayer(), L(), D_L(), activation(), activationDerivatives(){
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

    //Load Model from txt file
    void load(string filename);

    //Save Model to txt file
    void save(string filename);

    //Load weights and Biases
    void loadWB(vector<double> weights, vector<double> biases);

    //Update weights
    void update(double learning_rate, vector<double> expected);

    //Train model
    void train(vector<vector<double>> data, vector<vector<double>> expected, size_t epochs, double learning_rate,size_t batch_size, bool (*isAccurate)(vector<double>, vector<double>), bool shuffle, bool verbose);

    //Test multiple inputs (not training data and will not perform back prop)
    void test(vector<vector<double>> data, vector<vector<double>> expected, bool (*isAccurate)(vector<double>, vector<double>));

    //Predict value based on current weights
    vector<double> predict(double** nodes, vector<double> input);



    //Loss functions and derivatives 
    //Mean Squared Error
    long double static mse(double output, double expected){return (output-expected)*(output-expected);}
    long double static Dmse(double output, double expected){return 2*(output-expected);}

    //Cross Entropy
    long double static cross_entropy(double output, double expected){return -1*expected*log2(output);}
    long double static Dcross_entropy(double output, double expected){return -1*(expected/output) + (1-expected)/(1-output);}



    //Activation functions and derivatives 
    long double static relu(double val){ if (val == 0) throw "ERROR: ReLU(0) is undefined";   return (val < 0)? 0 : val;}
    long double static Drelu(double val){return (val < 0) ? 0 : 1;}

    long double static logistic(double val){ return 1.0 / (1.0+exp(-1*val));}
    long double static Dlogistic(double val){ return val*(1-val);}

    long double static tanh(double val){return (1-exp(-2*val))/(1+exp(-2*val));}
    long double static Dtanh(double val){ return 1-(val*val);}

    long double static linear(double val){return val;}
    long double static Dlinear(double val){return 1;}

    void static softmax(double* layer, size_t size){
        double denom = 0;
        for (size_t i = 0; i < size; i++) denom += exp(layer[i]);
        for(size_t i = 0; i < size; i++) layer[i] = exp(layer[i])/denom; 
    }
    long double static Dsoftmax(double val){ return val*(1-val);}

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
    void info();

    void printNodes();

    //getters
    size_t getLayerTotal() const{ return layerTotal;}
    size_t  getNodeTotal() const { return nodeTotal;}
    size_t  getWeightTotal() const{ return weightTotal;}
    string getLossFunction() const { return loss;} 
    double getWeight(size_t i, size_t j, size_t k) const{
        if (i >= getNodePerLayer().size()-1 || j >= getNodePerLayer().at(i+1) || k >= getNodePerLayer().at(i)) throw std::out_of_range("ERROR: Weight does not exist at this index.");
        return weights[i][j][k];
    }
    double getBias(size_t i) const{
        if (i >= getNodePerLayer().size()-1) throw std::out_of_range("ERROR: Bias does not exist at this index.");
        return biases[i];
    }
    vector<size_t> getNodePerLayer() const {return nodePerLayer;}

    vector<long double(*)(double)> getActivations() const {return activation;}
    vector<long double(*)(double)> getActivationsDerivatives() const {return activationDerivatives;}
    vector<string> getActivationStr() const {return activationPerLayer;}





};

#endif
