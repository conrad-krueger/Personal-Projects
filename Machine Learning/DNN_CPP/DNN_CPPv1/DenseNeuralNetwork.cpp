#include "DenseNeuralNetwork.h"
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using std::cout , std::endl, std::string, std::vector;


/**
 * Constructor that creates the Dense Neural Network Architecture
 * @param numOfNodes vector of integers that describe how many nodes are in each layer (index 0 describes how many nodes in first layer)
 * @update weights, bias, nodes, weightTotal, nodeTotal, layerTotal, numOfNodes
 */
DenseNeuralNetwork::DenseNeuralNetwork(vector<size_t> numOfNodes):  weights(), nodes(), biases(),layerTotal(numOfNodes.size()), nodeTotal(), weightTotal(), nodePerLayer(numOfNodes), activationPerLayer() {

    if (numOfNodes.size() < 2){
        throw "ERROR: Dense Neural Network should contain atleast 2 layers";
    }

    srand(time(NULL));


    //weights[connected section index][number of node in next layer][number of node in prev layer]

    weights = new double**[numOfNodes.size()-1]; //has n-1 connecting sections
    for (size_t i = 0; i < numOfNodes.size()-1; i++){

        weights[i] = new double*[numOfNodes.at(i+1)];

        for (size_t j = 0; j < numOfNodes[i+1]; j++){
            
            //init all to 1
            weights[i][j] = new double[numOfNodes[i]];
            for (size_t k = 0; k < numOfNodes[i]; k++){
                weights[i][j][k] = -1/sqrt(numOfNodes[i+1]) + ((double)rand() / RAND_MAX) * (1/sqrt(numOfNodes[i+1])*2);
                //to prevent oversaturation in the beginning I set each of the weights to have a value in the range of 0 +/- 1/sqrt(number of nodes in receiving layer)
                //cout << weights[i][j][k] << endl;
                weightTotal++;
            }
        }
    }

    //init nodes && activation functions for each layer (default is ReLU and last is logistic)
    nodes = new double*[numOfNodes.size()];

    for (size_t i = 0; i < numOfNodes.size(); i++){
        nodes[i] = new double[numOfNodes[i]]{};
        nodeTotal += numOfNodes[i];
    }

    
        
    //init biases (all to 0)
    biases = new double[numOfNodes.size()-1]{};
    for (size_t i = 0; i < numOfNodes.size()-1; i++){
        biases[i] = 0;

        activationPerLayer.push_back("logistic");
    }


}


/**
 * Copies another DenseNeuralNetwork object's weights and biases into this object
 * @param dnn DenseNeuralNetwork object to be copied
 * @return None
 */
void DenseNeuralNetwork::copy(const DenseNeuralNetwork& dnn){
    clear();

    //weights[connected section index][number of node in next layer][number of node in prev layer]

    weights = new double**[dnn.getNodePerLayer().size()-1]; //has n-1 connecting sections
    for (size_t i = 0; i < dnn.getNodePerLayer().size()-1; i++){

        weights[i] = new double*[dnn.getNodePerLayer().at(i+1)];

        for (size_t j = 0; j < dnn.getNodePerLayer().at(i+1); j++){
            
            weights[i][j] = new double[dnn.getNodePerLayer().at(i)];
            for (size_t k = 0; k < dnn.getNodePerLayer().at(i); k++){
                weights[i][j][k] = dnn.getWeight(i,j,k);
                
            }
        }
    }
    weightTotal = dnn.getWeightTotal();


    //init nodes && activation functions for each layer (default is ReLU and last is logistic)
    nodes = new double*[dnn.getNodePerLayer().size()];

    for (size_t i = 0; i < dnn.getNodePerLayer().size(); i++){
        nodes[i] = new double[dnn.getNodePerLayer().at(i)]{}; //no need to copy nodes values, will change based on input
    }
    nodeTotal = dnn.getNodeTotal();

     
    //init biases (all to 0)
    biases = new double[dnn.getNodePerLayer().size()-1]{};
    for (size_t i = 0; i < dnn.getNodePerLayer().size()-1; i++){
        biases[i] = dnn.getBias(i);
    }


    layerTotal = dnn.getNodePerLayer().size();
    nodePerLayer = dnn.getNodePerLayer();

    activationPerLayer = dnn.getActivations();

}


/**
 * Clear the contents on this DenseNeuralNetwork object (deallocate all malloc memory)
 * @update nodes, weights, biases, nodes, layerTotal, nodeTotal, weightTotal, nodePerLayer, activationPerLayer
 * @return None
 */
void DenseNeuralNetwork::clear(){

    //deallocate weight matricies
    if (weights){

        for (size_t i = 0; i < layerTotal-1; i++){
            for (size_t j = 0; j < nodePerLayer.at(i+1); j++){
                delete[] weights[i][j];
            }
            delete[] weights[i];
        }
        delete[] weights;

        weights = nullptr;
        weightTotal = 0;

    }
    

    //deallocate node matricies
    if (nodes){
        for(size_t i = 0; i < layerTotal; i++){
            delete[] nodes[i];
        }
        delete[] nodes;
        nodes = nullptr;
        nodeTotal = 0;
    }
    


    //deallocate bias array
    if (biases){
        delete[] biases;
        biases = nullptr;
    }
    


    layerTotal = 0;

    nodePerLayer = {};

    activationPerLayer = {};


}



/**
 * Prints out the values of every node
 * @return None
 */
void DenseNeuralNetwork::printNodes(){
     for (size_t i = 0; i < layerTotal; i++){
        for (size_t j = 0; j < nodePerLayer.at(i); j++){
             cout << nodes[i][j] << " ";
        }
        cout << endl;
     }
}

/**
 * Prints out information about the DNN Architecture, including the weight matricies, the biases, number of layers.
 * @param explain boolean value that explains how to read weight matricies
 * @return None
 */
void DenseNeuralNetwork::info(bool explain = false){
    cout << "==========================================================" << endl;
    cout << "Dense Neural Network Information:" << endl;


    cout << "Total Layers: " << layerTotal << "\t Total Nodes: " << nodeTotal << "\t Total Weights: "<< weightTotal << "\t Total Biases:"<< layerTotal-1 << endl << endl; 
    
    if (explain) cout << "Weight Matricies are read as matrix[i][j] = weight from node j to node i"<< endl;

    for (size_t i = 0; i < layerTotal-1; i++){
        cout << "Weight Matrix from Layer " << i << " [" << nodePerLayer.at(i) << " Node(s)] --> Layer "<<  i+1 << " [" << nodePerLayer.at(i) << " Node(s)]" << endl;
        cout << "----------------------------------" << endl;

        for (size_t j = 0; j < nodePerLayer.at(i+1); j++){

            //init all to 1
            for (size_t k = 0; k < nodePerLayer.at(i); k++){
               cout << weights[i][j][k] << " ";
            }
            cout << endl;

        }
        cout << "\n+ " << biases[i+1] << " (bias at Layer "<< i+1 << ")" << endl << endl << endl; 

    }
    cout << "==========================================================" << endl <<endl;

}

/**
 * Loads DNN Architecture with custom weights and biases
 * @param weights 1D vector that contains weights for each node connection. Weights should be ordered sequentially (first layer, then second layer, etc.). Weights pointing to the same node must be local to each other in memory. NOTE: Look at EX for better understanding of locality.
 * EX: Input layers: node a, b , c; Hidden Layer: node x, y; Output Layer: node z; Weights: [A -> X, B -> X, C -> X, A -> Y, B -> Y, C -> Y, X -> Z, Y -> Z] 
 * @param biases 1D vector that contains the bias amount for each layer. Should be ordered sequentially.
 * @updates weights, biases
 * @return None
 */
void DenseNeuralNetwork::loadModel(vector<double> weights, vector<double> biases){ //sofar good
    if (biases.size() != layerTotal-1 || weights.size() != weightTotal){
        string desc = "ERROR: Incorrect amount of weights and/or biases\nNeed ";
        desc += std::to_string(layerTotal-1) + " biases (Given: " +  std::to_string(biases.size()) + ")\nNeed ";
        desc += std::to_string(weightTotal) + " weights (Given: " +  std::to_string(weights.size()) + ")";
        throw desc;
    }
    
    //load weights 
    int currLoading = 0;
    for (size_t i = 0; i < layerTotal-1; i++){
        for (size_t j = 0; j < nodePerLayer.at(i+1); j++){
            for (size_t k = 0; k < nodePerLayer.at(i); k++){
               this->weights[i][j][k] = weights.at(currLoading);
               currLoading++;
            }
        }
    }

    //load biases
    for (size_t i = 0; i < layerTotal-1; i++){
        this->biases[i] = biases.at(i);
    }

}



/**
 * Updates each of the weights in the DNN
 * @param learning_rate determines magnitude of weight change
 * @param expected 1D vector that contains the expected values in the output node
 * @updates weights
 * @return None
 * 
 * MATH: 
 * w_new = w_old - learning rate * (D_w E), where D_w E is the partial derivative of the Loss Function (E) with respect to w
 * 
 * D_w E = oi * deltaj, where oi is the previous node's value
 * 
 * deltaj = D_oj E * D_netj oj, where oj is the current node's value (the current weight w is the weight from oi to oj), 
 * and netj is the summation for the previous layers nodes multiplied by each of their corresponding weights pointing to oj
 * 
 ** D_netj oj = The partial deriviative of the activation function on the current layer (where node oj is the input) 
 * ex: If the Activation Function is Logistic, D_netj oj = oj*(1 - oj)
 * 
 * D_oj E has a recursive definition.
 * If oj is in an output layer,
 * D_oj E = The partial derivative of the loss function (which accepts oj as a node and tj, the target value for oj) wrt oj 
 * ex: If the Loss Function is Mean Squared Error, D_oj E = oj - tj
 * 
 * If oj is in an inner layer,
 * D_oj E = Sum of (weights from oj to ol in the next layer multiplied by deltal) for all ol in nodeL (if nodeL is a set of all nodes in the next layer, ol is an element of that set)
 * 
 * IMPLEMENTATION:
 * On any given iteration of the update function,
 * 
 * weights[i][j][k] = the weight from node[i][k] to node[i+1][j]
 * 
 * If nodes[i][j] is output, 
 * delta[i-1][j] = D_nodes[i][j] L(nodes[i][j], expected.at(j)) * D of activation function with input (node[i][j]), where L is the Loss function that accepts a node and its target value IF output node
 * 
 * Else, 
 * For nextNode in 0 to amount of nodes in next layer:
 *      delta[i-1][j] += (weights[i][nextNode][j] * delta[i][nextNode]) 
 * delta[i-1][j] *=  D of activation function with input (nodes[i][j])
 * 
 * weights[i][j][k] -= learning_rate * nodes[i][k] * delta[i][j]
 */

void DenseNeuralNetwork::update(double learning_rate, vector<double> expected){
    double** delta = new double*[layerTotal-1]; 

    for (size_t i = layerTotal-1; i > 0; i--){
        delta [i-1] = new double[nodePerLayer.at(i)]{};

        if (i == layerTotal-1){//base case (output layer)

            for (size_t j = 0; j < nodePerLayer.at(i); j++){ //compare each of the output nodes to their expected values * derivative of activation function
                delta[i-1][j] = -1*(expected.at(j)/nodes[i][j]) + (1-expected.at(j))/(1-nodes[i][j]); //part deriv of cross entropy //(nodes[i][j] - expected.at(j));
                

                //activation function derivatives

                if(activationPerLayer.at(i-1) == "logistic"){
                    delta[i-1][j] *= (nodes[i][j] * (1-nodes[i][j]));
                    //cout << S[i-1][j] << " " << nodes[i][j] << " " <<  1-nodes[i][j] << endl;
                }
                else if(activationPerLayer.at(i-1) == "relu"){
                    if (nodes[i][j] < 0){
                        delta[i-1][j] = 0;
                    }
                }else{
                    throw "ERROR: Must use on of the following Activation Functions: relu or logistic";
                }


            }
        }else{  //recursive
            
            for (size_t j = 0; j < nodePerLayer.at(i); j++){  
                delta[i-1][j] = 0;

                //calculate the summation of all of the weights from Node j to each of the nodes in the next layer * S of each of those nodes in the next layer ^ derivative of activation func
                for (size_t nextNode = 0; nextNode < nodePerLayer.at(i+1); nextNode++ ){
                    delta[i-1][j] += (weights[i][nextNode][j] * delta[i][nextNode]); //weights[connected section index][number of node in next layer][number of node in prev layer]
                    
                }
                

                //activation function derivatives
                if(activationPerLayer.at(i-1) == "logistic"){
                    delta[i-1][j] *= (nodes[i][j] * (1-nodes[i][j]));
                    //cout << S[i-1][j] << " " << nodes[i][j] << " " <<  1-nodes[i][j] << endl;
                }
                else if(activationPerLayer.at(i-1) == "relu"){
                    if (nodes[i][j] < 0){
                        delta[i-1][j] = 0;
                    }
                }else{
                    throw "ERROR: Must use on of the following Activation Functions: relu or logistic";
                }
                
            }


        }

    }

    //update weights
    for (size_t i = 0; i < layerTotal-1; i++){
        for (size_t j = 0; j < nodePerLayer.at(i+1); j++){
            for (size_t k = 0; k < nodePerLayer.at(i); k++){
               weights[i][j][k] -= (learning_rate* nodes[i][k]*delta[i][j]);
               //cout << "MOD: " << (S[i][j]) << endl;
            }

        }
    }

    //deallocate memory
    for (size_t i = 0; i < layerTotal-1; i++){
        delete[] delta[i];
    }
    delete[] delta;
    

}



/**
 * Computes the values of a single layer of the DNN based on the current weights and biases and on the values of the previous layers nodes
 * @param layer represents which layer is being computed (will use the previous layer (layer-1() in computation)
 * @param activation activation function used on that current layer
 * @updates nodes[layer]
 * @return None
 */
void DenseNeuralNetwork::computeLayer(size_t layer, long double (*activation)(double)){ //sofar good
    if (layer >= layerTotal)
        throw std::out_of_range("ERROR: Attempted to compute the value of the input layer or a non-exsitent layer");
    
    for (size_t j = 0; j < nodePerLayer.at(layer); j++){
        double sum = 0;

        //computation formula is node[layer][j] = Activation(Sigma prev=0 to n (node[layer-1][prev] * weight from prev to j) + bias)
        for (size_t prev = 0; prev < nodePerLayer.at(layer-1); prev++){
            sum += nodes[layer-1][prev] * weights[layer-1][j][prev]; 
        }
        nodes[layer][j] = (*activation)(sum + biases[layer-1]);
    }
}

/**
 * Trains Neural Network by updating weights based on user given labels and features
 * @param data training input feature data
 * @param expected training input label data
 * @param activations vector of strings that contain the same of the activation function used on the corresponding inner/outer layers of the DNN
 * @param epochs number of times the DNN will view the same dataset
 * @param learning_rate determines magnitude of weight change
 * @param verbose boolean to depict current progress of training
 * @updates weights, nodes
 * @return None
 */
void DenseNeuralNetwork::train(vector<vector<double>> data, vector<vector<double>> expected, size_t epochs, double learning_rate = 0.0001, bool verbose = true){
    if (data.size() != expected.size())
        throw "ERROR: Dimensions of training dataset does not match number of labels";
    

    for (size_t iterations = 0; iterations < epochs; iterations++){
        int i = 0;
        int acc = 0;
        double loss = 0;
        if (verbose){
            cout << "EPOCH " << iterations+1 << ": Training... " <<endl;
            //info();
        }
        for (vector<double> datapoints: data){
            if (datapoints.size() != nodePerLayer.at(0))
                throw "ERROR: Dimensions of training dataset does not match number of input nodes";
            
            
            vector<double> pred = predict(datapoints);

            update(learning_rate, expected.at(i));
            

            //only makes sense if one output layer and using cross entropy function
            if (verbose){
                if (pred.at(0) - 0.5 < 0 && expected.at(i).at(0) == 0)
                    acc++;
                else if (pred.at(0) - 0.5 >= 0 && expected.at(i).at(0) == 1)
                    acc++;
                
                loss += expected.at(i).at(0)*log2(pred.at(0)) + (1-expected.at(i).at(0))* log2(1-pred.at(0));

            }
            i++;
        }

        if (verbose){
            cout << "DONE. Accuracy: " << (double) acc / data.size() << " Loss: " << -1* loss / data.size() << endl;
        }
        
    }
}

/**
 * Tests Neural Network accuracy via testing dataset. Prints accuracy percentage and a confidence interval IF the central limit theorem can be applied
 * @param data testing input feature data
 * @param expected testing input label data
 * @updates nodes
 * @return None
 */
void DenseNeuralNetwork::test(vector<vector<double>> data, vector<vector<double>> expected){

    int acc = 0;
    double loss = 0;

    for (size_t i = 0; i < data.size(); i++){
        if (data.at(i).size() != nodePerLayer.at(0))
            throw "ERROR: Dimensions of training dataset does not match number of input nodes";
        
        
        vector<double> pred = predict(data.at(i));
        

        //only makes sense if one output layer and using cross entropy function

        if (pred.at(0) - 0.5 < 0 && expected.at(i).at(0) == 0){
            acc++;
        }
        else if (pred.at(0) - 0.5 >= 0 && expected.at(i).at(0) == 1){
            acc++;
        }

        
        loss += expected.at(i).at(0)*log2(pred.at(0)) + (1-expected.at(i).at(0))* log2(1-pred.at(0));
    


    }

    long double totalAcc = (double) acc / data.size();

    cout << "Accuracy: " << totalAcc;


    //Using basic statistical assumption that CLT applies to proportions if n*p and n*q >= 5
    if (totalAcc *  data.size() >= 5 &&  (1-totalAcc) *  data.size() >= 5){
        cout << " +/- " << 2.5758*sqrt(totalAcc*(1-totalAcc)/data.size()) << " (99% CI)";
    }
    
    cout << " Loss: " << -1* loss / data.size() << endl;
    

}


/**
 * Makes a prediction based on current weights and biases of a given input
 * @param input 1D vector of input data 
 * @updates nodes
 * @return vector of doubles of the output layer.
 */
vector<double> DenseNeuralNetwork::predict(vector<double> input){ //sofar good
    if (input.size() != nodePerLayer.at(0)){
        throw "ERROR: Data's size does not match number of nodes in this Model's Input Layer";
    }
    for (size_t i = 0; i < input.size(); i++){
        nodes[0][i] = input[i];
    }

    //compute each layer starting at 1
    for (size_t i = 1; i < layerTotal; i++){
        if (activationPerLayer.at(i-1) == "relu")
            computeLayer(i, relu);
        else if (activationPerLayer.at(i-1) == "logistic")
            computeLayer(i, logistic);

        else
            throw "ERROR: Must use on of the following Activation Functions: relu or logistic";
        
    }

    //copy output layer into a vector
    vector<double> result(nodePerLayer.at(nodePerLayer.size()-1));
    for (size_t i = 0; i < result.size(); i++){
        result.at(i) = nodes[layerTotal-1][i];
    }

    return result;

}

