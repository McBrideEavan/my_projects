```python
import src.data_collection as dc
import src.analysis as an
import src.visualization as vis

def main():
    # Step 1: Collect data (game schedule and rosters)
    print("Collecting data...")
    schedule, rosters = dc.collect_data()
    
    # Step 2: Calculate roster consistency
    print("Calculating roster consistency...")
    consistency = an.calculate_roster_consistency(rosters)
    
    # Step 3: Perform correlation analysis
    print("Performing correlation analysis...")
    results = an.perform_correlation(consistency, schedule)
    
    # Step 4: Visualize results
    print("Visualizing results...")
    vis.plot_results(results)

if __name__ == "__main__":
    main()
