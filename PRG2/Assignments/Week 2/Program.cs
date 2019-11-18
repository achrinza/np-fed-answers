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

namespace Practical2
{
    class Program
    {
        static void Main(string[] args)
        {
            //Question 2
            //Create 5 Student objects

            //Creating Student object 1
            DateTime dob = new DateTime(2000, 10, 13);
            Student s1 = new Student(1, "John Tan", "88552211", dob);

            Student s2 = new Student(2, "Peter Lim", "85678141", new DateTime(2001, 11, 1));
            Student s3 = new Student(3, "David Chan", "88555461", new DateTime(2000, 1, 3));
            Student s4 = new Student(4, "Muhammed Faizal", "98762211", new DateTime(2000, 5, 7));
            Student s5 = new Student(5, "Esther Eng", "83352245", new DateTime(2000, 8, 9));

            List<Student> StudentList = new List<Student> { s1, s2, s3, s4, s5 };

            Console.WriteLine($"{"ID".PadRight(4)} {"Name".PadRight(15)} {"Phone".PadRight(8)} {"Date of Birth".PadRight(12)}");
            
            StudentList.ForEach(x =>
            {
                Console.WriteLine(
                    x.ID.ToString().PadRight(5) +
                    x.Name.PadRight(16) +
                    x.Phone.PadRight(9) +
                    x.DateOfBirth.ToString("dd/MM/yyyy").PadRight(12)
                );
            });

            DisplayOutput(StudentList);

            StudentList.Add(GetStudent());

            DisplayOutput(StudentList);

            bool IsFileValidFormat = true;

            Console.Write("Students.csv (default: ./Students.csv)? ");
            string StudentCSVPath = Console.ReadLine();

            if (StudentCSVPath == "") StudentCSVPath = "./Students.csv";

            List<Student> StudentList2 = new List<Student>();

            try
            {
                using (StreamReader Reader = new StreamReader(StudentCSVPath))
                {
                    int i = 0;
                    while (!Reader.EndOfStream)
                    {
                        string Line = Reader.ReadLine();

                        if (i > 0)
                        {
                            string[] LineArray = Line.Split(',');

                            StudentList2.Add(new Student(
                                Convert.ToInt32(LineArray[0]),
                                LineArray[1],
                                LineArray[2],
                                Convert.ToDateTime(LineArray[3])
                            ));
                        }

                        i++;
                    }
                }
            }
            catch (Exception e)
            {
                IsFileValidFormat = false;
                Console.WriteLine($"Error: {e}");
            }

            if (!IsFileValidFormat)
            {
                Console.ReadKey();
                Environment.Exit(1);
            }

            DisplayOutput(StudentList2);

            List<SalesEmployee> employeeList = new List<SalesEmployee> {
                new SalesEmployee(101, "Angie", 1200, 15000),
                new SalesEmployee(105, "Cindy", 1000, 12000),
                new SalesEmployee(108, "David", 1500, 20000),
                new SalesEmployee(112, "Jason", 3000, 30000),
                new SalesEmployee(127, "Vivian", 2000, 25000),
            };

            Console.WriteLine($"{"ID".PadRight(5)}{"Name".PadRight(7)}{"Basic Salary".PadRight(13)}{"Sales".PadRight(5)}");

            employeeList.ForEach(x =>
            {
                Console.WriteLine($"{x.id.ToString().PadRight(5)}{x.name.PadRight(7)}{x.basicSalary.ToString().PadRight(13)}{x.sales.ToString().PadRight(5)}");
            });

            Console.ReadKey();
        }

        public static void DisplayOutput(List<Student> aList)
        {
            Console.WriteLine($"{"ID".PadRight(4)} {"Name".PadRight(15)} {"Phone".PadRight(8)} {"Date of Birth".PadRight(12)}");

            for (int i = 0; i < aList.Count; i++)
            {
                Student x = aList[i];

                Console.WriteLine(
                    x.ID.ToString().PadRight(5) +
                    x.Name.PadRight(16) +
                    x.Phone.PadRight(9) +
                    x.DateOfBirth.ToString("dd/MM/yyyy").PadRight(12)
                );
            }
        }

        public static Student GetStudent()
        {
            Console.Write("ID? ");
            int id = Convert.ToInt32(Console.ReadLine());
            Console.Write("Name? ");
            string name = Console.ReadLine();
            Console.Write("Phone no.? ");
            string phone = Console.ReadLine();
            Console.Write("Date of birth? ");
            DateTime dob = Convert.ToDateTime(Console.ReadLine());

            return new Student(id, name, phone, dob);
        }

        public class SalesEmployee
        {
            public int id { get; set; }
            public string name { get; set; }
            public double basicSalary { get; set; }
            public double sales { get; set; }

            public SalesEmployee (int id, string name, double basicSalary, double sales) {
                this.id = id;
                this.name = name;
                this.basicSalary = basicSalary;
                this.sales = sales;
            }
        }
    }
}
