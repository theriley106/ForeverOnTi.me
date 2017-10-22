/*
 * modified demo script from https://github.com/96boards/Sensor_Mezzanine_Getting_Started
 */

#include <string>
#include "upm/jhd1313m1.hpp"
#include <iostream>
#include <stdio.h>
#include <time.h>

#define I2C_BUS  0
#define RGB_WHT 0xff,0xff,0xff
#define RGB_RED 0xff,0x00,0x00
#define RGB_GRN 0x00,0xff,0x00
#define RGB_BLU 0x00,0x00,0xff
#define SLEEP_TIME 2

using namespace std;
upm::Jhd1313m1* lcd;

// Get current date/time, format is YYYY-MM-DD.HH:mm:ss
const std::string currentDateTime() {
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    // Visit http://en.cppreference.com/w/cpp/chrono/c/strftime
    // for more information about date/time format
    strftime(buf, sizeof(buf), "%m-%d.%X", &tstruct);

    return buf;
}

void display(string str1, string str2, int red, int green, int blue)
{
	lcd->clear();
	lcd->setColor(red, green, blue);
	lcd->setCursor(0,0); /* first row */
	lcd->write(str1);
	lcd->setCursor(1,1); 
	lcd->write(str2);
	sleep(2);
}

int main(int argc, char* argv[])
{
	string str1 = argv[1];
	string str2 = argv[2];
	string str3 = argv[3];

	lcd = new upm::Jhd1313m1(I2C_BUS, 0x3e, 0x62);

	while (true) {
		str1 = argv[1];
		str2 = argv[2];
		str3 = argv[3];
		str4 = argv[4];
		display(str1, str2, RGB_GRN);
		display(str3, str4, RGB_GRN);
}	delete lcd;
	return 0;
}
