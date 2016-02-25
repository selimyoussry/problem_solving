# genuine_itw - Problem palantir_tech
palantir technical interview

This is the Scratch Pad. 
The contents of this pad are synced to the other participants, but are not saved. 
Use it ONLY for things you don't want saved in the CodePair report.



99 fair coins, 1 biased



pick one at random - flipping 10 times - recording results of the flip - not looking at the coin

if 10 heads is the result, what's P(biased coin)

P(biased coin | result) = P(result | biased) * P(biased) / (P(result))

P(result) = P(result|biased)P(biased) + P(result|unbiased)P(unbiased)

P(result|biased)=1
P(biased)=1/100
P(result|unbiased) = pow(0.5, 10)
P(unbiased)=99/100

~91%