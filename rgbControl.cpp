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
	lcd->begin(16,1);
	lcd->setColor(red, green, blue);
	lcd->setCursor(0,0); /* first row */
	lcd->write(str1);
	lcd->write(byte(2));
    lcd->write(byte(3));
    lcd->setCursor(2, 1);
    lcd->write(byte(3));
    lcd->write(byte(2));
	sleep(SLEEP_TIME);
}

int main(int argc, char* argv[])
{
	string str1 = argv[1];
	string str2 = argv[2];
	string str3 = argv[3];

	lcd = new upm::Jhd1313m1(I2C_BUS, 0x3e, 0x62);

	while (true) {
		display(str1, "Red", RGB_RED);
		display(str2, "Green", RGB_GRN);
		display(str3, "Blue", RGB_BLU);
	
}	delete lcd;
	return 0;
}
