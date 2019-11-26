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

namespace CashCardApp
{
    class Program
    {
        static void Main(string[] args)
        {
            List<CashCard> CashCardList = new List<CashCard>();

            InitCardList(CashCardList);
            WriteCardList(CashCardList);

            Console.Write("ID? ");
            string CashCardIDLookupValue = Console.ReadLine();

            CashCard CashCardLookup = CashCardList.Find(x => x.Id == CashCardIDLookupValue);

            if (CashCardLookup == default)
            {
                Console.WriteLine("Error: No card found.");
                Console.ReadKey();
                Environment.Exit(1);
            }

            WriteCardList(new List<CashCard> { CashCardLookup });

            Console.Write("Top up amt? ");
            CashCardLookup.TopUp(Convert.ToDouble(Console.ReadLine()));

            WriteCardList(new List<CashCard> { CashCardLookup });

            Console.ReadKey();
        }

        static void InitCardList(List<CashCard> cardList)
        {
            cardList.AddRange(new List<CashCard>
            {
                new CashCard("001", 25),
                new CashCard("002", 25),
                new CashCard("003", 30),
                new CashCard("004", 30),
                new CashCard("005", 50),
            });
        }

        private static void WriteCardList(List<CashCard> cardList)
        {
            Console.WriteLine("ID".PadRight(4) + "Balance".PadRight(8));
            cardList.ForEach(x =>
            {
                Console.WriteLine($"{x.Id.PadRight(4)}{x.Balance.ToString().PadRight(8)}");
            });
        }
    }
}
