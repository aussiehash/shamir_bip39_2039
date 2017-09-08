from api import mnemonic_to_shares, shares_to_mnemonic
from mnemonic import generate_mnemonic

mnemonic = generate_mnemonic(length=12)

print "Mnemonic:", mnemonic
#Mnemonic: ['session', 'quiz', 'swamp', 'quantum']

shares = mnemonic_to_shares(mnemonic)

print "\nShares:", shares
#Shares: {'share1': ['lazy', 'dizzy', 'viable', 'impulse'],
#         'share2': ['decade', 'soon', 'arrive', 'crush'],
#         'share3': ['various', 'garbage', 'caution', 'walnut']}

print "\nRecovered from shares 1 and 2:", shares_to_mnemonic(share1=shares['share1'], share2=shares['share2'])
#Recovered from shares 1 and 2: ['session', 'quiz', 'swamp', 'quantum']

print "Recovered from shares 1 and 3:", shares_to_mnemonic(share1=shares['share1'], share3=shares['share3'])
#Recovered from shares 1 and 3: ['session', 'quiz', 'swamp', 'quantum']

print "Recovered from shares 2 and 3:", shares_to_mnemonic(share2=shares['share2'], share3=shares['share3'])
#Recovered from shares 2 and 3: ['session', 'quiz', 'swamp', 'quantum']