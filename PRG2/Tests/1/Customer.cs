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

namespace CustomerApp_S10193294
{
    public class Customer
    {
        private string name;
        private double loanAmount;
        private int repaymentPeriod;
        private int interestRate;

        public string Name { get => name; set => name = value; }
        public double LoanAmount { get => loanAmount; set => loanAmount = value; }
        public int RepaymentPeriod { get => repaymentPeriod; set => repaymentPeriod = value; }
        public int InterestRate { get => interestRate; set => interestRate = value; }

        public Customer(string name, double loanAmount, int repaymentPeriod, int interestRate)
        {
            Name = name;
            LoanAmount = loanAmount;
            RepaymentPeriod = repaymentPeriod;
            InterestRate = interestRate;
        }

        public double CalculateAmountDue()
        {
            return LoanAmount + LoanAmount * InterestRate / 100 * RepaymentPeriod;
        }

        public override string ToString()
        {
            return $"Name: {Name}   Loan Amount: {LoanAmount}   Repayment Period: {RepaymentPeriod} Interest Rate: {InterestRate}";
        }
    }
}
