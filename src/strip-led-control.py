#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""
import RPi.GPIO as GPIO
import argparse
from time import sleep

def tristate(args):
    GPIO.setup(args.led, GPIO.IN)

def turn(args):
    led = args.led
    GPIO.setup(led, GPIO.OUT)
    on = args.on == 'on'
    if on:
        GPIO.output(led,1)
    else:
        GPIO.output(led,0)

def toggle_continuous(args):
    led = args.led
    GPIO.setup(led, GPIO.OUT)
    delay = args.delay/1000.0
    while True:
        GPIO.output(led,0)
        sleep(delay)
        GPIO.output(led,1)
        sleep(delay)
        
def brightness(args):
    led = PWMLED(args.led)
    led.value = args.level/100.0
    input('Hit Enter to exit')
    


def glow_up(led, delay, start, end):
    for brightness in range(start, end + 1):
        led.value = brightness/100.0
        sleep(delay)
    
def glow_down(led, delay, start, end):
    for brightness in range(end, start - 1, -1):
        led.value = brightness/100.0
        sleep(delay)
    
def glow(args):
    start = args.start
    end = args.end
    if end < start:
        fmtstr = 'The start value {} should be less than the end value {}.'
        print(fmtstr.format(start, end))
        return
        
    led = PWMLED(args.led)
    delay = args.time/1000.0/2 # /2 for 1/2 on and 1/2 off time
    step = delay/(end - start)
    while True:
        glow_up(led, step, start, end)
        sleep(args.highw/1000.0)
        glow_down(led, step, start, end)
        sleep(args.loww/1000.0)
        
def main():
    """
    Control LED light strip
    
    """
    parser = argparse.ArgumentParser(description='Contro the raspberry pi GPIO pins.')
    parser.add_argument('-l', '--led', help='LED to test', type=int, default=17)
    
    subparsers = parser.add_subparsers(help='Command to execute')

    parser_s = subparsers.add_parser('turn', help='Turn and LED on/off')
    parser_s.set_defaults(func=turn)
    parser_s.add_argument('on', choices=['on', 'off'])

    parser_s = subparsers.add_parser('toggle', help='toggle a LED continuously')
    parser_s.set_defaults(func=toggle_continuous)
    parser_s.add_argument('-d', '--delay', help='delay in milliseconds', type=int, default=0)

    parser_s = subparsers.add_parser('tristate', help='tristate a LED')
    parser_s.set_defaults(func=tristate)

    parser_s = subparsers.add_parser('bright', help='turns on an led at a specific brightness')
    parser_s.set_defaults(func=brightness)
    parser_s.add_argument('level', type=int, choices=range(1,101))

    parser_s = subparsers.add_parser('glow', help='makes the LED glow')
    parser_s.set_defaults(func=glow)
    parser_s.add_argument('-t', '--time', type=int, default=5000, help="glow interval in milliseconds")
    parser_s.add_argument('-s', '--start', type=int, default=0, choices=range(0,100), help="percent brightness to start with")
    parser_s.add_argument('-e', '--end', type=int, default=100, choices=range(0,100), help="percent brightness to end with")
    parser_s.add_argument('-l', '--loww', type=int, default=1000, help="wait time at low brightness")
    parser_s.add_argument('-b', '--highw', type=int, default=1000, help="wait time at high brightness")

    args = parser.parse_args()
    if len(vars(args)) < 2:
        parser.print_help()
        return
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    args.func(args)
    
if __name__ == "__main__":
    main()