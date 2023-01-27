import argparse
import scaling

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
Plots the scaling 
    """)
    parser.add_argument('--configuration_files', required=True, nargs="+", help="The configuration file to use")
    parser.add_argument('--show', action='store_true', help="Show the plot")
    parser.add_argument('--skip_missing', action='store_true', help="Skip missing data")
    parser.add_argument('--saveplot', type=str, help="Save the plot to a file")
    parser.add_argument('--time_key', type=str, default='Total time', help="Time key to get runtime from")
    parser.add_argument('--per_quantity', type=str, default=None, help="Plot runtime per quantity")

    
    args = parser.parse_args()
    
    scaling.plot_scalings(args.configuration_files, args.skip_missing, args.saveplot, args.show,
        time_key=args.time_key, per_quantity=args.per_quantity)