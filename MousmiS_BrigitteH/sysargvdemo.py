import sys

def main():
    if len(sys.argv) != 2:
        print('Usage:  ___.py infilename')
        sys.exit()
        
print(sys.argv)

if __name__ == '__main__':
    main()