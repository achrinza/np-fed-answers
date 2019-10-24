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

namespace Practical2
{
    class Student
    {
        public int ID { get; set; }

        public string Name { get; set; }

        public string Phone { get; set; }

        public DateTime DateOfBirth { get; set; }

        public Student(int id, string name, string hp, DateTime dob)
        {
            ID = id;
            Name = name;
            Phone = hp;
            DateOfBirth = dob;
        }
    }
}
