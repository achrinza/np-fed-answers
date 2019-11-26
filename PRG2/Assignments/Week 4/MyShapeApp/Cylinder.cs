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

namespace MyShapeApp
{
    public class Cylinder : Circle
    {
        private double length;

        public double Length { get => length; set => length = value; }

        public Cylinder() { }

        public Cylinder(double radius, double length) : base(radius)
        {
            Length = length;
        }

        public double CalculateArea()
        {
            return base.CalculateArea() * 2 + Length * Radius;
        }

        public double CalculateVolume()
        {
            return base.CalculateArea() * Length;
        }

        public override string ToString()
        {
            return base.ToString() + $" Length: {Length}";
        }

    }
}
