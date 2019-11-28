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
        static void InitShapeList(List<Shape> cList)
        {
            Shape shape1 = new Circle("Red", 20.0);
            Shape shape2 = new Square("Red", 10.0);
            Shape shape3 = new Circle("Green", 10.0);
            Shape shape4 = new Square("Green", 20.0);
            Shape shape5 = new Circle("Blue", 30.0);
            Shape shape6 = new Square("Blue", 30.0);

            cList.AddRange(new List<Shape>
            {
                shape1,
                shape2,
                shape3,
                shape4,
                shape5,
                shape6
            });
        }

        static string IndexedToStringListPrintoutGenerator<Shape>(List<Shape> cList)
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
            List<Shape> shapeList = new List<Shape>();
            uint UserInput = 0;

            InitShapeList(shapeList);

            while (true)
            {
                Console.Write(
                    "---------------- M E N U --------------------\n" +
                    "[1] List all the shapes\n" +
                    "[2] Display the areas of the shapes\n" +
                    "[3] Display the perimeters of the shapes\n" +
                    "[4] Add a new circle\n" +
                    "[5] Delete a circle\n" +
                    "[6] Change the sizes of the shapes\n" +
                    "[7] Display shapes sorted by area\n" +
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
                        if (shapeList.Count == 0)
                        {
                            Console.WriteLine("Error: empty circle list");
                            break;
                        }

                        Console.WriteLine(IndexedToStringListPrintoutGenerator(shapeList));
                        break;
                    case 2:
                        shapeList.ForEach(x =>
                        {
                            Console.WriteLine(x.ToString() + $" Area: {x.FindArea().ToString("0.00")}");
                        });
                        break;
                    case 3:
                        shapeList.ForEach(x =>
                        {
                            Console.WriteLine(x.ToString() + $" Perimeter: {x.FindPerimeter().ToString("0.00")}");
                        });
                        break;
                    case 4:
                        string newCircleColor;
                        double newCircleRadius;
                        try
                        {
                            Console.Write("Circle color: ");
                            newCircleColor = Console.ReadLine();
                            Console.Write("Circle radius: ");
                            newCircleRadius = Convert.ToDouble(Console.ReadLine());
                        }
                        catch(FormatException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                            break;
                        }

                        shapeList.Add(new Circle(
                            newCircleColor,
                            newCircleRadius
                        ));

                        Console.WriteLine($"New {newCircleColor.ToLower()} circle with radius {newCircleRadius} addded.");
                        break;
                    case 5:
                        if (shapeList.OfType<Circle>().ToList<Circle>().Count <= 0)
                        {
                            Console.WriteLine("Error: shape list does not contain any circles.");
                            break;
                        }
                        int selectedShapeIndex = 0;
                        Shape selectedShape = null;
                        Console.WriteLine(IndexedToStringListPrintoutGenerator(shapeList));

                        try
                        {
                            Console.Write("Enter circle number: ");
                            selectedShapeIndex = Convert.ToInt32(Console.ReadLine()) -1;
                            selectedShape = shapeList[selectedShapeIndex];

                            if (selectedShape is Circle)
                            {
                                shapeList.Remove(selectedShape);
                                Console.WriteLine("Circle removed.");
                            }
                            else
                            {
                                Console.WriteLine("Error: Not a circle.");
                                break;
                            }
                            
                        }
                        catch(FormatException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                            break;
                        }
                        catch(ArgumentOutOfRangeException)
                        {
                            Console.WriteLine("Error: unexpected shape index");
                            break;
                        }
                        break;
                    case 6:
                        int selectedShapeIndex2 = 0;
                        Console.WriteLine(IndexedToStringListPrintoutGenerator(shapeList));
                        Console.Write("Index?");
                        try
                        {
                            selectedShapeIndex2 = Convert.ToInt32(Console.ReadLine());
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine("Error: unexpected user input");
                        }

                        Shape selectedShape2 = shapeList[selectedShapeIndex2];

                        if (selectedShape2 is Circle)
                        {
                            int newCircleRadius2 = 0;

                            try
                            {
                                Console.Write("Radius? ");
                                newCircleRadius2 = Convert.ToInt32(Console.ReadLine());
                            }
                            catch (FormatException)
                            {
                                Console.WriteLine("Error: unexpected user input.");
                                break;
                            }

                            ((Circle)shapeList[selectedShapeIndex2]).Radius = newCircleRadius2;
                        }
                        else if (selectedShape2 is Square)
                        {
                            int newSquareLength = 0;

                            try
                            {
                                Console.Write("Length? ");
                                newSquareLength = Convert.ToInt32(Console.ReadLine());
                            }
                            catch (FormatException)
                            {
                                Console.WriteLine("Error: unexpected user input.");
                                break;
                            }

                            ((Square)shapeList[selectedShapeIndex2]).Length = newSquareLength;
                        }
                        break;
                    case 7:
                        foreach(var item in shapeList.OrderBy(x => x.FindArea()).ToList<Shape>().Select((value, i) => new { i, value }))
                        {
                            Console.WriteLine(
                                (item.i + 1).ToString().PadRight(5) +
                                item.value.Type.PadRight(11) +
                                item.value.FindArea().ToString("0.00")
                            );
                        }
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
