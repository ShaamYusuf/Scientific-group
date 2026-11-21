BIT 2118: SCIENTIFIC COMPUTING

TASK 02: NumPy Arrays and Numerical Computation
OBJECTIVE
To use NumPy arrays to analyze temperature readings and convert temperatures from Celsius to Fahrenheit.

INPUT DATA
24 hourly temperature readings in degrees Celsius.

MATHEMATICAL OPERTAIONS

* Calculate the mean, minimum and maximum temperatures.
* Convert the temperatures using F = 1.8C + 32.

RESULTS AND INTERPRETATION
The mean temperature was 23.12°C, the minimum was 17.50°C and the maximum was 29.40°C.

PARAMETER CHANGE
Changing 18.5°C to 20.5°C increases the mean by approximately 0.08°C,while the minimum and maximum remain unchanged.

RELATED REAL-WORLD EXAMPLE
TASK 02.1:
OBJECTIVE
This project demonstrates how NumPy arrays can be used to store and analyse electricity consumption data in a household over a 24-hour period.The program calculates the average, minimum and maximum hourly electricity consumption and converts all measurements from kilowatt-hours (kWh) to watt-hours (Wh).

INPUT DATA
The program uses the following 24 hourly electricity consumption readings:
[0.5, 0.4, 0.3, 0.3, 0.4, 0.6, 0.8, 1.2, 1.5, 1.0, 0.9, 0.7, 0.8, 0.9, 1.1, 1.3, 1.6, 2.0, 2.5, 2.2, 1.8, 1.4, 1.0, 0.7]
The readings are stored in a NumPy array called electricity_kwh.

MATHEMATICAL OPERTAIONS

*np.mean() calculates the average hourly electricity consumption.
*np.min() identifies the lowest hourly consumption.
*np.max() identifies the highest hourly consumption.
*electricity_kwh * 1000 converts all readings from kWh to Wh.

RESULTS
Average hourly consumption: 1.08 kWh
Minimum hourly consumption: 0.30 kWh
Maximum hourly consumption: 2.50 kWh
First six readings in Wh: [500. 400. 300. 300. 400. 600.]

INTERPRETATION
The results show that the household consumed approximately 1.09 kWh of electricity per hour on average.
The minimum consumption was 0.30 kWh, while the maximum consumption was 2.50 kWh.
The higher consumption readings may indicate periods when several electrical appliances were being used simultaneously.

TASK 03: Mathematical Functions and Vectorization
OBJECTIVE
To compare a Python loop with NumPy vectorization when processing network latency measurements.

INPUT DATA
One million simulated latency measurements between 5 and 250 milliseconds.

MATHEMATICAL OPERTAIONS
Convert milliseconds to seconds, square the values and measure execution time.

RESULTS

* Loop execution time: 0.6401 s
* Vectorized execution time: 0.0122 s
* Approximate speed-up: 52.4 x

INTERPRETATION
NumPy vectorization is generally faster because it uses optimized numerical operations, making it useful for large datasets.

PARAMETER CHANGE
Reducing the measurements from 1,000,000 to 100,000 generaly reduces execution time for both methods.The speed-up may also change.

RELATED REAL-WORLD EXAMPLE
PART 03.1:
OBJECTIVE
This project demonstrates how NumPy vectorization can be applied in banking and financial transaction processing.The program simulates one million bank transactions recorded in Kenyan Shillings (KES). It converts the transaction amounts into US Dollars (USD) and calculates the square of each converted amount.The program also compares the execution time of a traditional Python loop with NumPy vectorization.

INPUT DATA
One million simulated trasaction amounts using:rng.uniform(100,100000,1_000_000)
The exchange rate used is: exchange_rate = 130.0

MATHEMATICAL OPERTAIONS
*Generates one million random bank transaction amounts.
*Converts each transaction from KES to USD.
*Squares each converted transaction amount.
*Uses a traditional Python loop to process the transactions.
*Uses NumPy vectorization to perform the same calculations.
*Uses the timeit module to compare execution times.

RESULTS

* First five squared transaction values: [354649.65228352 114264.57280849 436351.01960614 288014.40903104
   5349.59131355]
* Loop time: 0.4528 s          Vectorized time: 0.0123 s
* Approximate speed-up: 36.7x


INTERPRETATION
The results demonstrate how transaction amounts can be converted from Kenyan Shillings into US Dollars and processed using NumPy.
The squared values represent the square of each converted transaction amount and can be used in certain statistical calculations.
The execution time comparison demonstrates how NumPy vectorization can process large amounts of financial data more efficiently than traditional Python loops.



