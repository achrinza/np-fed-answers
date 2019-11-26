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
    class BankAccount
    {
        private string accNo;
        private string accName;
        private double balance;

        public string AccNo { get => accNo; set => accNo = value; }
        public string AccName { get => accName; set => accName = value; }
        public double Balance { get => balance ; set => balance = value; }

        protected BankAccount() { }

        public BankAccount(string accNo, string accName, double balance)
        {
            this.AccNo = accNo;
            this.AccName = accName;
            this.balance = balance;
        }

        public void Deposit(double amt) => balance += amt;

        public bool Withdraw(double amt)
        {
            bool isSuccessful;

            if (balance >= amt)
            {
                balance -= amt;
                isSuccessful = true;
            }
            else
            {
                isSuccessful = false;
            }

            return isSuccessful;
        }

        public override string ToString()
        {
            return $"Acc No: {AccNo} Acc Name: {AccName} Balance: {balance}";
        }
    }
}
