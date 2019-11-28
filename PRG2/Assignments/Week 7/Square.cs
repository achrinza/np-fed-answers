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
    public class Square : Shape
    {
        public double Length { get; set; }

        public Square(string color, double length) : base("Rectangle", color)
        {
            Length = length;
        }

        public override double FindArea()
        {
            return Math.Pow(Length, 2);
        }

        public override double FindPerimeter()
        {
            return Length * 4;
        }

        public override string ToString()
        {
            return base.ToString() + $"Length: {Length}";
        }
    }
}
