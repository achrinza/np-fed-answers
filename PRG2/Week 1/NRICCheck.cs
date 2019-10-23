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

namespace NRICCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            bool IsICValid;
            Console.Write("Enter the IC to be validated: ");
            string UserICInput = Console.ReadLine();
            IsICValid = ValidateNRIC(UserICInput);

            Console.WriteLine("Validity of the IC: " + (IsICValid ? "True" : "False"));
            Console.ReadKey();
        }

        private static bool ValidateNRIC(string UserICInput)
        {
            char[] ICCheckDigitRef = { 'J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' };
            int[] ICCalcMultiplier = { 2, 7, 6, 5, 4, 3, 2 };
            bool IsICValid = true;
            if (UserICInput.Length != 9) IsICValid = false;

            if (IsICValid) if (UserICInput[0] != 'T') IsICValid = false;

            if (IsICValid == true)
            {
                List<char> UserICNoOnly = UserICInput.Substring(1, 7).ToList();
                int ICDigitsCalc = 0;

                foreach (var item in UserICNoOnly.Select((x, i) => new { x, i }))
                {
                    int x = Convert.ToInt32(item.x.ToString());
                    int i = item.i;

                    ICDigitsCalc += x * ICCalcMultiplier[i];
                }

                ICDigitsCalc = (ICDigitsCalc + 4) % 11;

                if (UserICInput[8] == ICCheckDigitRef[ICDigitsCalc])
                {
                    IsICValid = true;
                }
                else
                {
                    IsICValid = false;
                }
            }

            return IsICValid;
        }
    }
}
