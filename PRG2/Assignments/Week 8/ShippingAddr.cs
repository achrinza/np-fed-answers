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

namespace ShippingApp
{
    public class ShippingAddr
    {
        private string country;
        private string street;

        public string Country { get => country; set => country = value; }
        public string Street { get => street; set => street = value; }

        public ShippingAddr() { }

        public ShippingAddr(string country, string street)
        {
            Country = country;
            Street = street;
        }

        public override string ToString()
        {
            return $"Country: {Country}    Street: {Street}";
        }
    }
}
