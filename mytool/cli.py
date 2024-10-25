import argparse
import numpy as np 

def process_file(file, number, verbose):
    print(f"Processing file: {file}")

    # Print the number with its default value if not provided
    print(f"Number used for processing: {number}")

    # Handle verbose flag with default set to False
    if verbose:
        print("Verbose mode is enabled.")

    a = np.arange(5)
    a[[0, 0, 2]] = [1, 2, 3]
    print(a)

def main():
    parser = argparse.ArgumentParser(description="MyTool File Processor Utility")

    # Required argument: main file
    parser.add_argument("file", type=str, help="Path to the main file to be processed")

    # Optional argument: number with a default value
    parser.add_argument("--number", type=int, default=1, help="An integer number to use during processing (default: 1)")

    # Boolean flag: verbose with default set to False
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output (default: False)")

    # Parse the arguments
    args = parser.parse_args()

    # Execute the main function
    process_file(args.file, args.number, args.verbose)

if __name__ == "__main__":
    main()
