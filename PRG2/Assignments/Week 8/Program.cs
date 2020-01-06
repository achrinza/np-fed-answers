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
    class Program
    {
        static void Main(string[] args)
        {
            List<Customer> customerList = new List<Customer>();
            InitCustomerList(customerList);
            ListCustomers(customerList);
            Console.ReadKey();
        }

        static void InitCustomerList(List<Customer> customerList)
        {
            customerList.Add(new Customer("John Tan", "98501111", new ShippingAddr("Singapore", "Clementi Rd")));
            customerList.Add(new Customer("Amy Lim", "99991111", new ShippingAddr("Hong Kong", "Mong Kok Rd")));
            customerList.Add(new Customer("Tony Tay", "91112222", new ShippingAddr("Malaysia", "Malacca Rd")));
        }

        static void ListCustomers(List<Customer> customerList)
        {
            Console.WriteLine(
                "Name".PadRight(16) +
                "Tel".PadRight(16) +
                "Country".PadRight(16) +
                "Street"
            );

            customerList.ForEach(x =>
            {
                Console.WriteLine(
                    x.Name.PadRight(16) +
                    x.Tel.PadRight(16) + 
                    x.Addr.Country.PadRight(16) +
                    x.Addr.Street
                );
            });
        }
    }
}
