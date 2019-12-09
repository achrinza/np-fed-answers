using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oct2019Test
{
    public abstract class Vehicle
    {
        private string plateNumber;
        private string brand;
        private double rentalRate;

        public string PlateNumber { get => plateNumber; set => plateNumber = value; }
        public string Brand { get => brand; set => brand = value; }
        public double RentalRate { get => rentalRate; set => rentalRate = value; }

        public Vehicle() { }

        public Vehicle(string plateNumber, string brand, double rentalRate)
        {
            PlateNumber = plateNumber;
            Brand = brand;
            RentalRate = rentalRate;
        }

        public abstract double CalculateRentalCost(int noOfDays);

        public override string ToString()
        {
            return $"Plate Number: {PlateNumber}    Brand: {Brand}    Rental Rate: {RentalRate}";
        }
    }
}
