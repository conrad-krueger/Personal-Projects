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



//deallocated memory
template <typename T>
void Matrix<T>::clear(){
    for (int i = 0; i < M; i++){
        delete[] matrix[i];
    }

    delete[] matrix;
    matrix = nullptr;
}

//deep copy of another Matrix
template <typename T>
void Matrix<T>::copy(const Matrix<T>& other){
    if (matrix){
        clear();
    }
    
    //sets this matrix with new dimensions
    M = other.getRows();
    N = other.getCols();

    
    //allocates memory
    matrix = new T*[M];
    for (int i = 0; i < M; i++){
        matrix[i] = new T[N]{};
    }


    //goes to each cell and copies value
    for (int i = 0 ; i < M; i++){
        for(int j = 0; j < N; j++){
            matrix[i][j] = other.getEntry(i, j);
        }
    }
    
}

//misc

//returns transpose of current matrix
//transpose essentially "swaps" everything
template <typename T>
Matrix<T> Matrix<T>::transpose(){
    Matrix<T> transpose(N,M);

    for (int i = 0; i < M; i++){
        for(int j = 0; j < N; j++){
            transpose.insert(j,i,matrix[i][j]);
        }
    }
    return transpose;
}

//returns Matrix without the ith row and jth column
template <typename T>
Matrix<T> Matrix<T>::Aij(int i, int j){
    if(i > M || j > N){
        throw std::out_of_range("ERROR: Entry does not exist");
    }
    if (M-1 == 0 || N-1 == 0){
        Matrix<T> mtx(M-1,N-1);
        return mtx;
    }

    Matrix<T> mtx(M-1,N-1);
    int erri = 0; //will change to 1 after we pass i 
    int errj = 0; //will change to 1 after we pass j

    for(int x = 0; x < M; x++){
        if(x == i){
            erri = 1;
            continue;
        }
        for(int y = 0; y < N; y++){
            if(y == j){
                continue;
            }

            if(y >= j) errj = 1;
            else errj= 0;


            mtx.insert(x-erri, y-errj, matrix[x][y]);

        }
    }

    return mtx;

}

//fill each cell with item
template <typename T>
void Matrix<T>::fillAll(T item){
    for (int i = 0; i < M; i++){
        for(int j = 0; j < N; j++){
            matrix[i][j] = item;
        }
    }
}



#endif