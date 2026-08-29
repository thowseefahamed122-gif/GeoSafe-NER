print("========================================")
print("   AI LANDSLIDE RISK MONITORING SYSTEM")
print("========================================")

# Get environmental data from the user
rainfall = float(input("Enter rainfall (mm): "))
soil_moisture = float(input("Enter soil moisture (%): "))
slope = float(input("Enter slope angle (degrees): "))
water_level = float(input("Enter water level (%): "))

# Calculate risk score
risk_score = 0

# Rainfall contribution
if rainfall >= 100:
    risk_score += 30
elif rainfall >= 60:
    risk_score += 20
elif rainfall >= 30:
    risk_score += 10

# Soil moisture contribution
if soil_moisture >= 80:
    risk_score += 25
elif soil_moisture >= 60:
    risk_score += 15
elif soil_moisture >= 40:
    risk_score += 8

# Slope contribution
if slope >= 40:
    risk_score += 25
elif slope >= 30:
    risk_score += 15
elif slope >= 20:
    risk_score += 8

# Water level contribution
if water_level >= 80:
    risk_score += 20
elif water_level >= 60:
    risk_score += 12
elif water_level >= 40:
    risk_score += 5

# Maximum score
risk_score = min(risk_score, 100)

# Determine risk level
if risk_score >= 80:
    risk_level = "CRITICAL"
    warning = "Immediate warning recommended!"
elif risk_score >= 60:
    risk_level = "HIGH"
    warning = "Alert authorities and monitor closely."
elif risk_score >= 30:
    risk_level = "MEDIUM"
    warning = "Continue monitoring the area."
else:
    risk_level = "LOW"
    warning = "Normal monitoring."

# Display result
print("\n========================================")
print("           RISK ANALYSIS")
print("========================================")

print(f"Rainfall       : {rainfall} mm")
print(f"Soil Moisture  : {soil_moisture}%")
print(f"Slope Angle    : {slope}°")
print(f"Water Level    : {water_level}%")

print("----------------------------------------")
print(f"Risk Score     : {risk_score}/100")
print(f"Risk Level     : {risk_level}")
print(f"Recommendation : {warning}")
print("========================================")