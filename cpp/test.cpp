#include <iostream>

namespace construction{
    int man = 20;
    void worker(){
        man++;
        std::cout << man;
    }
}

int main(){
    construction::worker();
    return 0;
}