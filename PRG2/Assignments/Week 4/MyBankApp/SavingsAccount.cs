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

namespace MyBankApp
{
    class SavingsAccount : BankAccount
    {
        private double rate;

        public SavingsAccount(string accNo, string accName, double balance, double rate) : base(accNo,accName, balance)
        {
            this.Rate = rate;
        }

        public double Rate { get => rate; set => rate = value; }

        public double CalculateInterest()
        {
            return Balance * Rate / 100;
        }

        public override string ToString()
        {
            return base.ToString() + $" Rate: {Rate}";
        }
    }
}
