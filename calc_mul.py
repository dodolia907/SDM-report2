#!/usr/bin/python3

def calc(A,B):
        try:
                a = int(A)
                b = int(B)
                if 0<a and a<1000 and 0<b and b<1000:
                        valid=True
                else:
                        valid=False

        except (ValueError, TypeError):
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
