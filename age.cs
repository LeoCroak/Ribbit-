namespace Program;

class Mainmethod
{
    public static void Main(string[] args)
    {
        Boolean isrunning = true;

        while (isrunning)
        {
            Console.WriteLine("Enter your age:");
            try
            {
                String age = Console.ReadLine();
                int cage = Convert.ToInt32(age);

                Console.WriteLine($"You are {cage}:");

                Console.WriteLine("Would you like to continue yes/no:");
                String yesorno = Console.ReadLine().ToLower();
                if (yesorno != "yes")
                {
                    Console.WriteLine("Shutting processes down:");
                    Console.WriteLine("The program '[16928] MyC#Journey.exe: Program Trace' has exited with code 0 (0x0).\r\nThe program '[16928] MyC#Journey.exe' has exited with code 0 (0x0).\r\n");
                    isrunning = false;
                } 
            } catch (FormatException)
            {
                Console.WriteLine("Invalid input shutting processes down:");
                Console.WriteLine("The program '[16928] MyC#Journey.exe: Program Trace' has exited with code 0 (0x0).\r\nThe program '[16928] MyC#Journey.exe' has exited with code 0 (0x0).\r\n");
                isrunning = false;
            }

                
        }
    }
}