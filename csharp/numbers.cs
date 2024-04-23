using System;

class ExampleClass
{
    static void Main()
    {
        Console.WriteLine("Hello world!!!!!!!");

        while (true)
        {
            Console.WriteLine("\nChoose an option:");
            Console.WriteLine("1. Triangulate a number");
            Console.WriteLine("2. Prime split a number");
            Console.WriteLine("3. Inverse Triangulate a number");
            Console.WriteLine("Enter any other letter to quit");

            string choice = Console.ReadLine();
            if (!int.TryParse(choice, out int option) || option < 1 || option > 3)
            {
                break; // Break the loop if input is not 1 or 2
            }

            switch (option)
            {
                case 1:
                    int triangle = TriangulateNumber();
                    Console.WriteLine($"Triangular number: {triangle}");
                    break;
                case 2:
                    PrimeFactorise();
                    break;
                case 3:
                    inverseTriangulate();
                    break;
            }
        }

        Console.WriteLine("Goodbye!");
    }

    static void inverseTriangulate()
    {
        // User input for numnber to check:
        Console.Write("Enter a number to check if it is an inverse triangular number: ");
        string input = Console.ReadLine();

        if (!int.TryParse(input, out int number) || number <= 0)
        {
            Console.WriteLine("Invalid input. Please enter a positive integer.");
            return;
        }

        int i = 1;
        while (number > 0)
        {
            number -= i;
            i++;
        }
        if (number == 0)
            // Print out the inverse of the triangular number
            Console.WriteLine("The inverse of " + (input) + " is = " + (i - 1));
        else
            // Print out -1 if no such inverse exists
            Console.WriteLine(-1);
    }

    static int TriangulateNumber()
    {
        Console.Write("Enter a number to triangulate: ");
        string input = Console.ReadLine();

        if (!int.TryParse(input, out int number) || number <= 0)
        {
            Console.WriteLine("Invalid input. Please enter a positive integer.");
            return 0; // Return 0 if invalid input
        }

        int triangle = 0;
        for (int i = 1; i <= number; i++)
        {
            triangle += i;
        }
        return triangle;
    }

    public static void PrimeFactorise()
    {
        while (true)
        {
            Console.Write("Enter a number for which you want the prime factors (or 'q' to quit): ");
            string input = Console.ReadLine();

            if (input.ToLower() == "q")
            {
                break; // Break out of the loop to return to the main menu
            }

            if (!int.TryParse(input, out int number) || number <= 0)
            {
                Console.WriteLine("Invalid input. Please enter a positive integer.");
                continue; // Continue asking for input
            }

            string result = Factorize(number);
            Console.WriteLine($"{number} = {result}");
            break; // Successfully factorized, so break out of the loop
        }
    }

    private static string Factorize(int number)
    {
        int n = number;
        string factors = "";
        for (int divisor = 2; n > 1; divisor++)
        {
            while (n % divisor == 0)
            {
                factors += divisor + "*";
                n /= divisor;
            }
        }

        if (factors.EndsWith("*"))
        {
            factors = factors.Remove(factors.Length - 1);
        }

        return factors;
    }
}
