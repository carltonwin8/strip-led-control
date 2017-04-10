#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""

def main():
    """
    Description
    """
    VCC = 30 # power supply volts
    ips = 0.12 # power supply max current
    power = VCC * ips
    msg = "The power supply provides {} amps at {} volts for {:.2f} watts of power"
    fmtStr = msg.format(ips, VCC, power)
    print(fmtStr)

    hfe = 7
    ib = ips/hfe
    ibr = VCC/ib
    pbr = VCC * ib
    msg = "For beta {:.3f}, Ib {:.3f}, ibr {:.3f}, pbr {:.3f}"
    fmtStr = msg.format(hfe, ib, ibr, pbr)
    print(fmtStr)
    
    hfe2 = 100
    ib2 = ib/hfe2
    ibr2 = VCC/ib2
    pbr2 = VCC*ib2
    msg = "For beta {:.3f}, Ib {:.3f}, ibr {:.3f}, pbr {:.3f}"
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
