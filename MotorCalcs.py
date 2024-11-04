from CasingThickness import casing_thickness
from ForwardClosure import forward_closure_thickness
from LinerThickness import liner_thickness
from BoltingCalculations import bolt_shear, bolt_tear_out, casing_bearing_stress, casing_tensile_stress

# -------------------------VARIABLE INPUT---------------------------
# All lengths in mm
# All pressures in MPa

# casing
thickness = 6.17
casing_inside_radius = 50.93
casing_inside_diameter = 101.86
casing_outside_diameter = 114.2


allowable_stress = 58.0
casing_shear = 150.00
casing_yts = 214.00
casing_bys = 276.000

# bolts
bolt_dia_minor = 4.917
bolt_dia_major = 6.00
number_bolt = 8
bolt_shear_strength = 730
edge_distance = 2.5 * bolt_dia_major

# factors
te = 4.217
re = 0.25
f = 2.00
pressure_fos = 1.5
joint_efficiency = 1.00
attachment_factor = 0.33
# -----------------------------------------------------------------

DesignPressure, MEOP = casing_thickness(thickness,casing_inside_radius, allowable_stress, joint_efficiency, pressure_fos)

print(f"The design pressure is: {DesignPressure} MPa")
print(f"The maximum expected operating pressure is: {MEOP} MPa")

print(f"\nThe forward closure thickness is {forward_closure_thickness(DesignPressure, casing_inside_diameter, allowable_stress, joint_efficiency, attachment_factor)} mm")
print(f"\nThe liner thickness is {liner_thickness(te,re,f)} mm")

BoltShear, FSShear = bolt_shear(casing_inside_diameter, bolt_dia_minor, MEOP, number_bolt, bolt_shear_strength)
print(f"\nThe bolt shear stress is: {BoltShear} MPa")
print(f"The factor of safety is: {FSShear}")

TearoutStress, FSTearout = bolt_tear_out(casing_inside_diameter, bolt_dia_major, MEOP, number_bolt, edge_distance, thickness, casing_shear)
print(f"\nThe bolt tearout stress is: {TearoutStress} MPa")
print(f"The factor of safety is: {FSTearout}")

CasingTensile, FSTensile = casing_tensile_stress(casing_outside_diameter, thickness, number_bolt, bolt_dia_major, MEOP, casing_yts)
print(f"\nThe casing tensile stress is: {CasingTensile} MPa")
print(f"The factor of safety is: {FSTensile}")

CasingBearing, FSBearing = casing_bearing_stress(casing_inside_diameter, MEOP, number_bolt, bolt_dia_major, thickness, casing_bys)
print(f"\nThe casing bearing stress is: {CasingBearing} MPa")
print(f"The factor of safety is: {FSBearing}")

