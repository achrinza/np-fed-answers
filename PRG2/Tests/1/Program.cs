//
// (c) 2019 Rifa I. Achrinza
// This code is licensed under MIT license (See LICENSE.txt for details)
// SPDX-Short-Identifier: MIT
//

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CustomerApp_S10193294
{
    class Program
    {
        static void InitCustomerList(List<Customer> cList)
        {
            using(StreamReader reader = new StreamReader("./loans.csv"))
            {
                while(!reader.EndOfStream)
                {
                    string[] line = reader.ReadLine().Split(',');

                    cList.Add(new Customer(
                        line[0],
                        Convert.ToDouble(line[1]),
                        Convert.ToInt32(line[2]),
                        Convert.ToInt32(line[3])
                    ));
                }
            }
        }

        static Customer AddCustomer()
        {
            Console.WriteLine("Add new customer");

            Console.Write("Customer Name: ");
            string Name = Console.ReadLine();

            Console.Write("Customer loan: ");
            double LoanAmount = Convert.ToDouble(Console.ReadLine());

            Console.Write("Customer repayment period: ");
            int RepaymentPeriod = Convert.ToInt32(Console.ReadLine());

            Console.Write("Customer interest rate: ");
            int InterestRate = Convert.ToInt32(Console.ReadLine());

            return new Customer(Name, LoanAmount, RepaymentPeriod, InterestRate);
        }

        static Customer SearchCustomer(List<Customer> cList, string name)
        {
            Customer result = cList.Find(x => x.Name == name);

            return result;
        }

        static void DisplayOutput(List<Customer> cList)
        {
            Console.WriteLine(
                "Name        Loan Amount Repayment Period Interest Rate Total Amount Due\n" +
                "========    =========== ================ ============= ================"
            );

            cList.ForEach(x =>
            {
                Console.WriteLine(
                    x.Name.PadRight(12) +
                    x.LoanAmount.ToString("0,000.00").PadLeft(11) +
                    x.RepaymentPeriod.ToString().PadLeft(17) +
                    x.InterestRate.ToString().PadLeft(14) +
                    x.CalculateAmountDue().ToString("0,000.00").PadLeft(17)
                );
            });
        }

        static void Main(string[] args)
        {
            List<Customer> customerList = new List<Customer>();

            InitCustomerList(customerList);

            DisplayOutput(customerList);

            customerList.Add(AddCustomer());

            DisplayOutput(customerList);

            Console.Write("Enter the name of the customer: ");
            string SearchQuery = Console.ReadLine();

            Customer SearchResult = SearchCustomer(customerList, SearchQuery);

            if (SearchResult == null)
            {
                Console.WriteLine($"{SearchQuery} is not found!");
            }
            else
            {
                Console.WriteLine(SearchResult.ToString());
            }

            Console.ReadKey();
        }
    }
}
