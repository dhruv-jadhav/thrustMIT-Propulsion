from CasingThickness import casing_thickness
from ForwardClosure import forward_closure_thickness
from LinerThickness import liner_thickness
from BoltingCalculations import bolt_shear, bolt_tear_out, casing_bearing_stress, casing_tensile_stress, multiple_bolt_circle_tearout

# -------------------------VARIABLE INPUT---------------------------
# All lengths in mm
# All pressures in MPa

# casing
thickness = 6
casing_outside_diameter = 101.4
casing_inside_diameter = casing_outside_diameter - 2 * thickness
casing_inside_radius = casing_inside_diameter / 2

allowable_stress = 82
casing_shear = 210
casing_yts = 270
casing_bys = 386

# bolts
bolt_dia_minor = 4.917
bolt_dia_major = 6
number_bolt = 12
bolt_shear_strength = 730
edge_distance = 2 * bolt_dia_major

# Multiple Bolt Circles
edge_distance1 = 12
edge_distance2 = 24
N_circle = number_bolt / 2

# factors
te = 0
re = 0
f = 0
pressure_fos = 1.5
joint_efficiency = 1.00
attachment_factor = 0.33
# -----------------------------------------------------------------

DesignPressure, MEOP = casing_thickness(thickness, casing_inside_radius, allowable_stress, joint_efficiency,
                                        pressure_fos)

print(f"The design pressure is: {DesignPressure} MPa")
print(f"The maximum expected operating pressure is: {MEOP} MPa")

print(f"\nThe forward closure thickness is {forward_closure_thickness(MEOP, casing_inside_diameter, allowable_stress, joint_efficiency, attachment_factor)} mm")
print(f"\nThe liner thickness is {liner_thickness(te, re, f)} mm")

BoltShear, FSShear = bolt_shear(casing_inside_diameter, bolt_dia_minor, MEOP, number_bolt, bolt_shear_strength)
print(f"\nThe bolt shear stress is: {BoltShear} MPa")
print(f"The factor of safety is: {FSShear}")

TearoutStress, FSTearout = bolt_tear_out(casing_inside_diameter, bolt_dia_major, MEOP, number_bolt, edge_distance,
                                         thickness, casing_shear)
print(f"\nThe bolt tearout stress is: {TearoutStress} MPa")
print(f"The factor of safety is: {FSTearout}")

MultipleTearoutStress, FSMultipleBoltCircle = multiple_bolt_circle_tearout(casing_inside_diameter, bolt_dia_major, MEOP, edge_distance1, edge_distance2, thickness, bolt_shear_strength)
print(f"\nThe bolt tearout stress for 2 bolt circles is: {MultipleTearoutStress} MPa")
print(f"The factor of safety is: {FSMultipleBoltCircle}")

CasingTensile, FSTensile = casing_tensile_stress(casing_outside_diameter, thickness, N_circle, bolt_dia_major, MEOP,
                                                 casing_yts)
print(f"\nThe casing tensile stress is: {CasingTensile} MPa")
print(f"The factor of safety is: {FSTensile}")

CasingBearing, FSBearing = casing_bearing_stress(casing_inside_diameter, MEOP, number_bolt, bolt_dia_major, thickness,
                                                 casing_bys)
print(f"\nThe casing bearing stress is: {CasingBearing} MPa")
print(f"The factor of safety is: {FSBearing}")
