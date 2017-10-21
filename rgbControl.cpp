/*
 * modified demo script from https://github.com/96boards/Sensor_Mezzanine_Getting_Started
 */

#include <string>
#include "upm/jhd1313m1.hpp"

#define I2C_BUS  0
#define RGB_WHT 0xff,0xff,0xff
#define RGB_RED 0xff,0x00,0x00
#define RGB_GRN 0x00,0xff,0x00
#define RGB_BLU 0x00,0x00,0xff
#define SLEEP_TIME 2

using namespace std;
upm::Jhd1313m1* lcd;

void display(string str1, string str2, int red, int green, int blue)
{
	lcd->clear();
	lcd->setColor(red, green, blue);
	lcd->setCursor(0,0); /* first row */
	lcd->write(str1);
	sleep(SLEEP_TIME);
}

int main(int argc, char* argv[])
{
	string str1 = "test";
	string str2 = "test";
	string str3 = "test";
	str1 = argv[1];
	str2 = argv[2];
	str3 = argv[3];

	while (true) {
		display(str1, "Red", RGB_RED);
		display(str2, "Green", RGB_GRN);
		display(str3, "Blue", RGB_BLU);
	
}	delete lcd;
	return 0;
}
