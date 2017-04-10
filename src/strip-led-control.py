#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""
import RPi.GPIO as GPIO
import argparse
from time import sleep
import signal
import sys

gpios = [17, 18, 22, 23]
debug = False

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
    global gpios
    led = args.led
    freq = args.freq
    duty = args.level
    gpios_en(gpios, False) # disable gpios
    if led == 17 or led == 18:
        qs = gpios_path(gpios, 'one')
        gpios_en(qs)
        if led == 17:
            gpios_on(18)
        else:
            gpios_on(17)
    elif led == 22 or led == 23:
        qs = gpios_path(gpios, 'two')
        gpios_en(qs)
        if led == 22:
            gpios_on(23)
        else:
            gpios_on(22)
    else:
        gpios_en(led, True)
    p = GPIO.PWM(led, freq)
    p.start(duty)    
    input('Hit Enter To Stop')
    p.stop()
    GPIO.cleanup()
    
gpiosa = lambda gpios: gpios if type(gpios) == list else [gpios]

def gpios_en(gpios, en=True):
    gpios = gpiosa(gpios)
    if en:
        state = GPIO.OUT
    else:
        state = GPIO.IN
        
    for gpio in gpios:
        GPIO.setup(gpio, state)

def gpios_on(gpios, on='on'):
    gpios = gpiosa(gpios)
    value = 1 if on == 'on' else 0
    for gpio in gpios:
        GPIO.output(gpio, value) 

def gpios_path(gpios, path):
    if path == 'one':
        return gpios[:2]
    else:
        return gpios[2:]
        
def path(args):
    global gpios
    gpios_en(gpios, False) # disable gpios
    qs = gpios_path(gpios, args.path)    
    gpios_en(qs, True)
    gpios_on(qs, args.on)

def glow_up(led, delay, start, end):
    global debug
    stop_in = 0
    for brightness in range(start, end + 1):
        led.ChangeDutyCycle(brightness)
        sleep(delay)
        if debug:
            if stop_in == 0:
                msg = "{} {} {} Enter stop in value =>"
                strfmt = msg.format(start, end, brightness)
                stop_in = int(input(strfmt) or "0")
            else:
                stop_in -= 1
    
def glow_down(led, delay, start, end):
    for brightness in range(end, start - 1, -1):
        led.ChangeDutyCycle(brightness)
        sleep(delay)

def start_end(args):
    start = args.start
    end = args.end
    if end < start:
        fmtstr = 'The start value {} should be less than the end value {}.'
        msg = fmtstr.format(start, end)
        raise ValueError(msg)
    return start, end

def glow(args):
    start, end = start_end(args)
    gpios_en(gpios) 
    gpios_on(gpios, False) 
    qs = gpios_path(gpios, args.path)
    gpios_en(qs, True)
    gpios_on(qs, 'on')
    if args.top == 'top':
        led = GPIO.PWM(qs[1], 1000)
    else:
        led = GPIO.PWM(qs[0], 1000)
    led.start(start)
    
    delay = args.time/1000.0/2 # /2 for 1/2 on and 1/2 off time
    step = delay/(end - start)
    while True:
        glow_up(led, step, start, end)
        sleep(args.highw/1000.0)
        glow_down(led, step, start, end)
        sleep(args.loww/1000.0)

def glow2(args):
    start, end = start_end(args)
    
    delay = args.time/1000.0/2 # /2 for 1/2 on and 1/2 off time
    step = delay/(end - start)
    toggle = True

    gpios_en(gpios, False) # disable gpios
    one = 0
    two = 0
    toggle = 0
    while True:
        toggle = toggle + 1 if toggle < 1000 else 0
        qs = gpios_path(gpios, 'one') if toggle % 2 else  gpios_path(gpios, 'two')
        gpios_en(qs, True)
        if toggle % 2:
            one = one + 1 if one < 100 else 0
            if one < 30:
                gpios_on(qs, 'on')
            else:
                gpios_on(qs, 'off')
        else:
            two = two + 1 if two < 100 else 0            
            gpios_on(qs, 'on')
        #sleep(0.00001)
        if toggle % 2:
            if one < 50:
                gpios_on(qs, 'off')
        else:
            gpios_on(qs, 'off')            
        gpios_en(qs, False)
        
def signal_handler(signal, frame):
        global gpios
        print('You pressed Ctrl+C!')
        gpios_en(gpios, False) # disable gpios
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    """
    Control LED light strip
    
    """
    on_off = lambda parser: parser.add_argument('on', choices=['on', 'off'])

    parser = argparse.ArgumentParser(description='Contro the raspberry pi GPIO pins.')
    parser.add_argument('-l', '--led', help='LED to test', type=int, default=17)
    parser.add_argument('-s', '--stop', help='Stop at debug break points', action='store_true')
    
    subparsers = parser.add_subparsers(help='Command to execute')

    parser_s = subparsers.add_parser('turn', help='Turn and LED on/off')
    parser_s.set_defaults(func=turn)
    parser_s.add_argument('on', choices=['on', 'off'])

    parser_s = subparsers.add_parser('toggle', help='toggle a LED continuously')
    parser_s.set_defaults(func=toggle_continuous)
    parser_s.add_argument('-d', '--delay', help='delay in milliseconds', type=int, default=0)

    parser_s = subparsers.add_parser('tristate', help='tristate a LED')
    parser_s.set_defaults(func=tristate)

    path = lambda parser: parser.add_argument('path', choices=['one', 'two'])

    parser_s = subparsers.add_parser('path', help='select polarity of LED path')
    parser_s.set_defaults(func=path)
    on_off(parser_s)
    path(parser_s)
    
    parser_s = subparsers.add_parser('bright', help='turns on an led at a specific brightness')
    parser_s.set_defaults(func=brightness)
    parser_s.add_argument('level', type=int, choices=range(1,101))
    parser_s.add_argument('-f', '--freq', help='frequency in hz', type=int, default=1000)

    interval = lambda parser: parser.add_argument('-t', '--time', type=int, default=5000, help="glow interval in milliseconds")
    start = lambda parser: parser.add_argument('-s', '--start', type=int, default=0, choices=range(0,100), help="percent brightness to start with")
    end = lambda parser: parser.add_argument('-e', '--end', type=int, default=100, choices=range(0,100), help="percent brightness to end with")
    loww = lambda parser: parser.add_argument('-l', '--loww', type=int, default=1000, help="wait time at low brightness")
    highw = lambda parser: parser.add_argument('-b', '--highw', type=int, default=1000, help="wait time at high brightness")
    top = lambda parser: parser.add_argument('-q', '--top', choices=['top','bottom'], help="transistor that toggles", default='bottom')

    parser_s = subparsers.add_parser('glow', help='makes the LED glow')
    parser_s.set_defaults(func=glow)
    interval(parser_s)
    start(parser_s)
    end(parser_s)
    loww(parser_s)
    highw(parser_s)
    path(parser_s)
    top(parser_s)

    parser_s = subparsers.add_parser('glow2', help='makes two LEDs glow')
    parser_s.set_defaults(func=glow2)
    interval(parser_s)
    start(parser_s)
    end(parser_s)
    loww(parser_s)
    highw(parser_s)

    args = parser.parse_args()
    if len(vars(args)) < 2:
        parser.print_help()
        return
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    global debug
    debug = args.stop
    args.func(args)
    
if __name__ == "__main__":
    main()