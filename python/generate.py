import pandas as pd
import random


def generate(file):

    df = pd.read_csv(file)

    df['Date'] = pd.to_datetime(df['Date'])

    df_numeric = df.drop(columns=['Date'])

    hourly_consumption = df_numeric.groupby("Hour").sum()

    peak_hours = hourly_consumption.idxmax()

    recommendation = {
        1: {
            "Light": f"Reduce lighting usage during peak hours from {peak_hours['Light (kWh)']}:00 to {peak_hours['Light (kWh)'] + 1}:00 by using energy-efficient bulbs.",
            "Fan": f"Fans are used most during {peak_hours['Fan (kWh)']}:00 - {peak_hours['Fan (kWh)'] + 1}:00. Consider using natural ventilation to reduce dependency.",
            "AC": "Use programmable thermostats and insulation to reduce AC energy consumption.",
            "Computers": f"Computers consume the most energy from {peak_hours['Computers (kWh)']}:00 - {peak_hours['Computers (kWh)'] + 1}:00. Ensure to shut down unused systems."
        },
        2: {
            "Light": f"Install smart lighting systems that adjust brightness based on ambient light, avoiding excessive use during {peak_hours['Light (kWh)']}:00 - {peak_hours['Light (kWh)'] + 1}:00.",
            "Fan": f"Automate fan speeds using IoT-based sensors that adjust airflow based on temperature and occupancy, especially before {peak_hours['Fan (kWh)']}:00.",
            "AC": "Use AI-powered climate control systems that learn usage patterns and optimize cooling needs dynamically.",
            "Computers": f"Implement auto-shutdown policies for idle computers to prevent unnecessary energy drain, especially post {peak_hours['Computers (kWh)']}:00."
        },
        3: {
            "Light": f"Shift major lighting usage to daylight hours to minimize electricity costs, especially avoiding {peak_hours['Light (kWh)']}:00.",
            "Fan": f"Consider using energy-efficient BLDC fans to save up to 60% on fan power consumption, especially during peak hours {peak_hours['Fan (kWh)']}:00 - {peak_hours['Fan (kWh)'] + 1}:00).",
            "AC": "Invest in smart AC controllers that automatically adjust temperatures based on room occupancy to reduce power bills.",
            "Computers": f"Use cloud-based services for intensive tasks to offload local power consumption, especially from {peak_hours['Computers (kWh)']}:00 onwards."
        },
        4: {
            "Light": f"Replace incandescent bulbs with LEDs and turn off unnecessary lights, especially between {peak_hours['Light (kWh)']}:00 - {peak_hours['Light (kWh)']+1}:00.",
            "Fan": f"Use ceiling fans in combination with AC to reduce cooling costs. Run fans at lower speeds during peak hours {peak_hours['Fan (kWh)']}:00 - {peak_hours['Fan (kWh)'] + 1}:00.",
            "AC": "Maintain AC filters regularly to improve efficiency and set temperatures between 24-26°C for optimal performance.",
            "Computers": f"Enable power-saving modes on all computers and use sleep mode when inactive, especially from {peak_hours['Computers (kWh)']}:00 onward."
        },
        5: {
            "Light": f"Use motion-sensor lights to automatically reduce usage during non-essential hours, especially after {peak_hours['Light (kWh)']+1}:00.",
            "Fan": f"Encourage natural cooling strategies, such as cross-ventilation, before {peak_hours['Fan (kWh)']}:00 to minimize electric fan usage.",
            "AC": "Set AC timers to operate efficiently and avoid running during peak power demand hours.",
            "Computers": f"Schedule heavy computing tasks (like updates or data backups) between 02:00 - 05:00 AM to avoid peak load times."
        }

    }

    recommendations = recommendation[random.randrange(1, 6)]

    for key, value in recommendations.items():
        print(f"{key}: {value}")
    return recommendations
