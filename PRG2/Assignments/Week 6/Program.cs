//
// (c) 2019 Rifa I. Achrinza
// This code is licensed under MIT license (See LICENSE.txt for details)
// SPDX-Short-Identifier: MIT
//

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ShapeApp
{
    class Program
    {
        static void InitCircleList(List<Circle> cList)
        {
            cList.Add(new Circle("Red", 20.0));
            cList.Add(new Circle("Green", 10.0));
            cList.Add(new Circle("Blue", 30.0));
        }

        static string IndexedToStringListPrintoutGenerator<T>(List<T> cList)
        {
            string finalString = null;

            foreach (var item in cList.Select((value, i) => new { i, value }))
            {
                finalString += $"[{item.i + 1}] {item.value.ToString()}\n";
            }

            return finalString;
        }

        static void Main(string[] args)
        {
            List<Circle> circleList = new List<Circle>();
            List<Rectangle> rectList = new List<Rectangle>();
            uint UserInput = 0;

            InitCircleList(circleList);

            while (true)
            {
                Console.Write(
                    "---------------- M E N U --------------------\n" +
                    "[1] List all the circles\n" +
                    "[2] Display the areas of the circles\n" +
                    "[3] Display the perimeters of the circles\n" +
                    "[4] Change the size of a circle\n" +
                    "[5] Add a new circle\n" +
                    "[6] Delete a circle\n" +
                    "[7] Display circles sorted by area\n" +
                    "[8] Add new rectangles\n" +
                    "[9] List rectangles by area\n" +
                    "[10] Compare rectangle dimension equality\n" +
                    "[11] Find rectangle based on length and width\n" +
                    "[0] Exit\n" +
                    "---------------------------------------------\n" +
                    "Enter your option : ");

                try
                {
                    UserInput = Convert.ToUInt32(Console.ReadLine());
                }
                catch(FormatException)
                {
                    Console.WriteLine("Error: invalid option.");
                }

                switch(UserInput)
                {
                    case 1:
                        if (circleList.Count == 0)
                        {
                            Console.WriteLine("Error: empty circle list");
                            break;
                        }

                        Console.WriteLine(IndexedToStringListPrintoutGenerator(circleList));
                        break;
                    case 2:
                        circleList.ForEach(x =>
                        {
                            Console.WriteLine(x.ToString() + $" Area: {x.FindArea()}");
                        });
                        break;
                    case 3:
                        circleList.ForEach(x =>
                        {
                            Console.WriteLine(x.ToString() + $" Perimeter: {x.FindPerimeter()}");
                        });
                        break;
                    case 4:
                        int selectedCircle = 0;
                        double newRadius = 0;
                        Console.WriteLine(IndexedToStringListPrintoutGenerator(circleList));
                        Console.Write("Enter circle number: ");
                        try
                        {
                            selectedCircle = Convert.ToInt32(Console.ReadLine()) - 1;
                            Console.Write("Enter new radius: ");
                            newRadius = Convert.ToDouble(Console.ReadLine());
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine("Error: unexpected value keyed");
                            break;
                        }

                        try
                        {
                            circleList[selectedCircle].Radius = newRadius;
                        }
                        catch(IndexOutOfRangeException)
                        {
                            Console.WriteLine("Error: unexpected index keyed");
                            break;
                        }
                        break;
                    case 5:
                        string newCircleColor;
                        double newCircleRadius;
                        try
                        {
                            Console.Write("Circle color: ");
                            newCircleColor = Console.ReadLine();
                            newCircleRadius = Convert.ToDouble(Console.ReadLine());
                        }
                        catch(FormatException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                            break;
                        }

                        circleList.Add(new Circle(
                            newCircleColor,
                            newCircleRadius
                        ));

                        Console.WriteLine($"New {newCircleColor.ToLower()} circle with radius {newCircleRadius} addded.");
                        break;
                    case 6:
                        Console.WriteLine(IndexedToStringListPrintoutGenerator(circleList));

                        try
                        {
                            Console.Write("Enter circle number: ");
                            int selectedCircleIndex = Convert.ToInt32(Console.ReadLine()) -1 ;
                            circleList.RemoveAt(selectedCircleIndex);
                        }
                        catch(FormatException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                        }
                        catch(ArgumentOutOfRangeException)
                        {
                            Console.WriteLine("Error: unexpected circle index");
                        }
                        break;
                    case 7:
                        Console.WriteLine(IndexedToStringListPrintoutGenerator(circleList.OrderBy(x => x.Radius).ToList()));
                        break;
                    case 8:
                        Console.Write("Color? ");
                        string newRectColor = Console.ReadLine();
                        Console.Write("Length? ");
                        double newRectLength = Convert.ToDouble(Console.ReadLine());
                        Console.Write("Width? ");
                        double newRectWidth = Convert.ToDouble(Console.ReadLine());
                        rectList.Add(new Rectangle(
                            newRectColor,
                            newRectLength,
                            newRectWidth
                        ));
                        break;
                    case 9:
                        IndexedToStringListPrintoutGenerator(rectList.OrderBy(x => x.FindArea()).ToList());
                        break;
                    case 10:
                        IndexedToStringListPrintoutGenerator(rectList.OrderBy(x => x.FindArea()).ToList());
                        int comparableRect1 = 0;
                        int comparableRect2 = 0;

                        try
                        {
                            Console.Write("Comparable rect 1? ");
                            comparableRect1 = Convert.ToInt32(Console.ReadLine());
                            Console.Write("Comparable rect 2? ");
                            comparableRect2 = Convert.ToInt32(Console.ReadLine());
                        }
                        catch (FormatException)
                        {
                            Console.Write("Error: unexpected user input");
                            break;
                        }

                        try
                        {
                            if (
                                rectList[comparableRect1 - 1].Length == rectList[comparableRect2].Length
                                && rectList[comparableRect1 - 1].Width == rectList[comparableRect2].Width
                                )
                            {
                                Console.WriteLine("Matches");
                            }
                            else
                            {
                                Console.WriteLine("Does not match");
                            }

                        }
                        catch (IndexOutOfRangeException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                            break;
                        }
                        break;
                    case 11:
                        double FindableLength = 0;
                        double FindableWidth = 0;
                        try
                        {
                            Console.Write("Length? ");
                            FindableLength = Convert.ToDouble(Console.ReadLine());
                            Console.Write("Height? ");
                            FindableWidth = Convert.ToDouble(Console.ReadLine());

                        }
                        catch (FormatException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                            break;
                        }
                        rectList.Find(x =>
                        {
                            return (
                                x.Width == FindableWidth
                                && x.Length == FindableLength
                            );
                        });
                        break;
                    case 0:
                        Environment.Exit(0);
                        break;
                    default:
                        Console.WriteLine("Error: invalid option");
                        break;
                }
            }
        }
    }
}
