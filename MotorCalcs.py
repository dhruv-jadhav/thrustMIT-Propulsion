from CasingThickness import casing_thickness
from ForwardClosure import forward_closure_thickness
from LinerThickness import liner_thickness
from BoltingCalculations import bolt_shear, bolt_tear_out, casing_bearing_stress, casing_tensile_stress

# -------------------------VARIABLE INPUT---------------------------
# All lengths in mm
# All pressures in MPa

# casing
thickness = 0
casing_inside_radius = 0
casing_inside_diameter = 0
casing_outside_diameter = 0

allowable_stress = 0
casing_shear = 0
casing_yts = 0
casing_bys = 0

# bolts
bolt_dia_minor = 0
bolt_dia_major = 0
number_bolt = 0
bolt_uts = 0
edge_distance = 2 * bolt_dia_major

# factors
te = 0
re = 0
f = 0
joint_efficiency = 1.00
attachment_factor = 0.33
# -----------------------------------------------------------------
DesignPressure, MEOP = casing_thickness(thickness,casing_inside_radius, allowable_stress, joint_efficiency)

print(f"The design pressure is: {DesignPressure} MPa")
print(f"The maximum expected operating pressure is: {MEOP} MPa")

print(f"\nThe forward closure thickness is {forward_closure_thickness(DesignPressure, casing_inside_diameter, allowable_stress, joint_efficiency, attachment_factor)} mm")
print(f"\nThe liner thickness is {liner_thickness(te,re,f)} mm")

TearoutStress, FSTearout = bolt_tear_out(casing_inside_diameter, bolt_dia_major, MEOP, number_bolt, edge_distance, thickness, casing_shear)
print(f"\nThe bolt tearout stress is: {TearoutStress} MPa")
print(f"The factor of safety is: {FSTearout}")

BoltShear, FSShear = bolt_shear(casing_inside_diameter, bolt_dia_minor, MEOP, number_bolt, bolt_uts)
print(f"\nThe bolt tearout stress is: {BoltShear} MPa")
print(f"The factor of safety is: {FSShear}")

CasingTensile, FSTensile = casing_tensile_stress(casing_outside_diameter, thickness, number_bolt, bolt_dia_major, MEOP, casing_yts)
print(f"\nThe casing tensile stress is: {CasingTensile} MPa")
print(f"The factor of safety is: {FSTensile}")

CasingBearing, FSBearing = casing_bearing_stress(casing_inside_diameter, MEOP, number_bolt, bolt_dia_major, thickness, casing_bys)
print(f"\nThe casing bearing stress is: {CasingBearing} MPa")
print(f"The factor of safety is: {FSBearing}")

