import pandas as pd
import numpy as np

def generate_lotto_numbers(file_path, num_sets=100):
    # Read the historical lotto data
    df = pd.read_excel(file_path)
    
    # Collect all numeric columns (assuming they hold the drawn numbers).
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    # Combine all numbers into a single list
    all_numbers = []
    for col in numeric_cols:
        all_numbers.extend(df[col].dropna().astype(int).tolist())
    
    # Tally the frequencies
    from collections import Counter
    freq_counter = Counter(all_numbers)
    
    # Build a list of unique numbers and corresponding frequencies
    unique_numbers = sorted(freq_counter.keys())
    frequencies = np.array([freq_counter[n] for n in unique_numbers], dtype=float)
    
    # Convert frequencies to probabilities
    probabilities = frequencies / frequencies.sum()
    
    # Random number generator
    rng = np.random.default_rng()
    
    # Generate the requested number of sets
    results = []
    for _ in range(num_sets):
        chosen = set()
        while len(chosen) < 6:
            # Weighted choice of one number
            picked = rng.choice(unique_numbers, p=probabilities)
            chosen.add(picked)
        results.append(sorted(chosen))
    
    return results

# Example usage
if __name__ == "__main__":
    file_path = "C:/Users/Juanito Encinas/Downloads/lotto winning number2.xlsx"
    lotto_combinations = generate_lotto_numbers(file_path, 100)
    
     # Convert results to a DataFrame
    df_out = pd.DataFrame(lotto_combinations, 
                          columns=[f"Number_{i+1}" for i in range(6)])
    
    # Write to Excel (XLSX) file
    df_out.to_excel("LottoCombinations.xlsx", index=False)
    print("100 sets written to LottoCombinations.xlsx!")
