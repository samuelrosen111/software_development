#include <iostream> // This is a preprocessor directive allowing input and output operations. 

void demo_function(int input_integer); // This is a function prototype. It is a declaration of a function that will be defined later in the program.



int main() { // This is the main function. It is the entry point of the program and will execute when the program is compiled and run.
    int x = 5;
    std::cout << "Hello, World!" << std::endl;

    std::cout << "Using for-loop to count from 0 to 10:" << std::endl;
    for(int i=0; i<=10; i++){
        std::cout << i << std::endl;
    }

    int while_counter = 0;
    while(while_counter < 20){
        std::cout << "While loop counter has value:" << std::endl;
        std::cout << while_counter << std::endl;
        while_counter++;
    }

    int demo_input = 777;
    demo_function(demo_input);


    return 0;
}

void demo_function(int input_integer){
    std::cout << "This is a demo function." << std::endl;
    std::cout << "The input integer is:" << std::endl;
    std::cout << input_integer << std::endl;
}
