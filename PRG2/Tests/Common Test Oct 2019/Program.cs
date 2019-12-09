using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Oct2019Test
{
    class Program
    {
        static void DisplayVansWithNoOfSeats(List<Van> vList, int noOfSeats)
        {
            List<Van> vListSearch = vList.FindAll(x => x.NumberOfSeats == noOfSeats);

            if (vListSearch.Count() > 0)
            {
                vListSearch.ForEach(x =>
                {
                    Console.WriteLine(x.ToString());
                });
            }
            else
            {
                Console.WriteLine("No van was found");
            }
        }
        
        static void DisplayCars(List<Vehicle> vehicleList)
        {
            Console.WriteLine(
                "Plate Number".PadRight(14) +
                "Brand".PadRight(8) +
                "Rental Rate".PadRight(13) +
                "Engine Capacity".PadRight(17) +
                "Deposit"
            );

            vehicleList.OfType<Car>().ToList<Car>().ForEach(x =>
            {
                Console.WriteLine(
                    x.PlateNumber.PadRight(14) +
                    x.Brand.PadRight(8) +
                    x.RentalRate.ToString("0.00").PadLeft(11).PadRight(2) +
                    x.EngineCapacity.ToString("0.0").PadLeft(15).PadRight(2) +
                    (x is SportsCar ? ((SportsCar)x).CalculateDeposit().ToString() : "Not required")
                );
            });
        }

        static void Main(string[] args)
        {
            List<Van> vanList = new List<Van>();

            using (StreamReader reader = new StreamReader("./van.csv"))
            {
                int i = 0;
                while (!reader.EndOfStream)
                {
                    string line = reader.ReadLine();

                    if (i > 0)
                    {
                        string[] lineSplit = line.Split(',');
                        vanList.Add(new Van(
                            lineSplit[0],
                            lineSplit[1],
                            Convert.ToDouble(lineSplit[2]),
                            Convert.ToInt32(lineSplit[3])
                        ));
                    }

                    i++;
                }
            }

            DisplayVansWithNoOfSeats(vanList, Convert.ToInt32(Console.ReadLine()));

            List<Vehicle> vehicleList = new List<Vehicle>(); 

            do
            {
                Console.Write("Enter the vehicle type (Car/SportsCar/Van): ");
                string vehicleType = Console.ReadLine();

                if (vehicleType == "Exit") break;

                Console.Write("Enter the plate number: ");
                string plateNumber = Console.ReadLine();
                Console.Write("Enter the brand: ");
                string brand = Console.ReadLine();
                Console.Write("Enter the rental rate: ");
                double rentalRate = Convert.ToDouble(Console.ReadLine());

                double engineCapacity = default;
                int noOfSeats = default;

                switch (vehicleType)
                {
                    case "Car":
                    case "SportsCar":
                        Console.Write("Enter the engine capacity: ");
                        engineCapacity = Convert.ToDouble(Console.ReadLine());
                        break;
                    case "Van":
                        Console.Write("Enter the number of seats: ");
                        noOfSeats = Convert.ToInt32(Console.ReadLine());
                        break;
                }

                switch (vehicleType)
                {
                    case "Car":
                        vehicleList.Add(new Car(
                            plateNumber,
                            brand,
                            rentalRate,
                            engineCapacity
                        ));
                        break;
                    case "SportsCar":
                        vehicleList.Add(new SportsCar(
                            plateNumber,
                            brand,
                            rentalRate,
                            engineCapacity
                        ));
                        break;
                    case "Van":
                        vehicleList.Add(new Van(
                            plateNumber,
                            brand,
                            rentalRate,
                            noOfSeats
                        ));
                        break;
                }

                Console.WriteLine($"A {vehicleType} object created");
            }
            while (true);

            DisplayCars(vehicleList);
            Console.ReadLine();
        }
    }
}
