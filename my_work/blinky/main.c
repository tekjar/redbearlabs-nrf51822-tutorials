/* Copyright (c) 2014 Nordic Semiconductor. All Rights Reserved.
 *
 * The information contained herein is property of Nordic Semiconductor ASA.
 * Terms and conditions of usage are described in detail in NORDIC
 * SEMICONDUCTOR STANDARD SOFTWARE LICENSE AGREEMENT.
 *
 * Licensees are granted free, non-transferable use of the information. NO
 * WARRANTY of ANY KIND is provided. This heading must NOT be removed from
 * the file.
 *
 */

/** @file
 *
 * @defgroup blinky_example_main main.c
 * @{
 * @ingroup blinky_example
 * @brief Blinky Example Application main file.
 *
 */

#include <stdbool.h>
#include <stdint.h>
#include "nrf_delay.h"
#include "nrf_gpio.h"
#include "boards.h"

//Check 'nRF51822-Arduino/arduino-1.5.x/hardware/RBL/RBL_nRF51822/cores/RBL_nRF51822/pin_transform.c'
//nrf51822 pin 15 is configured as arduino LED PIN (pin 13)

//don't forget to change RAM section in blinky_gcc_nrf51.ld file to 0x2000

#define LED_MASK 1 << 15

const uint8_t leds_list[1] = {15};

/**
 * @brief Function for application main entry.
 */
int main(void)
{
    // Configure LED-pins as outputs.
    LEDS_CONFIGURE(LED_MASK);

    // Toggle LEDs.
    while (true)
    {
        for (int i = 0; i < 1; i++)
        {
            LEDS_INVERT(1 << leds_list[i]);
            nrf_delay_ms(2000);
        }
    }
}


/** @} */
