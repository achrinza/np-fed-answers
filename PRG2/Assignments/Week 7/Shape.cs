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
    public abstract class Shape: IComparable<Shape>
    {
        public string Type { get; set; }
        public string Color { get; set; }

        public Shape() { }

        public Shape(string type, string color)
        {
            Type = type;
            Color = color;
        }

        public abstract double FindArea();

        public abstract double FindPerimeter();

        public override string ToString()
        {
            return $"Type: {Type.PadRight(10)}Color: {Color.PadRight(9)}";
        }

        public int CompareTo(Shape s2)
        {
            if (this.FindArea() > s2.FindArea())
            {
                return 1;
            }
            else if (this.FindArea() < s2.FindArea())
            {
                return -1;
            }
            else
            {
                return 0;
            }
        }
    }
}
