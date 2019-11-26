using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MyShapeApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Circle CircleInstance = new Circle(5);
            Cylinder CylinderInstance = new Cylinder(5, 10);
            bool IsValidOption = true;
            int UserOption = -1;

            while (true)
                {
                try
                {
                    Console.Write(
                        "----------------M E N U------------------\n" +
                        "[1] Change the radius of circle\n" +
                        "[2] Change the radius of cylinder\n" +
                        "[3] Change the length of cylinder\n" +
                        "[4] Display the area of circle\n" +
                        "[5] Display the surface area of cylinder\n" +
                        "[6] Display the volume of cylinder\n" +
                        "[0] Exit\n" +
                        "------------------------------------------\n" +
                        "Enter your option:"
                    );
                    UserOption = Convert.ToInt32(Console.ReadLine());
                }
                catch(FormatException)
                {
                    Console.WriteLine("Error: Invalid option.");
                    IsValidOption = false;
                }

                if (IsValidOption)
                {
                    switch(UserOption)
                    {
                        case 1:
                            Console.Write("Radius? ");
                            try
                            {
                                double radius = Convert.ToInt32(Console.ReadLine());
                                CircleInstance.Radius = radius;

                                if (radius < 0)
                                {
                                    Console.WriteLine("Invalid radius.");
                                    break;
                                }
                            }
                            catch(FormatException)
                            {
                                Console.WriteLine("Invalid Radius.");
                            }
                            break;
                        case 2:
                            Console.Write("Radius? ");
                            try
                            {
                                double radius = Convert.ToInt32(Console.ReadLine());
                                CylinderInstance.Radius = radius;

                                if (radius < 0)
                                {
                                    Console.WriteLine("Invalid radius.");
                                    break;
                                }
                            }
                            catch (FormatException)
                            {
                                Console.WriteLine("Invalid Radius.");
                            }
                            break;
                        case 3:
                            Console.Write("Radius? ");
                            try
                            {
                                double Length = Convert.ToInt32(Console.ReadLine());
                                CylinderInstance.Length = Length;

                                if (Length < 0)
                                {
                                    Console.WriteLine("Invalid length.");
                                    break;
                                }
                            }
                            catch (FormatException)
                            {
                                Console.WriteLine("Invalid length.");
                            }
                            break;
                        case 4:
                            Console.WriteLine($"Area: {CircleInstance.CalculateArea()}");
                            break;
                        case 5:
                            Console.WriteLine($"Surface Area: {CylinderInstance.CalculateArea()}");
                            break;
                        case 6:
                            Console.WriteLine($"Volume: {CylinderInstance.CalculateVolume()}");
                            break;
                        case 0:
                            Environment.Exit(0);
                            break;
                        default:
                            Console.WriteLine("Invalid option.");
                            break;
                    }
                }
            }
        }
    }
}
