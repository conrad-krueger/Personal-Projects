#ifndef MATRIX_H
#define MATRIX_H

template<typename T>
class Matrix{
    protected:

    int M, N;
    T** matrix;

    //deallocated memory
    void clear();
    
    //deep copy of another Matrix
    void copy(const Matrix& other);

    public:

    //getter and setters

    T** getMatrix() const {
        return matrix;
    }

    T getEntry(int i, int j) const {
        if(i > M || j > N)
            throw std::out_of_range("ERROR: Entry does not exist");
        return matrix[i][j];
    }

    int getRows() const {
        return M;
    }

    int getCols() const {
        return N;
    }


    //inserts item into matrix[i][j]
    void insert(int i, int j, T item){
        matrix[i][j] = item;
    }


    //Constructors

    //Default
    Matrix(): M(), N(), matrix() {}

    //"empty" Matrix of size MxN
    Matrix(int m, int n): M(m), N(n), matrix(nullptr){

        if (!(m == 0 || n == 0)){
            matrix = new T*[m];

            for (int i = 0; i < m; i++){
                matrix[i] = new T[n]{};
            }

        }

    }

    //Matrix of size MxN but whose entries are determined by an array (NOT BOUNDS PROTECTED!)
    Matrix(int m, int n, T* arr): M(m), N(n), matrix(nullptr){

        if (!(m == 0 || n == 0)){
            matrix = new T*[m];
            for (int i = 0; i < m; i++){
                matrix[i] = new T[n]{};
            }

            int t = 0;
            for (int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    matrix[i][j] = arr[t];
                    t++;
                }
            }
        }

    }

    Matrix(int m, int n, T** arr): M(m), N(n), matrix(nullptr){

        if (!(m == 0 || n == 0)){
            matrix = new T*[m];
            for (int i = 0; i < m; i++){
                matrix[i] = new T[n]{};
            }

            int t = 0;
            for (int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    matrix[i][j] = arr[i][j];
                    t++;
                }
            }
        }

    }

    //Rule of 3

    //Destructor
    ~Matrix(){ clear();} 

    //Copy Constructor
    Matrix(const Matrix& obj):  M(0), N(0), matrix(nullptr) {copy(obj);}

    //Copy Assignment Operator
    Matrix& operator=(const Matrix& rhs){
        if (this != &rhs)
            copy(rhs);
        return *this;
    }

    //returns transpose of current matrix
    //transpose essentially "swaps" everything
    virtual Matrix transpose();

    //returns Matrix without the ith row and jth column
    Matrix Aij(int i, int j);

    //fill each cell with item
    void fillAll(T item);


};



#endif