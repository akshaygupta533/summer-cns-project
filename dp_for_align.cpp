#include <iostream>
#include <string>
using namespace std;
//Can adjust the following variables
int match = 1;
int mis_match = 0;
int gap_penalty = -1;

int compare(char c1, char c2){
    if(c1==c2)
        return match;
    else
        return mis_match;
}

// int dp(i,j)

int main(){
    string seq1,seq2;
    cin>>seq1;
    cin>>seq2;
    int mat[10][10];

    for(int i=0;i<seq1.length();i++){
        for(int j=0;j<seq2.length();j++)
            mat[i][j]=__INT_MAX__;
        cout<<endl;
    }

    for(int i=0;i<seq1.length();i++){
        for(int j=0;j<seq2.length();j++)
            cout<<mat[i][j]<<" ";
        cout<<endl;
    }
    for(int i=0;i<seq1.length();i++)
        mat[i][0] = i*gap_penalty;
    for(int j=0;j<seq2.length();j++)
        mat[0][j] = j*gap_penalty;
}