# colorgamut
This code is for calculating the color gamut of a led display. It uses a Matlab to show the gamut areas

Color gamut is a important specs in led display, especially in TV studio, XR and VP projects. even though many suppliers claim that their led lamp has 
reach xx% of BT2020, but for most of the time, they do not even know what color gamut is, and how to measure it. 

To measure the color gamut, it need a specific device which is called color meter. while for most company they only have a brightness meter that can measure the 
brightness and the color coordinates. So the code here is to teach the company with only brightness meter to measure the color gamut.

The theory is that, the color gamut is the LED display's R,G,B. 
Then we can use the brightness meter to measure the color coordinates of the R,G,B. Then we can calculate the intersection area of the tested R,G,B with the existing REC709, DCI, and REC2020's area.
Then Using its intersection area to divide the Areas of REC709, DCI, and REC2020. Then we would know the portion of the color space.

Or you can directly contact with professional led display supplier who can provide the color space data. Like you can contact with https://tepixel.com
