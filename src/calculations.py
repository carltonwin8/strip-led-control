#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""

def main():
    case3()
    
def case3():
    VCC = 30 # power supply volts
    ips = 0.12 # power supply max current
    power = VCC * ips
    msg = "The power supply provides {} amps at {} volts for {:.2f} watts of power"
    fmtStr = msg.format(ips, VCC, power)
    print(fmtStr)
    
    r_npn_b = 820
    msg = 'lower npn connnects to GPIO via {} ohm resistor'
    fmtStr = msg.format(r_npn_b)
    print(fmtStr)

    gpio_high = 3.3
    i_r_npn_b = gpio_high / r_npn_b
    msg = 'Current provided to base of npn at {}v is {:.3f}'
    fmtStr = msg.format(gpio_high, i_r_npn_b)
    print(fmtStr)
    
    hfe = 30 # nte373 hfe min
    i_npn_ce = hfe * i_r_npn_b
    msg = 'Current provided through the npn is {:.3f} for a beta of {}'
    fmtStr = msg.format(i_npn_ce, hfe)
    print(fmtStr)
    
    i_pnp_c_2_e = 0.121 # for the pnp to be similar to the npn above
    i_pnp_b_2_gnd = i_pnp_c_2_e / hfe
    i_pnp_ce = hfe * i_pnp_b_2_gnd
    pnp_c = VCC 
    msg = 'The pnp base to gnd current required is {:.3f} for a beta of {} so the '
    msg += 'current through pnp is {:.3f}.'
    fmtStr = msg.format(i_pnp_b_2_gnd, hfe, i_pnp_ce)
    print(fmtStr)

    i_pnp_pd = VCC / i_pnp_b_2_gnd
    pwr_pd =  VCC * i_pnp_b_2_gnd
    msg = 'The pull down should be {:.1f} for above V I with a PD of {:.3f}'
    fmtStr = msg.format(i_pnp_pd, pwr_pd)
    print(fmtStr)

    r_pnp_b_pd = 4000
    i_pnp_b_pd = VCC / r_pnp_b_pd
    pwr_pnp_b_pd = VCC * i_pnp_b_pd
    msg = 'For a {} pd the current is {:.3f} and PD is {:.3f}'
    fmtStr = msg.format(r_pnp_b_pd, i_pnp_b_pd, pwr_pnp_b_pd)
    print(fmtStr)
    

def case2():
    VCC = 30 # power supply volts
    ips = 0.12 # power supply max current
    power = VCC * ips
    msg = "The power supply provides {} amps at {} volts for {:.2f} watts of power"
    fmtStr = msg.format(ips, VCC, power)
    print(fmtStr)
    
    r_npn_b = 820
    msg = 'lower npn connnects to GPIO via {} ohm resistor'
    fmtStr = msg.format(r_npn_b)
    print(fmtStr)

    gpio_high = 3.3
    i_r_npn_b = gpio_high / r_npn_b
    msg = 'Current provided to base of npn at {}v is {:.3f}'
    fmtStr = msg.format(gpio_high, i_r_npn_b)
    print(fmtStr)
    
    hfe = 30 # nte373 hfe min
    i_npn_ce = hfe * i_r_npn_b
    msg = 'Current provided through the npn is {:.3f} for a beta of {}'
    fmtStr = msg.format(i_npn_ce, hfe)
    print(fmtStr)
    
    i_pnp_b_2_gnd = 0.004 # to turn the pnp similar to the npn above
    i_pnp_ce = hfe * i_pnp_b_2_gnd
    pnp_c = VCC 
    msg = 'The pnp base to gnd voltage required is {} for a beta of {} so the '
    msg += 'current through pnp is {:.3f}.'
    fmtStr = msg.format(i_pnp_b_2_gnd, hfe, i_pnp_ce)
    print(fmtStr)

    i_pnp_pd = VCC / i_pnp_b_2_gnd
    pwr_pd =  VCC * i_pnp_b_2_gnd
    msg = 'The pull down should be {:.1f} for above V I with a PD of {:.3f}'
    fmtStr = msg.format(i_pnp_pd, pwr_pd)
    print(fmtStr)

    r_pnp_b_pu = 11000
    r_pnp_b_pd = 4000
    r_pnp_b_pu_p_pd = r_pnp_b_pu + r_pnp_b_pd
    i_pnp_b_pu_p_pd = VCC / r_pnp_b_pu_p_pd
    pwr_pnp_b_pu_p_pd = VCC * i_pnp_b_pu_p_pd
    msg = 'For a {} pd and {} pu the current is {:.3f} and PD is {:.3f}'
    fmtStr = msg.format(r_pnp_b_pu, r_pnp_b_pd, i_pnp_b_pu_p_pd, pwr_pnp_b_pu_p_pd)
    print(fmtStr)

    i_pnp_b_pd = VCC / r_pnp_b_pd
    pwr_pnp_b_pd = VCC * i_pnp_b_pd
    msg = 'For a {} pd the current is {:.3f} and PD is {:.3f}'
    fmtStr = msg.format(r_pnp_b_pd, i_pnp_b_pd, pwr_pnp_b_pd)
    print(fmtStr)
    
    return 
    r_pu_s_pd_mf = 10
    r_pu_s_pd = r_pu_s_pd_mf * i_pnp_b_2_gnd
    r_pnp_pu_s_pd = VCC / r_pu_s_pd
    r_pwr = VCC * r_pu_s_pd
    msg = 'To current throught the pull up and pull down connected to the base'
    msg += 'should be {} times the base current of {:.3f} which is {}.'
    fmtStr = msg.format(r_pu_s_pd_mf, i_pnp_b_2_gnd, r_pu_s_pd)
    print(fmtStr)
    msg = 'For {} VCC and {:.3f} current the pull up and pull down resistors'
    msg += 'should be {:.1f} and have a power rating of {:.3f}.'
    fmtStr = msg.format(pnp_c, r_pu_s_pd, r_pnp_pu_s_pd, r_pwr)
    print(fmtStr)
    
    
def case1():
    VCC = 30 # power supply volts
    ips = 0.12 # power supply max current
    power = VCC * ips
    msg = "The power supply provides {} amps at {} volts for {:.2f} watts of power"
    fmtStr = msg.format(ips, VCC, power)
    print(fmtStr)

    hfe = 30
    ib = ips/hfe
    ibr = VCC/ib
    pbr = VCC * ib
    msg = "For beta {}, Ib {:.3f}, ibr {:.3f}, pbr {:.3f}"
    fmtStr = msg.format(hfe, ib, ibr, pbr)
    print(fmtStr)
    
    hfe2 = 100
    ib2 = ib/hfe2
    ibr2 = VCC/ib2
    pbr2 = VCC*ib2
    msg = "For beta {}, Ib {:.3f}, ibr {:.3f}, pbr {:.3f}"
    fmtStr = msg.format(hfe2, ib2, ibr2, pbr2)
    print(fmtStr)
    
    ibr3 = 1500
    ib3 = VCC/ibr3
    ips3 = ib3*hfe
    pbr3 = VCC * ib3
    msg = "ibr {:.3f}, Ib {:.3f}, pbr {:.3f}, ips {:.3f}"
    fmtStr = msg.format(ibr3, ib3, pbr3, ips3)
    print(fmtStr)
    
    ibr3 = 1800
    ib3 = VCC/ibr3
    ips3 = ib3*hfe
    pbr3 = VCC * ib3
    msg = "ibr {:.3f}, Ib {:.3f}, pbr {:.3f}, ips {:.3f}"
    fmtStr = msg.format(ibr3, ib3, pbr3, ips3)
    print(fmtStr)

    
if __name__ == "__main__":
    main()
