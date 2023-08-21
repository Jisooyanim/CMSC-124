/*
Grammar rules:
<expr> ::= +<num> | -<num> | <num>
<num> ::= <num><digits> | <digits>
<digits> ::= <digit> | <digit>.<digit>
<digit> ::= 0|1|2|3|4|5|6|7|8|9
Terminate every input string with ‘$’.

BNF:
<expr>    ::= +<num> | -<num> | <num>
<num>     ::= <digits> | <digits>.<digits>
<digits>  ::= <digit><digits'>
<digits'> ::= <digit><digits'> | e
<digit>   ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
*/

#include <iostream>
#include <string>
#include <regex>
using namespace std;

class Solution{
    public:
    int i = 0;
    char token;
    string userInput;

    void lex(){
        i++;
        token = userInput[i];
    }

    void expression(){
        number();
        if(token == '$'){
            lex();
            if(token == '\0'){
                cout << "Valid" << endl;
            }else{
                cout << "Invalid" << endl;
            }
        }else{
            cout << "Invalid" << endl;
        }
    }

    void number(){
        digits();
        if(regex_match(&token, regex("\\+?|\\-?"))){
            lex();
            digits();
        }if(regex_match(&token, regex("\\."))){
            lex();
            if(!(regex_match(&token, regex("\\d")))){
                i--;
                token = userInput[i];
            }
            digits();
        }
    }

    void digits(){
        digit();
        if(regex_match(&token, regex("\\d"))){
            lex();
            notDigits();
        }
    }

    void notDigits(){
        digit();
        if(regex_match(&token, regex("\\d"))){
            lex();
            notDigits();
        }
    }

    void digit(){
        if(regex_match(&token, regex("\\d"))){
            lex();
        }
    }
};

int main(){
    Solution s;
    regex re("\\s+");
    cout << "Enter string: ";
    cin >> s.userInput;

    s.userInput = regex_replace(s.userInput, re, "");
    s.token = s.userInput[s.i];
    s.expression();

    return 0;
}