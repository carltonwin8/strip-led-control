# LED Light Strip Control

Use the raspberry pi to control a LED light strip.

## Schematic

![](images/schematic.png)

The test LED circuit between the signals LED+ and LED- will be replaced
with LED strip once the circuit and software has been debugged and working.

## Implementation Plan

### Phase 1

Create the circuit without the following components.
  - R3, R4, Q3, Q3

Write code to keep GPIO18 high and use GPIO17 to control brightness via the PWM.

### Phase 2

Create the circuit with all the components.
Write code to that centralizes the GPIO control to one routine that makes sure
that `Q1` and `Q2` are never turned on at the same time.
Also make sure that `Q3` and `Q4` are never turned on at the same time.

Verify that the both LED1 and LED2 can be turned on by the circuit.

### Phase 3

Once [Phase 2] is operational solder down the components on a plated through
hole board and verify the circuit works with the test LED setup shown in the
schematics.

### Phase 4

Replace the LED test setup and verify the circuit board works the LED strip.

### Phase 5

Write software to allow Internet control of the board.
