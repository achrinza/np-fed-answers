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
    public class Circle: Shape
    {
        public double Radius { get; set; }

        public Circle() { }

        public Circle(string color, double radius): base("Circle", color)
        {
            Radius = radius;
        }

        public override double FindArea()
        {
            return Math.PI * Math.Pow(Radius, 2);
        }

        public override double FindPerimeter()
        {
            return 2 * Math.PI * Radius;
        }

        public override string ToString()
        {
            return base.ToString() + $"Radius: {Radius}";
        }
    }
}
