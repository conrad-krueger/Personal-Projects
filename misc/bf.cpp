#include <iostream>
#include <string>
#include <stdexcept>
#include <fstream>

using std::out_of_range, std::string, std::cout, std::cin, std::ifstream, std::endl;

char* memory = new char[30000]{};

char* bf(char* ptr, std::string cmd){

    for (size_t i = 0; i < cmd.size(); i++){
        //move pointer to left
        if(cmd.at(i) == '>'){
            if (&memory[29999] == ptr) throw out_of_range("ERROR: Memory space is 30,000 bytes");
            ++ptr;
        }
        else if(cmd.at(i) == '<'){ //move pointer to right
            if (&memory[0] == ptr) throw out_of_range("ERROR: Attempted to move left at beginning of memory");
            --ptr;
        }
        else if(cmd.at(i) == '.'){ //output char at current memory location
            cout << *ptr;
        }
        else if(cmd.at(i) == '-'){ //decrement memory value by 1
            if (*ptr == 0) throw out_of_range("ERROR: No negative ASCII values");
            --(*ptr);
        }
        else if(cmd.at(i) == '+'){ //increment memory value by 1
            if (*ptr == 127) throw out_of_range("ERROR: No ASCII values past 127");
            ++(*ptr);
        }
        else if(cmd.at(i) == ','){ //accept input at current memory
            char c;
            std::cin >> c;
            *ptr = c;

        }
        else if(cmd.at(i) == '['){ //while (*ptr != 0), recursive definition to deal with embedded while loops
            std::string smallCmd = "";
            int nested = 1;
            size_t x = i+1;
            while(nested != 0){ //keep track of how many inner while loops to take care of
                if (x == cmd.size()) throw "SyntaxError: No Terminating while loop character( ] )";
                
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
            while(*ptr != 0){ //perform bf interp on inner while loop
                ptr = bf(ptr, smallCmd);
            }
            i = x; //set pointer to after all of the while loop
        }
        
        
    }
    return ptr;

}


int main(int argc, char** argv){
    
    char* ptr = memory;
    
    //read syntax from txt file
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
    
    //interpret
    bf(ptr,cmd);

    delete[] memory; //deallocate mem
    
}


