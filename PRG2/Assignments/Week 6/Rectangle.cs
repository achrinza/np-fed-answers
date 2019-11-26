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
    public class Rectangle : Shape
    {
        public double Length { get; set; }
        public double Width { get; set; }

        public Rectangle(string color, double length, double width) : base("Rectangle", color)
        {
            Length = length;
            Width = width;
        }

        public override double FindArea()
        {
            return Length * Width;
        }

        public override double FindPerimeter()
        {
            return Length * 2 + Width * 2;
        }

        public bool Equal(Rectangle obj)
        {
            if (this.Length == obj.Length && this.Width == obj.Width)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public override string ToString()
        {
            return base.ToString() + $"        Length: {Length} Width: {Width}";
        }
    }
}
