#!/usr/bin/env python3
"""Blaine air-permeability fineness calculation (ASTM C204 / EN 196-6).

Mirrors the formulas used in the web UI so the same method can run on the
command line or be embedded in an automated QC pipeline.
"""
import argparse
import math

MU_AIR = 0.0000176  # air viscosity (Pa.s) at ~20 C, used for direct method


def surface_from_reference(ref_s, ref_time, sample_time, ref_k, sample_k):
    """Specific surface (cm^2/g) via calibration against a reference sample.

    S = Ss x (t x Ks) / (ts x K)

    ref_s      : known Blaine surface of the reference sample (cm^2/g)
    ref_time   : measured permeability time for the reference (s)
    sample_time: measured permeability time for the sample     (s)
    ref_k      : K constant for the reference bed
    sample_k   : K constant for the sample bed
    """
    if sample_time <= 0 or ref_time <= 0 or sample_k == 0:
        raise ValueError("times must be > 0 and sample K nonzero")
    return ref_s * (sample_time * ref_k) / (ref_time * sample_k)


def surface_direct(density, time, porosity, cell_f=1.0):
    """Specific surface (cm^2/g) from bed geometry when no reference is handy.

    S = (1/rho) x sqrt( eta x t / eps^3 ) x F
    """
    if density <= 0 or time <= 0 or porosity <= 0 or porosity >= 1:
        raise ValueError("bad inputs: density>0, time>0, 0<porosity<1")
    return (1.0 / density) * math.sqrt(MU_AIR * time / porosity ** 3) * cell_f


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ref", type=float, help="reference Blaine surface (cm2/g)")
    p.add_argument("--ref-time", type=float, required=True, help="reference time (s)")
    p.add_argument("--time", type=float, required=True, help="sample time (s)")
    p.add_argument("--density", type=float, default=3.15, help="sample density (g/cm3)")
    p.add_argument("--ref-k", type=float, default=1.0)
    p.add_argument("--sample-k", type=float, default=1.0)
    p.add_argument("--porosity", type=float, help="bed porosity for direct method")
    args = p.parse_args()

    if args.ref is not None:
        s = surface_from_reference(args.ref, args.ref_time, args.time,
                                   args.ref_k, args.sample_k)
        print(f"Blaine surface (reference method): {s:,.0f} cm2/g")
    else:
        s = surface_direct(args.density, args.time, args.porosity)
        print(f"Blaine surface (direct method):    {s:,.0f} cm2/g")
