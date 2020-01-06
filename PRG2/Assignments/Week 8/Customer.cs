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
    public class Customer
    {
        private string name;
        private string tel;
        private ShippingAddr addr;
        public string Name { get => name; set => name = value; }
        public string Tel { get => tel; set => tel = value; }
        public ShippingAddr Addr { get => addr; set => addr = value; }

        public Customer() { }

        public Customer(string name, string tel, ShippingAddr addr)
        {
            Name = name;
            Tel = tel;
            Addr = addr;
        }

        public override string ToString()
        {
            return $"Name: {Name}    Tel: {Tel}    {Addr.ToString()}";
        }
    }
}
