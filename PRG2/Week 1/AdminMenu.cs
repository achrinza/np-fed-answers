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

namespace AdminMenu
{
    class Program
    {
        static void Main(string[] args)
        {
            int UserInput;
            bool IsUserInputInt;
            do
            {
                Console.WriteLine("ADMIN MENU"
                    + "\n=========="
                    + "\n[1] Read bicycle info from file"
                    + "\n[2] Display all bicycle info with servicing indication"
                    + "\n[3] Display selected bicycle info"
                    + "\n[4] Add a bicycle"
                    + "\n[5] Perform bicycle maintenance"
                    + "\n[0] Exit"
                );

                Console.Write("Enter your option: ");
                string UserInputRaw = Console.ReadLine();
                IsUserInputInt = int.TryParse(UserInputRaw, out UserInput);

                Console.WriteLine("You have selected option " + UserInputRaw + "\n");
            }
            while (UserInput != 0 || !IsUserInputInt);

            Console.WriteLine("Thank you. Bye-bye!");
            Console.ReadKey();
        }
    }
}
