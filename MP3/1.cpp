/* Grammar rules
<expr> ::= <expr>+<term> | <expr>-<term> | <term>
<term> ::= <term>*<factor> | <term>/<factor> | <factor>
<factor> ::= (<expr>) |<digit>
<digit> ::= 0|1|2|3
Terminate every input string with ‘$’.

BNF:
<expr> ::= <term><expr'>
<expr'> ::= +<tetm><expr'> | -<term><expr'> | ε
<term> ::= <factor><term'>
<term'> ::= *<factor><term'> | /<factor><term'> | ε
<factor> ::= (<expr>) |<digit>
<digit> ::= 0|1|2|3 */

#include <iostream>
#include <string>
#include <regex>
using namespace std;

class Solution{
    public:
        int i = 0;
        int error = 0;
        char token;
        string userInput;

        void lex(){
            i++;
            token = userInput[i];
        }

        void expression(){
            term();
            notExpression();
        }

        void notExpression(){
            if(regex_match(&token, regex("\\+?|\\-?"))){
                lex();
                term();
                notExpression();
            }else{
                return;
            }
        }

        void term(){
            factor();
            notTerm();
        }

        void notTerm(){
            if(regex_match(&token, regex("\\*?|\\/?"))){
                lex();
                factor();
                notTerm();
            }else{
                return;
            }
        }

        void factor(){
            if(token == '('){
                lex();
                expression();
                if(token == ')'){
                    lex();
                }else{
                    error = 1;
                    return;
                }
            }else{
                digit();
            }
        }
        void digit(){
            if(token == '0' || token == '1' || token == '2' || token == '3'){
                lex();
            }else{
                error = 1;
                return;
            }
        }
};

int main(){
    Solution s;
    regex re("\\s+");
    
    cout << "Enter String: ";
    cin >> s.userInput;

    s.userInput = regex_replace(s.userInput, re, "");
    s.token = s.userInput[s.i];
    s.expression();

    if(s.error == 0){
        if(s.token == '$'){
            s.lex();
            if (s.token == '\0'){
                cout <<"Valid" << endl;
            }else{
                cout << "Invalid" << endl;
            }
        }else{
            cout << "Invalid" << endl;
        }   
    }else{
        cout << "Invalid" << endl;
    }

    return 0;
}