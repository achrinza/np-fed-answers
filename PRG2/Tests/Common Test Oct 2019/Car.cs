using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oct2019Test
{
    public class Car : Vehicle
    {
        private double engineCapacity;

        public double EngineCapacity { get => engineCapacity; set => engineCapacity = value; }

        public Car() { }

        public Car(string plateNumber, string brand, double rentalRate, double engineCapacity) : base(plateNumber, brand, rentalRate)
        {
            EngineCapacity = engineCapacity;
        }

        public override double CalculateRentalCost(int noOfDays)
        {
            return 10 + noOfDays * RentalRate;
        }

        public override string ToString()
        {
            return base.ToString() + $"    Engine Capacity: {EngineCapacity}";
        }
    }
}
