//
// (c) 2019 Rifa I. Achrinza
// This code is licensed under MIT license (See LICENSE.txt for details)
// SPDX-Short-Identifier: MIT
//

namespace CashCardApp
{
    class CashCard
    {
        private string id;
        private double balance;

        public string Id { get => id; set => id = value; }
        public double Balance { get => balance; set => balance = value; }

        public CashCard() { }
        public CashCard(string id, double balance)
        {
            this.Id = id;
            this.Balance = balance;
        }

        public void TopUp(double amt)
        {
            Balance += amt;
        }

        public bool Deduct(double amt)
        {
            if (amt > Balance) return false;

            Balance -= amt;
            return true;
        }

        public override string ToString()
        {
            return $"ID: {Id}\nBalance: {Balance}";
        }
    }
}
