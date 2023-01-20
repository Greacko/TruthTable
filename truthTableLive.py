import truthTableV1_5DE as tt5DE

tt5DE.mDefault("(P im Q)[P Q]")
print()
tt5DE.mDefault("(((P1 or P2) and ((P1 im Q) and (P2 im Q))) im Q)[P1 P2 Q]")

