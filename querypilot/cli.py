import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question",type=str,required=True)
    parser.add_argument("--config",type=str,required=True)
    
    args = parser.parse_args()
    print(f"Processing question: {args.question}")
    print(f"Using configuration path: {args.config}")

if __name__ == "__main__":
    main()