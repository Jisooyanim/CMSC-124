/*
BNF GRAMMAR
<palindfrome> ::= aa | ... | zz | AA | ... | ZZ | a<palindrome>a | ... | Z<palindrome?Z | letter
<letter> ::= a | ... | z | A | ... | Z | ' ' | ∈
*/
#include <iostream>
using namespace std;

int main(){
    cout << "Enter string: ";
    string inputString;
    getline(cin, inputString);

    string tempString;
    for(char c:inputString){
        if(c != ' '){
            tempString += c;
        }
    }

    for(char c:tempString){
        if(!((c >= 'a' && c <= 'z') || (c >= 'A' && 'Z'))){
           cout << inputString << " is not a palindrome in the grammar";
           return 0; 
        }
    }

    bool isPal = true;

    for(int i = 0; i < tempString.size()/2;i++){
        if(tempString[i] != tempString[tempString.size() - i - 1]){
            isPal = false;
        }
    }

    if(isPal){
        cout << inputString << " is a palindrome";
    }else{
        cout << inputString << " is not a palindrome";
    }

    return 0;
}