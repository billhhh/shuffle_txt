import random
in_file = 'train.csv'
out_file = 'train_11w_shuffle.csv'

data = [x.strip() for x in open(in_file)]
random.shuffle(data)
with open(out_file, 'w') as f:
    f.write('\n'.join(data))
