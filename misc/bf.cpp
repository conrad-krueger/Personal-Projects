#include <iostream>
#include <string>
#include <stdexcept>
#include <fstream>

using std::out_of_range, std::string, std::cout, std::cin, std::ifstream, std::endl;

char* memory = new char[30000]{};

char* bf(char* ptr, std::string cmd){

    for (size_t i = 0; i < cmd.size(); i++){
        if(cmd.at(i) == '>'){
            if (&memory[29999] == ptr) throw out_of_range("ERROR: Memory space is 30,000 bytes");
            ++ptr;
        }
        else if(cmd.at(i) == '<'){
            if (&memory[0] == ptr) throw out_of_range("ERROR: Attempted to move left at beginning of memory");
            --ptr;
        }
        else if(cmd.at(i) == '.'){
            cout << *ptr;
        }
        else if(cmd.at(i) == '-'){
            if (*ptr == 0) throw out_of_range("ERROR: No negative ASCII values");
            --(*ptr);
        }
        else if(cmd.at(i) == '+'){
            if (*ptr == 127) throw out_of_range("ERROR: No ASCII values past 127");
            ++(*ptr);
        }
        else if(cmd.at(i) == ','){
            char c;
            std::cin >> c;
            *ptr = c;

        }
        else if(cmd.at(i) == '['){
            std::string smallCmd = "";
            int nested = 1;
            size_t x = i+1;
            while(nested != 0){
                if (x == cmd.size()) throw "SyntaxError: No Terminating character for while loop ( ] )";
                
                if (cmd.at(x) == '['){
                    nested++;
                }
                if (cmd.at(x) == ']'){
                    nested--;
                    if(nested == 0) break;
                }
                smallCmd.push_back(cmd.at(x));
                x++;
            }
            while(*ptr != 0){
                ptr = bf(ptr, smallCmd);
            }
            i = x;
        }
        
        
    }
    return ptr;

}


int main(int argc, char** argv){
    
    char* ptr = memory;
    
    string file = argv[1];

    ifstream inFile(file); 

    if(!inFile.is_open()){
        cout << "Failed to Open File" << endl;
        exit(1);
    }

    string cmd ="";
    string currentCmd;

    while(!inFile.eof()) {
        std::getline(inFile,currentCmd);
        cmd += currentCmd;
    }

    bf(ptr,cmd);

    delete[] memory;
    
}


