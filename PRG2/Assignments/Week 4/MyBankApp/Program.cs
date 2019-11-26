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

namespace MyBankApp
{
    class Program
    {
        static void Main(string[] args)
        {
            List<SavingsAccount> SavingsAccList = new List<SavingsAccount>();
            bool IsValidOption = true;
            bool IsValidFileFormat = true;
            int UserOption = 0;

            try
            {
                using (StreamReader reader = new StreamReader("./savings_account.csv"))
                {
                    int i = 0;

                    while (!reader.EndOfStream)
                    {
                        string Line = reader.ReadLine();

                        if (i > 0)
                        {
                            string[] LineSplit = Line.Split(',');

                            try
                            {
                                SavingsAccList.Add(new SavingsAccount(
                                    LineSplit[0],
                                    LineSplit[1],
                                    Convert.ToDouble(LineSplit[2]),
                                    Convert.ToDouble(LineSplit[3])
                                ));
                            }
                            catch (Exception)
                            {
                                Console.WriteLine("Error: Invalid file format.");
                                IsValidFileFormat = false;
                            }
                        }

                        i++;
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Error: Cannot load file.");
                IsValidFileFormat = false;
            }

            if (!IsValidFileFormat)
            {
                Console.ReadKey();
                Environment.Exit(1);
            }


            while (true)
            {
                IsValidOption = true;

                Console.Write(
                    "Menu\n" +
                    "[1] Display all accounts\n" +
                    "[2] Deposit\n" +
                    "[3] Withdraw\n" +
                    "[4] Display all accounts with interest\n" +
                    "[0] Exit\n" +
                    "Enter option: "
                );

                try
                {
                    UserOption = Convert.ToInt32(Console.ReadLine());
                }
                catch (Exception)
                {
                    Console.WriteLine("Invalid option.");
                    IsValidOption = false;

                }

                Console.WriteLine();


                if (IsValidOption)
                {

                    switch (UserOption)
                    {
                        case 0:
                            Environment.Exit(0);
                            break;
                        case 1:
                            DisplayAll(SavingsAccList);
                            break;
                        case 2:
                            SavingsAccount SelectedDepositAccount;
                            Console.Write("Enter the Account Number: ");
                            SelectedDepositAccount = SearchAcc(SavingsAccList, Console.ReadLine());
                            if (SelectedDepositAccount == default)
                            {
                                Console.WriteLine("Error: Account not found.");
                                IsValidOption = false;
                                break;
                            }
                            Console.Write("Amount to deposit: ");
                            double CurrentAmt = SelectedDepositAccount.Balance;
                            double DepositAmt = Convert.ToDouble(Console.ReadLine());
                            if (DepositAmt < 0)
                            {
                                Console.WriteLine("Error: Invalid deposit amt.");
                                IsValidOption = false;
                                break;
                            }
                            SelectedDepositAccount.Deposit(DepositAmt);
                            Console.WriteLine($"${DepositAmt} deposit {(CurrentAmt == SelectedDepositAccount.Balance ? "un" : "")}sucessful");
                            break;
                        case 3:
                            Console.Write("Enter the Account Number: ");
                            SavingsAccount SelectedWithdrawAccount = SearchAcc(SavingsAccList, Console.ReadLine());
                            if (SelectedWithdrawAccount == default)
                            {
                                Console.WriteLine("Error: Account not found.");
                                IsValidOption = false;
                                break;
                            }
                            Console.Write("Amount to withdraw: ");
                            double WithdrawlAmt = Convert.ToDouble(Console.ReadLine());
                            if (WithdrawlAmt < 0)
                            {
                                Console.WriteLine("Error: Invalid withdrawl amt.");
                                IsValidOption = false;
                                break;
                            }
                            bool IsWithdrawlSuccessful = SelectedWithdrawAccount.Withdraw(WithdrawlAmt);
                            if (!IsWithdrawlSuccessful)
                            {
                                Console.WriteLine("Insufficient funds.");
                                IsValidOption = false;
                                break;
                            }
                            Console.WriteLine($"${WithdrawlAmt} withdrawn successfully");
                            break;
                        case 4:
                            SavingsAccList.ForEach(x =>
                            {
                                Console.WriteLine($"Acc No: {x.AccNo} Acc Name: {x.AccName} Balance: {x.Balance} Rate: {x.Rate} Interest: {x.CalculateInterest()}");
                            });
                            break;
                        default:
                            Console.WriteLine("Invalid option.");
                            break;
                    }
                }

                Console.WriteLine();

                //Console.ReadKey();

                //if (!IsValidOption) Environment.Exit(1);
            }
        }

        static void DisplayAll(List<SavingsAccount> sList)
        {
            sList.ForEach(x => Console.WriteLine(x.ToString()));
        }

        static SavingsAccount SearchAcc(List<SavingsAccount> sList, string accNo)
        {
            return sList.Find(x => x.AccNo == accNo);
        }
    }
}
