#print *.bam files#
import glob
for i in glob.iglob("/**/**/**/Files/*.bam"):
    print(i)
#python path.py > pathsub.txt#
#print cmds for extracting region bam file#
with open('pathsub.txt') as f:
    for line in f:
    name = line.rstrip().split('/')[-4]
    print('samtools view -b {0} chrX:67500000-67800000 > {1}.chrX.bam && samtools index {1}.chrX.bam'.format(line.rstrip(), name))
#python pathcmd.py>cmd.txt#
