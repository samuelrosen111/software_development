using System;

class ExampleClass
{
    static void Main()
    {
        Console.WriteLine("Hello world!!!!!!!");

        int triangle = TriangulateNumber();
        Console.WriteLine(triangle);

        PrimeFactorise();
    }

    static int TriangulateNumber()
    {
        // Prompts user for a number
        Console.WriteLine("Enter a number (to triangulate): ");
        string input = Console.ReadLine();
        
        // Try to parse the input to an integer
        if (!int.TryParse(input, out int number) || number <= 0)
        {
            Console.WriteLine("Invalid input. Please enter a positive integer.");
            return 0;
        }

        // Calculate the triangular number
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
            Console.Write("Enter a number for which you want to find the prime factors of (or 'q' to quit): ");
            string input = Console.ReadLine();
            
            if (input.ToLower() == "q")
            {
                break;
            }

            if (!int.TryParse(input, out int number))
            {
                Console.WriteLine("Invalid input. Please enter a valid integer.");
                continue;
            }

            if (number <= 0)
            {
                Console.WriteLine("Please enter a positive integer.");
                continue;
            }

            string result = Factorize(number);
            Console.WriteLine($"{number} = {result}");
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
