import argparse
import sys
import pypbe

parser = argparse.ArgumentParser(description="PyPBE is a resource for tabletop " +
            "gaming which allows Gamemasters (GM) to fairly select which random " +
            "rolling method is closest to an equivalent Point Buy value.")
parser.add_argument('--system', help='Choose the rpg system for the point buy mapping:', 
                    type=str, default='pf', choices=['pf','3e','4e','5e'])
parser.add_argument('--num_dice', help='Total number of dice to roll (e.g. "3" in "3d6"):', 
                    type=int, default=3, choices=range(1, 11))
parser.add_argument('--dice_type', help='Number of sides on the dice (e.g. "6" in "3d6"):', 
                    type=int, default=6, choices=range(1, 21))
parser.add_argument('--add_value', help='Add a constant value to the roll (e.g. "2" in "4d4+2"):', 
                    type=int, default=0, choices=range(-20, 21))
parser.add_argument('--keep_dice', help='Keep the best X dice (e.g. roll "4d6", keep "3"):', 
                    type=int, default=3, choices=range(1, 11))
parser.add_argument('--num_attrs', help='The total number of attributes to roll (e.g. STR, CON, DEX, INT, WIS, CHA):', 
                    type=int, default=6, choices=range(1, 21))
parser.add_argument('--keep_attrs', help='Keep the best X attributes (e.g. "6" in "roll 4d4+2 7 times, keep the best 6"):', 
                    type=int, default=6, choices=range(1, 7))
parser.add_argument('--num_arrays', help='Number of dice arrays to choose from (e.g. "3" in "roll 3d6 for 6 attributes, for 3 arrays"):', 
                    type=int, default=1, choices=range(1, 21))
parser.add_argument('--rerolls', help='Cumulatively reroll these dice values (e.g. 0 reroll nothing, 1 reroll 1s, 2 reroll 1s and 2s, etc.):', 
                    type=int, default=0, choices=range(0, 21))


def main():
    args = parser.parse_args()
    lowest_val = args.keep_dice + args.add_value
    highest_val = (args.dice_type * args.keep_dice) + args.add_value
    if args.keep_dice > args.num_dice:
        print("Number of dice to keep cannot be greater than the number of dice.")
    elif args.keep_attrs > args.num_attrs:
        print("Number of attributes to keep cannot be greater than the number of attributes.")      
    elif args.rerolls >= args.dice_type:
        print("Number to re-roll must be less than the dice type.")
    elif lowest_val < 3:
        er_str = "The lowest possible value is " + str(lowest_val) + \
                 ". PBE is not defined for values less than 3. Please " + \
                 "increase the number of dice (or dice to keep) or the " + \
                 "add value."
        print(er_str)    
    elif highest_val > 18:
        er_str = "The highest possible value is " + str(highest_val) + \
                 ". PBE is not defined for values greater than 18. Please " + \
                 "decrease the number of dice (or dice to keep) or the " + \
                 "add value."
        print(er_str)   
    else:          
        pbe = pypbe.PBE(args.num_dice, args.dice_type, args.add_value, 
                        args.num_attrs, args.num_arrays, args.rerolls, 
                        args.keep_dice, args.keep_attrs, args.system)
        title = pbe._construct_title(args.num_dice, args.dice_type, args.add_value, 
                        args.num_attrs, args.keep_attrs, args.keep_dice,
                        args.rerolls, args.num_arrays)
        pbe.roll_mc(int(10e5)).plot_histogram().savefig(title + '.jpg')

if __name__ == "__main__":
    sys.exit(main())