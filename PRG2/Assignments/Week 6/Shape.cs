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
    public abstract class Shape
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
            return $"Type: {Type}        Color: {Color}";
        }
    }
}
