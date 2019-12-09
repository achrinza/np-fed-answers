using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oct2019Test
{
    public class SportsCar : Car
    {
        public SportsCar(string plateNumber, string brand, double rentalRate, double engineCapacity) : base(plateNumber, brand, rentalRate, engineCapacity) { }

        public double CalculateDeposit()
        {
            if (EngineCapacity < 3)
            {
                return 2000;
            }
            else if (EngineCapacity < 4.5)
            {
                return 4000;
            }
            else
            {
                return 5000;
            }
        }
    }
}
