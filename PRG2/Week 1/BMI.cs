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

namespace BMI
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Weight (kg): ");
            double weight = Convert.ToDouble(Console.ReadLine());
            Console.Write("Height (m): ");
            double height = Convert.ToDouble(Console.ReadLine());
            double bmi = weight / Math.Pow(height, 2);
            Console.WriteLine("BMI: " + bmi);
            Console.ReadKey();
        }
    }
}
