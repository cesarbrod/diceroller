import random
import multiprocessing

def roll_batch(num_rolls):
    """
    Simulates a batch of dice rolls and returns the counts.
    
    Args:
        num_rolls (int): Number of rolls to perform.
        
    Returns:
        tuple: (die1_counts, die2_counts, sum_counts)
    """
    die1_counts = {i: 0 for i in range(1, 7)}
    die2_counts = {i: 0 for i in range(1, 7)}
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        die1_counts[die1] += 1
        die2_counts[die2] += 1
        sum_counts[total] += 1
        
    return die1_counts, die2_counts, sum_counts

def main():
    """Main function to manage parallel execution and display statistics."""
    
    # Get number of rolls
    while True:
        try:
            num_rolls = int(input("How many rolls would you like to simulate? "))
            if num_rolls > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    cpu_count = multiprocessing.cpu_count()
    print(f"\nSimulating {num_rolls} rolls using {cpu_count} CPUs...")

    # Distribute work
    pool = multiprocessing.Pool(processes=cpu_count)
    
    rolls_per_cpu = num_rolls // cpu_count
    remainder = num_rolls % cpu_count
    
    tasks = []
    for i in range(cpu_count):
        count = rolls_per_cpu + (1 if i < remainder else 0)
        if count > 0:
            tasks.append(count)
            
    # Execute in parallel
    results = pool.map(roll_batch, tasks)
    pool.close()
    pool.join()
    
    # Aggregate results
    final_die1_counts = {i: 0 for i in range(1, 7)}
    final_die2_counts = {i: 0 for i in range(1, 7)}
    final_sum_counts = {i: 0 for i in range(2, 13)}
    
    for d1, d2, s in results:
        for k, v in d1.items():
            final_die1_counts[k] += v
        for k, v in d2.items():
            final_die2_counts[k] += v
        for k, v in s.items():
            final_sum_counts[k] += v

    # Display statistics
    print("\n" + "="*45)
    print(f"STATISTICS (Total Rolls: {num_rolls})")
    print("="*45)
    
    print("\nDICE OUTCOMES")
    print(f"{'Value':<6} | {'Die 1 #':<8} | {'Die 1 %':<8} | {'Die 2 #':<8} | {'Die 2 %':<8}")
    print("-" * 46)
    for i in range(1, 7):
        d1_c = final_die1_counts[i]
        d1_p = (d1_c / num_rolls) * 100 if num_rolls > 0 else 0
        d2_c = final_die2_counts[i]
        d2_p = (d2_c / num_rolls) * 100 if num_rolls > 0 else 0
        print(f"{i:<6} | {d1_c:<8} | {d1_p:<7.1f}% | {d2_c:<8} | {d2_p:<7.1f}%")

    print("\nSUM OUTCOMES")
    print(f"{'Value':<6} | {'Count':<8} | {'Percentage':<10}")
    print("-" * 30)
    for i in range(2, 13):
        c = final_sum_counts[i]
        p = (c / num_rolls) * 100 if num_rolls > 0 else 0
        print(f"{i:<6} | {c:<8} | {p:<9.1f}%")

if __name__ == "__main__":
    main()
