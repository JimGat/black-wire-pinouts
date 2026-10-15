# WS-C5-35 camera/battery specimen: contributor test record

Contributor: @jimgat

Reported: 2026-10-15

Assembly: ESP32-C5-Touch-LCD-3.5-C / SKU 35419. Exact PCB revision unknown. Tests were performed and reported by the contributor, not independently repeated by the reference maintainer.

## Map versus function reference

The 32 rows retain manufacturer schematic numbering. No claim is made that a physical mating-face orientation or pin-1 drawing has been independently established. The native functions-only coverage badge remains intentional.

## Disconnected native GPIO routes

Camera/battery specimen SKU 35419: @jimgat confirmed by unpowered continuity from the J3 contact to the unconnected 0-ohm selector pad that the labeled GPIO0, GPIO1, GPIO9, U0TXD/GPIO11 and U0RXD/GPIO12 routes are not connected through to their native ESP32 GPIOs on this specimen. Camera routes (GPIO0/1/11/12) and SDCS (GPIO9) are selected instead per the schematic selector matrix. Disabling the camera in firmware does not reconnect an unpopulated hardware route. Do not assume the same routing on every camera-model board or revision. GPIO4/R60 is an additional onboard selector, not another numbered spare J3 GPIO.

Continuity method reported for the selector tests: continuity/beep mode, battery disconnected and no USB connection; J3 contact to the unconnected selector pad. Resistor identities and alternate functions come from the manufacturer schematic.

## GPS and shared BOOT line

ATGM336H GPS: @jimgat reports working receive-only GPS with UART1 RX=GPIO28, ESP32 UART TX disabled, 9600 baud and common ground. GPIO28 also shares the BOOT button: continuity confirmed by @jimgat. Holding GPIO28 to GND during reset/power-up for more than 100 ms entered boot mode in the contributor test; this is an observed test condition, not a specified minimum timing. A connected external device must tolerate that line being pulled to GND. Do not press BOOT against an actively driven GPS TX/push-pull output; isolate or disconnect the driver first. GPIO28 cannot be treated as an independent input while BOOT is used; application input and BOOT operation are not simultaneously independent.

## External I2C

Contributor @jimgat functionally verified external I2C on the tested camera/battery specimen by connecting an external air-quality sensor and successfully polling it. Sensor model, I2C address, bus speed, supply voltage and pull-up arrangement were not supplied; no general electrical limits or compatibility with other sensors are inferred. Manufacturer schematic/BSP assignments are ESP32_SCL=GPIO26 (schematic J3 pin 25) and ESP32_SDA=GPIO27 (schematic J3 pin 27). The reported polling test verifies external-bus operation on this specimen; it does not independently establish physical mating-face orientation or separate continuity measurements for each contact.

## Supply and control observations

### VBUS (Schematic pin 1)

Rear sticker label: 5V. Contributor @jimgat confirms continuity to the 5 V bus before the 3.3 V regulator, and reports that this contact can accept supply voltage and provides voltage with USB connected. Not a 5 V buck-boost output. Current/power handling, allowed input range, reverse-current protection and simultaneous USB/external-supply safety have not been qualified; do not assume safe backfeeding or parallel supplies.

### VBAT1 (Schematic pin 2)

Contributor @jimgat confirms battery voltage by continuity and voltage measurement to GND. Supplied battery: 500 mAh (capacity, not a current rating). Not a regulated 3.3 V output. Header-current capability and charging-circuit behavior with an external battery are unknown; external battery/parallel battery wiring is not qualified.

### GND (Schematic pin 3)

Contributor @jimgat confirms continuity for all J3 ground contacts on the tested camera/battery specimen. Current capacity and physical mating-face orientation have not been qualified.

### CHIP_PU (Schematic pin 22)

Rear sticker label: RST. Contributor @jimgat functionally confirms that pulling this contact to GND resets the device. Reset/enable signal, not a spare GPIO.

### PWRON (Schematic pin 24)

Rear sticker label: PWR. Contributor @jimgat functionally confirms that a momentary connection to GND with the unit off powers it on; holding to GND for 5 seconds while powered turns it off. Power-control signal, not a spare GPIO.

All J3 ground contacts are reported continuity-tested; their schematic positions are 3, 4, 29 and 30.

## Evidence boundaries

The external I2C polling, GPS, voltage, reset, power-button and BOOT observations are functional/electrical contributor evidence. No exact voltage readings, instrument specifications, current limits, battery chemistry, charger design, protection topology or universal BOOT minimum pulse width were supplied. No such values are inferred. Unknown external power and charging behavior remains unknown.
