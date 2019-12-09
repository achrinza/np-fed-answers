using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oct2019Test
{
    public class Van : Vehicle
    {
        private int numberOfSeats;
        public int NumberOfSeats { get => numberOfSeats; set => numberOfSeats = value; }

        public Van() { }

        public Van(string plateNumber, string brand, double rentalRate, int numberOfSeats) : base(plateNumber, brand, rentalRate)
        {
            NumberOfSeats = numberOfSeats;
        }

        public override double CalculateRentalCost(int noOfDays)
        {
            return noOfDays * RentalRate;
        }

        public override string ToString()
        {
            return base.ToString() + $"    Number of Seats: {numberOfSeats}";
        }
    }
}
