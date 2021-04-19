import pandas as pd

if __name__ == "__main__":
    file_name = input("input file name\n")

    vehicle = pd.read_excel(file_name, sheet_name="Vehicles", dtype=str)
    csv_name = f"{file_name.strip('.xlsx')}.csv"
    vehicle.to_csv(csv_name, index=None)

    num_rows = vehicle.shape[0]

    print(f"{num_rows} {'lines were' if num_rows > 1 else 'line was'} added to {csv_name}")
