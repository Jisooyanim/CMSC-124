/* BNF GRAMMAR
<string> ::= <expression>
<expression> ::= (<expression>) | <operation>
<operation> ::= <expression> <sign> <expression> | <unary> <expression> | <identifier>
<sign> ::= + | -
<unary> ::= ~
<identifier> ::= x | y | z 
*/

#include <iostream>
using namespace std;

int main(){
    cout << "String: ";
    string inputString;
    getline(cin, inputString);

    string tempString;
    for(char c : inputString){
        if(c != ' '){
            tempString += c;
        }
    }

    bool inGrammar = true;

    int parCounter = 0;
    for(char c : tempString){
        if(c == '('){
            parCounter++;
        }else if(c == ')'){
            parCounter--;
        }
    }

    if(parCounter != 0){
        cout << inputString << " is not in the grammar";
        return 0;
    }

    for(int i = 0; i < tempString.size() - 1; i++){
        char current = tempString[i];
        char next = tempString[i + 1];
        cout << "current: " << current << endl;
        cout << "next: " << next << endl;

        if(current == 'x' || current == 'y' || current == 'z'){
            if(next == '+' || next == '-' || next == ')'){
                continue;
            }else{
                inGrammar = false;
                break;
            }
        }else if(current == '~'){
            if(next == 'x' || next == 'y' || next == 'z'){
                continue;
            }else{
                inGrammar = false;
                break;
            }
        }else if(current == '('){
            if(next == 'x' || next == 'y' || next == 'z' || next == '~'){
                continue;
            }else{
                inGrammar = false;
                break;
            }
        }else if(current == '+' || current == '-'){
            if(next == 'x' || next == 'y' || next == 'z' || next == '(' || next == '~'){
                continue;
            }else{
                inGrammar = false;
                break;
            }
        }
    }

    if(inGrammar){
        cout << inputString << " is in the grammar";
    }else{
        cout << inputString << " is not in the grammar";
    }  

    return 0;  
}