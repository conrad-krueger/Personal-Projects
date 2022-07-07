#include <iostream>
#include <stdexcept>
#include "matrix.h"
using std::cin, std::cout, std::string, std::endl;


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




//Operator Overloading
template <typename T>
std::ostream& operator<<(std::ostream& out, const Matrix<T>& rhs){
    for (int i = 0; i < rhs.getRows(); i++){
        for (int j = 0; j < rhs.getCols(); j++){
            out << rhs.getEntry(i,j) << "\t";
        }
        out << endl; //prints matrix each row at a time seperated by spaces
    }
    return out;
}


//Matrix multiplications
Matrix<double> operator*(const Matrix<double>& lhs, const Matrix<double>& rhs){ 
    //lhs's cols must equal rhs's row or else multiplication is impossible
    if(lhs.getCols() != rhs.getRows()){
        throw std::invalid_argument("ERROR: Cannot multiply 2 matricies (incorrect dimensions)");
    } 
    int m = lhs.getRows();
    int n = rhs.getCols();

    Matrix<double> mx(m,n);

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            int sum = 0;
            int k;
            for (k = 0; k < rhs.getRows(); k++){
                sum += lhs.getEntry(i,k) * rhs.getEntry(k,j); 
            }
            k--;
            mx.insert(i,j,sum);
        }
    }

    return mx;    
}


Matrix<double> operator*(double scalar, const Matrix<double>& rhs){ 

    Matrix<double> mx(rhs.getRows(), rhs.getCols());

    for (int i = 0; i < rhs.getRows(); i++){
        for (int j = 0; j < rhs.getCols(); j++){
            mx.insert(i, j, scalar * rhs.getEntry(i,j));
        }
    }

    return mx;    

}


Matrix<double> operator+(const Matrix<double>& lhs, const Matrix<double>& rhs){
    if(lhs.getRows() != rhs.getRows() || lhs.getCols() != rhs.getCols() ){
        throw std::invalid_argument("ERROR: Dimensions of matricies do not match");
    }

    Matrix<double> mx(lhs.getRows(),lhs.getCols());

    for(int i = 0; i < lhs.getRows(); i++){
        for(int j = 0; j < lhs.getRows(); j++){
            mx.insert(i,j, lhs.getEntry(i,j) + rhs.getEntry(i,j));
        }
    }

    return mx;
}


Matrix<double> operator-(const Matrix<double>& lhs, const Matrix<double>& rhs){
    return lhs + (-1 * rhs);
}


bool operator==(const Matrix<double>& lhs, const Matrix<double>& rhs){
    if(lhs.getRows() != rhs.getRows() || lhs.getCols() != rhs.getCols() ){
        return false;
    }

    for(int i = 0; i < lhs.getRows(); i++){
        for(int j = 0; j < lhs.getRows(); j++){
            if (lhs.getEntry(i,j) != rhs.getEntry(i,j)) return false;
        }
    }

    return true;

}


bool operator!=(const Matrix<double>& lhs, const Matrix<double>& rhs){
    return !(lhs == rhs);
}



class IdentityMatrix : public Matrix<int>{
    public:

    IdentityMatrix(int N) : Matrix<int>(N,N){
        fillAll(0);
        for (int i = 0; i < N; i++){
            matrix[i][i] = 1;
        }
            
    }

    Matrix transpose(){ //not defining a virtual destructor since this is basically the same method as Matrix's transpose
        cout << "The transpose of the Identity Matrix is the same Identity Matrix" << endl;
        return *this;
    }


};



double det(Matrix<double> mtx){
    if(mtx.getRows() != mtx.getCols()){
        throw std::invalid_argument("ERROR: Matrix is not square");
    }

    if(mtx.getRows() == 0) return 1;

    if(mtx.getRows() == 1) return mtx.getEntry(0,0); //1x1 matrix

    //base case
    if(mtx.getRows() == 2 && mtx.getCols() == 2){
        return (mtx.getEntry(0,0) * mtx.getEntry(1,1) - mtx.getEntry(0,1)*mtx.getEntry(1,0));
    }

    double answer = 0;
    double isNeg = 1;
    for(int col = 0; col < mtx.getCols(); col++){
        answer += isNeg * mtx.getEntry(0,col) * det(mtx.Aij(0,col));
        isNeg *= -1;
    }

    return answer;
}



Matrix<double> inverse(Matrix<double> mtx){
    if(mtx.getRows() != mtx.getCols()) 
        throw std::invalid_argument("ERROR: Matrix is not square");

    Matrix<double> cofactor(mtx.getRows(),mtx.getCols());

    double detAll = det(mtx);

    if (detAll == 0){
        throw std::invalid_argument("ERROR: Matrix is not invertable | det(A) = 0");
    }  

    int negOrPos = 1;

    for (int i = 0; i < mtx.getRows(); i++){
        for(int j = 0; j < mtx.getCols(); j++){
            cofactor.insert(i,j, negOrPos * 1/detAll * det( mtx.Aij(j,i) ) );
            negOrPos *= -1;
        }
    }
    return cofactor;
}


int main(){


   //ERRORS
   //Matrix<double> err(4,2);
   //Matrix<double> zero(4,4);
   //zero.fillAll(0);

   //det(err);
   //err = err * err;
   //inverse(err);
   //inverse(zero);
   //zero = zero + err;
   //err.getEntry(100,100);
   //err.Aij(100,100);



    double nat[] = {1,2,3,4,5,6,7,8,9};
    double** identity = new double*[3];
    identity[0] = new double[3]{1,0,0};
    identity[1] = new double[3]{0,1,0};
    identity[2] = new double[3]{0,0,1};

    Matrix<double> mtx(3,3,nat);
    Matrix<double> mtx2(3,3,identity);


    Matrix<double> mtx4;
    mtx4 = mtx2*mtx2;

    Matrix<double> mtx5(mtx2);


    //mtx4.insert(0,0,100);

    cout << "Printing Out Matrix" << endl;
    cout << mtx << endl;
    cout << mtx2 << endl;

    cout << "Matrix 2 * Matrix 2" << endl;
    cout << mtx4 << endl;

    cout << "Matrix 1 - Matrix 2" << endl;
    cout << (mtx - mtx2) << endl;

      cout << "Matrix 2 - Matrix 1" << endl;
    cout << (mtx2 - mtx) << endl;

    cout << "Copy Constructor (copied Matrix 2)" << endl;
    cout << mtx5 << endl;


    double arr[] = {1,2,3};
    Matrix<double> mtx6(3,1,arr);

    cout << "3x1 Matrix" << endl;
    cout << mtx6 << endl;

    Matrix<double> trans = mtx6.transpose();

    cout << "Transpose of Above Matrix" << endl;
    cout << trans << endl;


    cout << "Original Matrix * transpose" << endl;
    cout << mtx6*trans << endl;  


    Matrix<double> mtx7;
    cout << "Multiply matrix by scalar" << endl;
    mtx7 = 10.1 * mtx6;

    cout << mtx7 << endl;

    Matrix<double> mtx8;

    mtx8 = trans * mtx;

    cout << "Multiply transpose matrix [1,2,3] with first matrix matrix" << endl;
    cout << mtx8 << endl;



    cout << "Destructor and Copy Assignment Operator" << endl;
    mtx8 = mtx;
    cout << mtx8 << endl;

    
    Matrix<int>* mtx9 = new IdentityMatrix(3);

    cout << "Matrix Object that points to IdentityMatrix" << endl;

    cout << *mtx9 << endl;

    cout << "Shows overriden transpose method is called (which is the same as the parent matrix transpose except it prints a message that the transpose of the identity matrix is the same exact matrix)" << endl;
    cout << mtx9->transpose() << endl;

    cout << "Destructor..." << endl << endl;
    delete mtx9;
    


    Matrix<double> id(3,3, identity);

    cout << "Determinant of the Identity Matrix (1):" << endl;
    cout << det(id) << endl << endl;

    cout << "Determinant of 5x5 Matrix but has a row of zeros (0):" << endl;

    double big[] = {1,2,3,4,5,6,7,8,9,12,22,45,67,88,2,44,56,78,11,1232,0,0,0,0,0};

    Matrix<double> mtx10(5,5,big);
    cout << mtx10 << endl;
    cout << "det = " << det(mtx10) << endl << endl;


    cout << "No longer has row of zeros:" << endl;
    for (int x = 0; x < 5; x++){
        mtx10.insert(4,x, x*x);
    }

    cout << mtx10 << endl;
    cout << "det = " << det(mtx10) << endl;

    /* Error since no match for Matrix<double> == IdentityMatrix
    cout << "Matrix<double> identity == IdentityMatrix?" << endl;
    IdentityMatrix id2(3);
    cout << (id == id2) << endl; //No
    */

    cout << "Copy Constructor. Copies id into id3. id == id3?" << endl;
    Matrix<double> id3(id);
    cout << (id == id3) << endl; 

    cout << "Change last entry in id3 to 100. id == id3?" << endl;
    id3.insert(2,2,100);
    cout << (id == id3) << endl<< endl;


    double arr3[] = {1,0,1,0,1,0,0,0,1};
    cout << "Matrix A:" << endl;
    Matrix<double> mx(3,3,arr3);
    cout << mx << endl; 
    cout << "A^(-1)" <<  endl;

    cout << inverse(mx) << endl;

    double naturaldub[] = {10,10,10,4,5,10,7,8,10};
    Matrix<double> mtx12(3,3,naturaldub);
    cout << "Matrix B:" << endl;
    cout << mtx12 << endl; 
    cout << "B^(-1)" << endl;
    cout << inverse(mtx12) << endl;




}
