# DataScience
Pandas
# Dynamic Pricing Script

This Python script performs **dynamic price analysis and updates** on a product catalog based on sales performance and stock levels using business rules. It merges product and sales data, applies pricing logic, and outputs a CSV file with updated prices.

---

## 📁 Files Required

Place the following CSV files in the correct path (currently set to Desktop in the script):

- `product.csv` – Contains product information (`sku`, `stock`, `cost_price`, `current_price`)
- `sales.csv` – Contains sales data (`sku`, `quantity_sold`)

---

## 🔧 Pricing Rules Applied

1. **Rule 1 – Low Stock, High Demand (Highest Priority):**
   - **Condition:** `stock < 20` and `quantity_sold > 30`
   - **Action:** Increase price by **15%**

2. **Rule 2 – Dead Stock (Second Priority):**
   - **Condition:** `stock > 200` and `quantity_sold == 0`
   - **Action:** Decrease price by **30%**

3. **Rule 3 – Overstocked Inventory (Third Priority):**
   - **Condition:** `stock > 100` and `quantity_sold < 20`
   - **Action:** Decrease price by **10%**

4. **Rule 4 – Minimum Profit Constraint (Always Applied Last):**
   - Ensures final price is at least **20% above `cost_price`**

5. **Final Rounding:**
   - Final updated price is rounded to **2 decimal places**

---

## 🧾 Output

- Output file: `output.csv` saved to Desktop.
- Columns in the output:
  - `sku`
  - `old_price`
  - `new_price`

---

## ▶️ How to Run

1. Make sure Python and `pandas` are installed:

   ```bash
   pip install pandas
