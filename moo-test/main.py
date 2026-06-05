import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set up the web page title
st.title("⚖️ Multi-Objective Trade-off Simulator")
st.write("Adjust the material slider to see how minimizing weight increases cost.")

# 1. Define the trade-off functions
def calculate_metrics(material_premium):
    # Higher premium = lighter weight but higher cost
    weight = 10 + (90 / (1 + (material_premium / 30)))
    cost = 50 + (2 * material_premium) + (0.1 * (material_premium ** 2))
    return weight, cost

# 2. Pre-calculate the Pareto Frontier (the curved line of all possible best choices)
premium_range = np.linspace(0, 100, 200)
all_weights, all_costs = calculate_metrics(premium_range)

# 3. Create the interactive slider
premium_input = st.slider(
    label="Material Premium Level (0 = Steel, 100 = Exotic Carbon)",
    min_value=0,
    max_value=100,
    value=30, # Default starting position
    step=1  
)

# 4. Calculate current values based on slider position
current_weight, current_cost = calculate_metrics(premium_input)

# 5. Display the live numerical updates side-by-side
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Weight (Lower is Better)", value=f"{current_weight:.1f} kg")
with col2:
    st.metric(label="Cost (Lower is Better)", value=f"${current_cost:.2f}")

# 6. Generate the Trade-off Plot
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the ideal Pareto curve
ax.plot(all_weights, all_costs, color="gray", linestyle="--", alpha=0.7, label="Pareto Frontier (All Choices)")

# Highlight the user's current slider selection
ax.scatter(current_weight, current_cost, color="red", s=150, zorder=5, label="Your Design Point")

# Aesthetics
ax.set_xlabel("Weight (kg) → [Lower is Better]")
ax.set_ylabel("Cost ($) → [Lower is Better]")
ax.set_title("The Optimization Space")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend()

# Invert axes if you want origin to represent the unattainable 'perfect' 0,0 design
ax.set_xlim(5, 105)
ax.set_ylim(40, 400)

# Render plot in the browser
st.pyplot(fig)


if __name__ == "__main__":
    None