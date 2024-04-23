using System;

// Define a class to demonstrate basic C# features
class CSharpWalkthrough
{
    // Main method acts as the entry point for the program
    static void Main(string[] args)
    {
        Console.WriteLine("C# Walkthrough Program\n");

        // Demonstrating variables
        int age = 30; // Integer variable
        double weight = 72.5; // Double for decimal numbers
        string name = "Alice"; // String variable

        Console.WriteLine($"Name: {name}, Age: {age}, Weight: {weight}\n");

        // Control structure example: if-else
        if (age > 18)
        {
            Console.WriteLine("You are an adult.\n");
        }
        else
        {
            Console.WriteLine("You are not an adult.\n");
        }

        // Loop example: for loop
        Console.WriteLine("Counting from 1 to 5:");
        for (int i = 1; i <= 5; i++)
        {
            Console.WriteLine(i);
        }

        // While loop example
        Console.WriteLine("\nUsing while loop to count down from 5 to 1:");
        int counter = 5;
        while (counter > 0)
        {
            Console.WriteLine(counter);
            counter--; // Decrement counter
        }

        // Method calling
        Console.WriteLine("\nCalculating area of a circle with radius 5:");
        double area = CalculateArea(5);
        Console.WriteLine($"Area: {area}\n");

        // Demonstrating object creation and class usage
        Person person = new Person("Bob", 25);
        person.Introduce();

        Console.WriteLine("\nProgram finished.");
    }

    // Method to calculate area of a circle
    static double CalculateArea(double radius)
    {
        return Math.PI * radius * radius; // PI * r^2
    }
}

// Class to demonstrate basic OOP in C#
class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    // Constructor
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // Method to introduce the person
    public void Introduce()
    {
        Console.WriteLine($"Hello, my name is {Name} and I am {Age} years old.");
    }
}
